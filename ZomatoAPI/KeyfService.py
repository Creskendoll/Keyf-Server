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
    
    def writeShop(self, shop):
        shops_db = db.coffee_shops
        result = None
        try:
            if shop.id == -1:
                id_result = list(shops_db.find({}, {"id": 1}).sort([("id",-1)]).limit(1))
                if not id_result:
                    shop.id = 1
                else:
                    max_id = id_result[0]["id"]
                    shop.id = max_id + 1
                print("Writing shop with ID:", shop.id)
                result = shops_db.insert_one(shop.serialize()).inserted_id
            else:
                print("Replacing shop with name:", shop.name)
                result = shops_db.replace_one({"name": shop.name}, shop.serialize(), upsert=True).upserted_id
        except Exception as e:
            print("Error connecting to DB.", e)

        return result
