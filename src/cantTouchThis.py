import pygame
import random
from enemy import Enemy
from player import Player
from cloud import Cloud

pygame.init()

#Keyboard Constants
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    RLEACCEL,
)

#Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
SKY_COLOR = (39, 145, 225)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500



#New add_enemy event
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 500)

#New add_cloud event
ADD_CLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_CLOUD, 1000)

#Clock set
clock = pygame.time.Clock()

#Program start
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Can't Touch This")
plane_image = pygame.image.load("../assets/plane/biplane.png")
plane_scale_x = 1200
plane_scale_y = 654
plane_image = pygame.transform.scale(plane_image, (32,32))
pygame.display.set_icon(plane_image)


player = Player(SCREEN_HEIGHT, SCREEN_WIDTH)
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
clouds = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
                running = False

        elif event.type == ADD_ENEMY:
            new_enemy = Enemy(SCREEN_HEIGHT, SCREEN_WIDTH)
            all_sprites.add(new_enemy)
            enemies.add(new_enemy)
        
        elif event.type == ADD_CLOUD:
            new_cloud = Cloud(SCREEN_HEIGHT, SCREEN_WIDTH)
            clouds.add(new_cloud)
    
    pressed_keys = pygame.key.get_pressed()
    player.update_position(pressed_keys)
    enemies.update()
    clouds.update()

    screen.fill(SKY_COLOR)

    #Clouds are drawn first, so others sprites overlap it
    for cloud in clouds:
        screen.blit(cloud.surface, cloud.rect)

    for entity in all_sprites:
        screen.blit(entity.surface, entity.rect)

    #Lastly, in case a player collide with any enemy
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    
    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()
