import random
import pygame as py
import constants as c

# clock/fps
clock = py.time.Clock()

# counter
counter = 10

# player
player_pos = 0
dt = 0

# the list that represents our map with walls("w"), open spaces("o"), and the goal("g")
map = [["w" for i in range(c.MAP_LIST_WIDTH)] for j in range(c.MAP_LIST_HEIGHT)]

walls = []

# while loop for the game
running = True

# screen
screen = py.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

# Function to generate a random maze using Depth-First Search algorithm
def generate_maze():
    global map
    
    # Start at a specified point
    start_x = 0
    start_y = 0
    
    # Distance from the end point
    dist_end_x = c.MAP_LIST_WIDTH - 1
    dist_end_y = c.MAP_LIST_HEIGHT - 1

    # Mark the starting point as empty
    map[start_y][start_x] = "o"
    
    # generates a path from the starting point to the goal
    while dist_end_x != 0 or dist_end_y != 0:
        if (random.randint(0, 1) == 0 and dist_end_x != 0):
            map[start_y][start_x + 1] = "o"
            start_x += 1
            dist_end_x -= 1
        elif dist_end_y != 0:
            map[start_y + 1][start_x] = "o"
            start_y += 1
            dist_end_y -= 1

    # creates branching paths from the main path
    for i in range(c.NUMBER_OF_BRANCHING_PATHS):
        # random x value for the branching path
        random_x = random.randint(0, c.MAP_LIST_WIDTH - 1)
        
        # creates the branching path in the y axis
        for j in range(c.MAP_LIST_HEIGHT):
            map[j][random_x] = "o"
    

    # mark the goal position
    map[-1][-1] = "g"

# initialize the map and player
def init():
    global player_pos
    
    # player position
    player_pos = py.Vector2(c.PLAYER_START_X, c.PLAYER_START_Y)
    
    # map generation
    generate_maze()
            

# main game loop
def main_loop():
    global clock
    global counter
    global player_pos
    global dt
    global map
    global walls
    global running
    
    while running:
        # event handling
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
        
        # timer
        counter -= dt
        py.display.set_caption(str(int(counter)))
        
        # if the counter reaches 0, the player loses
        if counter <= 0:
            py.display.set_caption("YOU LOSE!")
            print("YOU LOSE!")
            running = False
        
        # clear screen
        screen.fill(c.BACKGROUND_COLOR)
        
        # creating our circles to represent the player
        main_circle = py.draw.circle(screen, c.PLAYER_COLOR, player_pos, c.PLAYER_CIRCLE_RADIUS)
        
        # these circles are used to allow the player to wrap around the screen
        top_circle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x, player_pos.y + c.SCREEN_HEIGHT), c.PLAYER_CIRCLE_RADIUS)
        bottom_circle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x, player_pos.y - c.SCREEN_HEIGHT), c.PLAYER_CIRCLE_RADIUS)
        left_circle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x - c.SCREEN_WIDTH, player_pos.y), c.PLAYER_CIRCLE_RADIUS)
        right_circle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x + c.SCREEN_WIDTH, player_pos.y), c.PLAYER_CIRCLE_RADIUS)
        quad_one_circle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x + c.SCREEN_WIDTH, player_pos.y + c.SCREEN_HEIGHT), c.PLAYER_CIRCLE_RADIUS)
        quad_two_circle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x - c.SCREEN_WIDTH, player_pos.y + c.SCREEN_HEIGHT), c.PLAYER_CIRCLE_RADIUS)
        quad_three_circle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x - c.SCREEN_WIDTH, player_pos.y - c.SCREEN_HEIGHT), c.PLAYER_CIRCLE_RADIUS)
        quad_four_circle = py.draw.circle(screen, c.PLAYER_COLOR, (player_pos.x + c.SCREEN_WIDTH, player_pos.y - c.SCREEN_HEIGHT), c.PLAYER_CIRCLE_RADIUS)
        
        circles = [main_circle, top_circle, bottom_circle, left_circle, right_circle, quad_one_circle, quad_two_circle, quad_three_circle, quad_four_circle]
        
        # creating the walls based on how the map list is initialized
        for row in range(len(map)):
            for col in range(len(map[row])):
                if map[row][col] == "w":
                    # wall creation
                    wall = py.draw.rect(screen, c.WALL_COLOR, ((c.WALL_WIDTH * col, c.WALL_HEIGHT * row), (c.WALL_WIDTH, c.WALL_HEIGHT)))
                    walls.append(wall)
                if map[row][col] == "g":
                    # goal creation
                    goal = py.draw.rect(screen, c.GOAL_COLOR, ((c.WALL_WIDTH * col, c.WALL_HEIGHT * row), (c.WALL_WIDTH, c.WALL_HEIGHT)))
                # if no wall or goal, then it's an open space with no need to draw anything
        
        # collision detection
        for wall in walls:
            for circle in circles:
                if wall.colliderect(circle):
                    # when hitting a wall, the player is reset to the starting position
                    player_pos = py.Vector2(c.PLAYER_START_X, c.PLAYER_START_Y)
        
        # goal detection
        for circle in circles:
            if goal.colliderect(circle):
                # when hitting the goal, the player wins the game
                py.display.set_caption("YOU WIN!")
                print("YOU WIN!")
                running = False
        
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