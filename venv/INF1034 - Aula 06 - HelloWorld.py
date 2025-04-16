import pygame

width = 800  # Largura Janela
height = 600 # Altura Janela

def load():
    global sys_font, clock
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    clock = pygame.time.Clock() 


def draw_screen(screen):   
    # Preenche o fundo da tela com branco ⇒ (255,255,255)
    screen.fill((255,255,255))

    # Cria Imagem da String com cor preto ⇒ (0,0,0)
    t = sys_font.render("Hello World", False, (0,0,0))

    # Renderiza Texto (Desenha texto)
    screen.blit(t, t.get_rect(top = 290, left=343))

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