'''
Created on Aug 18, 2013

@author: Justin Hellsten
'''

GRAVITY_CONSTANT = 9.81

DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1
DIRECTION_TOP = 2
DIRECTION_BOTTOM = 3

def init():
    pass

def calc_position(x, y, dx, dy):
    x += dx
    y += dy
    

def accelerate(dx, dy, xamt, yamt):
    dx += xamt
    dy += yamt
    

