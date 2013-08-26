'''
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
    
    