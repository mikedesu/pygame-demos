import pygame
import time
import threading
from color import Color
from animatedsprite import AnimatedSprite
from spritesheet import SpriteSheet
from random import randint 
import sys
import pygame
import os

pygame.init()
window_width = 400
window_height = 300
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Hello World!')
font = pygame.font.Font("Terminus.ttf", 16)
debug_panel_text = None

FPS = 60
clock = pygame.time.Clock()


def load_spritesheet_from_image(imagepath):
    print("load_spritesheet_from_image()")
    spritesheet = SpriteSheet(imagepath)
    images = []
    images.append( spritesheet.get_image(0,0,32,32).convert() )
    images.append( spritesheet.get_image(32,0,32,32).convert() )
    images.append( spritesheet.get_image(64,0,32,32).convert() )
    images.append( spritesheet.get_image(96,0,32,32).convert() )
    return images


def load_images(imagespath):
    print("load_images()")
    images = []
    for filename in os.listdir(imagespath):
        print(f"\tfilename: {filename}")
        image = pygame.image.load(imagespath + os.sep + filename).convert()
        images.append(image)
        print(f"image info: {image}")
    return images


def draw_debug_panel():
    global display_surface
    global font
    global debug_panel_text
    global window_width, window_height
    debug_panel_text = font.render( f"abcd", True, Color.white, Color.black)
    text_rect = debug_panel_text.get_rect()
    text_rect.center = ( window_width//8, window_height//8 )
    display_surface.blit(debug_panel_text, text_rect)


def draw_screen():
    global display_surface
    display_surface.fill(Color.black)
    #draw_debug_panel()
    pygame.display.update()


#images = load_images("./demo5images/")
images = load_spritesheet_from_image("./demo5images/bluebird-1.gif")
print(f"len(images): {len(images)}")
player = AnimatedSprite(position=(100,100), images=images)
all_sprites = pygame.sprite.Group(player)
player_velocity = 1

# init starfield
stars = []
num_stars = 1000
total_window_widths = 10
width_max = window_width * total_window_widths  
for i in range(num_stars):
    rx = randint(0, width_max)
    ry = randint(0, window_height)
    stars.append([rx,ry])


def draw_stars():
    global stars
    global display_surface
    i = 0
    while i < len(stars):
        star = stars[i]
        rx = star[0]
        ry = star[1]
        pygame.draw.rect(display_surface, Color.white, (rx, ry, 1, 1))
        star[0] -= 1
        stars[i] = star 
        i += 1


def handle_keypress(pressed):
    if pressed[pygame.K_q]:
        print("Quit pressed. Quitting...")
        pygame.quit()
        sys.exit()
    elif pressed[pygame.K_UP]:
        print("Pressed up")
        player.velocity.y -= player_velocity
    elif pressed[pygame.K_DOWN]:
        print("Pressed down")
        player.velocity.y += player_velocity
    elif pressed[pygame.K_LEFT]:
        print("Pressed left")
        player.velocity.x -= player_velocity
    elif pressed[pygame.K_RIGHT]:
        print("Pressed right")
        player.velocity.x += player_velocity


while True: # main game loop
    dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            handle_keypress(pressed)
    draw_screen()
    draw_stars()
    all_sprites.update(dt)
    all_sprites.draw(display_surface)
    pygame.display.update()

