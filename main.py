'''
Created on Aug 17, 2013

@author: Justin Hellsten

'''

import gameEngine


class SplashScene(gameEngine.interpreter.SceneInterpreter):
    def __init__(self):
        gameEngine.interpreter.SceneInterpreter.__init__(self)
        
        self.title = "Splash Scene - by Justin Hellsten"
        
    def execute(self):
        gameEngine.interpreter.SceneInterpreter.execute(self)
        
        
def main():
    gameEngine.init()
    game = gameEngine.interpreter.GameInterpreter()
    game.splashInterpreter = SplashScene()
    
    game.start()
    
    
if __name__ == "__main__": 
    main()
