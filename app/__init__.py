from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

from config import app_config

from app import views

from flask_login import LoginManager

db = SQLAlchemy()

# To use Alchemy database in order to store user data

# Initialise a database variable

login_manager = LoginManager()


def dev_app(config_name):
	"""
		Function to start the app and initialise key variables
		"""
	app = Flask(__name__, instance_relative_config=True)
	
	#ensure specified file is loaded from instance directory
	
	app.config.from_object(app_config[config_name])
	
	#method config.from_object to load specific configurations of 'app'
	
	# app.config.from_pyfile('config.py')

	#method config.from_pyfile for reference to the 'config.py' file
    
	db.init_app(app)

	# Use login manager to simplify login access to users
	
	login_manager.init_app(app)

	login_manager.login_message = "You must login to view page."

	login_manager.login_view = "auth.login"

	from . import views

	# @app.route('/')
	# def index():
	# 	return render_template("index.html")

	return app

	# Implement blueprint structure in order to run app