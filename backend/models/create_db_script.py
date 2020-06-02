# function to create all the tables and schemas automatically using the model definitions
from database import Base, db_engine

def init_db():
    from garden import Garden
    import garden, location, media, plant_event, plant_instance, plant, user

    Base.metadata.create_all(bind=db_engine)

init_db()