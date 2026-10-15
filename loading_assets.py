import pygame
from pathlib import Path

script_folder = Path(__file__).parent
assets_folder = script_folder / "assets"

def load_game_objects(width, height):

    background = pygame.image.load(assets_folder / "battle_map.png")
    background_rect = background.get_rect()
    manu = pygame.image.load(assets_folder / "sm_placeholder.png")
    manu_rect = manu.get_rect()


    return (background, background_rect, manu, manu_rect)