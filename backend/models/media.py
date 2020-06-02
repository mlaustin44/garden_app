from sqlalchemy import Column, String, Integer, ForeignKey

from models.database import Base

class Media(Base):
    __tablename__ = 'media'
    id = Column('media_id', Integer, primary_key=True)
    user = Column('media_user', Integer, ForeignKey("user.user_id"))
    plant = Column('media_plant', Integer, ForeignKey("plant.plant_id"))
    uuid = Column('media_uuid', String)
    extension = Column('media_extension', String)