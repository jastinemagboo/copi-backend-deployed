import os
from flask import Flask
from config import Config
from extensions import db, migrate
from flask_cors import CORS
from seed import run_seed  

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    from routes.post_routes import post_bp
    app.register_blueprint(post_bp)

    return app

app = create_app()

if __name__ == '__main__':

    # Only run seed if NOT reloading (i.e., not the auto-reloader)
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        with app.app_context():
            try:
                from seed import run_seed
                run_seed()
            except Exception as e:
                print(f"Seed error (ignored): {e}")
                
    app.run(debug=True)
