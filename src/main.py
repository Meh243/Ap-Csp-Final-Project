# regular imports
import constants as c
import pygame as py

# games are imported here
import games.game_example as game_example

# pygame initialization
py.init()
screen = py.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
clock = py.time.Clock()
py.display.set_caption("spin the wheel!")
running = True

# running pygame/the program
while running:
    # checks if the user quits the game
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    # fills the screen with a color to wipe away the previous frame
    screen.fill("white")
    
    # temporary code for testing
    game_example.start_game()
    
    # displays the new frame
    py.display.flip()
    
    # setting the fps
    clock.tick(c.FPS)

# quits pygame
py.quit()