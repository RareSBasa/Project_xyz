import pygame, sys, random
from pathlib import Path

script_folder = Path(__file__).parent
assets_folder = script_folder / "assets"

size = width, height = 1080, 720

background = pygame.load.image(assets_folder / "battle_map.png")
