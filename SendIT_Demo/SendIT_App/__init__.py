from flask import Flask
from instance.config import Config
from SendIT_App.api.Version1 import parcels_bp, bp

def create_app(config_class =Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	parcels_bp.init_app(app)
	app.register_blueprint(bp,url_prefix='/api/v1')




	return app