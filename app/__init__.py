from ensurepip import bootstrap
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

#initialize flask extensions
bootstrap = Bootstrap()

# Initialize app
def create_app(config_name):

    app = Flask(__name__)

    #create app configurations
    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .request import configure_request
    configure_request(app)

    #initialize flask extensions
    bootstrap.init_app(app)

    return app