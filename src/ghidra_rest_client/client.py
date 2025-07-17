
from typing import Optional
from dataclass_rest.http.requests import RequestsClient
from dataclass_rest import get
from adaptix import Retort, name_mapping, NameStyle, dumper, as_is_loader

from .util import RawRequestsMethod

from .model.api_responses import (
    GhidraAddressSpacesResult, GhidraBookmarksResult, GhidraMemoryBlocksResult, GhidraMemoryResult,
    GhidraRelocationsResult, GhidraFunctionsResult, GhidraSymbolsResult, GhidraTypesResult
)

class GhidraClient(RequestsClient):
    kGhidraServerPort = 18489

    def __init__(self, uri: str | None = None):
        if uri is None:
            uri = f"http://127.0.0.1:{self.kGhidraServerPort}/"

        super().__init__(uri)

    def _init_request_args_factory(self) -> Retort:
        return Retort(recipe=[
            name_mapping(name_style=NameStyle.CAMEL),
            dumper(int, lambda value: hex(value))
        ])

    def _init_response_body_factory(self) -> Retort:
        return Retort(recipe=[
            name_mapping(name_style=NameStyle.CAMEL),
            as_is_loader(bytes)
        ])

    @get("/v1/address-spaces")
    def get_address_spaces(self) -> GhidraAddressSpacesResult:
        """Get the address spaces"""
        pass

    @get("/v1/bookmarks")
    def get_bookmarks(self) -> GhidraBookmarksResult:
        """Get the bookmarks"""
        pass

    @get("/v1/memory-blocks")
    def get_memory_blocks(self) -> GhidraMemoryBlocksResult:
        """Get the memory blocks"""
        pass

    @get("/v1/memory")
    def get_memory(self, address: int | str, length: int) -> GhidraMemoryResult:
        """Get the memory"""
        pass

    @get("/v1/memory?format=raw", method_class=RawRequestsMethod)
    def get_memory_raw(self, address: int | str, length: int) -> bytes:
        """Get the memory as bytes"""
        pass

    @get("/v1/relocations")
    def get_relocations(self) -> GhidraRelocationsResult:
        """Get the relocations"""
        pass

    @get("/v1/functions")
    def get_functions(self) -> GhidraFunctionsResult:
        """Get the functions"""
        pass

    @get("/v1/symbols")
    def get_symbols(self) -> GhidraSymbolsResult:
        """Get the symbols"""
        pass

    @get("/v1/types")
    def get_types(self, exclude_undefined_components: Optional[bool]) -> GhidraTypesResult:
        """Get the types"""
        pass
