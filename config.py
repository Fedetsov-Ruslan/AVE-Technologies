from pydantic_settings import BaseSettings


class BaseEnvSettings(BaseSettings):
    class Config:
        env_file = '.env'
        extra = 'ignore'


class RedisSettings(BaseEnvSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str


redis_settings = RedisSettings()
