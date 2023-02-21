import pygame
import random
import asyncio
from game import*
import numpy as np

fc1 =[[-0.0904248 , -0.18438685,  0.1414369 , -0.19389527, -0.16965224,
        -0.14829643, -0.29979154, -0.09371044],
       [ 0.58959025,  0.351604  , -0.9236297 ,  0.14803159,  0.07810185,
        -0.8792623 ,  0.39464372,  0.07586305],
       [ 0.38030463,  0.15537038,  0.00613188,  0.0861648 ,  0.73382366,
        -0.11766044, -0.16081649,  0.63894266],
       [-0.4554326 ,  0.01135212, -0.13814145,  0.3159984 , -0.06313638,
        -0.1683577 ,  0.9561267 ,  0.39963764],
       [-0.13782935, -0.04771541,  0.07723986,  0.10098641, -0.28691852,
        -0.65067774,  0.29239017,  0.88764524],
       [ 0.05454277,  0.29268187, -0.31406265,  0.05512328, -0.07011997,
         0.7624972 , -0.11415049, -0.12839916],
       [ 0.13846982,  0.37058282,  0.5448833 , -0.1848408 ,  0.26309797,
         0.7743549 ,  0.42429975,  0.26155955],
       [ 0.18179837,  0.15897076, -0.14080288, -0.01993187, -0.5654355 ,
         0.00368249,  0.4538788 ,  0.118145  ],
       [ 0.12508284,  0.11650252, -0.35244778,  0.05315715,  0.3136381 ,
         0.62516886,  0.95549685,  0.5510709 ],
       [-0.2567081 ,  0.30247676,  0.10115149,  0.20424978, -0.26771414,
        -0.31034067,  0.24560343, -0.58461386],
       [-0.34271982, -0.07455757,  0.17337728,  0.05313777, -0.6932333 ,
         0.2867276 , -0.36366573,  0.43223122],
       [ 0.07258815,  0.09051716, -0.44870335,  0.21321812,  0.03895395,
         0.60418785, -0.4314582 ,  0.21944374],
       [-0.12741612, -0.00938284,  0.05320287, -0.07443117, -0.0561514 ,
         0.2596226 , -0.04043712, -0.15480149],
       [-0.43317422,  0.1610588 ,  0.34492612,  0.628086  , -0.09055167,
        -0.24093229, -0.31959894,  1.1972787 ],
       [-0.11046415,  0.46851492,  0.07345857,  0.34905457,  0.84514725,
        -0.06416046,  0.11208924, -0.32375085],
       [-0.13416342,  0.12054896,  0.40826744,  0.37846774, -0.37188825,
         0.26502606,  0.45642942,  0.62936205]]
fc2 = [[ 0.17254746,  0.16964981, -0.52280766,  0.56248856, -0.23731971,
         0.38468784,  0.31818032,  0.25545076,  0.3854349 ,  0.20130937,
         0.00412943,  0.43738297,  0.02263306, -0.49848711,  0.39780575,
         0.39900973],
       [ 0.23272398, -0.09369278, -0.03458059, -0.23512873,  0.1181252 ,
         0.24895394, -0.10449252, -0.03325874, -0.23851284,  0.08530065,
        -0.22668868, -0.05067453,  0.00920248,  0.10650522, -0.11776373,
        -0.07511562],
       [-0.14676723, -0.18030119,  0.05781644, -0.1728346 , -0.23738089,
        -0.02414605, -0.18315354, -0.07758716, -0.12414125, -0.06553525,
        -0.06621619,  0.17732659, -0.1368433 , -0.0386837 , -0.2066941 ,
        -0.2793616 ],
       [-0.13012728,  0.03964382,  0.54816645,  0.16869056,  0.04150983,
         0.4303764 ,  0.14919269, -0.16255848,  0.31182325, -0.32191423,
        -0.36924642,  0.12331124,  0.01402558,  0.4730379 ,  0.7710177 ,
        -0.27195662],
       [ 0.02122477,  0.5611311 , -0.18911149, -0.17055641, -0.1505082 ,
         0.92511445,  0.2428512 ,  0.11732333,  0.07708883, -0.13366796,
         0.7795085 ,  0.23933898,  0.16761674,  0.02864137, -0.22441499,
         0.33327466],
       [-0.1229566 , -0.05013229, -0.02962009,  0.45936832,  0.27683294,
        -0.49994233,  0.11057415,  0.309047  ,  0.51168233,  0.56034535,
        -0.35854855, -0.19070041, -0.15645379, -0.6684033 , -0.00680148,
         0.06226185],
       [ 0.02638793,  0.26683134,  0.07997771,  0.5920879 ,  0.40560952,
        -0.630322  , -0.08306476,  0.22556685,  0.424604  , -0.11409604,
         0.33120412,  0.5209828 ,  0.14698699,  0.7768877 , -0.3166339 ,
         0.6547674 ],
       [-0.07185674, -0.2759563 ,  0.18715745, -0.12026867,  0.44974592,
         0.20790532, -0.51083165,  0.39525473, -0.25154096,  0.767752  ,
         0.563481  , -0.34575403,  0.09648074,  0.09809881,  0.19229919,
        -0.3875519 ]]
fc3 = [[ 0.129491  , -0.29980245,  0.26404846, -0.825281  ,  0.37296063,
        -0.00369249,  0.23294505,  0.39715886],
       [-0.49621403, -0.05925674,  0.15706997,  0.06066914, -0.65814847,
         0.71936095,  0.14417821,  0.9205365 ],
       [-0.61650735,  0.14219129, -0.03817922,  0.20444869,  0.5266399 ,
        -0.49365953, -0.27039582,  0.22958492],
       [ 0.26667872,  0.34878042,  0.05815583, -0.01687377,  0.09511582,
         0.38133574, -0.6925335 ,  0.6417858 ]]
b1 = [-0.23510945, -0.22060533,  0.2706176 ,  0.03632661, -0.0273398 ,
        0.21158527, -0.0457688 ,  0.6713924 , -0.05527752,  0.60583615,
        0.9443976 , -0.12421431, -0.31587666,  0.06358013,  0.17543952,
        0.05077705]
b2 = [ 0.16108678, -0.18023956,  0.11888285,  0.1651831 ,  0.10468369,
        0.01283279,  0.2208323 ,  0.58652353]
b3 = [0.08725061, 0.18133354, 0.81122863, 0.4002299 ]

def action(state):
    result = np.matmul(fc1,np.array(state))
    result = result+b1
    result = np.maximum(result, 0)   # Apply ReLU activation function
    result = np.matmul(fc2,result)
    result = result+b2
    result = np.maximum(result, 0)   # Apply ReLU activation function
    result = np.matmul(fc3,result)
    result = result+b3
    return result

# AI here
ai = True

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
    screen.blit(score_text, [screen_width/2, 0])
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


# Define the main game loop
async def gameLoop(g):
    high_score = 0
    new_high_score = 0
    snake_position,snake_body,food_position,score,direction,new_high_score = reset(g)    
    playing = True
    game_over = False
    while playing:
        # AI ACTION
        if ai == True:
            state = g.get_state()
            direction = np.argmax(action(state))
        # Set the event listeners
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
        clock.tick(20)
        
        
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