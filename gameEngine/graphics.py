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
    SIZE = 1
    def __init__(self, center):
        sprite.DynamicSprite.__init__(self, center, BLOOD_PARTICLE_SURFACE)



class BloodSplatter(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__()
        