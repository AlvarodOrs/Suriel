from typing import Any, TypeAlias
import requests


JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None

class CoinGeckoClient:
    def __init__(self, key: str, version: str | None = None):
        prefix = f'{version}-' if version else ''
        self.BASE_URL  = f"https://{prefix}api.coingecko.com/api/v3"
        self.session = requests.Session()

        if key: self.session.headers.update({f"x_cg_{prefix}_api_keys": key})
    
    def _get(self, endpoint: str, params: dict[str, Any] | None = None, timeout: int | None = None) -> JSON:
        url = f"{self.BASE_URL}/{endpoint}"

        response = self.session.get(
            url=url, params=params, timeout=timeout
            )
        response.raise_for_status()

        return response.json()