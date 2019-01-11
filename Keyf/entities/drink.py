from Keyf.Entities import DBEntity

class Drink (DBEntity):
    def __init__(self,data={}):
        if 'id' in data:
            self.id = data['id']
        else:
            self.id = -1
        if 'rating' in data:
            self.rating = data['rating']
        else:
            self.rating = 0.0
        if 'price' in data:
            self.price = data['price']
        else:
            self.price = 0.0
        if 'name' in data:
            self.name = data['name']
        else:
            self.name = ""
        if 'reviews' in data:
            self.reviews = data['reviews']
        else:
            self.reviews = []

    def serialize(self):
        obj = {
            "id": self.id,
            "rating": self.rating,
            "price": self.price,
            "name": self.name,
            "reviews": self.reviews,
        }       
        return obj