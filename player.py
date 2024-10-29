# class Player:
#     def __init__(self, canvas):
#         self.canvas = canvas
#         self.width = 50
#         self.height = 30
#         self.x = 375
#         self.y = 550
#         self.speed = 10
#         self.player_ship = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="blue")
#
#     def move_left(self, event):
#         if self.x > 0:
#             self.x -= self.speed
#             self.canvas.move(self.player_ship, -self.speed, 0)
#
#     def move_right(self, event):
#         if self.x < 750:  # Assuming window width of 800
#             self.x += self.speed
#             self.canvas.move(self.player_ship, self.speed, 0)
#
#     def update(self):
#         pass  # Player update logic can be added here (e.g., shooting cooldown)


from PIL import Image, ImageTk

class Player:
    def __init__(self, canvas, player_image_path):
        self.canvas = canvas
        self.width = 50  # The width of the player image (optional, for bounding checks)
        self.height = 30  # The height of the player image (optional, for bounding checks)
        self.x = 375  # Starting x position
        self.y = 550  # Starting y position (near the bottom)
        self.speed = 10  # Speed of the player movement

        # Load and resize the player image using Pillow
        self.image = Image.open(player_image_path)
        self.image = self.image.resize((50, 50), Image.Resampling.LANCZOS)  # Resize to appropriate size (50x50 pixels)
        self.tk_image = ImageTk.PhotoImage(self.image)  # Convert to Tkinter-compatible image

        # Create the player ship using the image
        self.player_ship = self.canvas.create_image(self.x, self.y, image=self.tk_image, anchor='nw')

    def move_left(self, event):
        if self.x > 0:  # Prevent moving out of bounds (left)
            self.x -= self.speed
            self.canvas.move(self.player_ship, -self.speed, 0)

    def move_right(self, event):
        if self.x < 750:  # Prevent moving out of bounds (right) assuming window width is 800
            self.x += self.speed
            self.canvas.move(self.player_ship, self.speed, 0)

    def update(self):
        # Player-specific updates can go here (e.g., shooting mechanics, cooldowns, etc.)
        pass
