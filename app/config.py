import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

pw = urllib.parse.quote_plus(os.environ.get('pw_pg'))

DATABASE_URL_PG = f'postgresql://postgres:{pw}@localhost/mydb2'
USER = 'Alex'
engine = create_engine(DATABASE_URL_PG)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()