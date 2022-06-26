import databases

from models import rate_table


class CurrencyDB:
    def __init__(self, database_url: str):
        self.database_url = database_url

    async def rates_get(self):
        database = databases.Database(self.database_url)

        await database.connect()

        query = rate_table.select().limit(20)
        rates = await database.fetch_all(query)

        result = []
        for rate in rates:
            result.append({
                'id': rate.id,
                'buy': rate.buy,
                'sale': rate.sale,
            })

        await database.disconnect()
        return result