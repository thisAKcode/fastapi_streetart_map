import uuid 
from sqlalchemy.orm import Session
from model import Item, DataSet
from config import USER
from schemas import ItemSchema, DataSetSchema


# Get All art_item data
def get_all_art_items(db:Session, skip:int=0, _limit:int=30):
    # get all datasets 
    datasets = db.query(DataSet).all()
    #_items = [db.query(Item).filter_by(dataset_id =_subdataset.id).all() 
    #    for _subdataset in datasets]
    _items = db.query(Item).limit(_limit).all()
    return _items


# get by id art_item
def get_art_item_by_id(db:Session, art_item_id:str):
    return db.query(Item).filter(Item.id == int(art_item_id)).first()

# Create dataset
def create_dataset(db:Session, dataset: DataSetSchema):
    pass

# Create art_item data 
def create_art_item(db:Session, art_item: ItemSchema):
    """datasets = [_dataset.name for _dataset in db.query(DataSet).all()]
    max_ds_id = max([_dataset.id for _dataset in db.query(DataSet).all()])
    # if dataset for given item is missing initiate it
    if not art_item.dataset_name in datasets:
        _dataset = DataSet(id = max_ds_id + 1,
                           name = 'filename',
                           owner = USER)
        db.add(_dataset)
    _art_item = Item(id =str(uuid.uuid4()),
                        title=art_item.title, 
                        dataset_id=art_item.dataset_id,
                        _data = art_item._data,
                        dataset = art_item.dataset.name)
    db.add(_art_item)
    db.commit()
    db.refresh(_art_item)
    return _art_item
    """
    pass

# Remove art_item data 
def remove_art_item(db:Session, art_item_id:int):
    """_art_item = get_art_item_by_id(db=db, art_item_id = art_item_id)
    db.delete(_art_item)
    db.commit()
    """
    pass

# update art_item data
def update_art_item(db:Session, art_item_id:int, 
                    title:str, description:str,
                    lat:float, lon:float,
                    image_one:bytes, image_two:str):
    """_art_item = get_art_item_by_id(db=db, art_item_id=art_item_id)
    _art_item.title = title
    _art_item.description = description
    _art_item.lat
    _art_item.lon
    _art_item.image_one
    _art_item.image_two
    db.commit()
    db.refresh(_art_item)
    return _art_item
    """
    pass