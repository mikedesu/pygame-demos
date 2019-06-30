import pygame
from color import Color
import time
import threading
from random import randint 

scale = 1
window_width = 320 * scale
window_height = 240 * scale

current_color = None
current_color_index = 0
current_color_rotation = None
total_colors = 5

enemies = []
enemy_sizes = [ 8*scale, 12*scale, 20*scale ]
enemy_spawn_rate = 4

display = None
mouse_pos = None
score = 0
font = None

LEFT = 1
RIGHT = 3

def check_collision(enemy):
    global mouse_pos 
    try:
        width = 30*scale
        height = 30*scale
        x = mouse_pos[0]
        y = mouse_pos[1]
        x0 = x + width
        y0 = y + height
        return enemy[0] in range(x, x0) and (enemy[1] in range(y, y0) or enemy[1] in range(y0, y))
    except:
        pass
    return False

def check_collision_color(enemy):
    global current_color 
    return current_color == enemy[3]

def check_collisions():
    global enemies
    global score
    i = 0
    while i < len(enemies):
        enemy = enemies[i]
        if check_collision(enemy):
            enemies.pop(i)
            i -= 1
            if check_collision_color(enemy):
                score += enemy[2]
            else:
                score -= enemy[2]
            print(f"Score: {score}")
        i += 1

def draw_square(x, y, w, h, color):
    global display
    pygame.draw.rect(display, color, (x, y, w, h))

def draw_cursor():
    global display
    global mouse_pos 
    global current_color 
    try:
        x = mouse_pos[0]
        y = mouse_pos[1]
        width = 30*scale
        height = 30*scale
        draw_square(x, y, width, height, current_color)
    except:
        pass

def start_generating_enemies():
    threading.Timer(3, generate_enemy).start()

def random_enemy_size():
    global enemy_sizes 
    return enemy_sizes[ randint(0, len(enemy_sizes)-1) ]

def generate_enemy():
    # an enemy is a 4-tuple (x, y, size, color)
    global window_height, window_width, enemies, enemy_sizes, enemy_spawn_rate
    e_size = random_enemy_size()
    x = window_width - e_size
    y = randint(0, window_height - e_size)
    c = current_color_rotation[ randint(0, len(current_color_rotation)-1) ]
    enemy = (x, y, e_size, c)
    enemies.append(enemy)
    threading.Timer(enemy_spawn_rate, generate_enemy).start()

def update_enemies():
    i = 0
    while i < len(enemies):
        new_enemy = (enemies[i][0]-1, enemies[i][1], enemies[i][2], enemies[i][3])
        enemies[i] = new_enemy
        i += 1

def draw_enemies():
    global enemies, enemy_size
    for enemy in enemies:
        x = enemy[0]
        y = enemy[1]
        e_size = enemy[2]
        c = enemy[3]
        draw_square(x, y, e_size, e_size, c)

def setup_font():
    global font
    font = pygame.font.Font("Terminus.ttf", 16)

def draw_debug_panel():
    global display
    global font
    global debug_panel_text
    global window_width, window_height
    debug_panel_text = font.render( f"Score: {score}", True, Color.white, Color.black)
    text_rect = debug_panel_text.get_rect()
    text_rect.center = ( window_width//8, window_height//8 )
    display.blit(debug_panel_text, text_rect)

def draw_screen():
    global display
    display.fill(Color.black)
    draw_cursor()
    draw_enemies()
    draw_debug_panel()
    pygame.display.update()

def handle_events():
    global mouse_pos 
    global current_color_rotation
    global current_color_index 
    global current_color 
    global LEFT, RIGHT
    exit = False
    while not exit:
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_q]:
                    exit = True
            elif event.type == pygame.MOUSEBUTTONUP:
                print(f"Clicked! Mouse pos: {mouse_pos}")
                if event.button == LEFT:
                    current_color_index += 1
                    if current_color_index >= len(current_color_rotation):
                        current_color_index = 0
                elif event.button == RIGHT:
                    current_color_index -= 1
                    if current_color_index <= 0:
                        current_color_index = len(current_color_rotation)-1
                current_color = current_color_rotation[ current_color_index ] 
        update_enemies()
        check_collisions()
        draw_screen()

def init_colors():
    global total_colors
    global current_color_rotation
    global current_color_index 
    global current_color 
    current_color_rotation = []
    for i in range(total_colors):
        current_color_rotation.append( Color.random_color())
    current_color = current_color_rotation[0]
    current_color_index = 0

def main():
    global display
    global window_width
    global window_height
    init_colors()
    pygame.init()
    setup_font()
    title = "what do i call this?"
    display = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption(title)
    start_generating_enemies()
    handle_events()

if __name__ == '__main__':
    main()

