'''
Created on Aug 17, 2013

@author: Justin Hellsten
'''

import pygame

class Scene(object):  
    def __init__(self, (width, height), title, flags = 0, depth = 32):
        self.width = width
        self.height = height
        self.title = title
        self.flags = flags
        self.depth = depth
        self.objects = []
        self.keepGoing = True

        
    def setStopBounds(self, bound):
        self.stopBound = bound

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
                    
            self.update()
            for object in self.objects:
                object.update()
                object.clear(self.screen, self.background)
                object.render(self.screen)

            pygame.display.flip()

    def stop(self):
        self.keepGoing = False

    def addObject(self, object):
        self.objects.append(object)
        
    def doEvents(self, event):
        pass
        
    def update(self):
        pass
    