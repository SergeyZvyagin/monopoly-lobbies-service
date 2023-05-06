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
import UsersMicroservice_pb2 as users_pb2
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
        self.logger.info("Create request from user #%d" % owner_id)
        
        settings = None
        if request.settings.name != "":
            try:
                settings = validateSettings(request.settings, self.config)
                self.logger.info("Settigs is validate")
            except ValueError as e:
                self.logger.error("Settings validation error: %s" % e)
                return pb2.AboutLobbyResponse(status=pb2.ExitStatus.BAD_VALUE)
        
        try:
            lobby_id = self.db.createLobby(owner_id, settings)
            self.db.connectUserToLobby(owner_id, lobby_id)       
            full_current_lobby_info = getFullCurrentLobbyInfo(self.db, lobby_id)
            return pb2.AboutLobbyResponse(lobbyInfo=full_current_lobby_info) 
        except Exception as e:
            return pb2.AboutLobbyResponse(status=pb2.ExitStatus.DB_LEVEL_ERROR)
    

    async def GetList(self, request, context):
        requester_id = request.requesterID
        self.logger.info("GetList request from user #%d" % requester_id)
        
        lobbies = self.db.getList()
        lobbies_pb = pb2.GetListResponse()
        for lobby in lobbies:
            short_info = pb2.ShortCurrentLobbyInfo(lobbyID=lobby[0],
                                                   name=lobby[1],
                                                   isPrivate=bool(lobby[2]-1),
                                                   maxPlayers=lobby[3],
                                                   playersNow=lobby[4])
            lobbies_pb.lobbies.append(short_info)
        return lobbies_pb


def getFullCurrentLobbyInfo(dbm: db.DatabaseManager, lobby_id: int) -> pb2.FullCurrentLobbyInfo:
    lobby_info = dbm.getFullLobbyInfo(lobby_id)
    if not lobby_info:
        return None
    
    owner_id = lobby_info[0]
    settings_pb = pb2.LobbySettings(name=lobby_info[1],
                                 type=lobby_info[2]-1,
                                 password=lobby_info[3],
                                 maxPlayers=lobby_info[4],
                                 timeForTurn=lobby_info[5],
                                 victoryType=lobby_info[6]-1,
                                 scoreVictoryValue=lobby_info[7],
                                 turnVictoryValue=lobby_info[8]
                                 )
    
    timer_is_activate = lobby_info[9]

    full_current_lobby_info = pb2.FullCurrentLobbyInfo(lobbyID=lobby_id,
                                                       ownerID=owner_id,
                                                       settings=settings_pb,
                                                       timerIsActivate=timer_is_activate,
                                                       )

    if timer_is_activate and lobby_info[10] and lobby_info[11]:
        full_current_lobby_info.connection = pb.GameConnectionInfo(address=lobby_info[10], port=lobby_info[11])
    
    players = dbm.getActivePlayersInLobby(lobby_id)
    for player_info in players:
        user_entity = users_pb2.User(ID=player_info[0],
                                     nickname=player_info[1],
                                     isGuest=player_info[2],
                                     rating=player_info[3])
        player = pb2.Player(userEntity=user_entity, isReady=bool(player_info[4]-1))
        full_current_lobby_info.players.append(player)

    return full_current_lobby_info

        
def validateSettings(settings: pb2.LobbySettings, config: dict) -> dict:
    valid_settings = dict()

    valid_settings["name"] = settings.name[:32]
    
    if settings.type != pb2.LobbyType.PUBLIC and settings.type != pb2.LobbyType.PRIVATE:
        raise ValueError('Bad lobby type')
    elif settings.type == pb2.LobbyType.PUBLIC:
        valid_settings["type"] = pb2.LobbyType.Value('PUBLIC') + 1
    elif settings.type == pb2.LobbyType.PRIVATE:
        valid_settings["type"] = pb2.LobbyType.Value('PRIVATE') + 1
        if not settings.password:
            raise ValueError('Empty password where lobby is PRIVATE')
            
    if settings.victoryType < 3:
        valid_settings["victoryType"] = settings.victoryType + 1
    else:
        raise ValueError('Bad victory type')

    if (settings.maxPlayers < config["LobbyRestrictions"]["minMaxPlayers"] or 
        settings.maxPlayers > config["LobbyRestrictions"]["maxMaxPlayers"] or
        settings.timeForTurn < config["LobbyRestrictions"]["minTimeForTurn"] or
        settings.timeForTurn > config["LobbyRestrictions"]["maxTimeForTurn"] or
        settings.scoreVictoryValue < config["LobbyRestrictions"]["minScoreVictoryValue"] or
        settings.scoreVictoryValue > config["LobbyRestrictions"]["maxScoreVictoryValue"] or
        settings.turnVictoryValue < config["LobbyRestrictions"]["minTurnVictoryValue"] or
        settings.turnVictoryValue > config["LobbyRestrictions"]["maxTurnVictoryValue"]):
        raise ValueError('Bad settings Restrictions')

    valid_settings["password"] = "" if not settings.password else settings.password[:16]
    valid_settings["maxPlayers"] = settings.maxPlayers
    valid_settings["timeForTurn"] = settings.timeForTurn
    valid_settings["scoreVictoryValue"] = settings.scoreVictoryValue
    valid_settings["turnVictoryValue"] = settings.turnVictoryValue
    
    return valid_settings
    
async def serve(config: dict, logger: logging.Logger) -> None:
    server = grpc.aio.server()
    listener = Listener(config, logger)
    pb2_grpc.add_LobbiesServiceServicer_to_server(listener, server)
    listen_addr = '[::]:' + str(config['gRPC']['port'])
    server.add_insecure_port(listen_addr)
    logger.info('Starting server on %s', listen_addr)
    await server.start()
    await server.wait_for_termination()


def run(config: dict, logger: logging.Logger) -> None:
    asyncio.run(serve(config, logger))
