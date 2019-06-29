import pygame
from color import Color


display = None
window_width = 320
window_height = 240


c1 = None
c2 = None
c3 = None
c4 = None


def refresh_colors():
    global c1, c2, c3, c4
    c1 = Color.random_color()
    c2 = Color.random_color()
    c3 = Color.random_color()
    c4 = Color.random_color()


def draw_square(x, y, w, h, color):
    global display
    pygame.draw.rect(display, color, (x, y, w, h))


def draw_background():
    global display, window_width, window_height
    global c1, c2, c3, c4
    mid_x = window_width / 2
    mid_y = window_height / 2
    draw_square(0, 0, mid_x, mid_y, c1)
    draw_square(0, mid_y, mid_x, window_height, c2)
    draw_square(mid_x, 0, window_width, mid_y, c3)
    draw_square(mid_x, mid_y, window_width, window_height, c4)


def draw_screen():
    global display
    draw_background()
    pygame.display.update()


def handle_events():
    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_q]:
                    exit = True
                else:
                    refresh_colors()
        draw_screen()


def main():
    global display
    global window_width
    global window_height
    pygame.init()
    window_width = 320
    window_height = 240
    title = "game_title"
    refresh_colors()
    display = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption(title)
    handle_events()


if __name__ == '__main__':
    main()

