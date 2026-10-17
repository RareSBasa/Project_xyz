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

def draw_char_boxes(char_boxes):
    for box in char_boxes:
        screen.blit(box[0], box[1])

def draw_char_box_bars(): # [[h_bar_x, h_bar_y, h_bar_height, h_bar_width, h_bar_max_width], [s_bar_x, s_bar_y, s_bar_height, s_bar_width, s_bar_max_width]]
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    bars = hud.get_bars()
    for bar in bars:
        h_bar_x = bar[0][0]
        h_bar_y = bar[0][1]
        h_bar_height = bar[0][2]
        h_bar_width = bar[0][3]
        s_bar_x = bar[1][0]
        s_bar_y = bar[1][1]
        s_bar_height = bar[1][2]
        s_bar_width = bar[1][3]
        pygame.draw.rect(screen, red, (h_bar_x, h_bar_y, h_bar_width, h_bar_height))
        pygame.draw.rect(screen, yellow, (s_bar_x, s_bar_y, s_bar_width, s_bar_height))

def draw_h_bar(x, y, bar_width, bar_height):
    red = (255, 0, 0)
    pygame.draw.rect(screen, red, (x, y, bar_width, bar_height))

def draw_s_bar(x, y, bar_width, bar_height):
    yellow = (255, 255, 0)
    pygame.draw.rect(screen, yellow, (x, y, bar_width, bar_height))

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
    draw_s_bar(hud.s_bar_x, hud.s_bar_y, hud.s_bar_width, hud.s_bar_height)
    draw_char_boxes(loading_assets.char_boxes)
    draw_char_box_bars()
    draw_hud_2()

def try_things(): # Test things using this function
    grid = grid_create()
    character_add_on_map(characters_properties.Ion.char_id, characters_properties.Ion.pos, grid)
    character_add_on_map(characters_properties.Manu.char_id, characters_properties.Manu.pos, grid)
    character_add_on_map(characters_properties.Hori.char_id, characters_properties.Hori.pos, grid)
    hud.h_bar_width = hud.set_width(48, 160, hud.h_bar_max_width)
    hud.s_bar_width = hud.set_width(6, 12, hud.s_bar_max_width)
    

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
