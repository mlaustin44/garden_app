from sqlalchemy import Column, String, Integer, ForeignKey

from database import Base


class PlantEvent(Base):
    __tablename__ = 'plant_event'
    id = Column('plant_event_id', Integer, primary_key=True)
    event_type = Column('plant_event_type', String)
    event_notes = Column('plant_event_notes', String)
    instance_id = Column('plant_instance_id', Integer, ForeignKey("plant_instance.plant_instance_id"))
    # Event date is in integer/unix epoch format because sqlite doesnt have a datetime
    event_date = Column('plant_event_date', Integer)