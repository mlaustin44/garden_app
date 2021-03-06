# describes a garden instance, which contains multiple locations, plants, etc

from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base

class Garden(Base):
    __tablename__ = 'garden'
    id = Column('garden_id', Integer, primary_key=True)
    name = Column('garden_name', String, nullable=False)
    owner = Column('garden_owner', Integer, ForeignKey("user.user_id"), nullable=False)
    lat = Column('garden_lat', Float)
    lon = Column('garden_lon', Float)

    def as_dict(self):
        return {"id": self.id,
                "name": self.name,
                "owner": self.owner,
                "latitude": self.lat,
                "longitude": self.lon}