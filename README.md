# Snake Game AI using Deep Q-Learning
## Overview
This project presents an AI-powered version of the classic Snake game, developed using the Pygame library and enhanced with Deep Q-Learning techniques. The AI agent, trained with PyTorch, navigates the game with adjustable parameters, showcasing an innovative approach to an NP-hard problem.

## Features
- **Dynamic Game Environment**: Adjustable board size, independent of the AI agent's sensors.
- **Advanced Sensory Inputs**: The snake's head is equipped with sensors for apple direction and obstacle detection, adaptable to varying game complexities.
- **Deep Q-Learning**: Utilizes a DQN model for training the agent with parameters like learning rate, discount rate, and exploration rates, fine-tuned for optimal performance.
## Technical Stack
- **Programming Language**: Python
- **Libraries**: Pygame, PyTorch, Numpy
- **AI Technique**: Deep Q-Learning
## Challenges and Solutions
The primary challenge was to balance the snake's survival with path optimization. Addressing this involved:

- Designing efficient sensor placement on the snake.
- Managing resource consumption with different obstacle configurations.
- Overcoming common deep learning issues like gradient vanishing in larger models.
## Unique Selling Points
While the Snake game is universally known, this project elevates its complexity by tackling it as an NP-hard problem. The AI's performance, particularly in path optimization and survival, highlights the advanced problem-solving capabilities achieved through Deep Q-Learning.

## Demonstration
A live demonstration of the AI agent, with a smaller model for web compatibility, is available at [Snake Game AI Demo](https://parinya-siri.github.io/snake-game-ai/build/web).

## Installation
To set up the project, the following libraries are required:

Pygame
PyTorch
Numpy

## Usage
Run DQL.py to train the model. The Q-learning parameters and game settings like board size and snake sensors can be adjusted in game.py.

## Future Enhancements
Expanding the snake's sensory inputs to include all grid statuses within a 3-block radius.
Developing a new game mode featuring AI-player simultaneous play on the same screen.
## About the Developer
As the sole creator and developer of this project, I've gained extensive experience in the full lifecycle of AI project development, from ideation to deployment. Key learnings include AI model design, optimization challenges in reinforcement learning, and web integration of complex AI models.

