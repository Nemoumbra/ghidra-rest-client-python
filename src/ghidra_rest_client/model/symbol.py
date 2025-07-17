
from dataclasses import dataclass


@dataclass
class GhidraSymbol:
    address: int
    address_space_id: int
    name: str
    type: str
    global_: bool  # Note: adaptix trims the underscores to allow handling the reserved Python keywords
    primary: bool
    pinned: bool
    external_entry_point: bool
    source: str
    namespace: str
    pre_comment: str
    data_type_path_name: str | None  # Maybe Omittable works too?
