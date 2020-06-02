from sqlalchemy import Column, String, Integer, ForeignKey

from models.database import Base

class Plant(Base):
    __tablename__ = 'plant'
    id = Column('plant_id', Integer, primary_key=True)
    #todo - species and variety should eventually be linked to another db table
    species = Column('plant_species', String)
    variety = Column('plant_variety', String)
    location = Column('plant_location', Integer, ForeignKey("location.location_id"))
    description = Column('plant_description', String)
    plant_date = Column(Integer)    #epoch time since sqlite can't handle datetime
