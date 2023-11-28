# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import todo_pb2
import todo_pb2_grpc
import user_pb2
import user_pb2_grpc
import os
data = [{
    'id': '1',
    'user_id': '1',
    'message': 'message 1'
}, {
    'id': '2',
    'user_id': '2',
    'message': 'message for 2 1'
}]

def validate_session():
    with grpc.insecure_channel(os.environ['USER_SERVICE_BASE_URL']) as channel:
        stub = user_pb2_grpc.UserStub(channel)
        response = stub.validateSession(user_pb2.ValidateSessionRequest(auth_token="2"))
        return response.user_id

class ToDo(todo_pb2_grpc.ToDoServicer):
    def getTodo(self, request, context):
        return todo_pb2.Todo(message="Hello, %s!" % request.id)

    def searchTodos(self, request, context):
        user_id = validate_session()
        user_data = list(filter(lambda d: d['user_id'] == user_id, data))
        return todo_pb2.TodoSearchResult(todos=list(map(lambda d: todo_pb2.Todo(message=d['message']), user_data)))


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_ToDoServicer_to_server(ToDo(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()