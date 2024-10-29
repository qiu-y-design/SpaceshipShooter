
import tkinter as tk
from alien import Alien
from bullet import Bullet
from player import Player
from scoreboard import Scoreboard
from collision import Collision

#
# class Game:
#     def __init__(self):
#         # Set up the main window
#         self.window = tk.Tk()
#         self.window.title("Space Invaders: Alien Attack")
#
#         # Set up the canvas
#         self.canvas = tk.Canvas(self.window, width=800, height=600, bg="black")
#         self.canvas.pack()
#
#         # Load the alien image (use the actual path to your image file)
#         self.alien_image = "resources/alien.png"
#
#         # Initialize game objects
#         self.player = Player(self.canvas, './resources/gun.png')
#         self.aliens = self.create_aliens()
#         self.bullets = []
#         self.scoreboard = Scoreboard(self.canvas)
#
#         # Set the game state to active
#         self.game_active = True
#
#         # Bind keys for player movement and shooting
#         self.window.bind("<Left>", self.move_left)
#         self.window.bind("<Right>", self.move_right)
#         self.window.bind("<space>", self.shoot_bullet)
#
#         # Initialize collision detection and pass the scoreboard and game instance
#         self.collision = Collision(self.canvas, self.player, self.aliens, self.bullets, self.scoreboard, self)
#
#         self.game_over_text = None  # Variable to store the game over text
#
#     def create_aliens(self):
#         # Create a grid of aliens with images
#         aliens = []
#         for i in range(5):
#             for j in range(10):
#                 alien = Alien(self.canvas, x=50 + j*60, y=50 + i*40, alien_image=self.alien_image)
#                 aliens.append(alien)
#         return aliens
#
#     def move_left(self, event):
#         if self.game_active:  # Only allow movement if the game is active
#             self.player.move_left(event)
#
#     def move_right(self, event):
#         if self.game_active:  # Only allow movement if the game is active
#             self.player.move_right(event)
#
#     def shoot_bullet(self, event):
#         if self.game_active:  # Only allow shooting if the game is active
#             bullet = Bullet(self.canvas, self.player.x, self.player.y, direction="up")
#             self.bullets.append(bullet)
#
#     def run(self):
#         # Start the game loop by using Tkinter's after() method
#         self.update()
#         self.window.mainloop()  # Keep the window open and responsive until the user closes it
#
#     def update(self):
#         if not self.game_active:
#             return  # Stop updating game objects if the game is over
#
#         # Update game objects (move player, aliens, and bullets)
#         self.player.update()
#         for alien in self.aliens:
#             alien.update()
#         for bullet in self.bullets:
#             bullet.update()
#
#         # Check for collisions
#         self.collision.check_collisions()
#
#         # Continue updating after a short delay (50 ms)
#         self.window.after(3, self.update)  # Re-run update after 50 milliseconds
#
#     def game_over(self, message):
#         # Stop the game and display the "Game Lost" message
#         if self.game_over_text is None:
#             self.game_active = False  # Set the game as inactive
#             self.game_over_text = self.canvas.create_text(400, 300, text=message, fill="red", font=("Arial", 30))
#             self.window.update()


import random
import time

class Game:
    def __init__(self):
        # Set up the main window
        self.window = tk.Tk()
        self.window.title("Space Invaders: Alien Attack")

        # Set up the canvas
        self.canvas = tk.Canvas(self.window, width=800, height=600, bg="black")
        self.canvas.pack()

        # Load the alien image
        self.alien_image = "resources/alien.png"

        # Initialize game objects
        self.player = Player(self.canvas, './resources/gun.png')
        self.aliens = []
        self.bullets = []
        self.scoreboard = Scoreboard(self.canvas)

        # Set the game state to active
        self.game_active = True

        # Bind keys for player movement and shooting
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<space>", self.shoot_bullet)

        # Initialize collision detection and pass the scoreboard and game instance
        self.collision = Collision(self.canvas, self.player, self.aliens, self.bullets, self.scoreboard, self)

        self.game_over_text = None  # Variable to store the game over text

        # Start spawning aliens gradually
        self.spawn_aliens()

    def spawn_aliens(self):
        if self.game_active:
            # Randomly choose an x position along the top of the screen
            x_position = random.randint(0, 760)  # Ensure aliens spawn within the screen width
            alien = Alien(self.canvas, x_position, 0, self.alien_image)  # Start from y=0
            self.aliens.append(alien)

            # Continue spawning aliens every 2 seconds (adjust timing as needed)
            self.window.after(2000, self.spawn_aliens)

    def move_left(self, event):
        if self.game_active:
            self.player.move_left(event)

    def move_right(self, event):
        if self.game_active:
            self.player.move_right(event)

    def shoot_bullet(self, event):
        if self.game_active:
            bullet = Bullet(self.canvas, self.player.x, self.player.y, direction="up")
            self.bullets.append(bullet)

    def run(self):
        # Main game loop using Tkinter's after() method
        self.update()
        self.window.mainloop()

    def update(self):
        if not self.game_active:
            return  # Stop updating if the game is over

        # Update game objects (move player, aliens, and bullets)
        self.player.update()
        for alien in self.aliens:
            alien.update()
        for bullet in self.bullets:
            bullet.update()

        # Check for collisions
        self.collision.check_collisions()

        # Continue updating after a short delay
        self.window.after(2, self.update)

    def game_over(self, message):
        if self.game_over_text is None:
            self.game_active = False  # Set the game as inactive
            self.game_over_text = self.canvas.create_text(400, 300, text=message, fill="red", font=("Arial", 30))
            self.window.update()
