from flask import Flask, request, Response, jsonify
from flask_pymongo import PyMongo

from swagger_gen.swagger import Swagger
from dotenv import load_dotenv, find_dotenv

from flask.globals import current_app
import json

from parser.routes import parser

import traceback
import tempfile

app = Flask(__name__)
app.register_blueprint(parser)


swagger = Swagger(
    app=app,
    title='Resume Parser API',
    version="1.0.0",
    description="API Developed to be used in unison with React Resume Parser App",
    contact_email="omarsan786@gmail.com"
    )
swagger.configure()


client_URI = "mongodb+srv://admin:muqijo97ypPPGbVn@resumeparsercluster.hokokmj.mongodb.net/?retryWrites=true&w=majority"
mongodb_client = PyMongo(app, uri=client_URI)
db = mongodb_client.db