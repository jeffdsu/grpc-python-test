import typing
import strawberry
import grpc
import todo_pb2
import todo_pb2_grpc
import os
from fastapi import FastAPI
import fastapi
from fastapi.middleware.cors import CORSMiddleware
from strawberry.asgi import GraphQL
def get_todos():

    with grpc.insecure_channel(os.environ['TODO_SERVICE_BASE_URL']) as channel:
        stub = todo_pb2_grpc.ToDoStub(channel)
        response = stub.searchTodos(todo_pb2.Null(id="123"))
        return list(map(lambda tododata: Todo(message=tododata.message), response.todos))


@strawberry.type
class Todo:
    message: str


@strawberry.type
class Query:
    searchTodos: typing.List[Todo] = strawberry.field(resolver=get_todos)




schema = strawberry.Schema(query=Query)

app = FastAPI()
app.mount("/graphql", GraphQL(schema, debug=True))
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.get("/health")
def health_check():
    return {"status": "healthy"}
