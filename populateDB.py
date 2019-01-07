from Keyf.entities.Shop import CoffeeShop
from Keyf.entities.User import User
from pymongo import MongoClient
import json
conn_file = open("connection_string.txt", 'r')
client = MongoClient(conn_file.read())
db = client.keyf

users = db.users
shops = db.coffee_shops

# with open('example_shop.json') as json_file:  
#     data = json.load(json_file)
#     shop_ent = CoffeeShop(data=data)
#     print(shops.insert_one(shop_ent.serialize()).inserted_id)
    

with open('example_user.json') as json_file:  
    data = json.load(json_file)
    user_ent = User(data=data)
    print(users.insert_one(user_ent.serialize()).inserted_id)
    