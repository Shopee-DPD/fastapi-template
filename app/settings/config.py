from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class AppSettings(BaseConfig):
    app_tag: str = Field(alias="APP_TAG", default="dev")
    app_host: str = Field(alias="APP_HOST", default="http://localhost:8000")
    base_url: str = Field(alias="BASE_URL", default="")
    dev_email: str = Field(alias="DEV_EMAIL", default=None)
    allowed_origins: str = Field(alias="ALLOWED_ORIGINS", default="")
    docs_url: str = Field(alias="DOCS_URL", default="/docs")
    openapi_url: str = Field(alias="OPENAPI_URL", default="/openapi.json")


class LoggerSettings(BaseConfig):
    app_log_level: str = Field(alias="LOG_LEVEL_APP", default="DEBUG")
    uvicorn_log_level: str = Field(alias="LOG_LEVEL_UVICORN", default="INFO")
    logstash_log_level: str = Field(alias="LOG_LEVEL_LOGSTASH", default="DEBUG")
    logstash_host: str = Field(alias="LOGSTASH_HOST", default="localhost")
    logstash_port: str = Field(alias="LOGSTASH_PORT", default="50000")
    app_tag: str = Field(alias="APP_TAG", default="dev")


class DatabaseSettings(BaseConfig):
    drivername: str = "mysql+pymysql"
    host: str = Field(alias="DB_HOST", default="localhost")
    port: int = Field(alias="DB_PORT", default=3306)
    username: str = Field(alias="DB_USER", default="root")
    password: str = Field(alias="DB_PASSWORD", default="")
    database: str = Field(alias="DB_DATABASE", default="")
