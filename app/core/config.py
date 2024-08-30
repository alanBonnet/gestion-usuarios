import os
from typing import TypedDict
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"

load_dotenv(env_path)


class DbConfig:
    """
    Una clase que su función es definir una forma de proporcionar datos para la conexión a la base de datos
    el unico detalle es el `port` y el `driver_age`
    - `port` puede ser agregado como numero entero
    - `driver_age` hace referencia al año de versión de la base de datos:
        - por el momento existe 2008 y 2012.
        - por lo tanto recibe el 2012 y por defecto se configura para 2008
    """

    def __init__(
        self,
        username: str,
        password: str,
        dbname: str,
        host: str,
        identity: str,
        # driver_age: int | None = None,
        port: int | None = None,
    ):
        self.username: str = username
        self.password: str = password
        self.dbname: str = dbname
        self.host: str = host
        self.identity: str = identity

        # self.driver_age: str = driver_sql.get(driver_age, driver_sql[2008])
        self.port: str = f":{port}" if port is not None else ""

    def get_db_url(self) -> str:
        return f"postgresql+psycopg://{self.username}:{self.password}@{self.host}{self.port}/{self.dbname}"


# database_configs es un listado de configuraciones para Settings
database_configs: list[DbConfig] = [
    DbConfig(  # DB: Seguridad Web
        username=os.getenv("PGSQL_USERNAME"),
        password=os.getenv("PGSQL_PASSWORD"),
        dbname=os.getenv("PGSQL_DBNAME_P0"),
        host=os.getenv("PGSQL_HOST"),
        port=5432,
        identity="Gestion_Usuarios",
    )
]


class DbConfigTyped(TypedDict):
    Gestion_Usuarios: str


class Settings:
    """
    Una clase que gracias a la lista de `DbConfig` proporciona los links para la conexión a las bases de datos a `SQLAlchemy`
    """

    PROJECT_NAME: str = "PROYECTO-FAST-API"
    PROJECT_VERSION: str = "1.0"
    DB_MAIN = "POSTGRESQL"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM_HASH: str = os.getenv("ALGORITHM_HASH")
    URL_DBs: DbConfigTyped = {
        config.identity: config.get_db_url() for config in database_configs
    }
    # print(URL_DBs)


settings = Settings()
print(settings.URL_DBs["Gestion_Usuarios"])
