# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04todo\",\n\x16ValidateSessionRequest\x12\x12\n\nauth_token\x18\x01 \x01(\t\"&\n\x07Session\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t2H\n\x04User\x12@\n\x0fvalidateSession\x12\x1c.todo.ValidateSessionRequest\x1a\r.todo.Session\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_VALIDATESESSIONREQUEST']._serialized_start=20
  _globals['_VALIDATESESSIONREQUEST']._serialized_end=64
  _globals['_SESSION']._serialized_start=66
  _globals['_SESSION']._serialized_end=104
  _globals['_USER']._serialized_start=106
  _globals['_USER']._serialized_end=178
# @@protoc_insertion_point(module_scope)
