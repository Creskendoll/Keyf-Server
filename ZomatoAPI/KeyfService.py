from ZomatoService import ZomatoService
from pymongo import MongoClient
conn_file = open("../connection_string.txt", 'r')
client = MongoClient(conn_file.read())
db = client.keyf

class KeyfService(object):
    def __init__(self):
        self.zomatoService = ZomatoService()

    def readZomato(self):
        return self.zomatoService.search()
    
    def writeShop(self, shop_obj):
        shops_db = db.coffee_shops
        update_result = shops_db.replace_one({"id": shop_obj.id}, shop_obj, upsert=True).upserted_id
        if update_result is None:
            print("Shop updated with id:", shop_obj.id)
        else:
            print("Shop inserted with _id:", update_result)
