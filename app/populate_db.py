import os
import json
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
    print('####################################')
    _ds_id = 0
    '''
    try:
        _ds_id = db.query(func.max(DataSet.id))
    except:
        _ds_id = 0
    '''
    _dataset = DataSet(id = _ds_id,
                       name = _filename,
                       owner = USER)
    db.add(_dataset)
    feature_cnt = 0
    for _feature in _features2:
        _info = json.dumps(_feature)
        print(_info)
        _id = feature_cnt
        _item = Item(id = _id,
                        dataset_id = _ds_id,
                        _data = _info,
                        dataset_name = _filename
                        )
        db.add(_item)
        feature_cnt += 1
    db.add(_dataset)
    db.commit()
    db.close()