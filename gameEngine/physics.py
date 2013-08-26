'''
Created on Aug 18, 2013

@author: Justin Hellsten
'''

import math
import sprite

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


     
    
def collidesWith(obj, obj2):
    pass


def collidesWith(obj, center, (width, height)):
    pass
    
    

    
    
class PhysicsInterpreter():
    GRAVITY_DIR_LEFT = 180
    GRAVITY_DIR_TOP = 90
    GRAVITY_DIR_RIGHT = 0
    GRAVITY_DIR_BOTTOM = 270
    BOUND_NONE = 0
    BOUND_LEFT = 1
    BOUND_TOP = 2
    BOUND_RIGHT = 4
    BOUND_BOTTOM = 8
    BOUND_ALL = BOUND_LEFT | BOUND_TOP | BOUND_RIGHT | BOUND_BOTTOM
    def __init__(self, scene, gravityForce=BASIC_GRAVITY, gravityDir=GRAVITY_DIR_BOTTOM, bounds=BOUND_ALL):
        self.scene = scene
        self.gravityDir = gravityDir
        self.bounds = bounds
        self.gravityForce = gravityForce
        self.objects = []
        

    def addObject(self, obj):
        self.objects.append(obj)
        
        
    def setBounds(self, bounds):
        self.bounds = bounds
        

    def update(self):
        for obj in self.objects:
            if (obj.hwnd == sprite.INTERNAL_HWND_ID_1):
                """
                    Apply gravity force to objects
                """                 
                obj.dx, obj.dy, obj.speed, obj.dir = applyForce(obj.dx, obj.dy, obj.speed, obj.dir, 
                                                                self.gravityForce, self.GRAVITY_DIR_BOTTOM)

                """
                    Move objects
                """
                obj.rect.x, obj.rect.y = move(obj.rect.x, obj.rect.y, obj.dx, obj.dy)
                
            """ 
                Check in and out bounds
            """
            # Extract bound info
            exBounds = (self.bounds & self.BOUND_LEFT, self.bounds & self.BOUND_TOP,
                        self.bounds & self.BOUND_RIGHT, self.bounds & self.BOUND_BOTTOM)

            if (exBounds[0]):
                if (obj.rect.right < 0):
                    pass
                if (obj.rect.left < 0):
                    obj.rect.left = 0
            if (exBounds[1]):
                if (obj.rect.bottom < 0):
                    pass
                if (obj.rect.top < 0):
                    obj.rect.top = 0
            if (exBounds[2]):
                if (obj.rect.left > self.scene.width):
                    pass
                if (obj.rect.right > self.scene.width):
                    obj.rect.right = self.scene.width
            if (exBounds[3]):
                if (obj.rect.top > self.scene.height):
                    pass
                if (obj.rect.bottom > self.scene.height):
                    obj.rect.bottom = self.scene.height
                    
