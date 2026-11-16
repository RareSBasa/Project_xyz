import pygame

import loading_assets, characters_properties, buttons

def draw_char_boxes(char_boxes, screen):
    for box in char_boxes:
        screen.blit(box[0], box[1])

def draw_char_turn_order_box_bars(hud, screen, turn_manager):
    red = (225, 0, 0)
    bars = hud.get_turn_box_hp_bars(turn_manager)
    for bar in bars:
        h_bar_x = bar[0]
        h_bar_y = bar[1]
        h_bar_height = bar[2]
        h_bar_width = bar[3]
        pygame.draw.rect(screen, red, (h_bar_x, h_bar_y, h_bar_width, h_bar_height))

def draw_turn_box_highlight(screen, turn_manager):
    highlight, highlight_rect = loading_assets.get_char_turn(turn_manager.get_active_char_id(), turn_manager.turn_order)
    screen.blit(highlight, highlight_rect)

def draw_turn_boxes(hud, screen, turn_manager):
    turn_order = turn_manager.turn_order
    draw_char_turn_order_box_bars(hud, screen, turn_manager)
    turn_box_icons = loading_assets.load_turn_box_assets()
    turn_boxes = loading_assets.get_turn_boxes(len(turn_order))
    
    characters_properties.set_icon_order(turn_order)
    for char_id in turn_order:
        icon_asset = characters_properties.chars_turn_box_items[char_id][0]
        icon_rect = characters_properties.chars_turn_box_items[char_id][1]
        screen.blit(icon_asset, icon_rect)

    draw_char_boxes(turn_boxes, screen)
    draw_turn_box_highlight(screen, turn_manager)
      
def draw_hud_1(screen, icon_box, icon_box_rect, health_bar, health_bar_rect, stamina_bar, stamina_bar_rect):
    screen.blit(icon_box, icon_box_rect)
    screen.blit(health_bar, health_bar_rect)
    screen.blit(stamina_bar, stamina_bar_rect)

def draw_hud_2(screen, health_bar_lines, health_bar_lines_rect, stamina_bar_lines, stamina_bar_lines_rect):
    screen.blit(health_bar_lines, health_bar_lines_rect)
    screen.blit(stamina_bar_lines, stamina_bar_lines_rect)

def draw_text(text, font, text_color, x, y, screen):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def draw_highlight(mouse_pos, highlight_rect, screen, highlight, grid):
    highlight_rect.center = grid[mouse_pos]            # Draw a highlight on the cursor hovered battle map square
    screen.blit(highlight, highlight_rect)

def draw_selected_highlight(char_pos, selected_highlight_rect, screen, selected_highlight, grid):
    selected_highlight_rect.center = grid[char_pos]
    screen.blit(selected_highlight, selected_highlight_rect)

def redraw(screen, white, background, background_rect, characters_properties, selected_char_id, active_skill, select,
        char_pos, hover, mouse_pos, font, selected_highlight, grid, selected_highlight_rect, highlight, highlight_rect,
        hud, turn_manager, end_turn_button):
    
    screen.fill(white)
    screen.blit(background, background_rect)

    if select:
        draw_selected_highlight(char_pos, selected_highlight_rect, screen, selected_highlight, grid)

    if hover:
        draw_highlight(mouse_pos, highlight_rect, screen, highlight, grid)

    for char_id, (asset, rect) in characters_properties.char_draw.items():       # draws the chars's assets on the screen 
        character = characters_properties.characters[char_id]

        if character.status in {"Alive"}:
            screen.blit(asset, rect)

    if selected_char_id != None and active_skill != None:
        draw_text(f"Selected char: {str(selected_char_id)}, HP: {str(characters_properties.characters[selected_char_id].max_health)} and ST: {str(characters_properties.characters[selected_char_id].max_stamina)}",
                   font, white, 10, 32, screen)
                                                                                           # still need to make it work with the new select logic 
        draw_text(f"Active skill: {str(active_skill)}", font, white, 10, 64, screen)

        draw_text(f"Character's EXP: {str(characters_properties.characters[selected_char_id].exp)}",
                                        font, white, 10, 96, screen
                                        )
        draw_text(f"Character's LVL: {str(characters_properties.characters[selected_char_id].level)}",
                                                font, white, 10, 128, screen
                                                )
    
    end_turn_button.draw(screen)

    if end_turn_button.hovering():

        end_turn_button.draw_hover(screen)
    draw_turn_boxes(hud, screen, turn_manager)                   # draws the chars boxes on the right of the screen 
    
    pygame.display.flip()