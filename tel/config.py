from typing import Optional

from pydantic import (
    BaseSettings,
    PostgresDsn,
    root_validator,
    ValidationError,
)


class Settings(BaseSettings):
    telegram_token: str
    currency_url: Optional[str]
    pg_dsn: Optional[PostgresDsn]
    currency_class: str  # api, db

    @root_validator
    def validate_settings(cls, values):
        if values['currency_class'] == 'api':
            if not values.get('currency_url'):
                raise ValidationError('CURRENCY_ENV is required is api is used.')
        elif values['currency_class'] == 'db':
            if not values.get('pg_dsn'):
                raise ValidationError('PG_DSN is required is db is used.')
        else:
            raise ValidationError('CURRENCY_CLASS is required.')

        return values


settings = Settings()
