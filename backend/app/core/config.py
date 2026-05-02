from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    """
    Carga la configuracion desde las variables de entorno (.env)
    """
    DATABASE_URL:str
    STACK_API_URL:str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
    
config = Config()