from models.database import db_session

# automatically close database sessions at the end of requests
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()