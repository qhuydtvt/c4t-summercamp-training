import pygame
from bullets.bullet import Bullet

class Player:
    # 1. Describe properties (Properies: image, x, y)
    def __init__(self, x, y, input_manager):
        self.image = pygame.image.load('images/player/player1.png')
        self.x = x
        self.y = y
        self.input_manager = input_manager #reference

    def update(self):
        if self.input_manager.right_pressed:
            self.x += 10

        if self.input_manager.x_pressed:
            # 1. Create bullet
            new_bullet = Bullet(self.x, self.y)

            # 2. Add newly created bullet into pool (game_objects)
            game_objects.append(new_bullet)


    def render(self, canvas):
        canvas.blit(self.image, (self.x, self.y))
