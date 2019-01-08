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
from Keyf.providers import Users, CoffeeShops
from Keyf import Home

api.add_resource(Users.Users, '/users/<user_id>')
api.add_resource(CoffeeShops.CoffeeShops, '/shops/<shop_id>')
api.add_resource(Home.Home, '/')

if __name__ == "__main__":
    pass
    #app.run(debug=True)
