from sqlalchemy.orm import Session
from model import ArtItem
from schemas import ArtItemSchema


# Get All art_item data
def get_art_item(db:Session, skip:int=0, limit:int=100):
    return db.query(ArtItem).offset(skip).limit(limit).all()


# get by id art_item
def get_art_item_by_id(db:Session, art_item_id:int):
    return db.query(ArtItem).filter(ArtItem.id == art_item_id).first()

# Create art_item data 
def create_art_item(db:Session, art_item: ArtItemSchema):
    _art_item = ArtItem(title=art_item.title, 
                        description=art_item.description,
                        lat = art_item.lat,
                        lon = art_item.lon,
                        image_one = art_item.image_one, 
                        image_two = art_item.image_two)
    db.add(_art_item)
    db.commit()
    db.refresh(_art_item)
    return _art_item


# Remove art_item data 
def remove_art_item(db:Session, art_item_id:int):
    _art_item = get_art_item_by_id(db=db, art_item_id = art_item_id)
    db.delete(_art_item)
    db.commit()


# update art_item data
def update_art_item(db:Session, art_item_id:int, 
                    title:str, description:str,
                    lat:float, lon:float,
                    image_one:bytes, image_two:str):
    _art_item = get_art_item_by_id(db=db, art_item_id=art_item_id)
    _art_item.title = title
    _art_item.description = description
    _art_item.lat
    _art_item.lon
    _art_item.image_one
    _art_item.image_two
    db.commit()
    db.refresh(_art_item)
    return _art_item
