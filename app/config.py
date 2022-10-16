from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

pw = r"ljlkd%fFDFw12?Dg0vRiF"

#  conn = psycopg2.connect(     host="localhost",     database="python_db",     user="postgres",     password="ljlkd%fFDFw12?Dg0vRiF")
# postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
# DATABASE_URL = fr"postgresql://postgres:{pw}@localhost:5432/python_db"
DATABASE_URL = fr"postgresql://postgres:{pw}@localhost/python_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
