import pygame
import os

width = 800
height = 350

# player
player_x = 40
player_y = 250
player_speed = 4
walk_frames = []
current_frame = 0
frame_timer = 0
frame_delay = 100
is_moving = False
facing_right = True

def load():
    global sys_font, clock, city2, walk_frames
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    clock = pygame.time.Clock()

    city2 = pygame.image.load(os.path.join("City2", "Bright", "City2.png")).convert_alpha()
    city2 = pygame.transform.scale(city2, (800, 350))

    for i in range(1, 8):
        frame = pygame.image.load(f"./frames/Walk{i}.png").convert_alpha()
        frame = pygame.transform.scale(frame, (50, 70))
        walk_frames.append(frame)

def draw_screen(screen):   
    screen.blit(city2, (0, 0))

    if facing_right:
        screen.blit(walk_frames[current_frame], (player_x, player_y))
    else:
        flipped = pygame.transform.flip(walk_frames[current_frame], True, False)
        screen.blit(flipped, (player_x, player_y))

    pygame.display.flip()

def update(dt):
    global player_x, current_frame, frame_timer, is_moving, facing_right

    keys = pygame.key.get_pressed()
    is_moving = False

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x = min(width - 80, player_x + player_speed)
        is_moving = True
        facing_right = True

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x = max(0, player_x - player_speed)
        is_moving = True
        facing_right = False

    # Atualiza o frame da animação se estiver se movendo
    if is_moving:
        frame_timer += dt
        if frame_timer >= frame_delay:
            frame_timer = 0
            current_frame = (current_frame + 1) % len(walk_frames)
    else:
        current_frame = 0  # parado volta pro frame 1

def main_loop(screen):  
    global clock
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT: 
                running = False
                break

        dt = clock.tick(60)
        update(dt)
        draw_screen(screen)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animação do Personagem")
load()
main_loop(screen)
pygame.quit()
