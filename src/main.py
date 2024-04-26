import random
import pygame as py
import constants as c

# clock/fps
clock = py.time.Clock()

# player
player_pos = 0
dt = 0

obstacles = [["w" for i in range(c.OBSTACLE_LIST_WIDTH)] for j in range(c.OBSTACLE_LIST_HEIGHT)]

walls = []

# while loop for the game
running = True

# screen
screen = py.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

# Function to generate a random maze using Depth-First Search algorithm
def generate_maze(width, height):
    global obstacles

    # Start at a specified point
    start_x = 0
    start_y = 0
    
    # Distance from the end point
    dist_end_x = c.OBSTACLE_LIST_WIDTH - 1
    dist_end_y = c.OBSTACLE_LIST_HEIGHT - 1

    # Mark the starting point as empty
    obstacles[start_y][start_x] = "o"
    
    # generates a path from the starting point to the goal
    while dist_end_x != 0 or dist_end_y != 0:
        if (random.randint(0, 1) == 0 and dist_end_x != 0):
            obstacles[start_y][start_x + 1] = "o"
            start_x += 1
            dist_end_x -= 1
        elif dist_end_y != 0:
            obstacles[start_y + 1][start_x] = "o"
            start_y += 1
            dist_end_y -= 1
            
        print(dist_end_x, dist_end_y)

    # mark the goal position
    obstacles[-1][-1] = "g"

# initialize the obstacles and player
def init():
    global player_pos
    global obstacles
    
    # player position
    player_pos = py.Vector2(c.PLAYER_START_X, c.PLAYER_START_Y)
    
    # obstacle generation
    generate_maze(c.OBSTACLE_LIST_WIDTH, c.OBSTACLE_LIST_HEIGHT)
            

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
                    player_pos = py.Vector2(c.PLAYER_START_X, c.PLAYER_START_Y)
        
        # goal detection
        for circle in circles:
            if goal.colliderect(circle):
                # temporary winning condition for now
                player_pos = py.Vector2(c.PLAYER_START_X, c.PLAYER_START_Y)
        
        ''' Title: Pygame Front Page - Pygame v.2.6.0 Documentation
        Author: Kim, Youngmok
        Date: 2021
        Code version: 2.6.0
        Availability: https://www.pygame.org/docs/ref/pygame.html
        '''
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

# initializing and starting maze runner        
init()
main_loop()

# quits pygame
py.quit()