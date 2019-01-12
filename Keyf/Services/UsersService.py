from flask_restful import Resource
from Keyf import mongo
from flask import request
from Keyf.Entities import User

class UsersService(Resource):
    def get(self, user_id):
        users = mongo.db.users
        if user_id == '-1':
            cursor = users.find({})
        else:
            cursor = users.find({"id": id})
        user_list = [User(data=user).serialize() for user in cursor]
        
        return { "users": user_list }
    
    def put(self, user_id):
        users = mongo.db.users
        user = User(data=request.form.to_dict())
        users.replace_one(user.serialize())
        return { "user_id": user.id } 
    def update(self):
        pass
    def delete(self):
        pass