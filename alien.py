import random
from PIL import Image, ImageTk


class Alien:
    def __init__(self, canvas, x, y, alien_image):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.speed_x = random.choice([-3, -2, -1, 1, 2, 3])  # Random horizontal speed (left or right)
        self.speed_y = random.randint(1, 3)  # Random vertical speed (moving toward the player)

        # Load and resize the alien image
        self.image = Image.open(alien_image)
        self.image = self.image.resize((30, 30), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(self.image)

        # Create the alien ship on the canvas
        self.alien_ship = self.canvas.create_image(self.x, self.y, image=self.tk_image, anchor='nw')

    def update(self):
        # Move the alien randomly left or right, and always downwards
        self.canvas.move(self.alien_ship, self.speed_x, self.speed_y)
        self.x += self.speed_x
        self.y += self.speed_y

        # Reverse direction if hitting the canvas boundary (left/right)
        if self.x <= 0 or self.x >= 760:  # Assuming window width is 800
            self.speed_x = -self.speed_x

        # If the alien reaches the bottom of the screen, it keeps moving off-screen
        # The game will handle collisions with the player elsewhere
