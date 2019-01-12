from Keyf.Entities import *
from pymongo import MongoClient
import json
conn_file = open("connection_string.txt", 'r')
client = MongoClient(conn_file.read())
db = client.keyf

users = db.users
shops = db.coffee_shops
drinks = db.drinks

with open('example_shop.json') as shop_file:  
    with open('example_drink.json') as drink_file:
        drink_data = json.load(drink_file)
        shop_data = json.load(shop_file)

        for i in range(15):
            shop_obj = CoffeeShop(data=shop_data)
            shop_obj.id = i
            for i in range(3):
                drink_obj = Drink(data=drink_data)
                drink_obj.id = drink_obj.id + i
                drinks.replace_one({"id":drink_obj.id}, drink_obj.serialize(), upsert=True)
                shop_obj.menu['coffees_menu'].append(drink_obj.id)

            update_result = shops.replace_one({"id": shop_obj.id},shop_obj.serialize(), upsert=True).upserted_id
            if update_result is None:
                print("Shop updated with _id:", update_result)
            else:
                print("Shop inserted with _id:", update_result)



# with open('example_shop.json') as shop_file:  
#     with open('example_drink.json') as drink_file:
#         with open('example_user.json') as user_file:  
#             user_data = json.load(user_file)
#             user_ent = User(data=user_data)
#             for i in range(3):
#                 drink_obj = Drink(data=drink_data)
#                 drink_obj.id = drink_obj.id + i
#                 drinks.replace_one({"id":drink_obj.id}, drink_obj.serialize(), upsert=True)
#                 user_ent.lists['favourite_drinks'].append(drink_obj.id)
            
#             update_result = users.replace_one({"id": user_ent}, user_ent.serialize(), upsert=True).upserted_id
#             if update_result is None:
#                 print("User updated with _id:", update_result)
#             else:
#                 print("User inserted with _id:", update_result)

