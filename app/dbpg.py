import os
import model
import json
import uuid
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
from config import engine2,get_db, SessionLocal2, USER
from gis_tools import make_feature, to_geojson
from model import Base, Item, DataSet

load_dotenv()
DUMMY_DATA = os.environ.get('LOCAL_DATA')
db = get_db()

Base.metadata.create_all(bind=engine2)

def data_loader(path_to):
    with open(path_to) as json_file:
        data = json.load(json_file)
    return data

def insert_items(_path_to_input):
    # inserts objects into db
    _info = None
    _filename= os.path.basename(_path_to_input)
    db = SessionLocal2()
    _rawdata = data_loader(_path_to_input)
    _features2 = to_geojson(_rawdata)
    
    _ds_id = 0
    _dataset = DataSet(id = _ds_id,
                       name = _filename,
                       owner = USER)
    
    db.add(_dataset)
    for _feature in _features2:
        _info = json.dumps(_feature)
        _id = str(uuid.uuid4()) 
        _item = Item(id = _id,
                    dataset_id = _ds_id,
                    _data = _info
                    )
        db.add(_item)
    db.commit() 
    db.close()

def _reader():
    db = SessionLocal2()
    locations1 = db.query(model.Item).all()
    # print(locations1)

class B(Exception):
    pass

# how to wrap database operations that need to be executed together in a single transaction
def startup_populate_db():
    db = SessionLocal2()
    item_count = 0
    try:
        item_count = db.query(Item).count()
    except B: 
        item_count == 0
    if item_count == 0:
        insert_items(DUMMY_DATA)

def check_database():
    connection = psycopg2.connect(host="localhost", user="postgres", password="ljlkd%fFDFw12?Dg0vRiF") 
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = connection.cursor()
    # Check if the database exists
    cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    dbs = cur.fetchall()
    print(dbs)
    # cur.execute("CREATE DATABASE database_name;")
    if ('mydb',) not in dbs:
        cur.execute("CREATE DATABASE mydb;")
        return "Database created successfully"
    else:
        return "Database already exists"
    

def add_postgis():
    conn = psycopg2.connect(database="mydb", user="postgres", 
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
    

def _create_table():
    conn = psycopg2.connect(database="mydb", user="postgres", 
                            password="ljlkd%fFDFw12?Dg0vRiF", host="localhost", port="5432")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Create a cursor
    cursor = conn.cursor()
    # Create the table if it does not already exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS capital_cities (
        id serial PRIMARY KEY,
        name varchar(255),
        geom geometry(Point, 4326)
    )
    """)
    # Commit the changes, close the cursor and connection
    conn.commit()
    cursor.close()
    conn.close()



def insert_mock_data():
    # Connect to the database
    conn = psycopg2.connect(database="mydb", user="postgres", 
                            password="ljlkd%fFDFw12?Dg0vRiF", host="localhost", port="5432")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Create a cursor
    cursor = conn.cursor()
    # Select all rows from the capital_cities table
    cursor.execute("SELECT * FROM capital_cities")

    # Fetch the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Insert a row into the table
    cursor.execute("""
        INSERT INTO capital_cities (name, geom)
        VALUES (%s, ST_GeomFromText(%s, 4326))
    """, ('Paris', 'POINT(2.3522 48.8566)'))
    # Commit the changes
    conn.commit()
    # Close the cursor and connection
    cursor.close()
    conn.close()




if __name__ == "__main__":
    check_database()
    add_postgis()
    _create_table()
    insert_mock_data()
    # Base.metadata.create_all(bind=engine2)
    startup_populate_db()
    _reader()