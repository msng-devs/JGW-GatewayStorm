from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.main import Setting

DB_CONN_URL = f"mysql+pymysql://{Setting.DB_USER_NM}:{Setting.DB_USER_PW}@{Setting.DB_HOST}/{Setting.DB_NAME}"

Base = declarative_base()
db_engine = create_engine(DB_CONN_URL)
db_session = sessionmaker(bind=db_engine, autoflush=False, autocommit=False)


def get_db():
    try:
        db = db_session()
        yield db

    finally:
        db.close()
