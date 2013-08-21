'''
Created on Aug 18, 2013

@author: Justin Hellsten
'''

import pygame

class Interpreter():
    
    EXEC_SUCESS = 0
    EXEC_FAIL = -1
    
    def __init__(self):
        self.__running = True
        self.retex = self.EXEC_SUCESS
        
    def preload(self):
        pass
    
    def start(self):
        self.preload()
        while self.__running:
            self.execute()
        self.unload()
        return self.retex
    
    def execute(self):
        pass
    
    def stop(self):
        self.__running = False
        
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
        self.fps = 30
        
    def preload(self):
        self.screen = pygame.display.set_mode((self.width, self.height), self.flags, self.depth)
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        
    def execute(self):
        self.clock.tick(self.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
    
    
    def unload(self):
        pass
    

class GameInterpreter(Interpreter):
    
    EXEC_TERMINATE = -2
    EXEC_NEXT = 0
    EXEC_SPLASH = 1
    EXEC_MENU = 2
    EXEC_PLAY = 3
    EXEC_GAMEOVER = 4
    
    def __init__(self):
        Interpreter.__init__(self)

        self.__executeOrder = self.EXEC_SPLASH
        self.splashInterpreter = None
        self.menuInterpreter = None
        self.playInterpreter = None
        self.gameOverInterpreter = None


    def execute(self):
        """
            Run scenes in the following sequence: Splash, Menu, Play, Game Over...loop
        """
        if self.__executeOrder == self.EXEC_SPLASH and self.splashInterpreter != None:
            retVal = self.splashInterpreter.start()
        elif self.__executeOrder == self.EXEC_MENU and self.menuInterpreter != None:
            retVal = self.menuInterpreter.start()
        elif self.__executeOrder == self.EXEC_PLAY and self.playInterpreter != None:
            retVal = self.playInterpreter.start()
        elif self.__executeOrder == self.EXEC_GAMEOVER and self.gameOverInterpreter != None:
            retVal = self.gameOverInterpreter.start()
        else:
            retVal = self.retex = self.EXEC_FAIL
            self.stop()
            
        if retVal == self.EXEC_NEXT:
            if self.__executeOrder == self.EXEC_GAMEOVER:
                self.__executeOrder = self.EXEC_SPLASH
            else:
                self.__executeOrder += 1
        elif retVal == self.EXEC_TERMINATE:
            self.stop()
     
