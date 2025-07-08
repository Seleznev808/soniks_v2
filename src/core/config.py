from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseModel):
    DB: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: str

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DB}"


class SQLEngineSettings(BaseModel):
    ECHO: bool = False
    ECHO_POOL: bool = False
    POOL_SIZE: int = 10
    MAX_OVERFLOW: int = 20


class AlembicSettings(BaseModel):
    NAMING_CONVENTION: dict[str, str] = {
        "pk": "pk_%(table_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
    }


class AppSettings(BaseModel):
    DEBUG: bool = False


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
    )
    postgres: PostgresSettings
    sql_engine: SQLEngineSettings = SQLEngineSettings()
    alembic: AlembicSettings = AlembicSettings()
    app: AppSettings = AppSettings()


settings = Settings()
