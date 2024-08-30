from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Si deseas aún más detalles:
# logging.getLogger("sqlalchemy.dialects.postgresql").setLevel(logging.DEBUG)

Base = declarative_base()

Engine_P0 = create_engine(settings.URL_DBs["Gestion_Usuarios"])
Session_P0 = sessionmaker(bind=Engine_P0, autocommit=False, autoflush=False)


def get_db_P0():
    db = Session_P0()
    try:
        yield db
    finally:
        db.close()
