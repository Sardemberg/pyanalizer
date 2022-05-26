import json

class ShowChart:
    def __init__(self):
        self.cities_ceara = json.load(open('ui/geojson/file.json','r'))



    def show(self):
        print(self.cities_ceara['features'][0])


