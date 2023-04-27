# Snake Game

This is a simple implementation of the classic Snake game using Python's Turtle module.

![snake](https://user-images.githubusercontent.com/108518278/231439077-407c9838-bf7c-4b20-a825-629a18977fb8.gif)

## Description

The game consists of a player-controlled snake that moves around the screen, trying to eat food pellets that appear at random locations. Each time the snake eats a pellet, it grows longer, making it harder to avoid running into itself. The game ends when the snake collides with itself or with the screen's border.

## How to Play

The player uses the arrow keys to move the snake around the screen. The snake will move continuously in the direction it's facing until it hits a wall or a body segment. The objective is to eat as much food as possible without crashing.

## Features

- Snake movement using arrow keys
- Randomly generated food pellets
- Snake grows longer as it eats food
- Score counter that increases with each food pellet eaten
- Game over screen when the snake collides with itself or the border

## Installation

1. Clone the repository: `git clone https://github.com/<username>/snake-game.git`
2. Install the required modules: `pip install -r requirements.txt`
3. Run the game: `python main.py`

