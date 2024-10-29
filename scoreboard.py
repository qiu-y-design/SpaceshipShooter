class Scoreboard:
    def __init__(self, canvas):
        self.canvas = canvas
        self.score = 0
        # Create a text label to display the score
        self.text = self.canvas.create_text(50, 30, text=f"Score: {self.score}", fill="white", font=("Arial", 16))

    def update_score(self, points):
        # Increment the score by the specified points (e.g., 10 points for each alien destroyed)
        self.score += points
        # Update the text on the canvas to reflect the new score
        self.canvas.itemconfig(self.text, text=f"Score: {self.score}")
