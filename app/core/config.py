from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATA_DIR: str = "data/uploads"

settings = Settings()