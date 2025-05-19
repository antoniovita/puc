import pygame
import random

WIDTH, HEIGHT = 640, 480
BG_COLOR = (255, 255, 255)  # branco

def criarNotas():
    notas = []
    for _ in range(50):
        num = random.uniform(0, 10)
        notas.append(round(num, 2))
    print("Notas:", notas)
    print(len(notas))
    return notas

def calcularHistogram(notas):
    categorias = [0, 0, 0, 0, 0] 
    for nota in notas:
        if 0 <= nota <= 1.99:
            categorias[0] += 1
        elif 2 <= nota <= 3.99:
            categorias[1] += 1
        elif 4 <= nota <= 5.99:
            categorias[2] += 1
        elif 6 <= nota <= 7.99:
            categorias[3] += 1
        elif 8 <= nota <= 10:
            categorias[4] += 1
    return categorias

def desenharHistograma(tela, histogram):
    margin = 50
    n_categorias = len(histogram)
    bar_width = (WIDTH - 2 * margin) // n_categorias
    max_count = max(histogram)
    max_bar_height = HEIGHT - 2 * margin
    bar_color = (100, 149, 237)  # azul

    font = pygame.font.SysFont("Arial", 16)
    labels = ["0–2", "2–4", "4–6", "6–8", "8–10"]

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
    pygame.display.set_caption("Histograma de Notas")
    clock = pygame.time.Clock()

    notas = criarNotas()
    histogram = calcularHistogram(notas)

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
