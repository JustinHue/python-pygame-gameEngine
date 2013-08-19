'''
Created on Aug 17, 2013

@author: Justin Hellsten
'''

import pygame
import gameEngine

def main():
    gameEngine.init()
    
    mainScene = gameEngine.scene.Scene((800, 600), "Ritz by Justin Hellsten")
    bloodParticle = gameEngine.graphics.BloodParticle((100, 100))
    mainScene.addGroup(pygame.sprite.Group(bloodParticle, bloodParticle2))
    mainScene.start()
    
if __name__ == "__main__": main()
