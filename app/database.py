from databases import Database

from app.config import config

database = Database(url=config.database_url)