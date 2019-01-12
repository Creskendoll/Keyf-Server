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
        coffeshops.replace_one({"id": shop.id}, shop.serialize(), upsert=True)

        return { "shop_id": shop.id }

    def post(self):
        pass
    def delete(self, shop_id):
        pass
