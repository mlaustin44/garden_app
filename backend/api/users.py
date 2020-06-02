from flask import Blueprint, request
from models.database import db_session
from models.user import User

bp = Blueprint('users', __name__, url_prefix='/api/users')

#create a user
@bp.route('/', methods=['POST'])
def new_user():
    request_content = request.json
    user_name = request_content.get('name')
    user_email = request_content.get('email')
    #make sure all the needed parameters are there
    if (not user_name) or (not user_email):
        return 'Request is missing stuff!', 400
    # make sure the user doesnt already exist
    matches = User.query.filter(User.email == user_email).first()
    print(matches)
    if matches:
        return 'User already exists!', 409


    u = User(name = user_name, email = user_email)
    db_session.add(u)
    db_session.commit()
    return '', 200