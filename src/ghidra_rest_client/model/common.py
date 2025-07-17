
from dataclasses import dataclass


@dataclass
class GhidraFunctionParameter:
    ordinal: int
    name: str
    data_type_path_name: str
