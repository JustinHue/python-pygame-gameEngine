'''
Created on Aug 17, 2013

@author: Justin Hellsten
'''

import pygame
import physics

class Scene(object):  
    def __init__(self, (width, height), title, flags = 0, depth = 32):
        self.width = width
        self.height = height
        self.title = title
        self.flags = flags
        self.depth = depth
        self.groups = []
        self.keepGoing = True
        self.physicsHandle = physics.PhysicsHandle()


    def start(self):
        """
            Initialize pygame and screen
        """
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode((self.width, self.height), self.flags, self.depth)
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.background = pygame.surface.Surface(self.screen.get_size())
        self.background.fill((0,0,0))

        """
            Game Loop
        """
        while self.keepGoing:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                self.doEvents(event)
                for group in self.groups:
                    for sprite in group:
                        sprite.doEvents(event)
                        

            self.update()
            for group in self.groups:
                group.clear(self.screen, self.background)
                group.update()
                group.draw(self.screen)

            pygame.display.flip()

    def stop(self):
        self.keepGoing = False


    def addGroup(self, group):
        self.groups.append(group)
        """
            Add sprites in group to physics handle
        """
        if self.physicsHandle:
            for sprite in group:
                self.physicsHandle.addObject(sprite)

    def addSprite(self, sprite):
        self.addGroup(pygame.sprite.Group(sprite))
        

    def attachPhysicsHandle(self, handle):
        self.physicsHandle = handle
    
    
    def doEvents(self, event):
        pass
        

    def update(self):
        """
            Apply physics handler physics. All scene objects have been preloaded into the handler.
        """
        if self.physicsHandle:
            self.physicsHandle.update()
        
    