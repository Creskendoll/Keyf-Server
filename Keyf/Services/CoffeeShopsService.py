from flask_restful import Resource
from Keyf import mongo
from flask import request
from Keyf.Entities import CoffeeShop

class CoffeeShopsService(Resource):
    def get(self, shop_id):
        coffeshops = mongo.db.coffee_shops
        if shop_id == "-1":
            cursor = coffeshops.find({})
        else:
            cursor = coffeshops.find({"id": shop_id})    
        shops_list = [CoffeeShop(data=shop).serialize() for shop in cursor]

        return {'shops': shops_list}

    def put(self, shop_id):
        coffeshops = mongo.db.coffee_shops
        shop = CoffeeShop(data=request.form.to_dict())
        result = None
        try:
            if shop.id == -1:
                id_result = list(shop_db.find({}, {"id": 1}).sort({id:-1}).limit(1))
                max_id = id_result[0].id
                shop.id = max_id + 1
                result = coffeshops.insert_one(shop.serialize()).inserted_id
            else:
                result = coffeshops.replace_one({"id": shop.id}, shop.serialize(), upsert=True).upserted_id
        except:
            print("Error connecting to DB")

        if shop.id == -1:
            return { "shop_id": str(result), "operation_type": "insert" }
        else:
            return { "shop_id": str(result), "operation_type": "replace" }

    def post(self):
        pass
    def delete(self, shop_id):
        pass
