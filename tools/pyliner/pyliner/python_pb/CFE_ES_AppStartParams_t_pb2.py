# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _py_CFE_ES_AppStartParams_t.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='_py_CFE_ES_AppStartParams_t.proto',
  package='',
  serialized_pb=_b('\n!_py_CFE_ES_AppStartParams_t.proto\"\xb6\x01\n\x1a\x43\x46\x45_ES_AppStartParams_t_pb\x12\x0c\n\x04Name\x18\x01 \x02(\t\x12\x10\n\x08\x46ileName\x18\x02 \x02(\t\x12\x10\n\x08Priority\x18\x03 \x02(\r\x12\x12\n\nEntryPoint\x18\x04 \x02(\t\x12\x14\n\x0cStartAddress\x18\x05 \x02(\r\x12\x11\n\tStackSize\x18\x06 \x02(\r\x12\x17\n\x0f\x45xceptionAction\x18\x07 \x02(\r\x12\x10\n\x08ModuleId\x18\x08 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CFE_ES_APPSTARTPARAMS_T_PB = _descriptor.Descriptor(
  name='CFE_ES_AppStartParams_t_pb',
  full_name='CFE_ES_AppStartParams_t_pb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='CFE_ES_AppStartParams_t_pb.Name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FileName', full_name='CFE_ES_AppStartParams_t_pb.FileName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Priority', full_name='CFE_ES_AppStartParams_t_pb.Priority', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EntryPoint', full_name='CFE_ES_AppStartParams_t_pb.EntryPoint', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StartAddress', full_name='CFE_ES_AppStartParams_t_pb.StartAddress', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StackSize', full_name='CFE_ES_AppStartParams_t_pb.StackSize', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ExceptionAction', full_name='CFE_ES_AppStartParams_t_pb.ExceptionAction', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ModuleId', full_name='CFE_ES_AppStartParams_t_pb.ModuleId', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=220,
)

DESCRIPTOR.message_types_by_name['CFE_ES_AppStartParams_t_pb'] = _CFE_ES_APPSTARTPARAMS_T_PB

CFE_ES_AppStartParams_t_pb = _reflection.GeneratedProtocolMessageType('CFE_ES_AppStartParams_t_pb', (_message.Message,), dict(
  DESCRIPTOR = _CFE_ES_APPSTARTPARAMS_T_PB,
  __module__ = '_py_CFE_ES_AppStartParams_t_pb2'
  # @@protoc_insertion_point(class_scope:CFE_ES_AppStartParams_t_pb)
  ))
_sym_db.RegisterMessage(CFE_ES_AppStartParams_t_pb)


# @@protoc_insertion_point(module_scope)