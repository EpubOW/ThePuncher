from flask import Flask
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from flask_cors import CORS, cross_origin


# Base = declarative_base()


flask_app = Flask(__name__,template_folder='resources/templates',  static_folder='resources/static', static_url_path = '')
cors = CORS(flask_app, supports_credentials=True, resources={r"*": {"origins": "*"}})
flask_app.config['CORS_HEADERS'] = 'Content-Type'

# e = create_engine("postgresql://postgres:qwerty@localhost:5432/skat_db", echo=False)

