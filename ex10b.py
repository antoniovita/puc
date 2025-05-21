import pygame
import random

WIDTH, HEIGHT = 640, 480
BG_COLOR = (255, 255, 255)

palavras = ["sol", "lua", "estrela", "mar", "floresta", "montanha", "rio", "chuva", "vento", "neve"]

def criaLista(pal):
    lista = []
    for i in range(40):
        lista.append(pal[random.randrange(0, 10)])
    return lista

def quantidadeDePalavras(lista):
    quantidade = [0] * 10
    for elem in lista:
        for i in range(10):
            if elem == palavras[i]:
                quantidade[i] += 1
    return quantidade

def desenharHistograma(tela, histogram):
    margin = 50
    n_palavras = len(palavras)
    bar_width = (WIDTH - 2 * margin) // n_palavras
    max_count = max(histogram)
    max_bar_height = HEIGHT - 2 * margin
    bar_color = (100, 149, 237)

    font = pygame.font.SysFont("Arial", 12)
    labels = palavras

    for i, count in enumerate(histogram):
        bar_height = int((count / max_count) * max_bar_height) if max_count != 0 else 0
        x = margin + i * bar_width
        y = HEIGHT - margin - bar_height

        pygame.draw.rect(tela, bar_color, (x, y, bar_width - 10, bar_height))

        label = font.render(labels[i], True, (0, 0, 0))
        label_rect = label.get_rect(center=(x + (bar_width - 10) / 2, HEIGHT - margin / 2))
        tela.blit(label, label_rect)

        count_label = font.render(str(count), True, (0, 0, 0))
        count_rect = count_label.get_rect(center=(x + (bar_width - 10) / 2, y - 10))
        tela.blit(count_label, count_rect)

def main():
    pygame.init()
    tela = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Histograma de palavras")
    clock = pygame.time.Clock()

    palavras_geradas = criaLista(palavras)
    histogram = quantidadeDePalavras(palavras_geradas)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        tela.fill(BG_COLOR)
        desenharHistograma(tela, histogram)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
