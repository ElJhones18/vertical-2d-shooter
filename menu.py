import pygame
from settings import WIDTH, HEIGHT
from pathlib import Path

class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.big_font = pygame.font.SysFont(None, 64)

    def main_menu(self):
        options = ["JUGAR", "MEJOR PUNTAJE"]
        selected = 0

        while True:
            self.screen.fill((0, 0, 0))

            title = self.big_font.render("SHOOTER 2D", True, (255, 255, 255))
            self.screen.blit(title, (WIDTH//2 - title.get_width()//2, 120))

            for i, opt in enumerate(options):
                color = (255, 0, 0) if i == selected else (255, 255, 255)
                txt = self.font.render(opt, True, color)
                self.screen.blit(txt, (WIDTH//2 - 80, 300 + i * 60))
            back = self.font.render("Utiliza flechas/ENTER para navegar", True, (200, 200, 200))
            self.screen.blit(back, (WIDTH//2 - 170, 500))
            pygame.display.flip()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); exit()

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        selected = (selected - 1) % len(options)
                    if e.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)
                    if e.key == pygame.K_RETURN:
                        return options[selected]

    def difficulty_menu(self):
        options = ["easy", "normal", "hard"]
        selected = 0

        while True:
            self.screen.fill((0, 0, 0))

            title = self.font.render("DIFICULTAD", True, (255, 255, 255))
            self.screen.blit(title, (WIDTH//2 - 90, 150))

            for i, opt in enumerate(options):
                color = (255, 0, 0) if i == selected else (255, 255, 255)
                txt = self.font.render(opt.upper(), True, color)
                self.screen.blit(txt, (WIDTH//2 - 60, 250 + i * 60))
            back = self.font.render("Utiliza flechas/ENTER para navegar", True, (200, 200, 200))
            self.screen.blit(back, (WIDTH//2 - 170, 500))

            pygame.display.flip()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); exit()

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        selected = (selected - 1) % len(options)
                    if e.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)
                    if e.key == pygame.K_RETURN:
                        return options[selected]

    def highscore_screen(self):
        path = Path("highscore.txt")
        highscore = path.read_text() if path.exists() else "0"

        while True:
            self.screen.fill((0, 0, 0))

            title = self.font.render("MEJOR PUNTAJE", True, (255, 255, 255))
            score = self.big_font.render(highscore, True, (255, 215, 0))
            back = self.font.render("ENTER / ESC para volver", True, (200, 200, 200))

            self.screen.blit(title, (WIDTH//2 - 120, 150))
            self.screen.blit(score, (WIDTH//2 - score.get_width()//2, 230))
            self.screen.blit(back, (WIDTH//2 - 170, 330))

            pygame.display.flip()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); exit()

                if e.type == pygame.KEYDOWN:
                    if e.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                        return
