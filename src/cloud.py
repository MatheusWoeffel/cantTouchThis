import pygame
import random

class Cloud(pygame.sprite.Sprite):
    def __init__(self, SCREEN_HEIGHT, SCREEN_WIDTH):
        super(Cloud, self).__init__()
        cloud_selector = random.randint(1,3)
        self.cloud_image = pygame.image.load("../assets/clouds/cloud" + str(cloud_selector) + ".PNG")
        self.surface = self.cloud_image.convert_alpha()
        self.rect = self.surface.get_rect(
            center = (random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                      random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = 5


    def update(self):
        self.rect.move_ip(-self.speed, 0)
        
        if self.rect.left < 0:
            self.kill()
