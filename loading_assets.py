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

