from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
conn_str_file = "connection_string.txt"
try:
    conn_file = open(conn_str_file, 'r')
except FileNotFoundError:
    print("Please create a file named %s containing the connection string." % conn_str_file)
    exit()
app = Flask(__name__, static_url_path='')
app.config["MONGO_URI"] = conn_file.read()+"keyf?retryWrites=true"
mongo = PyMongo(app)
api = Api(app)
from Keyf.Services import *
from Keyf.Entities import *

api.add_resource(UsersService, '/users/<user_id>')
api.add_resource(CoffeeShopsService, '/shops/<shop_id>')
api.add_resource(DrinksService, '/drinks/<drink_id>')
api.add_resource(HomeService, '/')

if __name__ == "__main__":
    # app.run(debug=True)
    pass
