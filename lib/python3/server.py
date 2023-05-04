import asyncio
import sys
import logging
import grpc
import time
import requests
import json
import aiohttp
import jwt
import datetime
import vk_api

import database as db
import LobbiesMicroservice_pb2 as pb2
import LobbiesMicroservice_pb2_grpc as pb2_grpc

class Listener(pb2_grpc.LobbiesServiceServicer):
    def __init__(self, config: dict, logger: logging.Logger):
        self.config = config
        self.logger = logger
        self.db = db.DatabaseManager(logger,
                              db_name=config["DataBase"]["name"],
                              db_user=config["DataBase"]["user"],
                              db_pass=config["DataBase"]["password"],
                              db_host=config["DataBase"]["host"],
                              db_port=config["DataBase"]["port"]
                              )


    async def Create(self, request, context):
        owner_id = request.requesterID
        self.logger.info("Create request from user #%d" % user_id)
        
        settings = None
        if request.settings:
            try:
                settings = validateSettings(request.settings)
            except ValueError:
                return pb2.AuthResponse(status=pb2.ExitStatus.BAD_VALUE)
        
        try:
            lobby_id, applied_settings = self.db.createLobby(owner_id, settings)
            self.db.connectUserToLobby(owner_id, lobby_id)
        except Exception as e:
            return pb2.AuthResponse(status=pb2.ExitStatus.DB_LEVEL_ERROR)

        
def validateSettings(settings: pb2.LobbySettings) -> dict:
    valid_settings = dict()

    valid_settings["name"] = settings.name[:32]
    
    if settings.type != pb2.LobbyType.PUBLIC and settings.type != pb2.LobbyType.PRIVATE:
        raise ValueError('Bad lobby type')
    elif settings.type == pb2.LobbyType.PUBLIC:
        valid_settings["type"] = pb2.LobbyType.PUBLIC.number + 1
    elif settings.type == pb2.LobbyType.PRIVATE::
        valid_settings["type"] = pb2.LobbyType.PRIVATE.number + 1
            
    valid_settings["password"] = "" if not settings.password else settings.password
    valid_settings["maxPlayers"] = settings.maxPlayers
    valid_settings["timeForTurn"] = settings.timeForTurn
    valid_settings["victoryType"] = settings.victoryType.number + 1
    valid_settings["scoreVictoryValue"] = settings.scoreVictoryValue
    valid_settings["turnVictoryValue"] = settings.turnVictoryValue

    return valid_settings
    

async def serve(config: dict, logger: logging.Logger) -> None:
    server = grpc.aio.server()
    listener = Listener(config, logger)
    pb2_grpc.add_UsersServiceServicer_to_server(listener, server)
    listen_addr = '[::]:' + str(config['gRPC']['port'])
    server.add_insecure_port(listen_addr)
    logger.info('Starting server on %s', listen_addr)
    await server.start()
    await server.wait_for_termination()


def run(config: dict, logger: logging.Logger) -> None:
    asyncio.run(serve(config, logger))
