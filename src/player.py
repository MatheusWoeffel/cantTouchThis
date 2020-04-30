import pygame
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

class Player(pygame.sprite.Sprite):
    def __init__(self, SCREEN_HEIGHT, SCREEN_WIDTH):
        super(Player,self).__init__()
        self.SCREEN_HEIGHT= SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.plane_picture = pygame.image.load("../assets/plane/biplane.png")
        plane_picture_scale_x = 1200
        plane_picture_scale_y = 654
        self.plane_picture = pygame.transform.smoothscale(self.plane_picture,(plane_picture_scale_x//15, plane_picture_scale_y//15))
        
        self.surface = self.plane_picture.convert_alpha()
        self.rect = self.surface.get_rect()

        self.player_speed = 10

    def update_position(self, input_dict):
        if input_dict[K_UP]:
            self.rect.move_ip(0,-self.player_speed)
        if input_dict[K_DOWN]:
            self.rect.move_ip(0,self.player_speed)
        if input_dict[K_LEFT]:
            self.rect.move_ip(-self.player_speed,0)
        if input_dict[K_RIGHT]:
            self.rect.move_ip(self.player_speed,0)

        self.mantain_boundaries()

    def mantain_boundaries(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.SCREEN_WIDTH:
            self.rect.right = self.SCREEN_WIDTH
        if self.rect.bottom > self.SCREEN_HEIGHT:
            self.rect.bottom = self.SCREEN_HEIGHT 
        if self.rect.top < 0:
            self.rect.top = 0