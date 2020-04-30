import pygame
import random

class Cloud(pygame.sprite.Sprite):
    def __init__(self, SCREEN_HEIGHT, SCREEN_WIDTH):
        super(Cloud, self).__init__()
        cloud_selector = random.randint(1,3)
        CLOUD_WIDTH_SCALE = 900
        CLOUD_HEIGHT_SCALE = 600
        cloud_image = pygame.image.load("../assets/clouds/cloud" + str(cloud_selector) + ".PNG")
        cloud_image = pygame.transform.smoothscale(cloud_image, (CLOUD_WIDTH_SCALE//4, CLOUD_HEIGHT_SCALE//4))
        self.surface = cloud_image.convert_alpha()
        self.rect = self.surface.get_rect(
            center = (random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                      random.randint(0, SCREEN_HEIGHT//2),
            )
        )
        self.speed = 5


    def update(self):
        self.rect.move_ip(-self.speed, 0)
        
        if self.rect.right < 0:
            self.kill()
