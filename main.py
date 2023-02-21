import pygame
import random
import asyncio
from game import game
import numpy as np

ai = False

#import game
g = game()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the dimensions of the screen
screen_width = 20*g.border
screen_height = 20*g.border

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
def reset(g):
    g = game()
    score = 0
    direction = 1
    new_high_score = 0
    return g.head,g.body,g.food,score,direction,new_high_score

# class DQN(nn.Module):
#     def __init__(self, state_size, action_size):
#         super(DQN, self).__init__()
#         self.fc1 = nn.Linear(state_size, 128)
#         self.fc2 = nn.Linear(128, 64)
#         self.fc3 = nn.Linear(64, action_size)

#     def forward(self, x):
#         x = F.relu(self.fc1(x))
#         x = F.relu(self.fc2(x))
#         x = self.fc3(x)
#         return x

# if ai == True:
# ######################  Model path here #############################
#     agent = DQN(9,4)
#     agent.load_state_dict(torch.load('dqn_model_230.pth'))

# Define the main game loop
async def gameLoop(g):
    high_score = 0
    new_high_score = 0
    snake_position,snake_body,food_position,score,direction,new_high_score = reset(g)    
    playing = True
    game_over = False
    print('heeeeel')
    while playing:
        # AI ACTION
        if ai == True:
        #     q_values = agent(torch.FloatTensor(g.get_state()))
        #     direction = torch.argmax(q_values).item()
        # # Set the event listeners
            pass
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if direction != 3:
                            direction = 2
                    elif event.key == pygame.K_RIGHT:
                        if direction != 2:
                            direction = 3
                    elif event.key == pygame.K_UP:
                        if direction != 1:
                            direction = 0
                    elif event.key == pygame.K_DOWN:
                        if direction != 0:
                            direction = 1
        
        # Update the position of the snake
        print('heeeeel')
        g.move(direction)
        
        # Check if the snake has collided with the walls
        game_over = g.done
        
        # Add the position of the snake to the snake body
        snake_head = []
        snake_head.append(snake_position[0])
        snake_head.append(snake_position[1])
        snake_body.insert(0, snake_head)
        
        # Check if the snake has eaten the food
        if g.reward == 1:
            score += 10

        # Set the background color of the screen
        screen.fill(BLACK)
        
        # Draw the food
        pygame.draw.rect(screen, GREEN, [g.food[0]*20, g.food[1]*20, grid_size, grid_size])
        
        # Draw the snake
        for block in g.body:
            pygame.draw.rect(screen, WHITE, [block[0]*20, block[1]*20, grid_size, grid_size])
        
        # Display the score
        display_score(score)
        # Display the highest score
        if high_score<score:
            high_score = score
            new_high_score = 1
        display_high_score(high_score)
        # Update the screen
        pygame.display.update()
        await asyncio.sleep(0)
        # Set the speed of the game
        clock.tick(10)
        
        
        if game_over:
            pause = True
            game_over_screen = pygame.Surface((screen_width, screen_height))
            game_over_screen.fill((0, 0, 0))
            game_over_text = font.render("GAME OVER", True, RED)
            if new_high_score == 1:
                score_text = font.render("NEW HIGH SCORE! :" + str(score),True,WHITE)
                new_high_score = 0
            else:
                score_text = font.render("Youre score is :" + str(score),True,WHITE)
            press_text = font.render("Press any key to replay", True, WHITE)
            game_over_screen.blit(game_over_text, (screen_width/2 - game_over_text.get_width()/2, screen_height/2 - game_over_text.get_height()/2))
            game_over_screen.blit(score_text, (screen_width/2 - score_text.get_width()/2, screen_height/2 - score_text.get_height()/2+50))
            game_over_screen.blit(press_text, (screen_width/2 - press_text.get_width()/2, screen_height/2 - press_text.get_height()/2+100))
            screen.blit(game_over_screen, (0, 0))
            pygame.display.update()
            await asyncio.sleep(0)
            while pause:
                await asyncio.sleep(0)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        pause = False
                clock.tick(3)
            # Reset the game state
            g = game()
            direction = 1
            score = 0
            game_over = False


# Quit Pygame
asyncio.run(gameLoop(g))

# pygame.quit()