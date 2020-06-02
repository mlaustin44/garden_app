from flask import Flask

from api import users, gardens
from models.database import db_session

app = Flask(__name__)
app.register_blueprint(users.bp)
app.register_blueprint(gardens.bp)

# automatically close database sessions at the end of requests
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

app.debug = True
app.run(host="0.0.0.0", port=8080)