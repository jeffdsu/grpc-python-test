
from __future__ import print_function

import logging

import grpc
import user_pb2
import user_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = user_pb2_grpc.UserStub(channel)
        response = stub.validateSession(user_pb2.ValidateSessionRequest(auth_token="2"))
    print("Greeter client received: " + str(response))


if __name__ == "__main__":
    logging.basicConfig()
    run()