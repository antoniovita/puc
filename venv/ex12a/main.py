import pygame
import random
import os

TILE_SIZE = 50
MAP_WIDTH = 14
MAP_HEIGHT = 10
SCREEN_WIDTH = TILE_SIZE * MAP_WIDTH
SCREEN_HEIGHT = TILE_SIZE * MAP_HEIGHT

mapa = []
tile = {}
walk_image = pygame.image.load('walk.png')
walk_width = 
walk_height = 

def gerar_mapa_txt():
    if not os.path.exists("mapa.txt"):
        with open("mapa.txt", "w") as f:
            for _ in range(MAP_HEIGHT):
                linha = ""
                for _ in range(MAP_WIDTH):
                    linha += random.choice(["P", "G", "A"])
                f.write(linha + "\n")

def load_mapa(filename):
    global mapa
    mapa = []
    with open(filename, "r") as file:
        for line in file.readlines():
            mapa.append(line.strip())

def load():
    global clock, tile
    clock = pygame.time.Clock()
    load_mapa("mapa.txt")
    tile['P'] = pygame.image.load("sand.png").convert()
    tile['G'] = pygame.image.load("grass.png").convert()
    tile['A'] = pygame.image.load("water.png").convert()

def update(dt):
    pass

def draw_screen(screen):
    screen.fill((0, 0, 0))
    for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
            tipo = mapa[i][j]
            screen.blit(tile[tipo], (j * TILE_SIZE, i * TILE_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    gerar_mapa_txt()
    load()

    running = True
    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update(dt)
        draw_screen(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
