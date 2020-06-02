from flask import Blueprint, request
from models.database import db_session
from models.garden import Garden

bp = Blueprint('garden', __name__, url_prefix='/api/gardens')

#create a user
@bp.route('/', methods=['POST'])
def new_garden():