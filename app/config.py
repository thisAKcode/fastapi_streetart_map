import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

pw = urllib.parse.quote_plus(os.environ.get('pw_pg'))

#  conn = psycopg2.connect(     host="localhost",     database="python_db",     user="postgres",     password="ljlkd%fFDFw12?Dg0vRiF")
# postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
#DATABASE_URL = f'postgresql://postgres:{pw}@localhost/python_db'
DATABASE_URL = 'sqlite:///mydb.db'

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

