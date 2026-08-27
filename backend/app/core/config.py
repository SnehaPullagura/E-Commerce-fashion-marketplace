import os
from typing import List, Union
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    PROJECT_NAME: str = "Fashion Marketplace"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # Security & Tokens
    SECRET_KEY: str = "fashion-marketplace-super-secret-production-key-change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30
    BCRYPT_ROUNDS: int = 12

    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./fashion_marketplace.db"
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:3002",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
        "http://127.0.0.1:3002",
        "http://localhost:8000",
    ]

    # File uploads
    MEDIA_ROOT: str = "./media"
    UPLOAD_MAX_SIZE_MB: int = 10

    # Rate limiting
    RATE_LIMIT_PER_MINUTE: int = 120

    # Marketplace Business Logic Defaults
    DEFAULT_COMMISSION_PERCENTAGE: float = 15.0  # 15% marketplace commission
    STOCK_RESERVATION_EXPIRY_MINUTES: int = 15   # 15 minutes hold during checkout
    FREE_SHIPPING_THRESHOLD: float = 999.0       # Free shipping on orders >= Rs.999
    DEFAULT_SHIPPING_FEE: float = 79.0

    # Mock services toggle
    MOCK_PAYMENT_GATEWAY: bool = True
    MOCK_COURIER_SERVICE: bool = True


settings = Settings()
