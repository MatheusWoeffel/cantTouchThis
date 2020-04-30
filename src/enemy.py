import pygame
import random

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

class Enemy(pygame.sprite.Sprite):
    def __init__(self, SCREEN_HEIGHT, SCREEN_WIDTH):
        super(Enemy,self).__init__()
        self.SCREEN_HEIGHT= SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.missile_picture = pygame.image.load("../assets/missiles/missile_mixed.png")
        plane_picture_scale_x = 553
        plane_picture_scale_y = 406
        self.missile_picture = pygame.transform.smoothscale(self.missile_picture,(plane_picture_scale_x//12, plane_picture_scale_y//12))
        
        self.surface = self.missile_picture.convert_alpha()
        self.rect = self.surface.get_rect(
            center= ( random.randint(self.SCREEN_WIDTH + 20, self.SCREEN_WIDTH + 100),
                     random.randint(0, self.SCREEN_HEIGHT)
                    )
        )

        self.speed = random.randint(5,20)
    
    def update(self):
        self.rect.move_ip((-self.speed, 0))
        
        if self.rect.left < 0:
            self.kill()

