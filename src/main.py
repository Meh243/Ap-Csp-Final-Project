# regular imports
import constants as c
import pygame as py

'''
these will be the game functions will be
'''
def initialize_maze_runner():
    player_pos = py.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    return player_pos

def run_maze_runner(delta_time, player_pos):
    # player set up
    py.draw.circle(screen, "red", player_pos, 40)
    
    # lets the player wrap around screen cleanly
    # idea created by Nate Bailey
    py.draw.circle(screen, "red", (player_pos.x, player_pos.y + screen.get_height()), 40)
    py.draw.circle(screen, "red", (player_pos.x,  player_pos.y - screen.get_height()), 40)
    py.draw.circle(screen, "red", (player_pos.x + screen.get_width(), player_pos.y), 40)
    py.draw.circle(screen, "red", (player_pos.x - screen.get_width(), player_pos.y), 40)
    py.draw.circle(screen, "red", (player_pos.x + screen.get_width(), player_pos.y + screen.get_height()), 40)
    py.draw.circle(screen, "red", (player_pos.x - screen.get_width(),  player_pos.y - screen.get_height()), 40)
    py.draw.circle(screen, "red", (player_pos.x + screen.get_width(), player_pos.y - screen.get_height()), 40)
    py.draw.circle(screen, "red", (player_pos.x - screen.get_width(), player_pos.y + screen.get_height()), 40)
    
    # player movement
    keys = py.key.get_pressed()
    if keys[py.K_w]:
        player_pos.y -= c.PLAYER_SPEED * delta_time
    if keys[py.K_s]:
        player_pos.y += c.PLAYER_SPEED * delta_time
    if keys[py.K_a]:
        player_pos.x -= c.PLAYER_SPEED * delta_time
    if keys[py.K_d]:
        player_pos.x += c.PLAYER_SPEED * delta_time
        
    player_pos.y = (player_pos.y + screen.get_height()) % screen.get_height()
    player_pos.x = (player_pos.x + screen.get_width()) % screen.get_width()
    

def calculate_score_maze_runner():
    pass

'''
this is were the games will be run with pygame
'''


# pygame initialization
py.init()
screen = py.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
clock = py.time.Clock()
py.display.set_caption("spin the wheel!")
running = True

# TODO: temporary for testing
delta_time = 0
player_pos = initialize_maze_runner()

# running pygame/the selected game
while running:
    # checks if the user quits the game
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    # fills the screen with a color to wipe away the previous frame
    screen.fill("black")
    
    # TODO: temporary code for testing
    run_maze_runner(delta_time, player_pos)
    
    # displays the new frame
    py.display.flip()
    
    # setting the fps
    delta_time = clock.tick(c.FPS) / 1000

# quits pygame
py.quit()