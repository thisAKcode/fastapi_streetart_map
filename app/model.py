from sqlalchemy import Column, Integer, String, Float, BLOB, relationship, ForeignKey

from config import Base


class DataSet(Base):
    __tablename__ = 'dataset'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    items = relationship("Item", back_populates="dataset")


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    description = Column(String, nullable=True)
    image_one = Column(BLOB, nullable=True)
    image_two = Column(String, nullable=True)
    dataset_id = Column(Integer, ForeignKey("dataset.id"))
    dataset = relationship("DataSet", back_populates="items")
