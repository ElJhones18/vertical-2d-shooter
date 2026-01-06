import pygame
import random
from models.settings import WIDTH, HEIGHT, ENEMY_SPEEDS, ENEMY_HEALTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, enemy_type, speed_mult=1.0):
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

        self.health = ENEMY_HEALTH[enemy_type]
        self.speed = int(ENEMY_SPEEDS[enemy_type] * speed_mult)

        # Hitbox
        self.hitbox = self.rect.inflate(
            -self.rect.width * 0.3,
            -self.rect.height * 0.45
        )

    def take_damage(self):
        self.health -= 1

        if self.health <= 0:
            self.kill()
            return True   # murió
        return False      # sigue vivo

    def update(self):
        self.rect.x -= self.speed
        self.hitbox.center = self.rect.center

        if self.rect.right < 0:
            self.kill()
