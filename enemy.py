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

        # Hitbox más pequeña, no el asset completo
        self.hitbox = self.rect.inflate(
            -self.rect.width * 0.3,
            -self.rect.height * 0.45
        )

    def update(self):
        self.rect.x -= self.speed

        # Mantener hitbox centrada
        self.hitbox.center = self.rect.center

        if self.rect.right < 0:
            self.kill()
