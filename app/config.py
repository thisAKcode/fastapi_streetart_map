from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path
import urllib.parse


pw = urllib.parse.quote_plus("ljlkd%fFDFw12?Dg0vRiF")

#  conn = psycopg2.connect(     host="localhost",     database="python_db",     user="postgres",     password="ljlkd%fFDFw12?Dg0vRiF")
# postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
# DATABASE_URL = fr"postgresql://postgres:{pw}@localhost:5432/python_db"
#DATABASE_URL = f'postgresql://postgres:{pw}@localhost/python_db'
DATABASE_URL = 'sqlite:///mydb.db'
# DATABASE_URL2 = fr"postgresql:\\postgres:{pw}@localhost\python_db"

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
print(DATABASE_URL, Path(DATABASE_URL))
print(type(DATABASE_URL), type(Path(DATABASE_URL)))

