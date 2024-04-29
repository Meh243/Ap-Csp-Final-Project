import random

# Function to generate a random maze using Depth-First Search algorithm
def generate_maze(width, height):
    # Initialize the maze with all walls
    maze = [["#" for _ in range(width)] for _ in range(height)]

    # Start at a random point
    start_x = random.randint(0, width - 1)
    start_y = random.randint(0, height - 1)
    
    # probability of carving a path
    probability = 0.6

    # Mark the starting point as empty
    maze[start_y][start_x] = " "

    # Recursive function to carve paths in the maze
    def carve(x, y, p):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == "#" and random.random() < p:
                maze[y + dy // 2][x + dx // 2] = " "
                maze[ny][nx] = " "
                carve(nx, ny, p)


    # Start carving paths from the starting point
    carve(start_x, start_y, probability)

    return maze

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print("".join(row))

# Generate and print a 10x10 maze
maze = generate_maze(10, 10)
print_maze(maze)
