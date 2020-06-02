#describes a location within a garden (i.e., 'back patio' or 'north raised bed')

from sqlalchemy import Column, Integer, String, ForeignKey

from models.database import Base

# ORM class for location references
class Location(Base):
    __tablename__ = 'location'
    id = Column('location_id', Integer, primary_key=True)
    garden = Column('garden_id', Integer, ForeignKey("garden.garden_id"))
    #todo - change this to an enum
    location_type = Column(String)