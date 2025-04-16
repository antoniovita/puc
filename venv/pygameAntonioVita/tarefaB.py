import pygame

width = 800
height = 600

def load():
    global sys_font, clock, img_grama, arvore, house, cloud
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    clock = pygame.time.Clock()

    img_grama = pygame.image.load("grama.png").convert_alpha()
    img_grama = pygame.transform.scale(img_grama, (800, 150))

    arvore = pygame.image.load("arvore.png").convert_alpha()
    arvore = pygame.transform.scale(arvore, (250, 400))

    house = pygame.image.load("House.png").convert_alpha()
    house = pygame.transform.scale(house, (500, 300))

    cloud = pygame.image.load("cloud.png").convert_alpha()
    cloud  = pygame.transform.scale(cloud, (400, 100))

def draw_screen(screen):   
    screen.fill((pygame.Color("#8AFFE0")))
      
    
    pygame.draw.rect(screen, pygame.Color('#20b301'), (0, 500, 800, 100))
    screen.blit(arvore, (500, 170))
    screen.blit(house, (60, 230))
    screen.blit(img_grama, (0, 450))
    screen.blit(cloud, (60, 100))
   

    pygame.display.flip()

def update(dt):
    pass # faz nada...


def main_loop(screen):  
    global clock
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT: # fechamento do prog
                running = False
                break

        # Define FPS máximo
        clock.tick(60)
        # Tempo transcorrido desde a última atualização 
        dt = clock.get_time()
        # Atualiza posição dos objetos
        update(dt)
        # Desenha objetos
        draw_screen(screen)
        # Pygame atualiza a visualização da tela
        pygame.display.update()

# Programa principal
pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()