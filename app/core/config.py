
import os

class Config:
    API_TITLE = "Mini API de Usuários"
    API_VERSION = "1.0.0"
    OPENAPI_VERSION = "3.1.0"
    OPENAPI_URL_PREFIX = "/docs"
    OPENAPI_JSON_PATH = "openapi.json"
    OPENAPI_SWAGGER_UI_PATH = "/"
    OPENAPI_SWAGGER_UI_URL = "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.15.5/"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///" + os.path.join(os.getcwd(), "instance", "usuarios.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
