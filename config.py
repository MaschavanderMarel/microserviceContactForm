from pydantic import BaseSettings

class Settings(BaseSettings):
    email_pwd: str

    class Config:
        env_file = ".env"

settings = Settings()
