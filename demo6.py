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
window_width = 800
window_height = 600
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Space Shit 0.01a')
font = pygame.font.Font("Terminus.ttf", 24)
debug_panel_text = None
debug_panel_text_str = "Testing..."

FPS = 60
clock = pygame.time.Clock()

def load_spritesheet_from_image(imagepath):
    print(f"load_spritesheet_from_image({imagepath})")
    spritesheet = SpriteSheet(imagepath)
    images = []
    animation0 = []
    animation1 = []
    animation2 = []
    animation3 = []
    animation4 = []
    w = 64
    h = 64

    # first animation
    animation0.append( spritesheet.get_image(0,0,w,h).convert() )
    animation0.append( spritesheet.get_image(w,0,w,h).convert() )
    animation0.append( spritesheet.get_image(w*2,0,w,h).convert() )
    animation0.append( spritesheet.get_image(w*3,0,w,h).convert() )

    animation1.append( spritesheet.get_image(w*4,0,w,h).convert() )
    animation1.append( spritesheet.get_image(w*5,0,w,h).convert() )
    animation1.append( spritesheet.get_image(w*6,0,w,h).convert() )
    animation1.append( spritesheet.get_image(w*7,0,w,h).convert() )

    animation2.append( spritesheet.get_image(w*8,0,w,h).convert() )
    animation2.append( spritesheet.get_image(w*9,0,w,h).convert() )
    animation2.append( spritesheet.get_image(w*10,0,w,h).convert() )
    animation2.append( spritesheet.get_image(w*11,0,w,h).convert() )
    
    animation3.append( spritesheet.get_image(w*12,0,w,h).convert() )
    animation3.append( spritesheet.get_image(w*13,0,w,h).convert() )
    animation3.append( spritesheet.get_image(w*14,0,w,h).convert() )
    animation3.append( spritesheet.get_image(w*15,0,w,h).convert() )

    animation4.append( spritesheet.get_image(w*16,0,w,h).convert() )
    animation4.append( spritesheet.get_image(w*17,0,w,h).convert() )
    animation4.append( spritesheet.get_image(w*18,0,w,h).convert() )
    animation4.append( spritesheet.get_image(w*19,0,w,h).convert() )

    images.append(animation0)
    images.append(animation1)
    images.append(animation2)
    images.append(animation3)
    images.append(animation4)

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
    global debug_panel_text_str
    global window_width, window_height
    debug_panel_text = font.render( f"{debug_panel_text_str}", True, Color.white, Color.black)
    text_rect = debug_panel_text.get_rect()
    text_rect.center = ( window_width//8, window_height//8 )
    display_surface.blit(debug_panel_text, text_rect)


def draw_screen():
    global display_surface
    display_surface.fill(Color.black)
    draw_debug_panel()
    pygame.display.update()


images = load_spritesheet_from_image("./demo6images/bluebird-3-Sheet.png")

print(f"len(images): {len(images)}")
player = AnimatedSprite(position=(100,100), images=images)
all_sprites = pygame.sprite.Group(player)
player_velocity = 1

# init starfield
stars = []
num_stars = 2000
total_window_widths = 50
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
    global debug_panel_text_str
    if pressed[pygame.K_q]:
        print("Quit pressed. Quitting...")
        pygame.quit()
        sys.exit()
    elif pressed[pygame.K_UP]:
        print("Pressed up")
        player.velocity.y -= player_velocity
        player.set_current_animation()
        debug_panel_text_str = "omfg"
    elif pressed[pygame.K_DOWN]:
        print("Pressed down")
        player.velocity.y += player_velocity
        player.set_current_animation()
        debug_panel_text_str = "ffffff"
    elif pressed[pygame.K_LEFT]:
        print("Pressed left")
        player.velocity.x -= player_velocity
        player.set_current_animation()
        debug_panel_text_str = "Ayyyy sup"
    elif pressed[pygame.K_RIGHT]:
        print("Pressed right")
        player.velocity.x += player_velocity
        player.set_current_animation()
        debug_panel_text_str = "Sup playa"


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

