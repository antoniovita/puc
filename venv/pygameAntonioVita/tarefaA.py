import pygame

width = 800
height = 600

sun_x = 700
sun_y = 100
sun_radius = 50
sun_speed = 5

def load():
    global sys_font, clock
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 28)
    clock = pygame.time.Clock()

def get_background_color(y):
    if y < 200:
        return (135, 206, 250) 
    elif y < 400:
        return (100, 149, 237)  
    else:
        return (25, 25, 112)    

def draw_screen(screen):
    bg_color = get_background_color(sun_y)
    screen.fill(bg_color)

    pygame.draw.circle(screen, (255, 255, 100), (sun_x, sun_y), sun_radius + 10)
    pygame.draw.circle(screen, (255, 255, 0), (sun_x, sun_y), sun_radius)

    pygame.draw.rect(screen, (50, 205, 50), (0, 500, 800, 100))

    pygame.draw.rect(screen, (210, 180, 140), (300, 300, 200, 200))
    pygame.draw.polygon(screen, (139, 69, 19), [(280, 300), (520, 300), (400, 200)])

    pygame.draw.rect(screen, (173, 216, 230), (370, 370, 60, 60))
    pygame.draw.line(screen, (0, 0, 0), (370, 400), (430, 400), 2)
    pygame.draw.line(screen, (0, 0, 0), (400, 370), (400, 430), 2)

    pygame.draw.rect(screen, (101, 67, 33), (150, 370, 20, 130))  
    pygame.draw.circle(screen, (34, 139, 34), (160, 340), 50)    

    texto = sys_font.render("Antonio Vita", True, (255, 255, 255))
    screen.blit(texto, texto.get_rect(center=(width // 2, 560)))

    pygame.display.flip()

def update(dt):
    global sun_x, sun_y
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        sun_x = max(sun_radius, sun_x - sun_speed)
    if keys[pygame.K_RIGHT]:
        sun_x = min(width - sun_radius, sun_x + sun_speed)
    if keys[pygame.K_UP]:
        sun_y = max(sun_radius, sun_y - sun_speed)
    if keys[pygame.K_DOWN]:
        sun_y = min(height - 100 - sun_radius, sun_y + sun_speed)

def main_loop(screen):
    global clock
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        dt = clock.tick(60)
        update(dt)
        draw_screen(screen)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cenário Interativo - Antonio Vita")
load()
main_loop(screen)
pygame.quit()
