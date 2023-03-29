from sqlalchemy import Column, Integer, String, Float, BLOB, ForeignKey, DateTime, LargeBinary
from geoalchemy2 import Geometry
from sqlalchemy.orm import declarative_base, relationship
from config import Base


class DataSet(Base):
    __tablename__ = 'dataset'

    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String, nullable=True)
    owner = Column(String, nullable=True)
    items = relationship("Item", back_populates="dataset")


class Item(Base):
    __tablename__ = 'item'
    # properties are dumped into geojson except mandatory fields:
    #  id, creator, from_date, to_date
    id = Column(String, primary_key=True)
    # point, polyline or polygon geometries with properties stored in geojson
    # geometry: standard    https://geojson.org/#:~:text=GeoJSON%20supports%20the%20following%20geometry,additional%20properties%20are%20Feature%20objects.
    # properties: description, image_one, image_two, title, author
    _data = Column(String, nullable=True) # https://gis.stackexchange.com/a/142479
    geometry = Column(Geometry('POINT'), nullable=True) # Column(Geometry('POINT')) or Column(LargeBinary, nullable=True)
    # dataset_name = relationship("DataSet", back_populates="dataset.name")
    dataset_id = Column(Integer, ForeignKey("dataset.id"))
    dataset = relationship("DataSet", back_populates="items")
