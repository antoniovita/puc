import pygame
import os

width = 800
height = 350

player_x = 40
player_y = 200
player_speed = 4

walk_frames = []
shot_frames = []

current_frame = 0
frame_timer = 0
frame_delay = 100

is_moving = False
facing_right = True
is_shooting = False

walk_frame_width = 80
walk_frame_height = 128
walk_frame_count = 8

shot_frame_width = 85
shot_frame_height = 128
shot_frame_count = 4

def load():
    global sys_font, clock, city2, walk_frames, shot_frames
    sys_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    clock = pygame.time.Clock()

    city2 = pygame.image.load(os.path.join("City2", "Bright", "City2.png")).convert_alpha()
    city2 = pygame.transform.scale(city2, (800, 350))

    walk_sheet = pygame.image.load("./frames/Walk.png").convert_alpha()
    for i in range(walk_frame_count):
        rect = pygame.Rect(i * walk_frame_width, 0, walk_frame_width, walk_frame_height)
        frame = walk_sheet.subsurface(rect)
        walk_frames.append(frame)

    shot_sheet = pygame.image.load("./frames/Shot.png").convert_alpha()
    for i in range(shot_frame_count):
        rect = pygame.Rect(i * shot_frame_width, 0, shot_frame_width, shot_frame_height)
        frame = shot_sheet.subsurface(rect)
        shot_frames.append(frame)

def draw_screen(screen):   
    screen.blit(city2, (0, 0))

    if is_shooting:
        frame = shot_frames[current_frame]
    else:
        frame = walk_frames[current_frame]

    if not facing_right:
        frame = pygame.transform.flip(frame, True, False)

    screen.blit(frame, (player_x, player_y))
    pygame.display.flip()

def update(dt):
    global player_x, current_frame, frame_timer, is_moving, facing_right, is_shooting

    keys = pygame.key.get_pressed()
    is_moving = False
    is_shooting = False

    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not keys[pygame.K_p]:
        player_x = min(width - 80, player_x + player_speed)
        is_moving = True
        facing_right = True

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not keys[pygame.K_p]:
        player_x = max(0, player_x - player_speed)
        is_moving = True
        facing_right = False

    if keys[pygame.K_p]:
        is_shooting = True
        is_moving = False

    frame_timer += dt
    if frame_timer >= frame_delay:
        frame_timer = 0
        if is_shooting:
            current_frame = (current_frame + 1) % len(shot_frames)
        elif is_moving:
            current_frame = (current_frame + 1) % len(walk_frames)
        else:
            current_frame = 0

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
load()
main_loop(screen)
pygame.quit()
