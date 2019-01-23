from ZomatoService import ZomatoService

class KeyfService(object):
    def __init__(self):
        self.zomatoService = ZomatoService() 

    def readZomato(self):
        return self.zomatoService.search()
