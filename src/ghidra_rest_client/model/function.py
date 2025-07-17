
from dataclasses import dataclass
from .common import GhidraFunctionParameter


@dataclass
class GhidraAddressRange:
    max_address: int
    max_address_space_id: int
    min_address: int
    min_address_space_id: int


@dataclass
class GhidraFunction:
    name: str
    return_type_path_name: str
    parameters: list[GhidraFunctionParameter]
    has_var_args: bool
    entry_point: int
    entry_point_space_id: int
    address_ranges: list[GhidraAddressRange]
