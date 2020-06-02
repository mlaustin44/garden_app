from sqlalchemy import Column, String, Integer, ForeignKey

from database import Base

class PlantInstance(Base):
    __tablename__ = 'plant_instance'
    id = Column('plant_instance_id', Integer, primary_key=True)
    plant_type = Column('plant_instance_type', String, ForeignKey("plant.plant_id"))
    location = Column('plant_instance_location', Integer, ForeignKey("location.location_id"))
    description = Column('plant_instance_description', String)