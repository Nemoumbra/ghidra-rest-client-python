
from dataclasses import dataclass


@dataclass
class GhidraAddressSpace:
    id: int
    physical_space_id: int
    default: bool
    name: str
    size: int
    addressable_unit_size: int
    pointer_size: int
    type: str
    mapped_registers: bool
    signed_offset: bool
    overlay_space: bool
    hash_space: bool
