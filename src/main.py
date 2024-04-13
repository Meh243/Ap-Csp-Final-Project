import pygame as py
import constants as c

# clock/fps
clock = py.time.Clock()

# player
player_pos = 0
dt = 0

# obstacles
obstacles = []

# screen
screen = py.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

# initialize the obstacles and player
def init():
    global player_pos
    global obstacles
    
    # player position
    player_pos = py.Vector2(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
    
    # obstacles will be done later

# main game loop
def main_loop():
    global player_pos
    global dt
    global obstacles
    
    while True:
        # event handling
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()
        
        # clear screen
        screen.fill(c.BACKGROUND_COLOR)
        
        # creating our circles to represent the player
        mainCircle = py.draw.circle(screen, c.PLAYER_COLOR, player_pos, 40)
        
        # these circles are used to allow the player to wrap around the screen
        topCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x, player_pos.y + c.SCREEN_HEIGHT), 40)
        bottomCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x, player_pos.y - c.SCREEN_HEIGHT), 40)
        leftCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x - c.SCREEN_WIDTH, player_pos.y), 40)
        rightCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x + c.SCREEN_WIDTH, player_pos.y), 40)
        quadOneCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x + c.SCREEN_WIDTH, player_pos.y + c.SCREEN_HEIGHT), 40)
        quadTwoCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x - c.SCREEN_WIDTH, player_pos.y + c.SCREEN_HEIGHT), 40)
        quadThreeCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x - c.SCREEN_WIDTH, player_pos.y - c.SCREEN_HEIGHT), 40)
        quadFourCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x + c.SCREEN_WIDTH, player_pos.y - c.SCREEN_HEIGHT), 40)
        
        circles = [mainCircle, topCircle, bottomCircle, leftCircle, rightCircle, quadOneCircle, quadTwoCircle, quadThreeCircle, quadFourCircle]
        
        # update player
        keys = py.key.get_pressed()
        if keys[py.K_w]:
            player_pos.y -= c.PLAYER_SPEED * dt
        if keys[py.K_s]:
            player_pos.y += c.PLAYER_SPEED * dt
        if keys[py.K_a]:
            player_pos.x -= c.PLAYER_SPEED * dt
        if keys[py.K_d]:
            player_pos.x += c.PLAYER_SPEED * dt
            
        # wraps the player position around the screen
        player_pos.y = (player_pos.y + screen.get_height()) % screen.get_height()
        player_pos.x = (player_pos.x + screen.get_width()) % screen.get_width()
        
        
        # update display
        py.display.flip()
        
        # delta time for the player
        dt = clock.tick(c.FPS) / 1000
        
init()
main_loop()

# quits pygame
py.quit()