import random
import pygame as py
import constants as c

# clock/fps
clock = py.time.Clock()

# player
player_pos = 0
dt = 0

# obstacles
obstacles = [["w", "o", "o", "o", "o", "o", "o", "o", "o", "o"], 
             ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], 
             ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], 
             ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], 
             ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], 
             ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], 
             ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], 
             ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], 
             ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o"], 
             ["o", "o", "o", "o", "o", "o", "o", "o", "o", "g"]]
walls = []

# while loop for the game
running = True

# screen
screen = py.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

# initialize the obstacles and player
def init():
    global player_pos
    global obstacles
    
    # player position
    player_pos = py.Vector2(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
    
    # obstacles will be done later
    for row in range(len(obstacles)):
        for col in range(len(obstacles[row])):
            if random.randint(0, 1) == 1 and obstacles[row][col] != "g":
                obstacles[row][col] = "w"
    
    for row in obstacles:
        for box in row:
            if random.randint(0, 1) == 1 and box != "g":
                box = "w"

    obstacles[3][4] = "o"
    obstacles[3][5] = "o"
    obstacles[4][4] = "o"
    obstacles[4][5] = "o"
    obstacles[5][4] = "o"
    obstacles[5][5] = "o"
            

# main game loop
def main_loop():
    global player_pos
    global dt
    global obstacles
    global walls
    global running
    
    while running:
        # event handling
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
        
        # clear screen
        screen.fill(c.BACKGROUND_COLOR)
        
        # creating our circles to represent the player
        mainCircle = py.draw.circle(screen, c.PLAYER_COLOR, player_pos, c.PLAYER_CIRCLE_RADIUS)
        
        # these circles are used to allow the player to wrap around the screen
        # idea by Nate Bailey
        topCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x, player_pos.y + c.SCREEN_HEIGHT), c.PLAYER_CIRCLE_RADIUS)
        bottomCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x, player_pos.y - c.SCREEN_HEIGHT), c.PLAYER_CIRCLE_RADIUS)
        leftCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x - c.SCREEN_WIDTH, player_pos.y), c.PLAYER_CIRCLE_RADIUS)
        rightCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x + c.SCREEN_WIDTH, player_pos.y), c.PLAYER_CIRCLE_RADIUS)
        quadOneCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x + c.SCREEN_WIDTH, player_pos.y + c.SCREEN_HEIGHT), c.PLAYER_CIRCLE_RADIUS)
        quadTwoCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x - c.SCREEN_WIDTH, player_pos.y + c.SCREEN_HEIGHT), c.PLAYER_CIRCLE_RADIUS)
        quadThreeCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x - c.SCREEN_WIDTH, player_pos.y - c.SCREEN_HEIGHT), c.PLAYER_CIRCLE_RADIUS)
        quadFourCircle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x + c.SCREEN_WIDTH, player_pos.y - c.SCREEN_HEIGHT), c.PLAYER_CIRCLE_RADIUS)
        
        circles = [mainCircle, topCircle, bottomCircle, leftCircle, rightCircle, quadOneCircle, quadTwoCircle, quadThreeCircle, quadFourCircle]
        
        # creating the walls based on how the obstacles list is initialized
        for row in range(len(obstacles)):
            for col in range(len(obstacles[row])):
                if obstacles[row][col] == "w":
                    # wall creation
                    wall = py.draw.rect(screen, c.WALL_COLOR, ((c.WALL_WIDTH * col, c.WALL_HEIGHT * row), (c.WALL_WIDTH, c.WALL_HEIGHT)))
                    walls.append(wall)
                if obstacles[row][col] == "g":
                    # goal creation
                    goal = py.draw.rect(screen, c.GOAL_COLOR, ((c.WALL_WIDTH * col, c.WALL_HEIGHT * row), (c.WALL_WIDTH, c.WALL_HEIGHT)))
                # if no wall or goal, then it's an open space with no need to draw anything
        
        # collision detection
        for wall in walls:
            for circle in circles:
                if wall.colliderect(circle):
                    # temporary losing condition for now
                    player_pos = py.Vector2(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
        
        # goal detection
        for circle in circles:
            if goal.colliderect(circle):
                # temporary winning condition for now
                player_pos = py.Vector2(c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2)
        
        # update player
        # general movement learned from pygame documentation
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
        # idea by Nate Bailey
        player_pos.y = (player_pos.y + screen.get_height()) % screen.get_height()
        player_pos.x = (player_pos.x + screen.get_width()) % screen.get_width()
        
        
        # update display
        py.display.flip()
        
        # delta time for the player
        dt = clock.tick(c.FPS) / 1000

# initializing and starting maze runner        
init()
main_loop()

# quits pygame
py.quit()