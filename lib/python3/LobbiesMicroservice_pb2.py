# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LobbiesMicroservice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import UsersMicroservice_pb2 as UsersMicroservice__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19LobbiesMicroservice.proto\x12\x13LobbiesMicroservice\x1a\x17UsersMicroservice.proto\"\xb9\x02\n\rLobbySettings\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x04type\x18\x02 \x01(\x0e\x32\x1e.LobbiesMicroservice.LobbyType\x12\x15\n\x08password\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x12\n\nmaxPlayers\x18\x04 \x01(\r\x12\x13\n\x0btimeForTurn\x18\x05 \x01(\r\x12\x35\n\x0bvictoryType\x18\x06 \x01(\x0e\x32 .LobbiesMicroservice.VictoryType\x12\x1e\n\x11scoreVictoryValue\x18\x07 \x01(\x05H\x01\x88\x01\x01\x12\x1d\n\x10turnVictoryValue\x18\x08 \x01(\x05H\x02\x88\x01\x01\x42\x0b\n\t_passwordB\x14\n\x12_scoreVictoryValueB\x13\n\x11_turnVictoryValue\"F\n\x06Player\x12+\n\nuserEntity\x18\x01 \x01(\x0b\x32\x17.UsersMicroservice.User\x12\x0f\n\x07isReady\x18\x02 \x01(\x08\"3\n\x12GameConnectionInfo\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"q\n\x15ShortCurrentLobbyInfo\x12\x0f\n\x07lobbyID\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tisPrivate\x18\x03 \x01(\x08\x12\x12\n\nmaxPlayers\x18\x04 \x01(\r\x12\x12\n\nplayersNow\x18\x05 \x01(\r\"\x86\x02\n\x14\x46ullCurrentLobbyInfo\x12\x0f\n\x07lobbyID\x18\x01 \x01(\r\x12\x0f\n\x07ownerID\x18\x02 \x01(\r\x12\x34\n\x08settings\x18\x03 \x01(\x0b\x32\".LobbiesMicroservice.LobbySettings\x12,\n\x07players\x18\x04 \x03(\x0b\x32\x1b.LobbiesMicroservice.Player\x12\x17\n\x0ftimerIsActivate\x18\x05 \x01(\x08\x12@\n\nconnection\x18\x06 \x01(\x0b\x32\'.LobbiesMicroservice.GameConnectionInfoH\x00\x88\x01\x01\x42\r\n\x0b_connection\"\x96\x01\n\x12\x41\x62outLobbyResponse\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.LobbiesMicroservice.ExitStatus\x12\x41\n\tlobbyInfo\x18\x02 \x01(\x0b\x32).LobbiesMicroservice.FullCurrentLobbyInfoH\x00\x88\x01\x01\x42\x0c\n\n_lobbyInfo\"+\n\x14RequesterOnlyRequest\x12\x13\n\x0brequesterID\x18\x01 \x01(\r\"H\n\x19RequesterAndTargetRequest\x12\x13\n\x0brequesterID\x18\x01 \x01(\r\x12\x16\n\x0etargetPlayerID\x18\x02 \x01(\r\"E\n\x12StatusOnlyResponse\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.LobbiesMicroservice.ExitStatus\"l\n\rCreateRequest\x12\x13\n\x0brequesterID\x18\x01 \x01(\r\x12\x39\n\x08settings\x18\x02 \x01(\x0b\x32\".LobbiesMicroservice.LobbySettingsH\x00\x88\x01\x01\x42\x0b\n\t_settings\"Z\n\x0e\x43onnectRequest\x12\x13\n\x0brequesterID\x18\x01 \x01(\r\x12\x0f\n\x07lobbyID\x18\x02 \x01(\r\x12\x15\n\x08password\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_password\"\x7f\n\x0fGetListResponse\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.LobbiesMicroservice.ExitStatus\x12;\n\x07lobbies\x18\x02 \x03(\x0b\x32*.LobbiesMicroservice.ShortCurrentLobbyInfo\"b\n\x15UpdateSettingsRequest\x12\x13\n\x0brequesterID\x18\x01 \x01(\r\x12\x34\n\x08settings\x18\x02 \x01(\x0b\x32\".LobbiesMicroservice.LobbySettings\"q\n\x16UpdateSettingsResponse\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.LobbiesMicroservice.ExitStatus\x12\x17\n\nerrMessage\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\r\n\x0b_errMessage\"\x99\x01\n\x15\x43heckInActiveResponse\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.LobbiesMicroservice.ExitStatus\x12@\n\nconnection\x18\x02 \x01(\x0b\x32\'.LobbiesMicroservice.GameConnectionInfoH\x00\x88\x01\x01\x42\r\n\x0b_connection*\x95\x01\n\nExitStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\x10\n\x0c\x43ODING_ERROR\x10\x01\x12\x12\n\x0e\x44\x45\x43ODING_ERROR\x10\x02\x12\x15\n\x11\x46\x41ILED_DEPENDENCY\x10\x03\x12\x1a\n\x16RESOURCE_NOT_AVAILABLE\x10\x04\x12\x12\n\x0e\x44\x42_LEVEL_ERROR\x10\x05\x12\r\n\tBAD_VALUE\x10\x06*,\n\x0bVictoryType\x12\t\n\x05SCORE\x10\x00\x12\x08\n\x04TURN\x10\x01\x12\x08\n\x04\x42OTH\x10\x02*0\n\tLobbyType\x12\n\n\x06PUBLIC\x10\x00\x12\x0b\n\x07PRIVATE\x10\x01\x12\n\n\x06RANKED\x10\x02\x32\x86\n\n\x0eLobbiesService\x12U\n\x06\x43reate\x12\".LobbiesMicroservice.CreateRequest\x1a\'.LobbiesMicroservice.AboutLobbyResponse\x12Z\n\x07GetList\x12).LobbiesMicroservice.RequesterOnlyRequest\x1a$.LobbiesMicroservice.GetListResponse\x12W\n\x07\x43onnect\x12#.LobbiesMicroservice.ConnectRequest\x1a\'.LobbiesMicroservice.AboutLobbyResponse\x12]\n\x07GetInfo\x12).LobbiesMicroservice.RequesterOnlyRequest\x1a\'.LobbiesMicroservice.AboutLobbyResponse\x12i\n\x0eUpdateSettings\x12*.LobbiesMicroservice.UpdateSettingsRequest\x1a+.LobbiesMicroservice.UpdateSettingsResponse\x12\x65\n\x0f\x43onnectToRanked\x12).LobbiesMicroservice.RequesterOnlyRequest\x1a\'.LobbiesMicroservice.AboutLobbyResponse\x12`\n\nDisconnect\x12).LobbiesMicroservice.RequesterOnlyRequest\x1a\'.LobbiesMicroservice.StatusOnlyResponse\x12\x65\n\x0fSwitchReadiness\x12).LobbiesMicroservice.RequesterOnlyRequest\x1a\'.LobbiesMicroservice.StatusOnlyResponse\x12\x66\n\x0bRaisePlayer\x12..LobbiesMicroservice.RequesterAndTargetRequest\x1a\'.LobbiesMicroservice.StatusOnlyResponse\x12\x65\n\nKickPlayer\x12..LobbiesMicroservice.RequesterAndTargetRequest\x1a\'.LobbiesMicroservice.StatusOnlyResponse\x12\x66\n\rCheckInActive\x12).LobbiesMicroservice.RequesterOnlyRequest\x1a*.LobbiesMicroservice.CheckInActiveResponse\x12Y\n\x03Run\x12).LobbiesMicroservice.RequesterOnlyRequest\x1a\'.LobbiesMicroservice.StatusOnlyResponse\x12\\\n\x06\x44\x65lete\x12).LobbiesMicroservice.RequesterOnlyRequest\x1a\'.LobbiesMicroservice.StatusOnlyResponseB\x0eZ\x0c./lobbies_pbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'LobbiesMicroservice_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\014./lobbies_pb'
  _EXITSTATUS._serialized_start=1942
  _EXITSTATUS._serialized_end=2091
  _VICTORYTYPE._serialized_start=2093
  _VICTORYTYPE._serialized_end=2137
  _LOBBYTYPE._serialized_start=2139
  _LOBBYTYPE._serialized_end=2187
  _LOBBYSETTINGS._serialized_start=76
  _LOBBYSETTINGS._serialized_end=389
  _PLAYER._serialized_start=391
  _PLAYER._serialized_end=461
  _GAMECONNECTIONINFO._serialized_start=463
  _GAMECONNECTIONINFO._serialized_end=514
  _SHORTCURRENTLOBBYINFO._serialized_start=516
  _SHORTCURRENTLOBBYINFO._serialized_end=629
  _FULLCURRENTLOBBYINFO._serialized_start=632
  _FULLCURRENTLOBBYINFO._serialized_end=894
  _ABOUTLOBBYRESPONSE._serialized_start=897
  _ABOUTLOBBYRESPONSE._serialized_end=1047
  _REQUESTERONLYREQUEST._serialized_start=1049
  _REQUESTERONLYREQUEST._serialized_end=1092
  _REQUESTERANDTARGETREQUEST._serialized_start=1094
  _REQUESTERANDTARGETREQUEST._serialized_end=1166
  _STATUSONLYRESPONSE._serialized_start=1168
  _STATUSONLYRESPONSE._serialized_end=1237
  _CREATEREQUEST._serialized_start=1239
  _CREATEREQUEST._serialized_end=1347
  _CONNECTREQUEST._serialized_start=1349
  _CONNECTREQUEST._serialized_end=1439
  _GETLISTRESPONSE._serialized_start=1441
  _GETLISTRESPONSE._serialized_end=1568
  _UPDATESETTINGSREQUEST._serialized_start=1570
  _UPDATESETTINGSREQUEST._serialized_end=1668
  _UPDATESETTINGSRESPONSE._serialized_start=1670
  _UPDATESETTINGSRESPONSE._serialized_end=1783
  _CHECKINACTIVERESPONSE._serialized_start=1786
  _CHECKINACTIVERESPONSE._serialized_end=1939
  _LOBBIESSERVICE._serialized_start=2190
  _LOBBIESSERVICE._serialized_end=3476
# @@protoc_insertion_point(module_scope)