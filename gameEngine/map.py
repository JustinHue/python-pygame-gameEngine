'''
Created on Aug 17, 2013

@author: Justin Hellsten
'''

class MapLoader():
    def __init__(self, filepath):
        self.filepath = filepath
        
        
class TileMapLoader(MapLoader):
    def __init__(self, filepath):
        MapLoader.__init__(self, filepath)
        
        