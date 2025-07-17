
from typing import Any
from dataclass_rest.http.requests import RequestsMethod
from requests import Response


class RawRequestsMethod(RequestsMethod):
    def _response_body(self, response: Response) -> Any:
        return response.content
