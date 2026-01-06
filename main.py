import pygame
from menu import Menu
from game import Game
from settings import WIDTH, HEIGHT

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter PyGame")

font = pygame.font.SysFont(None, 48)

def game_over(score, highscore):
    while True:
        screen.fill((0, 0, 0))
        t1 = font.render("GAME OVER", True, (255, 0, 0))
        t2 = font.render(f"Score: {score}", True, (255, 255, 255))
        t3 = font.render(f"Highscore: {highscore}", True, (255, 255, 255))
        t4 = font.render("ENTER - Menu", True, (200, 200, 200))

        screen.blit(t1, (WIDTH//2 - 100, 200))
        screen.blit(t2, (WIDTH//2 - 100, 260))
        screen.blit(t3, (WIDTH//2 - 100, 310))
        screen.blit(t4, (WIDTH//2 - 150, 380))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                return

while True:
    menu = Menu(screen, font)
    difficulty = menu.run()

    game = Game(screen, difficulty)
    score, highscore = game.run()

    game_over(score, highscore)
