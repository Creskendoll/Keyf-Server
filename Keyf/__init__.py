from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
conn_file = open("connection_string.txt", 'r')
app = Flask(__name__)
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
