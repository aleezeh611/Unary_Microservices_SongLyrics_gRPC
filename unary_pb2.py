# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unary.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bunary.proto\x12\x05unary\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"3\n\x0fMessageResponse\x12\x0e\n\x06lyrics\x18\x01 \x01(\t\x12\x10\n\x08received\x18\x02 \x01(\x08\x32\x46\n\x05Unary\x12=\n\x11GetServerResponse\x12\x0e.unary.Message\x1a\x16.unary.MessageResponse\"\x00\x62\x06proto3')



_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
_MESSAGERESPONSE = DESCRIPTOR.message_types_by_name['MessageResponse']
Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'unary_pb2'
  # @@protoc_insertion_point(class_scope:unary.Message)
  })
_sym_db.RegisterMessage(Message)

MessageResponse = _reflection.GeneratedProtocolMessageType('MessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERESPONSE,
  '__module__' : 'unary_pb2'
  # @@protoc_insertion_point(class_scope:unary.MessageResponse)
  })
_sym_db.RegisterMessage(MessageResponse)

_UNARY = DESCRIPTOR.services_by_name['Unary']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGE._serialized_start=22
  _MESSAGE._serialized_end=48
  _MESSAGERESPONSE._serialized_start=50
  _MESSAGERESPONSE._serialized_end=101
  _UNARY._serialized_start=103
  _UNARY._serialized_end=173
# @@protoc_insertion_point(module_scope)
