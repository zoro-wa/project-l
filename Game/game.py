import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Marimo')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load("Graphics/sky.png").convert()
ground_surface = pygame.image.load("Graphics/ground.png").convert()
score_surface = test_font.render('Marimo', False, (64,64,64))
score_rect = score_surface.get_rect(center =(400, 50))

snail_surface = pygame.image.load('Graphics/Snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom =(600,300))


player_surface = pygame.image.load("Graphics/Player/player_walk_1.png")
player_rect = player_surface.get_rect(bottomright = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,'#c0ebec', score_rect)
    pygame.draw.rect(screen,'#c0ebec', score_rect,10) 
    screen.blit(score_surface,score_rect)
    
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surface,player_rect)



    pygame.display.update()
    clock.tick(60)


 