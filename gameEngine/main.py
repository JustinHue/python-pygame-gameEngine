'''
<<<<<<< HEAD
Created on Aug 24, 2013

@author: justin
'''

import scene
import pygame

class DemoPlayScene(scene.PlayScene):
    
    
def main():
    pygame.init()
    splashScene = scene.SplashScene()
    creditsScene = scene.CreditScene()
    playScene = scene.PlayScene()
    splashScene.start()
    
    while (splashScene.run() != splashScene.ON_QUIT):
        pass


    
    playScene.start()
    
    while (playScene.run() != playScene.ON_QUIT):
        pass
    
    creditsScene.start()
    creditsScene.addName(creditsScene.EXECUTIVE_PRODUCER, "Justin Hellsten")
    creditsScene.addName(creditsScene.PRODUCER, "Justin Hellsten")
    creditsScene.addName(creditsScene.DIRECTOR, "Justin Hellsten")
    creditsScene.addName(creditsScene.MAIN_PROGRAMMER, "Justin Hellsten")
    creditsScene.addName(creditsScene.PROGRAMMERS, "Justin Hellsten")
    creditsScene.addName(creditsScene.SOUND_COMPOSER, "Justin Hellsten")
    creditsScene.addName(creditsScene.SCRIPT_WRITER, "Justin Hellsten")
    creditsScene.addName(creditsScene.ASSISTANT_DIRECTORS, "Justin Hellsten")
    creditsScene.addName(creditsScene.GRAPHICS_DESIGNERS, "Justin Hellsten")
    creditsScene.addName(creditsScene.GRAPHICS_DESIGNERS, "Jessica Hellsten")
    creditsScene.addName(creditsScene.PROGRAM_DIRECTOR, "Justin Hellsten")

    
    while (creditsScene.run() != creditsScene.ON_QUIT):
        pass
        
if __name__ == "__main__": 
    main()
    
    
=======
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
>>>>>>> 8cd61d62314461559641254d06a23226552ab81f
