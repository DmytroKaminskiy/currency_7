import httpx


class CurrencyAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def rates_get(self):
        async with httpx.AsyncClient() as client:
            full_url = f'{self.base_url}/api/v1/rates/'
            response = await client.get(full_url)
            content = response.json()['results']
            return content
