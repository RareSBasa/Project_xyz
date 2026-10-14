import pygame
from pathlib import Path

script_folder = Path(__file__).parent
assets_folder = script_folder / "assets"

def load_game_objects(width, height):

    background = pygame.image.load(assets_folder / "battle_map.png")
    background = pygame.transform.scale(background, (width, height))
    background_rect = background.get_rect()
    Manu_img = pygame.image.load(assets_folder / "sm_placeholder.png")
    Manu_img_rect = Manu_img.get_rect()


    return (background, background_rect, Manu_img, Manu_img_rect)