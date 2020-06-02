from flask import Blueprint, request
from models.database import db_session
from models.garden import Garden
import json

bp = Blueprint('garden', __name__, url_prefix='/api/gardens')

#create a new garden
@bp.route('/', methods=['POST'])
def new_garden():
    request_content = request.json
    name = request_content.get('name')
    owner = request_content.get('owner')
    lat = request_content.get('latitude')
    lon = request_content.get('longitude')
    
    g = Garden(name = name,
                owner = int(owner),
                lat = lat,
                lon = lon)
    
    db_session.add(g)
    db_session.commit()
    return '', 200

#get a list of gardens for a user
@bp.route("/<userid>", methods=['GET'])
def user_gardens(userid):
    g = Garden.query.filter(Garden.owner == int(userid)).all()
    print(g)
    return {"results": [o.as_dict() for o in g]}, 200