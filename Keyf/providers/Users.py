from flask_restful import Resource
from Keyf import mongo
from flask import request
from Keyf.entities import User

class Users(Resource):
    def get(self, user_id):
        users = mongo.db.users
        if user_id == '-1':
            cursor = users.find({})
        else:
            cursor = users.find({"id": id})

        user_list = [User.User(data=user).serialize() for user in cursor]
        
        return { "users": user_list }
    
    def put(self, user_id):
        users = mongo.db.users
        # print(request.form.to_dict())
        user = User.User(data=request.form.to_dict())
        inserted_id = str(users.insert_one(user.serialize()).inserted_id)
        return { "user_id": inserted_id } 
    def update(self):
        pass
    def delete(self):
        pass