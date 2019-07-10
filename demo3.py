import pygame
import time
import threading
from color import Color
from random import randint 
import sys
import pygame

pygame.init()
window_width = 400
window_height = 300
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Hello World!')
font = pygame.font.Font("Terminus.ttf", 16)
debug_panel_text = None

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
    draw_debug_panel()
    pygame.display.update()

while True: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_q]:
                print("Quit pressed. Quitting...")
                pygame.quit()
                sys.exit()
    draw_screen()
    pygame.display.update()

