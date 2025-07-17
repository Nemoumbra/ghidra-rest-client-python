
from dataclasses import dataclass


@dataclass
class GhidraMemoryBlock:
    name: str
    comment: str
    source_name: str
    address_space_name: str
    address_space_id: int
    start: int
    end: int
    size: int
    read: bool
    write: bool
    execute: bool
    volatile: bool
    overlay: bool
    initialized: bool
    mapped: bool
    external: bool
    loaded: bool
    artificial: bool
    type: str
