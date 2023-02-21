import random
import numpy as np

def random_food(body,border):
    while True:
        x = random.randint(0,border-1)
        y = random.randint(0,border-1)
        if [x,y] not in body:
            food = [x,y]
            return food
class game:
    def __init__(self,head = (1,4), body=((1,2),(1,3),(1,4)), food = (5,5), direction=1, border = 13):
        self.head = list(head)
        self.body = [list(pos) for pos in body]
        self.direction = int(direction)
        self.border = int(border)
        self.done = False
        self.reward = 0
        self.food = random_food(self.body,self.border)
    
    def snake_growth(self):
        if self.head != self.food:
            self.body = self.body[1:]
            # if self.distance(self.food,self.body[-2])>self.distance(self.food,self.head):
            #     self.reward = 1
            # else:
            #     self.reward = 0
            self.reward = 0
        else:
            self.reward = 1
            self.food = random_food(self.body,self.border)
        self.body.append(list(self.head))
        if self.head[0] >= self.border or self.head[0] < 0  or self.head[1] < 0 or self.head[1] >= self.border:
            self.done = True
            self.reward = -1
        if self.head in self.body[:len(self.body)-1]:
            self.done = True
            self.reward = -1
        
    def move(self,key):
        self.direction = key
        if self.direction == 0:#UP
            self.head[1] -= 1
            self.snake_growth()
        elif self.direction == 1:#DOWN
            self.head[1] += 1
            self.snake_growth()
        elif self.direction == 2:#LEFT
            self.head[0] -= 1
            self.snake_growth()
        elif self.direction == 3:#RIGHT
            self.head[0] += 1
            self.snake_growth()
    def distance(self,pos,food):
        distance = np.absolute(pos[1] - food[1])+np.absolute(pos[0] - food[0])
        return distance
    
    def call(self):
        
        return self.head, self.body, self.food, self.direction, self.border
    
    def is_done(self):
        return self.done
    
    def get_reward(self):
        return self.reward
    
    def visualize(self):
        pass