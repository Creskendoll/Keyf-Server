import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from Keyf.Entities.Shop import CoffeeShop

class ZomatoShop(object):
    """
        name: string
        URL: string
        location: lat, long (double, double)
        rating: double
        price_range: int
        image: string
    """
    def __init__(self, data):
        shop = data['restaurant']
        self.name = shop['name']
        self.url = shop['url']
        self.location = {
            "lat": float(shop['location']['latitude']),
            "long": float(shop['location']['longitude'])
        } 
        self.rating = shop['user_rating']['aggregate_rating']
        self.price_range = shop['price_range']
        self.image = shop['featured_image']
    
    def toKeyfEntity(self):
        keyf_data = {
            'name': self.name,
            'image': self.image,
            'location': self.location,
            'rating': float(self.rating)
        }
        return CoffeeShop(data=keyf_data)