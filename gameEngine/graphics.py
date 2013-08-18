'''
Created on Aug 17, 2013

@author: Justin Hellsten
'''

import pygame
import physics

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
__BLOOD_PARTICLE_SURFACE = None
__BLOOD_PARTICLE_RECT = None

def init():
    __BLOOD_PARTICLE_SURFACE = pygame.surface.Surface((BloodParticle.SIZE, BloodParticle.SIZE))
    __BLOOD_PARTICLE_SURFACE.fill(COLOR_BLOOD)
    __BLOOD_PARTICLE_RECT = __BLOOD_PARTICLE_SURFACE.get_rect()
    pass
    

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Object Definitions
   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
class BloodParticle(object):
    SIZE = 1
    def __init__(self, center):
        self.rect = __BLOOD_PARTICLE_RECT
        self.rect.center = center


    def render(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    def clear(self, cl_surface, cl_background):
        cl_image = self.image.copy()
        cl_image.blit(cl_background, self.rect)
        cl_surface.blit(cl_image, self.rect)
        
        
"""
class BloodSplatter(object):
    DENSITY = 25
    def __init__(self, center, density=DENSITY, size=BloodParticle.SIZE):
        self.blood_image = pygame.surface.Surface((size, size))
        self.blood_image.fill(BLOOD_COLOR)
        self.blood_particles = []
        while (density > 0):
            self.blood_particles.append(BloodParticle())
            density -= 1
            
        
    def update(self):
        pass
        
    def render(self, surface):
        for particle in self.blood_particles:
            surface.blit(self.blood_image, (particle[0], particle[1]))
        

    def clear(self, surface, background):
        for particle in self.blood_particles:
            particle_copy = self.blood_image.copy()
            particle_copy.blit(background, self.rect)
            surface.blit(particle_copy, self.rect)
            
"""