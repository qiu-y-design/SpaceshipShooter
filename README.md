# Space Invaders-Inspired Game

This is a simple Space Invaders-inspired game built using Python's `tkinter` library for the GUI and `Pillow` for image processing. The player controls a spaceship to shoot down invading aliens. Aliens spawn from the top and randomly move toward the player. The game ends when an alien collides with the player's spaceship.

## Features

- Player-controlled spaceship with left and right movement.
- Shooting bullets to destroy aliens.
- Aliens spawn randomly from the top and move toward the player.
- Score tracking.
- Game-over state with a "Game Lost" message.

## Getting Started

### Prerequisites

Make sure you have Python 3.6+ installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/qiu-y-design/SpaceshipShooter.git
   cd SpaceshipShooter


2. **Create a virtual environment (optional)**

It is recommended to create a virtual environment to manage dependencies.

``` bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. **Install dependencies**

Run the following command to install the required Python libraries:

```bash

pip install -r requirements.txt
```
The dependencies include

Pillow: Used for image handling.
tkinter: Standard Python library for GUI (already included with Python).
Run the game:

Once the dependencies are installed, you can run the game by executing

```bash
python main.py
```
# **Game Instructions**

Move Left: Use the left arrow key (←) to move the spaceship left.

Move Right: Use the right arrow key (→) to move the spaceship right.

Shoot: Press the space bar to shoot bullets upward.

## Project Structure
```bash
space-invaders-game/
│
├── main.py               # Main game logic
|── game.py               # Main game logic
├── player.py             # Player logic (movement, shooting)
├── alien.py              # Alien logic (movement, spawn)
├── bullet.py             # Bullet behavior
├── collision.py          # Collision detection between objects
├── scoreboard.py         # Scoreboard management
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── resources/            # Folder to store images, sounds, etc.
│   ├── alien.png         # Image of the alien
│   ├── gun.png   # Image of the player's spaceship
├── .gitignore            # Git ignore file (e.g., to ignore Python virtual environments)
```
### 6. **Adding Project Dependencies (`requirements.txt`)**

To manage Python dependencies, create a `requirements.txt`. Run the following command to generate the `requirements.txt`:

```bash
pip freeze > requirements.txt
