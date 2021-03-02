from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    
    # everything that runs in the block will have access to current_app.
    with app.app_context():
        from .view import view
        from .database import Database

        Database.establish_connection()
        app.register_blueprint(view, url_prefix="/")
        
    return app