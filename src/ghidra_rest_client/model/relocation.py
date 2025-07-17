
from dataclasses import dataclass


@dataclass
class GhidraRelocation:
    address: int
    address_space_id: int
    status: str
    type: int
    values: list[int]
    bytes: bytes | None
    symbol_name: str | None
