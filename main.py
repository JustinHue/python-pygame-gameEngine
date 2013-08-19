'''
Created on Aug 17, 2013

@author: Justin Hellsten

'''

import gameEngine

def main():
    gameEngine.init()
    
    physicsHandle = gameEngine.physics.PhysicsHandle()
    mainScene = gameEngine.scene.Scene((800, 600), "Ritz by Justin Hellsten")
    mainScene.attachPhysicsHandle(physicsHandle)
    
    bloodSplatter = gameEngine.graphics.BloodSplatter((300, 300))
    bloodSplatter2 = gameEngine.graphics.BloodSplatter((400, 400))
    mainScene.addGroup(bloodSplatter)
    mainScene.addGroup(bloodSplatter2)
    mainScene.start()
    
if __name__ == "__main__": main()
