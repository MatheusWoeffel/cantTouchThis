import pygame
import random
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
WHITE=(255,255,255)
BLACK=(0,0,0)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.plane_picture = pygame.image.load("../assets/plane/biplane.png")
        plane_picture_scale_x = 1200
        plane_picture_scale_y = 654
        self.plane_picture = pygame.transform.scale(self.plane_picture,(plane_picture_scale_x//10, plane_picture_scale_y//10))
        
        self.surface = self.plane_picture.convert_alpha()
        self.rect = self.surface.get_rect()

    def update_position(self, input_dict):
        if input_dict[K_UP]:
            self.rect.move_ip(0,-5)
        if input_dict[K_DOWN]:
            self.rect.move_ip(0,5)
        if input_dict[K_LEFT]:
            self.rect.move_ip(-5,0)
        if input_dict[K_RIGHT]:
            self.rect.move_ip(5,0)

        self.mantain_boundaries()

    def mantain_boundaries(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT 
        if self.rect.top < 0:
            self.rect.top = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.surface = pygame.surface.Surface((20,20))
        self.surface.fill(BLACK)
        self.rect = self.surface.get_rect(
            center=( random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                     random.randint(0, SCREEN_HEIGHT)
                    )
        )

        self.speed = random.randint(5,20)
    
    def update(self):
        self.rect.move_ip((-self.speed, 0))
        
        if self.rect.left < 0:
            self.kill()


#New event
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 100)

#Clock set
clock = pygame.time.Clock()

#Program start
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)

player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
                running = False

        elif event.type == ADD_ENEMY:
            new_enemy = Enemy()
            all_sprites.add(new_enemy)
            enemies.add(new_enemy)
    
    pressed_keys = pygame.key.get_pressed()
    player.update_position(pressed_keys)
    enemies.update()

    screen.fill(WHITE)
    for entity in all_sprites:
        screen.blit(entity.surface, entity.rect)

    #Lastly, in case a player collide with any enemy
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    
    pygame.display.flip()
    clock.tick(30)
    

pygame.quit()
