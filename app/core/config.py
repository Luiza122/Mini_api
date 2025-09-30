import os
from typing import Optional

class Settings:
    PROJECT_NAME: str = "Mini API Usuários"
    PROJECT_VERSION: str = "1.0.0"
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./usuarios.db")
    
    # API
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()