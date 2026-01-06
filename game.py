import pygame
import random
from player import Player
from bullet import Bullet
from enemy import Enemy
from settings import *
from pathlib import Path

class Game:
    def __init__(self, screen, difficulty):
        self.screen = screen
        self.difficulty = difficulty
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)

        # Sprites
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # Assets
        self.background = pygame.image.load("assets/background.jpg").convert()
        self.player_img = pygame.image.load("assets/player.png").convert_alpha()
        self.bullet_img = pygame.image.load("assets/shot.png").convert_alpha()

        self.enemy_images = {
            "basic": pygame.image.load("assets/enemy1.png").convert_alpha(),
            "fast": pygame.image.load("assets/enemy2.png").convert_alpha(),
            "tank": pygame.image.load("assets/enemy3.png").convert_alpha()
        }

        # Player
        self.player = Player(self.player_img)
        self.all_sprites.add(self.player)

        # Score
        self.score = 0
        self.start_ticks = pygame.time.get_ticks()

        # Highscore
        self.highscore = self.load_highscore()

        self.spawn_timer = 0

    def load_highscore(self):
        path = Path("highscore.txt")
        if path.exists():
            return int(path.read_text())
        return 0

    def save_highscore(self):
        if self.score > self.highscore:
            with open("highscore.txt", "w") as f:
                f.write(str(self.score))

    def choose_enemy_type(self):
        r = random.random()
        acc = 0
        for etype, prob in SPAWN_RATE[self.difficulty].items():
            acc += prob
            if r <= acc:
                return etype

    def spawn_enemy(self):
        etype = self.choose_enemy_type()
        enemy = Enemy(self.enemy_images[etype], etype)
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def run(self):
        running = True

        while running:
            self.clock.tick(FPS)
            self.spawn_timer += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(
                            self.bullet_img,
                            self.player.rect.right,
                            self.player.rect.centery
                        )
                        self.all_sprites.add(bullet)
                        self.bullets.add(bullet)

            keys = pygame.key.get_pressed()
            self.player.update(keys)

            if self.spawn_timer > 60:
                self.spawn_enemy()
                self.spawn_timer = 0

            self.enemies.update()
            self.bullets.update()


            # Colisiones bala-enemigo
            hits = pygame.sprite.groupcollide(
                self.enemies,
                self.bullets,
                True,
                True,
                collided=lambda e, b: e.hitbox.colliderect(b.hitbox)
            )

            for enemy in hits:
                self.score += SCORE_KILL[enemy.type]

            # Colisión jugador-enemigo
            if pygame.sprite.spritecollideany(
                self.player,
                self.enemies,
                collided=lambda p, e: p.hitbox.colliderect(e.hitbox)
            ):
                self.save_highscore()
                return self.score, self.highscore

            # Puntaje por tiempo
            seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000
            self.score = seconds * SCORE_TIME_MULT + self.score

            # Dibujo
            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)
            
            # DEBUG HITBOXES 
            # pygame.draw.rect(self.screen, (0, 255, 0), self.player.hitbox, 1)

            # for enemy in self.enemies:
            #     pygame.draw.rect(self.screen, (255, 0, 0), enemy.hitbox, 1)

            # for bullet in self.bullets:
            #     pygame.draw.rect(self.screen, (0, 0, 255), bullet.hitbox, 1)

            score_txt = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_txt, (10, 10))

            pygame.display.flip()
