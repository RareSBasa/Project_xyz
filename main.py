import pygame, sys, random, characters_properties, loading_assets, hud 

from grid import detect_pos, grid_create, map, grid
from actions import move, character_add_on_map 

import actions

pygame.init()
size = width, height = 1920, 1080  
white = (255, 255, 255)
black = (0, 0, 0)   

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project Name TBD")
font = pygame.font.SysFont(None, 32)

(background, background_rect, _, _,
_, _, _, _, _, _, _, _) = loading_assets.load_game_objects()

(icon_box, icon_box_rect, health_bar, health_bar_rect, health_bar_lines,
health_bar_lines_rect, stamina_bar, stamina_bar_rect, stamina_bar_lines, stamina_bar_lines_rect) = loading_assets.load_hud_objects()

characters = characters_properties.characters
attacker = ""

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
    for chars in characters_properties.char_draw:       # draws the chars boxes on the right of the screen 
        screen.blit(chars[0], chars[1])
    # draw_hud_1()
    # draw_h_bar(hud.h_bar_x, hud.h_bar_y, hud.h_bar_width, hud.h_bar_height)
    # draw_s_bar(hud.s_bar_x, hud.s_bar_y, hud.s_bar_width, hud.s_bar_height)
    # draw_hud_2()

    for char_box, char_rect in characters_properties.chars_huds.values():       # draws the hp and stamina bars for each char according to current health compared to max_health
        screen.blit(char_box, char_rect)

    if attacker != "":
        draw_text(f"Selected char: {str(attacker.char_id)}", font, white, 10, 32)
        
        draw_text(f"Selected skill: {str(selected_skill)}", font, white, 10, 64)

    draw_char_box_bars()
    pygame.display.flip()

def try_things(): # Test things using this function
    grid = grid_create()
    character_add_on_map(characters_properties.Ion.char_id, characters_properties.Ion.pos, grid)
    character_add_on_map(characters_properties.Manu.char_id, characters_properties.Manu.pos, grid)
    character_add_on_map(characters_properties.Hori.char_id, characters_properties.Hori.pos, grid)
    character_add_on_map(characters_properties.enemy_1.char_id, characters_properties.enemy_1.pos, grid)
    character_add_on_map(characters_properties.enemy_2.char_id, characters_properties.enemy_2.pos, grid)
    # hud.h_bar_width = hud.set_width(96, 160, hud.h_bar_max_width)
    # hud.s_bar_width = hud.set_width(8, 12, hud.s_bar_max_width)
    
    # characters_properties.Manu.health = 70
    # characters_properties.Hori.stamina = 10
    # characters_properties.Ion.health = 69
    # characters_properties.enemy_1.health = 45

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
            
        if event.type == pygame.MOUSEBUTTONUP:           #  - - - If the click button is being held, the program will take only one click and IGNORES the rest.
            print(str(detect_pos(event.pos)))
            print(str(event.pos))                        # --- map = {(1, 1) : "Manu" } --- Manu --- detect_pos turns (532, 432) to (1, 1)
            print(str(map[detect_pos(event.pos)]))
            if type(map[detect_pos(event.pos)]) == str:  # Checks if map[click_pos] is a string ("char_id"), otherwise it would be int (0).
                print(map[detect_pos(event.pos)])
                select = True
                old_pos = detect_pos(event.pos)
                char_id = map[old_pos]
                
                attacker = characters_properties.characters[char_id]    # attributes the selected char as an attacke in case it needs to attack 
                selected_skill = attacker.skills[0]                     # reset to this character s first skill
                print(f"Selected attacker: {attacker.char_id}")

    while select:  # While loop that waits for user to click where to move the selected character
        #clock.tick(60)
        redraw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if detect_pos(event.pos) != old_pos and 0 not in detect_pos(event.pos):
                    new_pos = detect_pos(event.pos)
                    if new_pos == old_pos:
                        select = False
                    elif new_pos not in map:
                        select = False
                    
                    else:
                    
                        target_id = map[new_pos]

                        if isinstance(target_id, str):               # asking if the square is occupied 
                            target = characters[target_id]

                            if target.team != attacker.team:
                                actions.attack(attacker.char_id, target_id, selected_skill)

                            # else:                             
                            #     ...
                        while attacker.stamina > 0 and old_pos != new_pos:   
                            print("old_pos:", old_pos)
                            print("new_pos:", new_pos)
                            print("same position:", old_pos == new_pos)
                            print("map at destination:", map.get(new_pos))                                
                            move(char_id, old_pos, new_pos, grid) 
                            old_pos = new_pos
                            new_pos = detect_pos(event.pos)                           # gives new position after each move 
                            select = True 
                        select = False
                        
                        redraw()
                
                elif 0 in detect_pos(event.pos) or detect_pos(event.pos) == old_pos:          # Select turns False if user clicks outside the grid or on the same character
                    select = False
            
            keys = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    selected_skill = attacker.skills[0]
                    print(selected_skill["name"])
                
                elif event.key == pygame.K_2:
                    selected_skill = attacker.skills[1]
                    print(selected_skill["name"])
                            
                elif event.key == pygame.K_t:
                    actions.attack(attacker.char_id, "en_swordsman_1",selected_skill)         # used to test if attack function works as intended 
    
    redraw()
    #pygame.display.flip()
