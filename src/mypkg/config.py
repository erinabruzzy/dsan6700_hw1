from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "DSAN 6700"
    environment: str
    port: int = 8000

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()