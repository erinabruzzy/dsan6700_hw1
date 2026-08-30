"""
Configure your application. Add typed configuration with Pydantic Settings:
the app reads its settings from the environment, with validators that fail
fast at startup on bad config (crash loudly, do not limp along). Provide
paired example environment files (for example a local-dev shape and a deployed shape)
so a new developer knows exactly which knobs exist. Never commit real secrets.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "DSAN 6700"
    environment: str = "local-dev"  # mypy static analysis
    port: int = 8000

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
