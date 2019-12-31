from Keyf.Entities import DBEntity


class User(DBEntity):
    def __init__(self, data={}):
        if "id" in data:
            self.id = data["id"]
        else:
            self.id = -1
        if "name" in data:
            self.name = data["name"]
        else:
            self.name = ""
        if "photo" in data:
            self.photo = data["photo"]
        else:
            self.photo = -1
        if "lists" in data:
            self.lists = data["lists"]
        else:
            self.lists = {"favorite_shops": [], "favorite_items": [], "wish_list": []}

    def serialize(self):
        obj = {
            "id": self.id,
            "name": self.name,
            "photo": self.photo,
            "lists": self.lists,
        }
        return obj
