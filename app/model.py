from sqlalchemy import Column, Integer, String, Float, BLOB

from config import Base

class ArtItem(Base):
    __tablename__ = 'art_item'
    
    id= Column(Integer, primary_key=True)
    title= Column(String)
    description = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    image_one = Column(BLOB)
    image_two = Column(String)