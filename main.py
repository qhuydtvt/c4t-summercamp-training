import pygame
from players.player import Player
from enemies.enemy import Enemy

BG_COLOR = (255, 0, 0)

# 1. Init pygame
pygame.init()

# 2. Game window & canvas
SIZE = (600, 800)
canvas = pygame.display.set_mode(SIZE)

# 3. Clock
clock = pygame.time.Clock()

player = Player(10, 300)
enemy = Enemy(200, 80)

# 3. Game loop
loop = True
right_pressed = False
left_pressed = False
while loop:
    # Game Loop 1: Events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right_pressed = True
            elif event.key == pygame.K_LEFT:
                left_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            elif event.key == pygame.K_LEFT:
                left_pressed = False

    player.update()
    enemy.update()

    # Game Loop 2: Draw
    canvas.fill(BG_COLOR)
    pygame.display.set_caption("Micro war")

    player.render(canvas)
    enemy.render(canvas)

    # Game Loop 3: Delay and flip
    pygame.display.flip()
    clock.tick(60)
