from re import L
import pygame
from pathlib import Path

screen_size = width, height = 1920, 1080

script_folder = Path(__file__).parent
assets_folder = script_folder / "assets"
characters_folder = assets_folder / "characters"
ui_elements_folder = assets_folder / "ui_elements"

def load_game_objects():

    background = pygame.image.load(assets_folder / "battle_map.png")
    background_rect = background.get_rect()

    manu_asset = pygame.image.load(assets_folder / characters_folder / "sm_placeholder.png")
    manu_rect = manu_asset.get_rect()

    ion_asset = pygame.image.load(assets_folder / characters_folder / "spearman_placeholder.png")
    ion_rect = ion_asset.get_rect()

    hori_asset = pygame.image.load(assets_folder / characters_folder / "archer_placeholder.png")
    hori_rect = hori_asset.get_rect()

    enemy_1_asset = pygame.image.load(assets_folder / characters_folder / "enemy_sm_placeholder.png")
    enemy_1_rect = enemy_1_asset.get_rect()

    enemy_2_asset = pygame.image.load(assets_folder / characters_folder / "enemy_sm_placeholder.png")
    enemy_2_rect = enemy_2_asset.get_rect()

    return (background, background_rect, manu_asset, manu_rect, ion_asset, ion_rect, hori_asset, hori_rect, 
            enemy_1_asset, enemy_1_rect, enemy_2_asset, enemy_2_rect) 

def load_hud_objects():

    icon_box = pygame.image.load(assets_folder / ui_elements_folder / "icon_box.png")
    icon_box_rect = icon_box.get_rect()
    icon_box_rect.center = (284, 503)

    health_bar = pygame.image.load(assets_folder / ui_elements_folder / "health_bar.png")
    health_bar_rect = health_bar.get_rect()
    health_bar_rect.center = (284, 639)

    health_bar_lines = pygame.image.load(assets_folder / ui_elements_folder / "health_bar_lines.png")
    health_bar_lines_rect = health_bar_lines.get_rect()
    health_bar_lines_rect.x = 133
    health_bar_lines_rect.y = 622

    stamina_bar = pygame.image.load(assets_folder / ui_elements_folder / "stamina_bar.png")
    stamina_bar_rect = stamina_bar.get_rect()
    stamina_bar_rect.center = (284, 674)

    stamina_bar_lines = pygame.image.load(assets_folder / ui_elements_folder / "stamina_bar_lines.png")
    stamina_bar_lines_rect = stamina_bar_lines.get_rect()
    stamina_bar_lines_rect.x = 159
    stamina_bar_lines_rect.y = 662

    highlight = pygame.image.load(assets_folder / ui_elements_folder / "highlight.png")
    highlight_rect = highlight.get_rect()

    selected_highlight = pygame.image.load(assets_folder / ui_elements_folder / "selected_highlight.png")
    selected_highlight_rect = selected_highlight.get_rect()

    return (icon_box, icon_box_rect, health_bar, health_bar_rect, health_bar_lines, health_bar_lines_rect, stamina_bar, stamina_bar_rect, stamina_bar_lines, stamina_bar_lines_rect, highlight, highlight_rect, selected_highlight, selected_highlight_rect)

def load_turn_box_assets():

    manu_turn_box_asset = pygame.image.load(assets_folder / characters_folder / "sm_placeholder_turn_box.png")
    manu_turn_box_rect = manu_turn_box_asset.get_rect()

    ion_turn_box_asset = pygame.image.load(assets_folder / characters_folder / "spearman_placeholder_turn_box.png")
    ion_turn_box_rect = ion_turn_box_asset.get_rect()

    hori_turn_box_asset = pygame.image.load(assets_folder / characters_folder / "archer_placeholder_turn_box.png")
    hori_turn_box_rect = hori_turn_box_asset.get_rect()

    enemy_1_turn_box_asset = pygame.image.load(assets_folder / characters_folder / "enemy_sm_placeholder_turn_box.png")
    enemy_1_turn_box_rect = enemy_1_turn_box_asset.get_rect()

    enemy_2_turn_box_asset = pygame.image.load(assets_folder / characters_folder / "enemy_sm_placeholder_turn_box.png")
    enemy_2_turn_box_rect = enemy_2_turn_box_asset.get_rect()

    return (manu_turn_box_asset, manu_turn_box_rect, ion_turn_box_asset, ion_turn_box_rect, hori_turn_box_asset, hori_turn_box_rect, enemy_1_turn_box_asset, enemy_1_turn_box_rect, enemy_2_turn_box_asset, enemy_2_turn_box_rect)



def get_turn_boxes(character_number):
    char_boxes = []
    start_point = (width // 2) - ((character_number // 2) * 92)

    for i in range(0, character_number):
        char_box = pygame.image.load(assets_folder / ui_elements_folder / "char_turn_box.png")
        char_box_rect = char_box.get_rect()
        if character_number % 2 == 0:
            char_box_rect.x = start_point + (i * 92)
            char_box_rect.y = 1
            char_boxes.append([char_box, char_box_rect])
        elif character_number % 2 == 1:
            char_box_rect.x = start_point + (i * 92) - 46
            char_box_rect.y = 1
            char_boxes.append([char_box, char_box_rect])
  
    return char_boxes


