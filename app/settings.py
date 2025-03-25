from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings for Hyperion
    The class is based on a dotenv file: `/.env`. All undefined variables will be populated from:
    1. An environment variable
    2. The dotenv .env file

    See [Pydantic Settings documentation](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support) for more information.
    See [FastAPI settings](https://fastapi.tiangolo.com/advanced/settings/) article for best practices with settings.

    To access these settings, the `get_settings` dependency should be used.
    """

    # By default, the settings are loaded from the `.env` file but this behaviour can be overridden by using
    # `_env_file` parameter during instantiation
    # Ex: `Settings(_env_file=".env.dev")`
    # Without this property, @cached_property decorator raise "TypeError: cannot pickle '_thread.RLock' object"
    # See https://github.com/samuelcolvin/pydantic/issues/1241
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    HIBOUTIK_API_URL: str
    HIBOUTIK_API_USER: str
    HIBOUTIK_API_KEY: str

    # By default, only production's records are logged
    LOG_DEBUG_MESSAGES: bool | None

    # Origins for the CORS middleware. `["http://localhost"]` can be used for development.
    # See https://fastapi.tiangolo.com/tutorial/cors/
    # It should begin with 'http://' or 'https:// and should never end with a '/'
    CORS_ORIGINS: list[str] = ["*"]

    ###################
    # Tokens validity #
    ###################

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    ###############################################
    # Authorization using OAuth or Openid connect #
    ###############################################

    # ACCESS_TOKEN_SECRET_KEY should contain a random string with enough entropy (at least 32 bytes long) to securely sign all access_tokens for OAuth and Openid connect
    ACCESS_TOKEN_SECRET_KEY: str
