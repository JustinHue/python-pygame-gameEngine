'''
Created on Aug 18, 2013

@author: Justin Hellsten
'''

import math


"""
    Physics Constants
"""
EARTH_SURFACE_GRAVITY = 9.81
MOON_SURFACE_GRAVITY = 1.60
BASIC_GRAVITY = 1.00

def init():
    pass


def calculateComponents(speed, angle):
    radians = angle * math.pi / 180
    dx = speed * math.cos(radians)
    dy = speed * math.sin(radians) * -1
    return dx, dy
 

def calculateVector(dx, dy):
    speed = math.sqrt((dx * dx) + (dy * dy))
    radians = math.atan2(dy, dx)
    dir = radians / math.pi * 180
    return speed, dir


def move(x, y, dx, dy):
    return x + dx, y + dy


def applyForce(dx, dy, speed, dir, amt, angle):
    fdx, fdy = calculateComponents(amt, angle)
    dx += fdx
    dy += fdy
    speed, dir = calculateVector(dx, dy)
    return dx, dy, speed, dir


class PhysicsHandle():
    GRAVITY_DIR_LEFT = 180
    GRAVITY_DIR_TOP = 90
    GRAVITY_DIR_RIGHT = 0
    GRAVITY_DIR_BOTTOM = 270
    def __init__(self, gravityForce=BASIC_GRAVITY, gravityDir=GRAVITY_DIR_BOTTOM):
        self.gravityDir = gravityDir
        self.gravityForce = gravityForce
        self.objects = []
        

    def addObject(self, obj):
        self.objects.append(obj)
        
        
    def update(self):
        for obj in self.objects:
            """
                Apply gravity force to objects
            """ 
            obj.dx, obj.dy, obj.speed, obj.dir = applyForce(obj.dx, obj.dy, obj.speed, obj.dir, 
                                                            self.gravityForce, self.GRAVITY_DIR_BOTTOM)
            """
                Move objects
            """
            obj.rect.x, obj.rect.y = move(obj.rect.x, obj.rect.y, obj.dx, obj.dy)
            
