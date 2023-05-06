# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import UsersMicroservice_pb2 as UsersMicroservice__pb2


class UsersServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AuthAsGuest = channel.unary_unary(
                '/UsersMicroservice.UsersService/AuthAsGuest',
                request_serializer=UsersMicroservice__pb2.AuthRequest.SerializeToString,
                response_deserializer=UsersMicroservice__pb2.AuthResponse.FromString,
                )
        self.AuthFromVK = channel.unary_unary(
                '/UsersMicroservice.UsersService/AuthFromVK',
                request_serializer=UsersMicroservice__pb2.AuthRequest.SerializeToString,
                response_deserializer=UsersMicroservice__pb2.AuthResponse.FromString,
                )
        self.ChangeNickname = channel.unary_unary(
                '/UsersMicroservice.UsersService/ChangeNickname',
                request_serializer=UsersMicroservice__pb2.ChangeNicknameRequest.SerializeToString,
                response_deserializer=UsersMicroservice__pb2.ChangeNicknameResponse.FromString,
                )
        self.RefreshAccessToken = channel.unary_unary(
                '/UsersMicroservice.UsersService/RefreshAccessToken',
                request_serializer=UsersMicroservice__pb2.RefreshAccessTokenRequest.SerializeToString,
                response_deserializer=UsersMicroservice__pb2.RefreshAccessTokenResponse.FromString,
                )
        self.GetInfo = channel.unary_unary(
                '/UsersMicroservice.UsersService/GetInfo',
                request_serializer=UsersMicroservice__pb2.GetInfoRequest.SerializeToString,
                response_deserializer=UsersMicroservice__pb2.GetInfoResponse.FromString,
                )


class UsersServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AuthAsGuest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuthFromVK(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeNickname(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RefreshAccessToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AuthAsGuest': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthAsGuest,
                    request_deserializer=UsersMicroservice__pb2.AuthRequest.FromString,
                    response_serializer=UsersMicroservice__pb2.AuthResponse.SerializeToString,
            ),
            'AuthFromVK': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthFromVK,
                    request_deserializer=UsersMicroservice__pb2.AuthRequest.FromString,
                    response_serializer=UsersMicroservice__pb2.AuthResponse.SerializeToString,
            ),
            'ChangeNickname': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeNickname,
                    request_deserializer=UsersMicroservice__pb2.ChangeNicknameRequest.FromString,
                    response_serializer=UsersMicroservice__pb2.ChangeNicknameResponse.SerializeToString,
            ),
            'RefreshAccessToken': grpc.unary_unary_rpc_method_handler(
                    servicer.RefreshAccessToken,
                    request_deserializer=UsersMicroservice__pb2.RefreshAccessTokenRequest.FromString,
                    response_serializer=UsersMicroservice__pb2.RefreshAccessTokenResponse.SerializeToString,
            ),
            'GetInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInfo,
                    request_deserializer=UsersMicroservice__pb2.GetInfoRequest.FromString,
                    response_serializer=UsersMicroservice__pb2.GetInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UsersMicroservice.UsersService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UsersService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AuthAsGuest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UsersMicroservice.UsersService/AuthAsGuest',
            UsersMicroservice__pb2.AuthRequest.SerializeToString,
            UsersMicroservice__pb2.AuthResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuthFromVK(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UsersMicroservice.UsersService/AuthFromVK',
            UsersMicroservice__pb2.AuthRequest.SerializeToString,
            UsersMicroservice__pb2.AuthResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeNickname(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UsersMicroservice.UsersService/ChangeNickname',
            UsersMicroservice__pb2.ChangeNicknameRequest.SerializeToString,
            UsersMicroservice__pb2.ChangeNicknameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RefreshAccessToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UsersMicroservice.UsersService/RefreshAccessToken',
            UsersMicroservice__pb2.RefreshAccessTokenRequest.SerializeToString,
            UsersMicroservice__pb2.RefreshAccessTokenResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/UsersMicroservice.UsersService/GetInfo',
            UsersMicroservice__pb2.GetInfoRequest.SerializeToString,
            UsersMicroservice__pb2.GetInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)