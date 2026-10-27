from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "PulseCommerce API"
    environment: str = "local"
    log_level: str = "INFO"
    database_url: str = "postgresql+psycopg://pulse:pulse@db:5432/pulsecommerce"


settings = Settings()
