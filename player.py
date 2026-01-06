import pygame
from settings import HEIGHT, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = 20
        self.rect.centery = HEIGHT // 2

        self.hitbox = self.rect.inflate(-self.rect.width * 0.25, 1600)

    def update(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += PLAYER_SPEED

        self.hitbox.center = self.rect.center
