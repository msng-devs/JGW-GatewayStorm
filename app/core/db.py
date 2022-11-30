from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.configs.config import settings

DB_CONN_URL = f"mysql+pymysql://{settings.DB_USER_NM}:{settings.DB_USER_PW}@{settings.DB_HOST}/{settings.DB_NAME}"

Base = declarative_base()
db_engine = create_engine(DB_CONN_URL)
db_session = sessionmaker(bind=db_engine, autoflush=False, autocommit=False)


def get_db():
    try:
        db = db_session()
        yield db

    finally:
        db.close()
