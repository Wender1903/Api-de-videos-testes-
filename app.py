from config import app, db
from videos.videos_routes import videos_blueprint
from flask_cors import CORS


app.register_blueprint(videos_blueprint)
CORS(app) 

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])