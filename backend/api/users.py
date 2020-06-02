from flask import Blueprint, request

bp = Blueprint('users', __name__, url_prefix='/api/users')

#create a user
@bp.route('/', methods=('POST'))
def new_user():