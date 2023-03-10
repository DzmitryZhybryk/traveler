from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Config(BaseSettings):
    token: str
    my_telegram_id: int
    greeting_strangers: str
    database_url: str

    class Config:
        env_file = BASE_DIR / ".env"


config = Config()
