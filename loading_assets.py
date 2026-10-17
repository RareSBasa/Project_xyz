import pygame
from pathlib import Path

script_folder = Path(__file__).parent
assets_folder = script_folder / "assets"

def load_game_objects():

    background = pygame.image.load(assets_folder / "battle_map.png")
    background_rect = background.get_rect()

    manu_asset = pygame.image.load(assets_folder / "sm_placeholder.png")
    manu_rect = manu_asset.get_rect()

    ion_asset = pygame.image.load(assets_folder / "spearman_placeholder.png")
    ion_rect = ion_asset.get_rect()

    hori_asset = pygame.image.load(assets_folder / "archer_placeholder.png")
    hori_rect = hori_asset.get_rect()

    return (background, background_rect, manu_asset, manu_rect, ion_asset, ion_rect, hori_asset, hori_rect) 

def load_hud_objects():

    icon_box = pygame.image.load(assets_folder / "icon_box.png")
    icon_box_rect = icon_box.get_rect()
    icon_box_rect.center = (284, 503)

    health_bar = pygame.image.load(assets_folder / "health_bar.png")
    health_bar_rect = health_bar.get_rect()
    health_bar_rect.center = (284, 639)

    health_bar_lines = pygame.image.load(assets_folder / "health_bar_lines.png")
    health_bar_lines_rect = health_bar_lines.get_rect()
    health_bar_lines_rect.x = 133
    health_bar_lines_rect.y = 622

    stamina_bar = pygame.image.load(assets_folder / "stamina_bar.png")
    stamina_bar_rect = stamina_bar.get_rect()
    stamina_bar_rect.center = (284, 674)

    stamina_bar_lines = pygame.image.load(assets_folder / "stamina_bar_lines.png")
    stamina_bar_lines_rect = stamina_bar_lines.get_rect()
    stamina_bar_lines_rect.x = 159
    stamina_bar_lines_rect.y = 662


    return (icon_box, icon_box_rect, health_bar, health_bar_rect, health_bar_lines, health_bar_lines_rect, stamina_bar, stamina_bar_rect, stamina_bar_lines, stamina_bar_lines_rect)

