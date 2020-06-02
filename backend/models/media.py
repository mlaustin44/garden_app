from sqlalchemy import Column, String, Integer, ForeignKey

from database import Base

class Media(Base):
    __tablename__ = 'media'
    id = Column('media_id', Integer, primary_key=True)
    user = Column('media_user', Integer, ForeignKey("user.user_id"))
    plant_instance = Column('media_plant_instance', Integer, ForeignKey("plant_instance.plant_instance_id"))
    plant_event = Column("media_plant_event", Integer, ForeignKey("plant_event.plant_event_id"))
    # uploaded date stored at integer/unix epoch because sqlite doesnt have a datetime
    uploaded_date = Column("media_uploaded_date", Integer)
    uuid = Column('media_uuid', String)
    extension = Column('media_extension', String)