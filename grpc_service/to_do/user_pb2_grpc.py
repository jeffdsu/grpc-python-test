# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import user_pb2 as user__pb2


class UserStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.validateSession = channel.unary_unary(
                '/todo.User/validateSession',
                request_serializer=user__pb2.ValidateSessionRequest.SerializeToString,
                response_deserializer=user__pb2.Session.FromString,
                )


class UserServicer(object):
    """The greeting service definition.
    """

    def validateSession(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'validateSession': grpc.unary_unary_rpc_method_handler(
                    servicer.validateSession,
                    request_deserializer=user__pb2.ValidateSessionRequest.FromString,
                    response_serializer=user__pb2.Session.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todo.User', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class User(object):
    """The greeting service definition.
    """

    @staticmethod
    def validateSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todo.User/validateSession',
            user__pb2.ValidateSessionRequest.SerializeToString,
            user__pb2.Session.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
