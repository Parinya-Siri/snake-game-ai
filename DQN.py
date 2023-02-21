import random
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from tqdm import tqdm
from game import*

class DQNAgent:
    def __init__(self, state_size, action_size, learning_rate, discount_rate, exploration_rate, exploration_decay, min_exploration_rate):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.discount_rate = discount_rate
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay
        self.min_exploration_rate = min_exploration_rate
        self.memory = []
        self.batch_size = 64
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = DQN(state_size, action_size).to(self.device)
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)
        self.criterion = nn.MSELoss()

    def choose_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return np.random.choice(self.action_size)
        state_tensor = torch.FloatTensor(state).to(self.device)
        q_values = self.model(state_tensor)
        return torch.argmax(q_values).item()

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def learn(self):
        if len(self.memory) < self.batch_size:
            return
        minibatch = random.sample(self.memory, self.batch_size)
        states = []
        targets = []
        for state, action, reward, next_state, done in minibatch:
            state_tensor = torch.FloatTensor(state).to(self.device)
            next_state_tensor = torch.FloatTensor(next_state).to(self.device)
            q_values = self.model(state_tensor)
            if done:
                target = reward
            else:
                next_q_values = self.model(next_state_tensor)
                max_next_q_value = torch.max(next_q_values).item()
                target = reward + self.discount_rate * max_next_q_value
            target_q_values = q_values.clone().detach()
            target_q_values[action] = target
            states.append(state)
            targets.append(target_q_values)
        states_tensor = torch.FloatTensor(states).to(self.device)
        targets_tensor = torch.stack(targets).to(self.device)
        self.optimizer.zero_grad()
        predictions_tensor = self.model(states_tensor)
        loss = self.criterion(predictions_tensor, targets_tensor)
        loss.backward()
        self.optimizer.step()
        self.exploration_rate = max(self.exploration_rate * self.exploration_decay, self.min_exploration_rate)

    def save_model(self, path):
        torch.save(self.model.state_dict(), path)

class DQN(nn.Module):
    def __init__(self, state_size, action_size):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(state_size, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, action_size)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
    
class GameEnv:
    def __init__(self):
        self.game = game()
        self.state_size = 8
        self.action_space = 4

    def reset(self):
        self.game = game()
        return self.get_state()

    def get_state(self):
        head, body, food, direction, border = self.game.call()
        state = np.zeros(self.state_size)
        if head[0]-food[0]>0:
            state[0] = 1
        if head[0]-food[0]<0:
            state[1] = 1
        if head[1]-food[1]>0:
            state[2] = 1
        if head[1]-food[1]<0:
            state[3] = 1
        if [head[0]-1,head[1]] in body or head[0]-1 < 0:
            state[4] = 1
        if [head[0]+1,head[1]] in body or head[0]+1 >= border:
            state[5] = 1
        if [head[0],head[1]-1] in body or head[1]-1 <0:
            state[6] = 1
        if [head[0],head[1]+1]  in body or head[1]+1 >= border:
            state[7] = 1
        return state

    def step(self, action):
        self.game.move(action)
        if not self.game.is_done():
            state = self.get_state()
        state = np.zeros(self.state_size)
        reward = self.game.get_reward()
        done = self.game.is_done()
        return state, reward, done

env = GameEnv()
agent = DQNAgent(env.state_size, env.action_space, 
                 learning_rate = 0.01, 
                 discount_rate = 0.95, 
                 exploration_rate = 1.0, 
                 exploration_decay = 0.995, 
                 min_exploration_rate = 0.01) 

num_episodes = 10000
batch_size = 32

for episode in tqdm(range(num_episodes)):
    state = env.reset()
    done = False
    steps = 0
    total_reward = 0
    dead = 0
    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.remember(state, action, reward, next_state, done)
        total_reward += reward
        if reward == 1:
            print('head: ', env.game.head, 'food: ', env.game.food ,'total: ',total_reward, 'episode: ',episode)
            dead = 1
        state = next_state
        agent.learn()
    if dead == 1:
        print('total: ',total_reward)
    if (episode+1) % 100 == 0:
        print("Episode: {:4d}, Score: {:4d}, Epsilon: {:.4f}".format(episode+1, total_reward, agent.exploration_rate))
    if (episode+1) % 500 == 0:
        agent.save_model("dqn_model_{}.pth".format(episode+1))
        print("model saved")
