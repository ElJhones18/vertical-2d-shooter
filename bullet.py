import pygame
from settings import WIDTH, BULLET_SPEED

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.x += BULLET_SPEED
        if self.rect.left > WIDTH:
            self.kill()
