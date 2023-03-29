import os
import json
import uuid
from shapely.geometry import shape
from sqlalchemy import func
from config import engine,get_db, SessionLocal, USER
from dotenv import load_dotenv
from model import Base, Item, DataSet
from gis_tools import make_feature, to_geojson

load_dotenv()

DB_PATH = './mydb2.db'
DUMMY_DATA = os.environ.get('LOCAL_DATA')
DATASET_CNT = None
db = get_db()


def data_loader(path_to):
    with open(path_to) as json_file:
        data = json.load(json_file)
    return data

def insert_items(_path_to_input):
    # inserts objects into db
    _info = None
    _filename= os.path.basename(_path_to_input)
    db = SessionLocal()
    _rawdata = data_loader(_path_to_input)
    _features2 = to_geojson(_rawdata)
    
    for _feature in _features2:
        _geom = shape(_feature.geometry)
        # trades in hex encoded wkb 
        _wkb = shape(_geom).wkb_hex
        print(f'--------------------------------------------geom{_wkb}')
        _info = json.dumps(_feature)


if __name__ == "__main__":
    insert_items(DUMMY_DATA)