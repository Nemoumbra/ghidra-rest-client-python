
from dataclasses import dataclass

from .address_space import GhidraAddressSpace
from .bookmark import GhidraBookmark
from .memory_block import GhidraMemoryBlock
from .relocation import GhidraRelocation
from .function import GhidraFunction
from .symbol import GhidraSymbol
from .type import (
    GhidraEnumType, GhidraTypedefType, GhidraPointerType, GhidraArrayType, GhidraStructType,
    GhidraUnionType, GhidraFunctionDefinitionType, GhidraBuiltinType, GhidraUnknownType
)


@dataclass
class GhidraAddressSpacesResult:
    address_spaces: list[GhidraAddressSpace]


@dataclass
class GhidraBookmarksResult:
    bookmarks: list[GhidraBookmark]


@dataclass
class GhidraMemoryBlocksResult:
    memory_blocks: list[GhidraMemoryBlock]


@dataclass
class GhidraMemoryResult:
    memory: str


@dataclass
class GhidraRelocationsResult:
    relocations: list[GhidraRelocation]


@dataclass
class GhidraFunctionsResult:
    functions: list[GhidraFunction]


@dataclass
class GhidraSymbolsResult:
    symbols: list[GhidraSymbol]


@dataclass
class GhidraTypesResult:
    types: list[GhidraEnumType | GhidraTypedefType | GhidraPointerType | GhidraArrayType | GhidraStructType | GhidraUnionType | GhidraFunctionDefinitionType | GhidraBuiltinType | GhidraUnknownType]
