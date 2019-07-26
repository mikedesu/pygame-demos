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

player_velocity = 1

player = None
asteroid = None

all_player_sprites = None
all_asteroid_sprites = None

player_images = None
asteroid_images = None

def load_spritesheet_from_image(imagepath,w,h,frames_per,total_frames):
    print(f"load_spritesheet_from_image({imagepath}, {frames_per}, {total_frames})")
    assert(imagepath != "" and imagepath != None)
    assert(frames_per > 0 and frames_per != None)
    assert(total_frames > 0 and total_frames != None)
    assert(w > 0 and w != None)
    assert(h > 0 and h != None)
    spritesheet = SpriteSheet(imagepath)
    images = []
    animation = []
    for i in range(0,total_frames):
        if i % frames_per == 0 and i > 0:
            #print(f"appending: {animation}")
            images.append(animation)
            animation = []
        x = w * i
        #print(f"x: {x}")
        image_to_append = spritesheet.get_image(x,0,w,h).convert()
        #print(f"image_to_append: {image_to_append}")
        animation.append(image_to_append)
    print(f"len(images): {len(images)}")
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


def handle_keypress(pressed):
    global debug_panel_text_str
    if pressed[pygame.K_q]:
        print("Quit pressed. Quitting...")
        pygame.quit()
        sys.exit()
    elif pressed[pygame.K_UP]:
        print("Pressed up")
        if player.velocity.y > -1:
            player.velocity.y -= player_velocity
        player.set_current_animation()
        debug_panel_text_str = "omfg"
    elif pressed[pygame.K_DOWN]:
        print("Pressed down")
        if player.velocity.y < 1:
            player.velocity.y += player_velocity
        player.set_current_animation()
        debug_panel_text_str = "ffffff"
    elif pressed[pygame.K_LEFT]:
        print("Pressed left")
        if player.velocity.x > -1:
            player.velocity.x -= player_velocity
        player.set_current_animation()
        debug_panel_text_str = "Ayyyy sup"
    elif pressed[pygame.K_RIGHT]:
        print("Pressed right")
        if player.velocity.x < 1:
            player.velocity.x += player_velocity
        player.set_current_animation()
        debug_panel_text_str = "Sup playa"


def main():
    global images
    global player_images
    global player
    global all_player_sprites
    global asteroid 
    global asteroid_images
    global all_asteroid_sprites 
    
    player_images = load_spritesheet_from_image("./demo7images/bluebird-3-Sheet.gif", 64, 64, 4, 21)
    player = AnimatedSprite(position=(100,100), images=player_images)

    asteroid_images = load_spritesheet_from_image("./demo7images/asteroid1-Sheet.gif", 64, 64, 25, 26)
    asteroid = AnimatedSprite(position=(300,100), images=asteroid_images)

    all_player_sprites = pygame.sprite.Group(player)
    all_asteroid_sprites = pygame.sprite.Group(asteroid)

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

        all_asteroid_sprites.update(dt)
        all_asteroid_sprites.draw(display_surface)
        all_player_sprites.update(dt)
        all_player_sprites.draw(display_surface)

        pygame.display.update()

if __name__ == '__main__':
    main()

