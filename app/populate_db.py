import os
import json
import uuid
from sqlalchemy import func
from config import engine,get_db, SessionLocal, USER
from dotenv import load_dotenv
from model import Base, Item, DataSet
from gis_tools import make_feature, to_geojson

load_dotenv()

DB_PATH = './mydb.db'
DUMMY_DATA = os.environ.get('LOCAL_DATA')
DATASET_CNT = None
db = get_db()


if not os.path.isfile(DB_PATH):
    print('NO DB')
    DATASET_CNT = 0

Base.metadata.create_all(bind=engine)


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