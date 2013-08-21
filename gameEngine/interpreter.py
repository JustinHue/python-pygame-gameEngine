'''
Created on Aug 18, 2013

@author: Justin Hellsten
'''

import pygame

class Interpreter():
        
    def __init__(self):
        self.running = True
        
        
    def preload(self):
        self.running = True

        
    def start(self):
        self.preload()
        while self.running:
            self.execute()
        self.unload()
    
    def execute(self):
        pass
    
    def stop(self):
        self.running = False
        
    def unload(self):
        pass



    
class SceneInterpreter(Interpreter):

    def __init__(self):
        Interpreter.__init__(self)
        
        """
            Set default values
        """
        self.groups = []
        self.width = 800
        self.height = 600
        self.title = "Scene Interpreter"
        self.flags = 0
        self.depth = 0
        self.screen = None
        self.clock = None
        self.background = None
        self.fps = 30

        
    def preload(self):

        self.screen = pygame.display.set_mode((self.width, self.height), self.flags, self.depth)
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.background = pygame.surface.Surface(self.screen.get_size())
        self.background.fill((0,0,0))
        
        Interpreter.preload(self)
        
        
    def execute(self):
        
        self.clock.tick(self.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            if event.type == pygame.KEYDOWN:
                self.stop()
                
        for group in self.groups:
            group.clear(self.screen, self.background)
            group.update()
            group.draw(self.screen)
    
    """
        Over head methods for the groups attribute
    """
    def addGroup(self, group):
        self.groups.append(group)

    def addSprite(self, sprite):
        self.addGroup(pygame.sprite.Group(sprite))
    
    
    def unload(self):
        pass
    

            
            
class SequentialInterpreter(Interpreter):
    
    START = 0
    NEXT = 1
    
    def __init__(self):
        Interpreter.__init__(self)

        self.interpreters = []
        self.order = 0
        self.LAST = -1
        self.lastOrder = self.order

    def execute(self):
        """
            Run the interpreters in sequential order
        """
        self.interpreters[self.order].start()
        
        if self.order == self.LAST:
            self.order = self.START
        else:
            self.order += self.NEXT


    def addInterpreter(self, interpreter):
        self.interpreters.append(interpreter)
        self.LAST += 1
        