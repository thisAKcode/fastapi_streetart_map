import os
import json
from config import engine,get_db, SessionLocal
from dotenv import load_dotenv
from model import Base, ArtItem

load_dotenv()

DB_PATH = './mydb.db'
DUMMY_DATA = os.environ.get('LOCAL_DATA')
db = get_db()


if not os.path.isfile(DB_PATH):
    print('NO DB')

Base.metadata.create_all(bind=engine)


def data_loader(path_to):
    with open(path_to) as json_file:
        data = json.load(json_file)
    return data

def insert_items(_path_to_input):
    # inserts objects into db
    db = SessionLocal()
    _rawdata = data_loader(_path_to_input)
    for k,v in _rawdata.items():
        for _item in v:
            db.add(ArtItem(**_item))
    db.commit()
    db.close()