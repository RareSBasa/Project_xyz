import pygame, sys, random, characters_properties, loading_assets, hud, actions, drawing
from grid import detect_pos, grid_create, map, grid

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
health_bar_lines_rect, stamina_bar, stamina_bar_rect, stamina_bar_lines, stamina_bar_lines_rect,
highlight, highlight_rect, selected_highlight, selected_highlight_rect) = loading_assets.load_hud_objects()

characters = characters_properties.characters
attacker = ""

def try_things(): # Test things using this function
    grid = grid_create()
    actions.character_add_on_map(characters_properties.Ion.char_id, characters_properties.Ion.pos, grid)
    actions.character_add_on_map(characters_properties.Manu.char_id, characters_properties.Manu.pos, grid)
    actions.character_add_on_map(characters_properties.Hori.char_id, characters_properties.Hori.pos, grid)
    actions.character_add_on_map(characters_properties.enemy_1.char_id, characters_properties.enemy_1.pos, grid)
    actions.character_add_on_map(characters_properties.enemy_2.char_id, characters_properties.enemy_2.pos, grid)

try_things()
hover = False
selected_char_id = None
active_skill = None
select = False
char_pos = ()

while True:
    clock.tick(60)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ### Back-End stuff \/
        
        if event.type == pygame.MOUSEBUTTONUP:            #  - - - If the click button is being held, the program will take only one click and IGNORES the rest.
            if 0 not in detect_pos(event.pos):
                if event.button == 1:                         # Left Click for select and attack(for now) 
                    print(str(detect_pos(event.pos)))
                         # --- map = {(1, 1) : "Manu" } --- Manu --- detect_pos turns (532, 432) to (1, 1)
                    print(str(map[detect_pos(event.pos)]))

                    #if type(map[detect_pos(event.pos)]) == str:  # Checks if map[click_pos] is a string ("char_id"), otherwise it would be int (0). --- changed the logic so no longer needed will delete after more testing 
                    print(map[detect_pos(event.pos)])
                
                    clicked_pos = detect_pos(event.pos)

                    if clicked_pos in map:                      # This should ignore clicks outside the map grid
                        occupant_id = map[clicked_pos]

                        if selected_char_id is None and type(map[detect_pos(event.pos)]) == str:
                            character = characters[occupant_id]
                            if character.team == "Friendly":
                                selected_char_id = occupant_id                          # This selects Friendly chars and their 1st skill, in order to move or attack 
                                active_skill = character.skills[0]            
                                print(f"Selected char is friendly: {character.char_id}")
                            
                        else:
                            selected_char = characters[selected_char_id]
                            # selected_char.pos = old_pos and clicked_pos = new_pos------so you know the logic 
                            
                            if occupant_id == 0:                                         # asks if tile is empty , 0 means no char is on it 
                                if selected_char.stamina > 0:
                                    actions.move(selected_char.char_id, selected_char.pos, clicked_pos, grid)

                            elif isinstance(occupant_id, str):                          # asks if tile is occupied by any chars 
                                target = characters[occupant_id]
                                distance = abs(selected_char.pos[0] - target.pos[0]) + abs(selected_char.pos[1] - target.pos[1])    # the distance between selected char and the enemy you want to attack 

                                if target.team != selected_char.team and distance <= active_skill["range"]:                   # asks if it's enemy and if so attacks

                                    actions.attack(selected_char.char_id, target.char_id, active_skill)
                                    while selected_char.exp >= 100 :
                                        characters_properties.selected_char.level_up()

                                else:                                                   # if not it's friendly and selects it instead 
                                    selected_char_id = occupant_id 
                                    active_skill = target.skills[0]
                if event.button == 2:
                    selected_char_id = None                     #Right click to Stop char selection
                    
            else:
                selected_char_id = None
                
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Why tho? --- A: I like to exit the program with ESC :p
                pygame.quit()
                sys.exit()
            
            if selected_char_id != None:                                # used to select active skill for selected char
                selected_char = characters[selected_char_id]

                if event.key == pygame.K_1:
                    active_skill = selected_char.skills[0]
                    print(active_skill["name"])
                
                elif event.key == pygame.K_2:
                    active_skill = selected_char.skills[1]
                    print(active_skill["name"])      

                        
    ### Front - End stuff \/

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pos = detect_pos((mouse_x, mouse_y))
    if 0 not in mouse_pos:                          # Hover for battlemap grid
        hover = True
    else:
        hover = False
    
    if selected_char_id != None:
        select = True # Rares NEMESIS
        char_pos = characters[selected_char_id].pos
    else:
        select = False


    drawing.redraw(screen, white, background, background_rect, characters_properties, selected_char_id, active_skill, select,
                   char_pos, hover, mouse_pos, font, selected_highlight, grid, selected_highlight_rect, highlight, highlight_rect,
                   hud)