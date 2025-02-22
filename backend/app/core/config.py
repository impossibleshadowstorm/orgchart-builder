from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    # Application configurations
    APP_NAME: str = "System"
    VERSION: str = "1.0.0"

    # Database settings
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()