
from dataclasses import dataclass
from typing import Literal
from .common import GhidraFunctionParameter


@dataclass
class GhidraEnumMember:
    name: str
    value: int
    comment: str


@dataclass
class GhidraEnumType:
    kind: Literal["ENUM"]
    name: str
    display_name: str
    path_name: str
    length: int
    aligned_length: int
    zero_length: bool
    not_yet_defined: bool
    description: str
    members: list[GhidraEnumMember]


@dataclass
class GhidraTypedefType:
    kind: Literal["TYPEDEF"]
    name: str
    display_name: str
    path_name: str
    length: int
    aligned_length: int
    zero_length: bool
    not_yet_defined: bool
    description: str
    type_path_name: str
    base_type_path_name: str


@dataclass
class GhidraPointerType:
    kind: Literal["POINTER"]
    name: str
    display_name: str
    path_name: str
    length: int
    aligned_length: int
    zero_length: bool
    not_yet_defined: bool
    description: str
    type_path_name: str

@dataclass
class GhidraArrayType:
    kind: Literal["ARRAY"]
    name: str
    display_name: str
    path_name: str
    length: int
    aligned_length: int
    zero_length: bool
    not_yet_defined: bool
    description: str
    type_path_name: str
    element_length: int
    element_count: int


@dataclass
class GhidraCompositeMember:
    field_name: str
    ordinal: int
    offset: int
    length: int
    type_path_name: str
    comment: str


@dataclass
class GhidraStructType:
    kind: Literal["STRUCTURE"]
    name: str
    display_name: str
    path_name: str
    length: int
    aligned_length: int
    zero_length: bool
    not_yet_defined: bool
    description: str
    members: list[GhidraCompositeMember]


@dataclass
class GhidraUnionType:
    kind: Literal["UNION"]
    name: str
    display_name: str
    path_name: str
    length: int
    aligned_length: int
    zero_length: bool
    not_yet_defined: bool
    description: str
    members: list[GhidraCompositeMember]


@dataclass
class GhidraFunctionDefinitionType:
    kind: Literal["FUNCTION_DEFINITION"]
    name: str
    display_name: str
    path_name: str
    length: int
    aligned_length: int
    zero_length: bool
    not_yet_defined: bool
    description: str
    prototype_string: str
    return_type_path_name: str
    parameters: list[GhidraFunctionParameter]


@dataclass
class GhidraBuiltinType:
    kind: Literal["BUILT_IN"]
    name: str
    display_name: str
    path_name: str
    length: int
    aligned_length: int
    zero_length: bool
    not_yet_defined: bool
    description: str
    group: str


@dataclass
class GhidraUnknownType:
    kind: Literal["UNKNOWN"]
    name: str
    display_name: str
    path_name: str
    length: int
    aligned_length: int
    zero_length: bool
    not_yet_defined: bool
    description: str
