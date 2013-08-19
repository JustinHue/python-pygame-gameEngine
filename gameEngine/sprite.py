'''
Created on Aug 18, 2013

@author: Justin
'''

import pygame

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
    def __init__(self, center, image, dx=0, dy=0):
        BasicSprite.__init__(self, center, image)
        self.dx = dx
        self.dy = dy
        
    
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        
        
    def doEvents(self, event):
        pass
        