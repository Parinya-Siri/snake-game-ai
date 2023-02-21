import random
import numpy as np

def random_food(body,border,head):
    while True:
        x = random.randint(0,border-1)
        y = random.randint(0,border-1)
        if [x,y] not in body+[head]:
            food = [x,y]
            return food
class game:
    def __init__(self,head = (1,4), body=((1,2),(1,3),(1,4)), food = (5,5), direction=1, border = 20):
        self.head = list(head)
        self.body = [list(pos) for pos in body]
        self.direction = int(direction)
        self.border = int(border)
        self.done = False
        self.reward = 0
        self.food = random_food(self.body,self.border,self.head)
        self.state_size = 9
    
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
            self.food = random_food(self.body,self.border,self.head)
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
        pic = np.zeros((self.border,self.border))
        for i in self.body:
            pic[i[0]][i[1]]=-1
        pic[self.head[0]][self.head[1]]=2
        pic[self.food[0],self.food[1]]=5
        return pic
    
    def get_state(self):
        head, body, food, direction, border = self.call()
        state = np.zeros(self.state_size)
        if head[0]-food[0]>0:
            state[0] = 1
        if head[0]-food[0]<0:
            state[1] = 1
        if head[1]-food[1]>0:
            state[2] = 1
        if head[1]-food[1]<0:
            state[3] = 1
        if [head[0],head[1]-1] in body or head[1]-1 <0:
            state[4] = 1
        if [head[0],head[1]+1]  in body or head[1]+1 >= border:
            state[5] = 1
        if [head[0]-1,head[1]] in body or head[0]-1 < 0:
            state[6] = 1
        if [head[0]+1,head[1]] in body or head[0]+1 >= border:
            state[7] = 1
        state[8] = np.absolute(head[0]-food[0])+np.absolute(head[1]-food[1])
        return state