import pygame
import sys
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("yokeru")

clock = pygame.time.Clock()

player_width = 50
player_height = 50

player_x = (SCREEN_WIDTH - player_width) // 2
player_y = SCREEN_HEIGHT - player_height - 20
player_speed = 10

obstacles1 = random.randint(1,800)
obstacles2 = random.randint(1,800)

obstacles1_width = 100
obstacles1_height = 100

obstacles2_width = 150
obstacles2_height = 150

obstacles1_x = obstacles1
obstacles1_y = 0
obstacles1_speed = 15

obstacles2_x = obstacles2
obstacles2_y = 0
obstacles2_speed = 12

while True:

    clock.tick(60)

    screen.fill((0,0,0))

    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_width, player_height))

    pygame.draw.rect(screen, (255, 255, 0), (obstacles1_x, obstacles1_y, obstacles1_width, obstacles1_height))
    pygame.draw.rect(screen, (255, 255, 0), (obstacles2_x, obstacles2_y, obstacles2_width, obstacles2_height))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    obstacles1_y += obstacles1_speed
    obstacles2_y += obstacles2_speed

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  
        player_x -= player_speed
    if keys[pygame.K_RIGHT]: 
        player_x += player_speed
    
    if player_x < 0:
        player_x = 0
    if player_x > SCREEN_WIDTH - player_width:
        player_x = SCREEN_WIDTH - player_width

    if obstacles1_y > 1000:
        obstacles1_y = -50
        obstacles1_x = random.randint(1,800)
    if obstacles2_y > 1000:
        obstacles2_y = -50
        obstacles2_x = random.randint(1,800)

    pygame.display.update()
