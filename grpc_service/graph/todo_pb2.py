# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntodo.proto\x12\x04todo\"\x1c\n\x0eGetToDoRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x12\n\x04Null\x12\n\n\x02id\x18\x01 \x01(\t\"\x17\n\x04Todo\x12\x0f\n\x07message\x18\x01 \x01(\t\"-\n\x10TodoSearchResult\x12\x19\n\x05todos\x18\x01 \x03(\x0b\x32\n.todo.Todo2j\n\x04ToDo\x12-\n\x07getTodo\x12\x14.todo.GetToDoRequest\x1a\n.todo.Todo\"\x00\x12\x33\n\x0bsearchTodos\x12\n.todo.Null\x1a\x16.todo.TodoSearchResult\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'todo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETTODOREQUEST']._serialized_start=20
  _globals['_GETTODOREQUEST']._serialized_end=48
  _globals['_NULL']._serialized_start=50
  _globals['_NULL']._serialized_end=68
  _globals['_TODO']._serialized_start=70
  _globals['_TODO']._serialized_end=93
  _globals['_TODOSEARCHRESULT']._serialized_start=95
  _globals['_TODOSEARCHRESULT']._serialized_end=140
  _globals['_TODO']._serialized_start=142
  _globals['_TODO']._serialized_end=248
# @@protoc_insertion_point(module_scope)