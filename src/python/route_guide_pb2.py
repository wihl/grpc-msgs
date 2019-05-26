# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: route_guide.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='route_guide.proto',
  package='routeguide',
  syntax='proto3',
  serialized_options=_b('\n\033io.grpc.examples.routeguideB\017RouteGuideProtoP\001\242\002\003RTG'),
  serialized_pb=_b('\n\x11route_guide.proto\x12\nrouteguide\"5\n\nStreamDesc\x12\x15\n\rbytes_per_row\x18\x01 \x01(\x03\x12\x10\n\x08num_rows\x18\x02 \x01(\x03\"9\n\x0eUniaryResponse\x12\'\n\x03msg\x18\x01 \x03(\x0b\x32\x1a.routeguide.StreamResponse\"*\n\x0eStreamResponse\x12\x0b\n\x03row\x18\x01 \x01(\t\x12\x0b\n\x03\x63rc\x18\x02 \x01(\x05\x32\x96\x01\n\nRouteGuide\x12\x43\n\x0bGenRepeated\x12\x16.routeguide.StreamDesc\x1a\x1a.routeguide.UniaryResponse\"\x00\x12\x43\n\tGenStream\x12\x16.routeguide.StreamDesc\x1a\x1a.routeguide.StreamResponse\"\x00\x30\x01\x42\x36\n\x1bio.grpc.examples.routeguideB\x0fRouteGuideProtoP\x01\xa2\x02\x03RTGb\x06proto3')
)




_STREAMDESC = _descriptor.Descriptor(
  name='StreamDesc',
  full_name='routeguide.StreamDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes_per_row', full_name='routeguide.StreamDesc.bytes_per_row', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_rows', full_name='routeguide.StreamDesc.num_rows', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=86,
)


_UNIARYRESPONSE = _descriptor.Descriptor(
  name='UniaryResponse',
  full_name='routeguide.UniaryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='routeguide.UniaryResponse.msg', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=145,
)


_STREAMRESPONSE = _descriptor.Descriptor(
  name='StreamResponse',
  full_name='routeguide.StreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='routeguide.StreamResponse.row', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='crc', full_name='routeguide.StreamResponse.crc', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=189,
)

_UNIARYRESPONSE.fields_by_name['msg'].message_type = _STREAMRESPONSE
DESCRIPTOR.message_types_by_name['StreamDesc'] = _STREAMDESC
DESCRIPTOR.message_types_by_name['UniaryResponse'] = _UNIARYRESPONSE
DESCRIPTOR.message_types_by_name['StreamResponse'] = _STREAMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamDesc = _reflection.GeneratedProtocolMessageType('StreamDesc', (_message.Message,), dict(
  DESCRIPTOR = _STREAMDESC,
  __module__ = 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:routeguide.StreamDesc)
  ))
_sym_db.RegisterMessage(StreamDesc)

UniaryResponse = _reflection.GeneratedProtocolMessageType('UniaryResponse', (_message.Message,), dict(
  DESCRIPTOR = _UNIARYRESPONSE,
  __module__ = 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:routeguide.UniaryResponse)
  ))
_sym_db.RegisterMessage(UniaryResponse)

StreamResponse = _reflection.GeneratedProtocolMessageType('StreamResponse', (_message.Message,), dict(
  DESCRIPTOR = _STREAMRESPONSE,
  __module__ = 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:routeguide.StreamResponse)
  ))
_sym_db.RegisterMessage(StreamResponse)


DESCRIPTOR._options = None

_ROUTEGUIDE = _descriptor.ServiceDescriptor(
  name='RouteGuide',
  full_name='routeguide.RouteGuide',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=192,
  serialized_end=342,
  methods=[
  _descriptor.MethodDescriptor(
    name='GenRepeated',
    full_name='routeguide.RouteGuide.GenRepeated',
    index=0,
    containing_service=None,
    input_type=_STREAMDESC,
    output_type=_UNIARYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GenStream',
    full_name='routeguide.RouteGuide.GenStream',
    index=1,
    containing_service=None,
    input_type=_STREAMDESC,
    output_type=_STREAMRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROUTEGUIDE)

DESCRIPTOR.services_by_name['RouteGuide'] = _ROUTEGUIDE

# @@protoc_insertion_point(module_scope)
