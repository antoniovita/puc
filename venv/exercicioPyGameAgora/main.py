import pygame

width = 800 
height = 600

hero_walk_right = []
hero_walk_left = []
hero_walk_up = []
hero_walk_down = []

hero_anim_frame = 0
hero_pos_x = 100
hero_pos_y = 225
hero_anim_time = 0 

hero_direction = 'right'

def load():
    global clock
    clock = pygame.time.Clock()

    hero_walk_up.append(pygame.image.load("./imagens_hero/Hero_Walk_09.png"))

    for i in range(1, 5):
        hero_walk_right.append(pygame.image.load(f"./imagens_hero/Hero_Walk_0{i}.png"))

    for i in range(6, 9):
        hero_walk_left.append(pygame.image.load(f"./imagens_hero/Hero_Walk_0{i}.png"))
    hero_walk_left.append(hero_walk_left[-1])  # Duplicar último frame para ter 4

    for i in range(10, 13):
        hero_walk_up.append(pygame.image.load(f"./imagens_hero/Hero_Walk_{i}.png"))

    for i in range(13, 17):
        hero_walk_down.append(pygame.image.load(f"./imagens_hero/Hero_Walk_{i}.png"))

def update(dt):
    global hero_anim_frame, hero_pos_x, hero_pos_y, hero_anim_time, hero_direction

    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_RIGHT]:
        hero_pos_x += 0.1 * dt
        hero_direction = 'right'
        moved = True
    elif keys[pygame.K_LEFT]:
        hero_pos_x -= 0.1 * dt
        hero_direction = 'left'
        moved = True
    elif keys[pygame.K_DOWN]:
        hero_pos_y += 0.1 * dt
        hero_direction = 'down'
        moved = True
    elif keys[pygame.K_UP]:
        hero_pos_y -= 0.1 * dt
        hero_direction = 'up'
        moved = True

    if moved:
        hero_anim_time += dt
        if hero_anim_time > 100:
            hero_anim_frame = (hero_anim_frame + 1) % 4
            hero_anim_time = 0
    else:
        hero_anim_frame = 0 

def draw_screen(screen):   
    screen.fill((255, 255, 255))

    if hero_direction == 'right':
        sprite = hero_walk_right[hero_anim_frame]
    elif hero_direction == 'left':
        sprite = hero_walk_left[hero_anim_frame]
    elif hero_direction == 'up':
        sprite = hero_walk_up[hero_anim_frame]
    else: 
        sprite = hero_walk_down[hero_anim_frame]

    screen.blit(sprite, (hero_pos_x, hero_pos_y))

def main_loop(screen):  
    global clock
    running = True
    while running:
        for e in pygame.event.get(): 
            if e.type == pygame.QUIT:
                running = False
                break

        clock.tick(60)
        dt = clock.get_time()
        update(dt)
        draw_screen(screen)
        pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()
