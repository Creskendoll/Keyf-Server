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
            cursor = coffeshops.find({"id": int(shop_id)})    
        shops_list = [CoffeeShop(data=shop).serialize() for shop in cursor] 
        return {'shops': shops_list}

    def put(self, shop_id):
        coffeshops = mongo.db.coffee_shops
        # print(request.form.to_dict())
        shop = CoffeeShop(data=request.form.to_dict())
        inserted_id = str(coffeshops.insert_one(shop.serialize()).inserted_id)

        return { "shop_id": inserted_id }

    def post(self):
        pass
    def delete(self, shop_id):
        pass
