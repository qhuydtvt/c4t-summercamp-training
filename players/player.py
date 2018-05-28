import pygame
# Game
# Properties + Function mixed up => classified
# Combine class
# 3 classes: Cat(p + m), Rock(m + p), Raindrop(m + p), function, variables
class Player:
    # 1. Describe properties (Properies: image, x, y)
    def __init__(self, x, y):
        self.image = pygame.image.load('images/player/player1.png')
        self.x = x
        self.y = y

    def update(self):
        pass

    def render(self, canvas):
        canvas.blit(self.image, (self.x, self.y))
