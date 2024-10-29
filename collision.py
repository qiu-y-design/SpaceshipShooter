#
#
# class Collision:
#     def __init__(self, canvas, player, aliens, bullets, scoreboard, game):
#         self.canvas = canvas
#         self.player = player
#         self.aliens = aliens
#         self.bullets = bullets
#         self.scoreboard = scoreboard
#         self.game = game  # Pass the game instance so we can stop the game
#
#     def check_collisions(self):
#         # Check for bullet-alien collisions
#         for bullet in self.bullets:
#             for alien in self.aliens:
#                 if self.canvas.bbox(bullet.bullet) and self.canvas.bbox(alien.alien_ship):
#                     if self.intersects(bullet, alien):
#                         # Remove both bullet and alien
#                         self.canvas.delete(bullet.bullet)
#                         self.canvas.delete(alien.alien_ship)
#                         self.bullets.remove(bullet)
#                         self.aliens.remove(alien)
#                         # Update the score when an alien is destroyed
#                         self.scoreboard.update_score(10)
#                         break
#
#         # Check for player-alien collisions (game over condition)
#         for alien in self.aliens:
#             if self.canvas.bbox(alien.alien_ship) and self.canvas.bbox(self.player.player_ship):
#                 if self.intersects(self.player, alien):
#                     self.end_game()  # End the game when a collision occurs
#
#     def intersects(self, obj1, obj2):
#         # Get the bounding box for both objects
#         bbox1 = self.canvas.bbox(obj1.player_ship) if hasattr(obj1, 'player_ship') else self.canvas.bbox(obj1.bullet)
#         bbox2 = self.canvas.bbox(obj2.alien_ship)
#
#         # Check if the bounding boxes overlap
#         return not (bbox1[2] < bbox2[0] or bbox1[0] > bbox2[2] or
#                     bbox1[3] < bbox2[1] or bbox1[1] > bbox2[3])
#
#     def end_game(self):
#         # Stop the game and display a "Game Lost" message
#         self.game.game_over("Game Lost!")


class Collision:
    def __init__(self, canvas, player, aliens, bullets, scoreboard, game):
        self.canvas = canvas
        self.player = player
        self.aliens = aliens
        self.bullets = bullets
        self.scoreboard = scoreboard
        self.game = game  # Pass the game instance so we can stop the game

    def check_collisions(self):
        # Check for bullet-alien collisions
        for bullet in self.bullets:
            for alien in self.aliens:
                if self.canvas.bbox(bullet.bullet) and self.canvas.bbox(alien.alien_ship):
                    if self.intersects(bullet, alien):
                        # Remove both bullet and alien
                        self.canvas.delete(bullet.bullet)
                        self.canvas.delete(alien.alien_ship)
                        self.bullets.remove(bullet)
                        self.aliens.remove(alien)
                        # Update the score when an alien is destroyed
                        self.scoreboard.update_score(10)
                        break

        # Check for player-alien collisions (game over condition)
        for alien in self.aliens:
            if self.canvas.bbox(alien.alien_ship) and self.canvas.bbox(self.player.player_ship):
                if self.intersects(self.player, alien):
                    self.end_game()  # End the game when a collision occurs

    def intersects(self, obj1, obj2):
        # Get the bounding box for both objects
        bbox1 = self.canvas.bbox(obj1.player_ship) if hasattr(obj1, 'player_ship') else self.canvas.bbox(obj1.bullet)
        bbox2 = self.canvas.bbox(obj2.alien_ship)

        # Check if the bounding boxes overlap
        return not (bbox1[2] < bbox2[0] or bbox1[0] > bbox2[2] or
                    bbox1[3] < bbox2[1] or bbox1[1] > bbox2[3])

    def end_game(self):
        # Stop the game and display a "Game Lost" message
        self.game.game_over("Game Lost!")
