from pydantic import BaseSettings


class Config(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    ENV: str = "local"
    DATABASE_URL: str
    CLIENT_SECRET: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


app_config = Config()
