import pygame
from color import Color

display = None
window_width = 320
window_height = 240

mouse_pos = None

current_color = None
current_color_index = 0
current_color_rotation = None
total_colors = 10

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
        width = 20
        height = 20
        draw_square(x, y, width, height, current_color)
    except:
        pass

def draw_screen():
    global display
    display.fill(Color.black)
    draw_cursor()
    pygame.display.update()

def handle_events():
    global mouse_pos 
    global current_color_rotation
    global current_color_index 
    global current_color 
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
                current_color_index += 1
                if current_color_index >= len(current_color_rotation):
                    current_color_index = 0
                current_color = current_color_rotation[ current_color_index ] 
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
    window_width = 320
    window_height = 240
    title = "game_title"
    display = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption(title)
    handle_events()

if __name__ == '__main__':
    main()

