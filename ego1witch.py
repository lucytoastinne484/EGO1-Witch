#lets teste some ideas i want make#

import pygame as engine


#setup#
engine.init()

win_gui = engine.display.set_mode((1270,720))

clock = engine.time.Clock()

running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in engine.event.get():
        if event.type == engine.QUIT:
            running = False
            
    
    # fill the screen with a color to wipe away anything from last frame
    win_gui.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    engine.display.flip()

    clock.tick(60)  # limits FPS to 60

engine.quit()