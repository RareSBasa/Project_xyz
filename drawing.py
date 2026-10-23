import pygame 

def draw_char_boxes(char_boxes, screen):
    for box in char_boxes:
        screen.blit(box[0], box[1])

def draw_char_box_bars(hud, screen): # [[h_bar_x, h_bar_y, h_bar_height, h_bar_width, h_bar_max_width], [s_bar_x, s_bar_y, s_bar_height, s_bar_width, s_bar_max_width]]
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

def draw_h_bar(x, y, bar_width, bar_height, screen):
    red = (255, 0, 0)
    pygame.draw.rect(screen, red, (x, y, bar_width, bar_height))

def draw_s_bar(x, y, bar_width, bar_height, screen):
    yellow = (255, 255, 0)
    pygame.draw.rect(screen, yellow, (x, y, bar_width, bar_height))

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
    highlight_rect.topleft = grid[mouse_pos]            # Draw a highlight on the cursor hovered battle map square
    screen.blit(highlight, highlight_rect)

def draw_selected_highlight(char_pos, selected_highlight_rect, screen, selected_highlight, grid):
    selected_highlight_rect.topleft = grid[char_pos]
    screen.blit(selected_highlight, selected_highlight_rect)

def redraw(screen, white, background, background_rect, characters_properties, selected_char_id, active_skill, select,
        char_pos, hover, mouse_pos, font, selected_highlight, grid, selected_highlight_rect, highlight, highlight_rect,
        hud ):
    
    screen.fill(white)
    screen.blit(background, background_rect)

    for char_id, (asset, rect) in characters_properties.char_draw.items():       # draws the chars's assets on the screen 
        character = characters_properties.characters[char_id]

        if character.status in {"Alive"}:
            screen.blit(asset, rect)

    for char_box, char_rect in characters_properties.chars_huds.values():       # draws the hp and stamina bars for each char according to current health compared to max_health
        screen.blit(char_box, char_rect)

    if selected_char_id != None and active_skill != None:
        draw_text(f"Selected char: {str(selected_char_id)}", font, white, 10, 32, screen)
                                                                                           # still need to make it work with the new select logic 
        draw_text(f"Active skill: {str(active_skill)}", font, white, 10, 64, screen)

        draw_text(f"Character's Status: {str(characters_properties.characters[selected_char_id].status)}",
                                        font, white, 10, 96, screen
                                        )

    if select:
        draw_selected_highlight(char_pos, selected_highlight_rect, screen, selected_highlight, grid)

    if hover:
        draw_highlight(mouse_pos, highlight_rect, screen, highlight, grid)

    draw_char_box_bars(hud, screen)                     # draws the chars boxes on the right of the screen 
    
    pygame.display.flip()