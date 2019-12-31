from Keyf.Entities import DBEntity

class Review(DBEntity):
    def __init__(self, data={}):
        if "rating" in data:
            self.rating = data["rating"]
        else:
            self.rating = 0
        if "text" in data:
            self.text = data["text"]
        else:
            self.text = ""
    
    def serialize(self):
        return {
            "rating": self.rating,
            "text": self.text
        }