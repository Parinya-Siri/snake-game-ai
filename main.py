import pygame
import random
import asyncio

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

# Define the function to display the score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [0, 0])
def display_high_score(high_score):
    score_text = font.render("Highest Score: " + str(high_score), True, RED)
    screen.blit(score_text, [400, 0])
def display_game_over(score,high_score):
    game_over_text = font.render("GAME OVER : Your score is :" + str(score), True, WHITE)
    screen.blit(game_over_text, [200, 200])    

# Define Reset state
def reset():
    # Define the starting position of the snake
    snake_position = [100, 40]
    snake_body = [[100, 40], [80, 40], [60, 40]]
    # Define the starting position of the food
    food_position = [random.randint(0, grid_width-1) * grid_size,
                     random.randint(0, grid_height-1) * grid_size]
    # Define the starting score
    score = 0
    new_high_score = 0
    # Define the direction of the snake
    direction = "RIGHT"
    return snake_position,snake_body,food_position,score,direction,new_high_score
    
# Create game over screen
    # play_again_button = pygame.Rect(screen_width/2 - 75, screen_height/2 + 50, 150, 50)
    # pygame.draw.rect(game_over_screen, (0, 255, 0), play_again_button)    

# Define the main game loop
async def gameLoop():
    high_score = 0
    new_high_score = 0
    snake_position,snake_body,food_position,score,direction,new_high_score = reset()    
    game = False
    game_over = False
    while not game:
        # Set the event listeners
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if direction != "RIGHT":
                        direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    if direction != "LEFT":
                        direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    if direction != "DOWN":
                        direction = "UP"
                elif event.key == pygame.K_DOWN:
                    if direction != "UP":
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
        # Display the highest score
        if high_score<score:
            high_score = score
            new_high_score = 1
        display_high_score(high_score)
        # Update the screen
        pygame.display.update()
        
        # Set the speed of the game
        clock.tick(10)
        
        await asyncio.sleep(0)
        if game_over:
            pause = True
            game_over_screen = pygame.Surface((screen_width, screen_height))
            game_over_screen.fill((0, 0, 0))
            game_over_text = font.render("GAME OVER", True, RED)
            if new_high_score == 1:
                score_text = font.render("NEW HIGH SCORE! :" + str(score),True,WHITE)
            else:
                score_text = font.render("Youre score is :" + str(score),True,WHITE)
            press_text = font.render("Press any key to replay", True, WHITE)
            game_over_screen.blit(game_over_text, (screen_width/2 - game_over_text.get_width()/2, screen_height/2 - game_over_text.get_height()/2))
            game_over_screen.blit(score_text, (screen_width/2 - score_text.get_width()/2, screen_height/2 - score_text.get_height()/2+50))
            game_over_screen.blit(press_text, (screen_width/2 - press_text.get_width()/2, screen_height/2 - press_text.get_height()/2+100))
            screen.blit(game_over_screen, (0, 0))
            pygame.display.update()
            while pause:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        pause = False
            # Reset the game state
            snake_position,snake_body,food_position,score,direction,new_high_score = reset()  
            game_over = False


# Quit Pygame
asyncio.run(gameLoop())

# pygame.quit()