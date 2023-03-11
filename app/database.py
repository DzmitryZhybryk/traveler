from databases import Database

from app.config import config


class DatabaseWorker:

    def __init__(self):
        self._database = Database(url=config.database_url)

    async def connect_database(self):
        await self._database.connect()

    async def disconnect_database(self):
        await self._database.disconnect()

    async def create_countries_table(self):
        query = (
            "CREATE TABLE IF NOT EXISTS countries ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "country_name VARCHAR(255))"
        )
        await self._database.execute(query)

    async def create_travels_table(self):
        query = (
            "CREATE TABLE IF NOT EXISTS travels ("
            "id INTEGER PRIMARY KEY, "
            "first_town VARCHAR(255), "
            "second_town VARCHAR(255),"
            "distance INTEGER,"
            "countries_id INTEGER,"
            "FOREIGN KEY(countries_id) references countries(id))"
        )
        await self._database.execute(query)

    async def select_country(self, country: str):
        query = f"SELECT * FROM countries WHERE country_name={country}"
        country = await self._database.execute(query)
        return country

    async def add_country(self, country: str):
        query = (
            f"INSERT INTO countries VALUES (:id, :country_name)"
        )
        await self._database.execute(query, {"id": 2, "country_name": country})


database = DatabaseWorker()
