from sqlalchemy import Column, String, Integer, ForeignKey

from database import Base


class Plant(Base):
    __tablename__ = 'plant'
    id = Column('plant_id', Integer, primary_key=True)
    species = Column('plant_species', String)
    variety = Column('plant_variety', String)
    source = Column('plant_source', String)
    description = Column('plant_description', String)
