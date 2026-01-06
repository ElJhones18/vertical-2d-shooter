import pygame
import random
from settings import WIDTH, HEIGHT, ENEMY_SPEEDS

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, enemy_type):
        super().__init__()

        # Escalar tank
        if enemy_type == "tank":
            w, h = image.get_size()
            image = pygame.transform.scale(image, (int(w * 1.4), int(h * 1.4)))

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)

        self.type = enemy_type
        self.speed = ENEMY_SPEEDS[enemy_type]

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
