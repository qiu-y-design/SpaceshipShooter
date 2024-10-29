class Bullet:
    def __init__(self, canvas, x, y, direction):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = 5
        self.height = 15
        self.direction = direction
        self.speed = 10
        self.bullet = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y - self.height, fill="yellow")

    def update(self):
        # Move the bullet in the specified direction
        if self.direction == "up":
            self.canvas.move(self.bullet, 0, -self.speed)
            self.y -= self.speed
        # Bullet off the screen can be removed or handled
