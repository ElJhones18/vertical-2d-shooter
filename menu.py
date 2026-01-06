import pygame
from settings import WIDTH, HEIGHT

class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.options = ["easy", "normal", "hard"]
        self.selected = 0

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            title = self.font.render("SHOOTER", True, (255, 255, 255))
            self.screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))

            for i, opt in enumerate(self.options):
                color = (255, 0, 0) if i == self.selected else (255, 255, 255)
                txt = self.font.render(opt.upper(), True, color)
                self.screen.blit(txt, (WIDTH//2 - 50, 250 + i * 50))

            pygame.display.flip()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    if e.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    if e.key == pygame.K_RETURN:
                        return self.options[self.selected]
