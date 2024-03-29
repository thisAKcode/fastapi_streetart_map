import uuid
from sqlalchemy.orm import Session
from model import Item, DataSet
from config import USER
from schemas import ItemSchema, DataSetSchema

class DataSetNotFound(Exception):
    """Used when no data set is found on dataset id"""


def get_all_art_items(db:Session, skip:int=0, _limit:int=30):
    datasets = db.query(DataSet).all()
    #_items = [db.query(Item).filter_by(dataset_id =_subdataset.id).all()
    #    for _subdataset in datasets]
    _items = db.query(Item).limit(_limit).all()
    return _items



def get_art_item_by_id(db:Session, art_item_id:str):
    return db.query(Item).filter(Item.id == int(art_item_id)).first()


def create_dataset(db:Session, dataset: DataSetSchema):
    print(f"create dataset {dataset}")
    datasets = [_dataset.name for _dataset in db.query(DataSet).all()]
    # if dataset for given item is missing initiate it
    if not dataset.dataset_name in datasets:
        _dataset = DataSet(name = dataset.filename,
                           owner = USER)
        db.add(_dataset)
    db.commit()
    db.refresh(_dataset)
    return _dataset


def create_art_item(db:Session, dataset_id:int, art_item: ItemSchema):
    # create dataset with id 1000000 the default one
    dataset = db.query(DataSet).one_or_none(dataset_id = dataset_id)
    if dataset is None:
        # create default dataset
        raise DataSetNotFound('use default dataset')
    # create
    _art_item = Item(id =str(uuid.uuid4()),
                    _data = art_item._data,
                    dataset = dataset,
                    geometry = art_item.geometry)
    db.add(_art_item)
    db.commit()
    db.refresh(_art_item)
    return _art_item


def remove_art_item(db:Session, art_item_id:int):
    """_art_item = get_art_item_by_id(db=db, art_item_id = art_item_id)
    db.delete(_art_item)
    db.commit()
    """
    pass


def update_art_item(db: Session,
                    art_item: ItemSchema):

    # one() can raise NoResultFound or MultipleResultsFound
    _art_item = db.query(Item).one(id=art_item.id)

    dataset = db.query(DataSet).one_or_none(
        dataset_id=art_item.dataset_id)
    if dataset is None:
       raise DataSetNotFound('use default dataset')

    _art_item._data = art_item._data
    _art_item.geometry = art_item.geometry
    _art_item.dataset = dataset

    db.add(_art_item)
    db.commit()
    db.refresh(_art_item)

    return art_item
