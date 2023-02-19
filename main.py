import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the dimensions of the screen
screen_width = 800
screen_height = 600

# Define the size of the grid squares and the number of grid squares
grid_size = 20
grid_width = screen_width // grid_size
grid_height = screen_height // grid_size

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption of the screen
pygame.display.set_caption("Snake Game")

# Set the clock for the game
clock = pygame.time.Clock()

# Define the font for the score
font = pygame.font.SysFont(None, 25)

# Define the starting position of the snake
snake_position = [100, 40]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Define the starting position of the food
food_position = [random.randint(0, grid_width-1) * grid_size,
                 random.randint(0, grid_height-1) * grid_size]

# Define the starting score
score = 0

# Define the direction of the snake
direction = "RIGHT"

# Define the function to display the score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [0, 0])

# Define the main game loop
def gameLoop():
    global direction
    global snake_position
    global snake_body
    global food_position
    global score
    
    game_over = False
    
    while not game_over:
        # Set the event listeners
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    direction = "UP"
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"
        
        # Update the position of the snake
        if direction == "RIGHT":
            snake_position[0] += grid_size
        elif direction == "LEFT":
            snake_position[0] -= grid_size
        elif direction == "UP":
            snake_position[1] -= grid_size
        elif direction == "DOWN":
            snake_position[1] += grid_size
        
        # Check if the snake has collided with the walls
        if snake_position[0] >= screen_width or snake_position[0] < 0 or snake_position[1] >= screen_height or snake_position[1] < 0:
            game_over = True
        
        # Check if the snake has collided with itself
        for block in snake_body[1:]:
            if snake_position == block:
                game_over = True
        
        # Add the position of the snake to the snake body
        snake_head = []
        snake_head.append(snake_position[0])
        snake_head.append(snake_position[1])
        snake_body.insert(0, snake_head)
        print(snake_body)
        # Check if the snake has eaten the food
        if snake_position == food_position:
            food_position = [random.randint(0, grid_width-1) * grid_size,
                             random.randint(0, grid_height-1) * grid_size]
            score += 10
        else:
            snake_body.pop()

        # Set the background color of the screen
        screen.fill(BLACK)
        
        # Draw the food
        pygame.draw.rect(screen, GREEN, [food_position[0], food_position[1], grid_size, grid_size])
        
        # Draw the snake
        for block in snake_body:
            pygame.draw.rect(screen, WHITE, [block[0], block[1], grid_size, grid_size])
        
        # Display the score
        display_score(score)
        
        # Update the screen
        pygame.display.update()
        
        # Set the speed of the game
        clock.tick(10)

# Quit Pygame
gameLoop()
pygame.quit()