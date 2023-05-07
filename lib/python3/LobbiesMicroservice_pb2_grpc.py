# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import LobbiesMicroservice_pb2 as LobbiesMicroservice__pb2


class LobbiesServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/LobbiesMicroservice.LobbiesService/Create',
                request_serializer=LobbiesMicroservice__pb2.SetSettingsRequest.SerializeToString,
                response_deserializer=LobbiesMicroservice__pb2.AboutLobbyResponse.FromString,
                )
        self.GetList = channel.unary_unary(
                '/LobbiesMicroservice.LobbiesService/GetList',
                request_serializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
                response_deserializer=LobbiesMicroservice__pb2.GetListResponse.FromString,
                )
        self.Connect = channel.unary_unary(
                '/LobbiesMicroservice.LobbiesService/Connect',
                request_serializer=LobbiesMicroservice__pb2.ConnectRequest.SerializeToString,
                response_deserializer=LobbiesMicroservice__pb2.AboutLobbyResponse.FromString,
                )
        self.GetInfo = channel.unary_unary(
                '/LobbiesMicroservice.LobbiesService/GetInfo',
                request_serializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
                response_deserializer=LobbiesMicroservice__pb2.AboutLobbyResponse.FromString,
                )
        self.UpdateSettings = channel.unary_unary(
                '/LobbiesMicroservice.LobbiesService/UpdateSettings',
                request_serializer=LobbiesMicroservice__pb2.SetSettingsRequest.SerializeToString,
                response_deserializer=LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
                )
        self.ConnectToRanked = channel.unary_unary(
                '/LobbiesMicroservice.LobbiesService/ConnectToRanked',
                request_serializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
                response_deserializer=LobbiesMicroservice__pb2.AboutLobbyResponse.FromString,
                )
        self.Disconnect = channel.unary_unary(
                '/LobbiesMicroservice.LobbiesService/Disconnect',
                request_serializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
                response_deserializer=LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
                )
        self.SwitchReadiness = channel.unary_unary(
                '/LobbiesMicroservice.LobbiesService/SwitchReadiness',
                request_serializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
                response_deserializer=LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
                )
        self.RaisePlayer = channel.unary_unary(
                '/LobbiesMicroservice.LobbiesService/RaisePlayer',
                request_serializer=LobbiesMicroservice__pb2.RequesterAndTargetRequest.SerializeToString,
                response_deserializer=LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
                )
        self.KickPlayer = channel.unary_unary(
                '/LobbiesMicroservice.LobbiesService/KickPlayer',
                request_serializer=LobbiesMicroservice__pb2.RequesterAndTargetRequest.SerializeToString,
                response_deserializer=LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
                )
        self.CheckInActive = channel.unary_unary(
                '/LobbiesMicroservice.LobbiesService/CheckInActive',
                request_serializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
                response_deserializer=LobbiesMicroservice__pb2.CheckInActiveResponse.FromString,
                )
        self.Run = channel.unary_unary(
                '/LobbiesMicroservice.LobbiesService/Run',
                request_serializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
                response_deserializer=LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/LobbiesMicroservice.LobbiesService/Delete',
                request_serializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
                response_deserializer=LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
                )


class LobbiesServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Connect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConnectToRanked(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disconnect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SwitchReadiness(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RaisePlayer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KickPlayer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckInActive(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Run(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LobbiesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=LobbiesMicroservice__pb2.SetSettingsRequest.FromString,
                    response_serializer=LobbiesMicroservice__pb2.AboutLobbyResponse.SerializeToString,
            ),
            'GetList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetList,
                    request_deserializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.FromString,
                    response_serializer=LobbiesMicroservice__pb2.GetListResponse.SerializeToString,
            ),
            'Connect': grpc.unary_unary_rpc_method_handler(
                    servicer.Connect,
                    request_deserializer=LobbiesMicroservice__pb2.ConnectRequest.FromString,
                    response_serializer=LobbiesMicroservice__pb2.AboutLobbyResponse.SerializeToString,
            ),
            'GetInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInfo,
                    request_deserializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.FromString,
                    response_serializer=LobbiesMicroservice__pb2.AboutLobbyResponse.SerializeToString,
            ),
            'UpdateSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSettings,
                    request_deserializer=LobbiesMicroservice__pb2.SetSettingsRequest.FromString,
                    response_serializer=LobbiesMicroservice__pb2.StatusOnlyResponse.SerializeToString,
            ),
            'ConnectToRanked': grpc.unary_unary_rpc_method_handler(
                    servicer.ConnectToRanked,
                    request_deserializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.FromString,
                    response_serializer=LobbiesMicroservice__pb2.AboutLobbyResponse.SerializeToString,
            ),
            'Disconnect': grpc.unary_unary_rpc_method_handler(
                    servicer.Disconnect,
                    request_deserializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.FromString,
                    response_serializer=LobbiesMicroservice__pb2.StatusOnlyResponse.SerializeToString,
            ),
            'SwitchReadiness': grpc.unary_unary_rpc_method_handler(
                    servicer.SwitchReadiness,
                    request_deserializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.FromString,
                    response_serializer=LobbiesMicroservice__pb2.StatusOnlyResponse.SerializeToString,
            ),
            'RaisePlayer': grpc.unary_unary_rpc_method_handler(
                    servicer.RaisePlayer,
                    request_deserializer=LobbiesMicroservice__pb2.RequesterAndTargetRequest.FromString,
                    response_serializer=LobbiesMicroservice__pb2.StatusOnlyResponse.SerializeToString,
            ),
            'KickPlayer': grpc.unary_unary_rpc_method_handler(
                    servicer.KickPlayer,
                    request_deserializer=LobbiesMicroservice__pb2.RequesterAndTargetRequest.FromString,
                    response_serializer=LobbiesMicroservice__pb2.StatusOnlyResponse.SerializeToString,
            ),
            'CheckInActive': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckInActive,
                    request_deserializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.FromString,
                    response_serializer=LobbiesMicroservice__pb2.CheckInActiveResponse.SerializeToString,
            ),
            'Run': grpc.unary_unary_rpc_method_handler(
                    servicer.Run,
                    request_deserializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.FromString,
                    response_serializer=LobbiesMicroservice__pb2.StatusOnlyResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=LobbiesMicroservice__pb2.RequesterOnlyRequest.FromString,
                    response_serializer=LobbiesMicroservice__pb2.StatusOnlyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LobbiesMicroservice.LobbiesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LobbiesService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LobbiesMicroservice.LobbiesService/Create',
            LobbiesMicroservice__pb2.SetSettingsRequest.SerializeToString,
            LobbiesMicroservice__pb2.AboutLobbyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LobbiesMicroservice.LobbiesService/GetList',
            LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
            LobbiesMicroservice__pb2.GetListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Connect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LobbiesMicroservice.LobbiesService/Connect',
            LobbiesMicroservice__pb2.ConnectRequest.SerializeToString,
            LobbiesMicroservice__pb2.AboutLobbyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LobbiesMicroservice.LobbiesService/GetInfo',
            LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
            LobbiesMicroservice__pb2.AboutLobbyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LobbiesMicroservice.LobbiesService/UpdateSettings',
            LobbiesMicroservice__pb2.SetSettingsRequest.SerializeToString,
            LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConnectToRanked(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LobbiesMicroservice.LobbiesService/ConnectToRanked',
            LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
            LobbiesMicroservice__pb2.AboutLobbyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disconnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LobbiesMicroservice.LobbiesService/Disconnect',
            LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
            LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SwitchReadiness(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LobbiesMicroservice.LobbiesService/SwitchReadiness',
            LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
            LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RaisePlayer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LobbiesMicroservice.LobbiesService/RaisePlayer',
            LobbiesMicroservice__pb2.RequesterAndTargetRequest.SerializeToString,
            LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KickPlayer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LobbiesMicroservice.LobbiesService/KickPlayer',
            LobbiesMicroservice__pb2.RequesterAndTargetRequest.SerializeToString,
            LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckInActive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LobbiesMicroservice.LobbiesService/CheckInActive',
            LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
            LobbiesMicroservice__pb2.CheckInActiveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Run(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LobbiesMicroservice.LobbiesService/Run',
            LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
            LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LobbiesMicroservice.LobbiesService/Delete',
            LobbiesMicroservice__pb2.RequesterOnlyRequest.SerializeToString,
            LobbiesMicroservice__pb2.StatusOnlyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
