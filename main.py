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
        
class MenuScene(gameEngine.interpreter.SceneInterpreter):
    def __init__(self):
        gameEngine.interpreter.SceneInterpreter.__init__(self)
        
        self.title = "Menu Scene - by Justin Hellsten"
        
    def execute(self):
        gameEngine.interpreter.SceneInterpreter.execute(self)
        
class PlayScene(gameEngine.interpreter.SceneInterpreter):
    def __init__(self):
        gameEngine.interpreter.SceneInterpreter.__init__(self)
        
        self.title = "Play Scene - by Justin Hellsten"
        
    def execute(self):
        gameEngine.interpreter.SceneInterpreter.execute(self)
        
class GameOverScene(gameEngine.interpreter.SceneInterpreter):
    def __init__(self):
        gameEngine.interpreter.SceneInterpreter.__init__(self)
        
        self.title = "Game Over Scene - by Justin Hellsten"
        
    def execute(self):
        gameEngine.interpreter.SceneInterpreter.execute(self)
            
            

class RitzInterpreter(gameEngine.interpreter.SequentialInterpreter):
    def __init__(self):
        gameEngine.interpreter.SequentialInterpreter.__init__(self)
        
        """
            Add scene interpreters
        """
        self.addInterpreter(SplashScene())
        self.addInterpreter(MenuScene())
        self.addInterpreter(PlayScene())
        self.addInterpreter(GameOverScene())
        
        
        
        
    def preload(self):
        gameEngine.interpreter.SequentialInterpreter.preload(self)
        

    def execute(self):
        gameEngine.interpreter.SequentialInterpreter.execute(self)
        """
            Exit game when we reach the game over scene
        """
        if self.order == self.LAST:
            self.stop()


    
def main():
    gameEngine.init()
    ritzInterpreter = RitzInterpreter()
    ritzInterpreter.start()

    
    
if __name__ == "__main__": 
    main()
