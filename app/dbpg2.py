import os
import model
import json
import uuid
import psycopg2
from shapely.geometry import shape
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
from config import engine,get_db, SessionLocal, USER
from gis_tools import make_feature, to_geojson
from model import Base, Item, DataSet

#load_dotenv()
#DUMMY_DATA = os.environ.get('LOCAL_DATA')
# db = get_db()

# Base.metadata.create_all(bind=engine)


def check_database():
    connection = psycopg2.connect(host="localhost", user="postgres", password="ljlkd%fFDFw12?Dg0vRiF") 
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = connection.cursor()
    # Check if the database exists
    cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    dbs = cur.fetchall()
    # cur.execute("CREATE DATABASE mydb2;")
    # cur.execute("CREATE DATABASE database_name;")
    if ('mydb2',) not in dbs:
        cur.execute("CREATE DATABASE mydb2;")
        return "Database created successfully"
    else:
        return "Database already exists"

def add_postgis():
    conn = psycopg2.connect(database="mydb2", user="postgres", 
                            password="ljlkd%fFDFw12?Dg0vRiF", host="localhost", port="5432")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Create a cursor
    cur = conn.cursor()
    cur.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
    # Close the cursor and connection
    cur.close()
    # Commit the changes
    conn.commit()
    conn.close()


if __name__ == "__main__":
    print('it')
    check_database()
    add_postgis()
    #_create_table()
    #insert_mock_data()
    #startup_populate_db()
    #_reader()
    #_JSON = quick_tester(DUMMY_DATA).geometry 
    #a, b = shape(_JSON).wkb,  shape(_JSON).wkt
    #print(a)
    #print(a, b)
