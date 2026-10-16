import pygame, sys, random, characters_properties, loading_assets 

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

# char_draw = [[char_img, char_rect]]

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def redraw():
    screen.fill(white)
    screen.blit(background, background_rect)
    for chars in characters_properties.char_draw:
        screen.blit(chars[0], chars[1])


def try_things(): # Test things using this function
    grid = grid_create()
    character_add_on_map(characters_properties.Ion.char_id, characters_properties.Ion.pos, grid)
    character_add_on_map(characters_properties.Manu.char_id, characters_properties.Manu.pos, grid)
    character_add_on_map(characters_properties.Hori.char_id, characters_properties.Hori.pos, grid)


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
            if type(map[detect_pos(event.pos)]) == str:
                print(map[detect_pos(event.pos)])
                select = True
                old_pos = detect_pos(event.pos)
                char_id = map[old_pos]

        if select:
        
            redraw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    if detect_pos(event.pos) != old_pos:
                           new_pos = detect_pos(event.pos)
                           move(char_id, old_pos, new_pos, grid)
                           select = False



                                                        

                            
                



        


    redraw()
    pygame.display.flip()
