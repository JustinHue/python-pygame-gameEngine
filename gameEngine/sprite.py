'''
Created on Aug 18, 2013

@author: Justin
'''

import pygame
import physics

class BasicSprite(pygame.sprite.Sprite):
    def __init__(self, center, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = center
    
        
    def update(self):
        pass
    
    
    def doEvents(self, event):
        pass
    
    
class DynamicSprite(BasicSprite):
    def __init__(self, center, image, speed=0, dir=0):
        BasicSprite.__init__(self, center, image)
        self.dir = dir
        self.speed = speed
        self.dx, self.dy = physics.calculateComponents(self.speed, self.dir)
        
        
    def update(self):
        pass
        
        
    def doEvents(self, event):
        pass
    
