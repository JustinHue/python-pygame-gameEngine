'''
Created on Aug 17, 2013

@author: Justin Hellsten
'''

import pygame
import sprite
import random

"""
    Color Constants
"""
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLOOD = (225, 10, 10)

"""
    Internal Graphic Definitions
"""
BLOOD_PARTICLE_SURFACE = None


def init():
    global BLOOD_PARTICLE_SURFACE, BLOOD_PARTICLE_RECT
    BLOOD_PARTICLE_SURFACE = pygame.surface.Surface((BloodParticle.SIZE, BloodParticle.SIZE))
    BLOOD_PARTICLE_SURFACE.fill(COLOR_BLOOD)


"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Object Definitions
   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
class BloodParticle(sprite.DynamicSprite):
    SIZE = 2
    def __init__(self, center, speed=0, dir=0):
        sprite.DynamicSprite.__init__(self, center, BLOOD_PARTICLE_SURFACE, speed, dir)

    
class BloodSplatter(pygame.sprite.Group):
    DENSITY=25
    SPEED_MAX = 20
    def __init__(self, center, density=DENSITY):
        pygame.sprite.Group.__init__(self)
        self.density = density
        bloodCount = 0
        while (bloodCount < density):
            speed = random.random() * self.SPEED_MAX
            dir = random.randint(0, 360)
            self.add(BloodParticle(center, speed, dir))
            bloodCount += 1

        

