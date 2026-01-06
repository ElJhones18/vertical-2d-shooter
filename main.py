import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de ventana
ANCHO = 800
ALTO = 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego PyGame")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

# Reloj
clock = pygame.time.Clock()

# Jugador
jugador = pygame.Rect(380, 500, 40, 40)
velocidad_jugador = 5

# Enemigos
enemigos = []
velocidad_enemigo = 3

# Fuente
fuente = pygame.font.SysFont(None, 50)

# ---------------- FUNCIONES ---------------- #

def mostrar_texto(texto, x, y):
    render = fuente.render(texto, True, BLANCO)
    VENTANA.blit(render, (x, y))


def crear_enemigo():
    x = random.randint(0, ANCHO - 40)
    enemigo = pygame.Rect(x, -40, 40, 40)
    enemigos.append(enemigo)


def mover_jugador(teclas):
    if teclas[pygame.K_LEFT] and jugador.x > 0:
        jugador.x -= velocidad_jugador
    if teclas[pygame.K_RIGHT] and jugador.x < ANCHO - jugador.width:
        jugador.x += velocidad_jugador


def mover_enemigos():
    for enemigo in enemigos:
        enemigo.y += velocidad_enemigo


def detectar_colisiones():
    for enemigo in enemigos:
        if jugador.colliderect(enemigo):
            return True
    return False


def menu():
    while True:
        VENTANA.fill(NEGRO)
        mostrar_texto("MI JUEGO", 300, 200)
        mostrar_texto("Presiona ENTER para jugar", 200, 300)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return


def game_over():
    while True:
        VENTANA.fill(NEGRO)
        mostrar_texto("GAME OVER", 280, 250)
        mostrar_texto("ESC para salir", 300, 320)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


def juego():
    enemigos.clear()
    tiempo_spawn = 0

    while True:
        clock.tick(60)
        VENTANA.fill(NEGRO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclas = pygame.key.get_pressed()
        mover_jugador(teclas)

        tiempo_spawn += 1
        if tiempo_spawn > 60:
            crear_enemigo()
            tiempo_spawn = 0

        mover_enemigos()

        if detectar_colisiones():
            game_over()

        pygame.draw.rect(VENTANA, BLANCO, jugador)
        for enemigo in enemigos:
            pygame.draw.rect(VENTANA, ROJO, enemigo)

        pygame.display.flip()


# ---------------- PROGRAMA PRINCIPAL ---------------- #
menu()
juego()
