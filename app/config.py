from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    admin_token: str
    env: str="dev"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings=Settings()