from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
from os import getcwd, chdir
from os.path import abspath
from platform import system

app = Flask(__name__, static_url_path="", static_folder="public/site",)

conn_str_file = "connection_string.txt"
try:
    conn_file = open(conn_str_file, "r")
    conn_str = conn_file.read()
    conn_file.close()
except FileNotFoundError:
    print(
        "Please create a file named %s containing the connection string."
        % conn_str_file
    )
    exit()

app.config["MONGO_URI"] = conn_str
mongo = PyMongo(app)
api = Api(app)
from Keyf.Services import *
from Keyf.Entities import *

api.add_resource(UsersService, '/users/<user_id>')
api.add_resource(ShopService, '/shops/<shop_id>')
api.add_resource(DrinksService, '/drinks/<drink_id>')
