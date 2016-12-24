# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player/player_stats.proto

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
  name='pogoprotos/data/player/player_stats.proto',
  package='pogoprotos.data.player',
  syntax='proto3',
  serialized_pb=_b('\n)pogoprotos/data/player/player_stats.proto\x12\x16pogoprotos.data.player\"\x9e\x05\n\x0bPlayerStats\x12\r\n\x05level\x18\x01 \x01(\x05\x12\x12\n\nexperience\x18\x02 \x01(\x03\x12\x15\n\rprev_level_xp\x18\x03 \x01(\x03\x12\x15\n\rnext_level_xp\x18\x04 \x01(\x03\x12\x11\n\tkm_walked\x18\x05 \x01(\x02\x12\x1c\n\x14pokemons_encountered\x18\x06 \x01(\x05\x12\x1e\n\x16unique_pokedex_entries\x18\x07 \x01(\x05\x12\x19\n\x11pokemons_captured\x18\x08 \x01(\x05\x12\x12\n\nevolutions\x18\t \x01(\x05\x12\x18\n\x10poke_stop_visits\x18\n \x01(\x05\x12\x18\n\x10pokeballs_thrown\x18\x0b \x01(\x05\x12\x14\n\x0c\x65ggs_hatched\x18\x0c \x01(\x05\x12\x1b\n\x13\x62ig_magikarp_caught\x18\r \x01(\x05\x12\x19\n\x11\x62\x61ttle_attack_won\x18\x0e \x01(\x05\x12\x1b\n\x13\x62\x61ttle_attack_total\x18\x0f \x01(\x05\x12\x1b\n\x13\x62\x61ttle_defended_won\x18\x10 \x01(\x05\x12\x1b\n\x13\x62\x61ttle_training_won\x18\x11 \x01(\x05\x12\x1d\n\x15\x62\x61ttle_training_total\x18\x12 \x01(\x05\x12\x1d\n\x15prestige_raised_total\x18\x13 \x01(\x05\x12\x1e\n\x16prestige_dropped_total\x18\x14 \x01(\x05\x12\x18\n\x10pokemon_deployed\x18\x15 \x01(\x05\x12\x1e\n\x16pokemon_caught_by_type\x18\x16 \x03(\x05\x12\x1c\n\x14small_rattata_caught\x18\x17 \x01(\x05\x12\x14\n\x0cused_km_pool\x18\x18 \x01(\x01\x12\x19\n\x11last_km_refill_ms\x18\x19 \x01(\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PLAYERSTATS = _descriptor.Descriptor(
  name='PlayerStats',
  full_name='pogoprotos.data.player.PlayerStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='pogoprotos.data.player.PlayerStats.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experience', full_name='pogoprotos.data.player.PlayerStats.experience', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prev_level_xp', full_name='pogoprotos.data.player.PlayerStats.prev_level_xp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_level_xp', full_name='pogoprotos.data.player.PlayerStats.next_level_xp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='km_walked', full_name='pogoprotos.data.player.PlayerStats.km_walked', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemons_encountered', full_name='pogoprotos.data.player.PlayerStats.pokemons_encountered', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_pokedex_entries', full_name='pogoprotos.data.player.PlayerStats.unique_pokedex_entries', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemons_captured', full_name='pogoprotos.data.player.PlayerStats.pokemons_captured', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolutions', full_name='pogoprotos.data.player.PlayerStats.evolutions', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='poke_stop_visits', full_name='pogoprotos.data.player.PlayerStats.poke_stop_visits', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokeballs_thrown', full_name='pogoprotos.data.player.PlayerStats.pokeballs_thrown', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eggs_hatched', full_name='pogoprotos.data.player.PlayerStats.eggs_hatched', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='big_magikarp_caught', full_name='pogoprotos.data.player.PlayerStats.big_magikarp_caught', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_attack_won', full_name='pogoprotos.data.player.PlayerStats.battle_attack_won', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_attack_total', full_name='pogoprotos.data.player.PlayerStats.battle_attack_total', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_defended_won', full_name='pogoprotos.data.player.PlayerStats.battle_defended_won', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_training_won', full_name='pogoprotos.data.player.PlayerStats.battle_training_won', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_training_total', full_name='pogoprotos.data.player.PlayerStats.battle_training_total', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prestige_raised_total', full_name='pogoprotos.data.player.PlayerStats.prestige_raised_total', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prestige_dropped_total', full_name='pogoprotos.data.player.PlayerStats.prestige_dropped_total', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_deployed', full_name='pogoprotos.data.player.PlayerStats.pokemon_deployed', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_caught_by_type', full_name='pogoprotos.data.player.PlayerStats.pokemon_caught_by_type', index=21,
      number=22, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='small_rattata_caught', full_name='pogoprotos.data.player.PlayerStats.small_rattata_caught', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='used_km_pool', full_name='pogoprotos.data.player.PlayerStats.used_km_pool', index=23,
      number=24, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_km_refill_ms', full_name='pogoprotos.data.player.PlayerStats.last_km_refill_ms', index=24,
      number=25, type=3, cpp_type=2, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=740,
)

DESCRIPTOR.message_types_by_name['PlayerStats'] = _PLAYERSTATS

PlayerStats = _reflection.GeneratedProtocolMessageType('PlayerStats', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERSTATS,
  __module__ = 'pogoprotos.data.player.player_stats_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.player.PlayerStats)
  ))
_sym_db.RegisterMessage(PlayerStats)


# @@protoc_insertion_point(module_scope)
