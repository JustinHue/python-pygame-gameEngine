'''
Created on Aug 17, 2013

@author: Justin Hellsten
'''

import gameEngine

def main():
    gameEngine.init()
    
    mainScene = gameEngine.scene.Scene((800, 600), "Ritz by Justin Hellsten")
    mainScene.start()
    
if __name__ == "__main__": main()
