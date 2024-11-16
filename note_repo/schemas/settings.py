from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    PydanticBaseSettingsSource,
    YamlConfigSettingsSource,
    SecretsSettingsSource
)
from pydantic import PostgresDsn
from typing import Tuple, Type
from pathlib import Path
from pydantic import Field
import os

MINIBLOG_CONFIGS_PATH = Path('./configs.yaml')

class AppSettings(BaseSettings):
    database_url: PostgresDsn 

    @classmethod
    def settings_customise_sources(
        cls, 
        settings_cls: BaseSettings, 
        init_settings: PydanticBaseSettingsSource, 
        env_settings: PydanticBaseSettingsSource, 
        dotenv_settings: PydanticBaseSettingsSource, 
        file_secret_settings: PydanticBaseSettingsSource) -> Tuple[PydanticBaseSettingsSource]:
        return (
            file_secret_settings,
            YamlConfigSettingsSource(settings_cls, yaml_file=os.getenv('MINIBLOG_CONFIGS_PATH', MINIBLOG_CONFIGS_PATH))
        )

    