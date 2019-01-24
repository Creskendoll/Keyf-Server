from KeyfService import KeyfService
from ZomatoShop import ZomatoShop
import json

service = KeyfService()

data = service.readZomato()

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

for shop_data in data['restaurants']:
    zomato_shop = ZomatoShop(shop_data)

