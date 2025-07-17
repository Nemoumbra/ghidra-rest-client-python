
from dataclasses import dataclass


@dataclass
class GhidraBookmark:
    address: int
    address_space_id: int
    category: str
    comment: str
    id: int
    type: str
