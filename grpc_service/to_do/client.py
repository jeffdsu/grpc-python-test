
from __future__ import print_function

import logging

import grpc
import todo_pb2
import todo_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = todo_pb2_grpc.ToDoStub(channel)
        response = stub.searchTodos(todo_pb2.Null(id="123"))
    print("Greeter client received: " + str(response))


if __name__ == "__main__":
    logging.basicConfig()
    run()