import pygame
from models.settings import WIDTH, BULLET_SPEED

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))

        self.hitbox = self.rect.inflate(-90, -100)

    def update(self):
        self.rect.x += BULLET_SPEED
        self.hitbox.center = self.rect.center

        if self.rect.left > WIDTH:
            self.kill()
