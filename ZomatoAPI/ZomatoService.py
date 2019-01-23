import io
import json
import requests

class ZomatoService(object):
    def __init__(self):
        # Read JSON for options 
        with io.open('config.json', mode='r', encoding='utf-8') as config_file:
            config_data = json.load(config_file)
            # Connection URL
            self.URL = config_data['BASE_URL']
            # Connection key
            self.API_KEY = config_data['ZOMATO_API_KEY']
            # Search options
            self.search_options = config_data['search_options']
    
    # Get request with API key
    def get(self, params={}):
        # Mandatory parameter
        headers = {
            'content-type': 'application/json',
            'user-key': self.API_KEY
        }
        # TODO: Add better error handling
        result = requests.get(self.URL, headers=headers, params=params)
        if result.status_code == 200:
            return result.json()
        else:
            return None

    # Search Zomato
    def search(self, options={}):
        """
        - lat : double 
        - lon : double 
        - radius : double (meters)
        - count : integer
        - category : string: 6 (Cafes), 5 (Takeaway) {https://developers.zomato.com/documentation#!/common/categories}
        """
        # Change params logically  
        # options['lat'] = 0.0
        # options['lon'] = 0.0
        # options['radius'] = 0.0
        # options['category'] = str(6)
        # Get options from self
        self.URL = self.URL + "search"
        options = self.search_options

        return self.get(params=options)
