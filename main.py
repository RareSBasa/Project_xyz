import pygame, sys, random, characters_properties, loading_assets, hud 

from grid import detect_pos, grid_create, map, grid
from actions import move, character_add_on_map 

import actions

pygame.init()
size = width, height = 1920, 1080  #used to attribute the size of my monitor 
white = (255, 255, 255)
black = (0, 0, 0)   # or neighnour 

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project Name TBD")
font = pygame.font.SysFont(None, 70)

(background, background_rect, _, _,
_, _, _, _) = loading_assets.load_game_objects()

(icon_box, icon_box_rect, health_bar, health_bar_rect, health_bar_lines,
health_bar_lines_rect, stamina_bar, stamina_bar_rect, stamina_bar_lines, stamina_bar_lines_rect) = loading_assets.load_hud_objects()


def draw_h_bar(x, y, bar_width, bar_height):
    red = (255, 0, 0)
    pygame.draw.rect(screen, red, (x, y, bar_width, bar_height))

def draw_hud_1():
    screen.blit(icon_box, icon_box_rect)
    screen.blit(health_bar, health_bar_rect)
    screen.blit(stamina_bar, stamina_bar_rect)

def draw_hud_2():
    screen.blit(health_bar_lines, health_bar_lines_rect)
    screen.blit(stamina_bar_lines, stamina_bar_lines_rect)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def redraw():
    screen.fill(white)
    screen.blit(background, background_rect)
    for chars in characters_properties.char_draw:
        screen.blit(chars[0], chars[1])
    draw_hud_1()
    draw_h_bar(hud.h_bar_x, hud.h_bar_y, hud.h_bar_width, hud.h_bar_height)
    draw_hud_2()

def try_things(): # Test things using this function
    grid = grid_create()
    character_add_on_map(characters_properties.Ion.char_id, characters_properties.Ion.pos, grid)
    character_add_on_map(characters_properties.Manu.char_id, characters_properties.Manu.pos, grid)
    character_add_on_map(characters_properties.Hori.char_id, characters_properties.Hori.pos, grid)
    hud.h_bar_width = hud.set_width(48, 160)
    

try_things()
select = False    

while True:
    clock.tick(60)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Why tho? --- A: I like to exit the program with ESC :p
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:  #  - - - If the click button is being held, the program will take only one click and IGNORES the rest.
            print(str(detect_pos(event.pos)))
            print(str(event.pos))                                             # --- map = {(1, 1) : "Manu" } --- Manu --- detect_pos turns (532, 432) to (1, 1)
            print(str(map[detect_pos(event.pos)]))
            if type(map[detect_pos(event.pos)]) == str:  # Checks if map[click_pos] is a string ("char_id"), otherwise it would be int (0).
                print(map[detect_pos(event.pos)])
                select = True
                old_pos = detect_pos(event.pos)
                char_id = map[old_pos]

    while select:  # While loop that waits for user to click where to move the selected character
        
        redraw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if detect_pos(event.pos) != old_pos and 0 not in detect_pos(event.pos):
                    new_pos = detect_pos(event.pos)
                    move(char_id, old_pos, new_pos, grid)
                    select = False
                if 0 in detect_pos(event.pos) or detect_pos(event.pos) == old_pos: # Select turns False if user clicks outside the grid or on the same character
                    select = False

    redraw()
    pygame.display.flip()
