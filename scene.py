'''
Created on Aug 24, 2013

@author: Justin Hellsten
'''

import pygame
import color
import sprite
import text

class Scene():
    ON_MOUSEMOTION = 5
    ON_MOUSEUP = 4
    ON_MOUSEDOWN = 3
    ON_KEYUP = 2
    ON_KEYDOWN = 1
    ON_CONTINUE = 0
    ON_QUIT = -1
    def __init__(self, width, height, title, flags=0, depth=0):
        pygame.init()
        self.width = width
        self.height = height
        self.title = title
        self.flags = flags
        self.depth = depth
        self.clock = pygame.time.Clock()
        self.fps = 30
        
        self.screen = None
        self.background = None
        
        self.retval = self.ON_CONTINUE
        self.groups = []
        
    def start(self):
        
        self.screen = pygame.display.set_mode((self.width, self.height), self.flags, self.depth)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(color.BLACK)
        self.screen.blit(self.background, (0,0))
        pygame.display.set_caption(self.title)
        pygame.mouse.set_visible(False)
        
    def run(self):
        self.clock.tick(self.fps)
        for event in pygame.event.get():
            for group in self.groups:
                for sprite in group:
                    sprite.doEvent(event)
            
            if event.type == pygame.QUIT:
                self.retval = self.ON_QUIT
            elif event.type == pygame.KEYDOWN:
                self.retval = self.ON_KEYDOWN
            elif event.type == pygame.KEYUP:
                self.retval = self.ON_KEYUP
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.retval = self.ON_MOUSEDOWN
            elif event.type == pygame.MOUSEMOTION:
                self.retval = self.ON_MOUSEMOTION
            elif event.type == pygame.MOUSEBUTTONUP:
                self.retval = self.ON_MOUSEUP
        
        self.update()
        for group in self.groups:
            group.clear(self.screen, self.background)
            group.update()
            group.draw(self.screen)
            
            """
                Handle sprite objects
            """
            for sprite in group:
                try:
                    sprite.rect.x += sprite.dx
                    sprite.rect.y += sprite.dy
                except:
                    continue
                    
                    
        pygame.display.flip()
        
        return self.retval
    
    def addSprite(self, sprite):
        self.addGroup(pygame.sprite.Group(sprite))

    def addGroup(self, group):
        self.groups.append(group)
        
    def update(self):
        pass
    
class SplashScene(Scene):
    DELAY_MAX = 120
    def __init__(self, width=800, height=600, title="Splash Scene - Hellsten Inc", flags=0, depth=0):
        Scene.__init__(self, 800, 600, title, flags, depth)
        self.__splashImage = sprite.StaticSprite((width/2, height/2), pygame.image.load("gfx/splashscreen.png"))
        self.addSprite(self.__splashImage)
        self.__delayCounter = 0
        
    def start(self):
        Scene.start(self)
        
        pygame.mixer.music.load("mfx/splash_scene_them.ogg")
        pygame.mixer.music.play()
        
    def update(self):
        Scene.update(self)
        if (self.__delayCounter != self.DELAY_MAX):
            self.__delayCounter += 1
        else:
            self.retval = self.ON_QUIT
        
    def changeSplashImage(self, image):
        self.__splashImage.changeImage(image)
        
    
class PlayScene(Scene):
    def __init__(self, width=800, height=600, title="Play Scene - Hellsten Inc", flags=0, depth=0):
        Scene.__init__(self, 800, 600, title, flags, depth)

        
    def start(self):
        Scene.start(self)

        
    def update(self):
        Scene.update(self)

        

        
        
class CreditScene(Scene):
    EXECUTIVE_PRODUCER = "Executive Producer"
    PRODUCER = "Producer"
    DIRECTOR = "Director"
    MAIN_PROGRAMMER = "Main Programmer"
    PROGRAMMERS = "Programmers"
    SOUND_COMPOSER = "Sound Composer"
    SCRIPT_WRITER = "Script Writer"
    ASSISTANT_DIRECTORS = "Assistant Directors"
    GRAPHICS_DESIGNERS = "Graphics Designers"
    PROGRAM_DIRECTOR = "Program Director"
    SECTIONS = "sections"
    NAMES = "names"
    OFF_SCREEN_MARGIN = 100
    TEXT_ANGLE = 0
    SECTION_SPACE = 250
    def __init__(self, width=800, height=600, title="Credit Scene - Hellsten Inc", flags=0, depth=0):
        Scene.__init__(self, 800, 600, title, flags, depth)
        self.centery = height + self.OFF_SCREEN_MARGIN
        self.centerx = width / 2
        self.credits = {self.EXECUTIVE_PRODUCER:text.CreditSection((self.centerx, self.centery), self.EXECUTIVE_PRODUCER), 
                        self.PRODUCER:text.CreditSection((self.centerx, self.__ySectionOffSet()), self.PRODUCER), 
                        self.DIRECTOR:text.CreditSection((self.centerx, self.__ySectionOffSet()), self.DIRECTOR), 
                        self.MAIN_PROGRAMMER:text.CreditSection((self.centerx, self.__ySectionOffSet()), self.MAIN_PROGRAMMER),
                        self.PROGRAMMERS:text.CreditSection((self.centerx, self.__ySectionOffSet()), self.PROGRAMMERS), 
                        self.SOUND_COMPOSER:text.CreditSection((self.centerx, self.__ySectionOffSet()), self.SOUND_COMPOSER), 
                        self.SCRIPT_WRITER:text.CreditSection((self.centerx, self.__ySectionOffSet()), self.SCRIPT_WRITER), 
                        self.ASSISTANT_DIRECTORS:text.CreditSection((self.centerx, self.__ySectionOffSet()), self.ASSISTANT_DIRECTORS),
                        self.GRAPHICS_DESIGNERS:text.CreditSection((self.centerx, self.__ySectionOffSet()), self.GRAPHICS_DESIGNERS), 
                        self.PROGRAM_DIRECTOR:text.CreditSection((self.centerx, self.__ySectionOffSet()), self.PROGRAM_DIRECTOR)}
        

        for credit in self.credits.items():
            self.addGroup(credit[1])
            
    def start(self):
        Scene.start(self)
        
        pygame.mixer.music.load("mfx/credits.ogg")
        pygame.mixer.music.play()
                
    def addName(self, section, name):
        self.credits[section].addName(text.CreditText((self.centerx, self.centery), name))
        
    def update(self):
        Scene.update(self)
        
    def __ySectionOffSet(self):
        self.centery += self.SECTION_SPACE
        return self.centery
    
        