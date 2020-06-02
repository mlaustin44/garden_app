from flask import Blueprint, request

bp = Blueprint('plants', __name__, url_prefix='/api/plants')

#create a plant
@bp.route('/', methods=('POST'))
def new_plant():
    