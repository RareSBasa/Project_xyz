import pygame, sys, random, characters_properties, grid, loading_assets 
from pathlib import Path

pygame.init()
size = width, height = 1920, 1080
white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project Name TBD")
font = pygame.font.SysFont(None, 70)

(background, background_rect) = loading_assets.load_game_objects(width, height)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def redraw():
    screen.fill(white)

    screen.blit (background, background_rect)

while True:
    clock.tick(60)

    redraw()
    pygame.display.flip()

