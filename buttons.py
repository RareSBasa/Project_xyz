from re import L
import pygame
from pathlib import Path

script_folder = Path(__file__).parent
assets_folder = script_folder / "assets"
ui_elements_folder = assets_folder / "ui_elements"
buttons_folder = ui_elements_folder / "buttons"

screen_size = width, height = 1920, 1080
screen = pygame.display.set_mode(screen_size)

class Button:

    def __init__(self, image_path, image_highlight_path, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = (x, y)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.mask = pygame.mask.from_surface(self.image)

        self.image_hover = pygame.image.load(image_highlight_path).convert_alpha()
        self.hover_rect = self.image_hover.get_rect()
        self.hover_rect.x = self.pos[0]
        self.hover_rect.y = self.pos[1]

    def hovering(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        relative_x = mouse_x - self.rect.x
        relative_y = mouse_y - self.rect.y

        if self.rect.collidepoint(mouse_x, mouse_y):           
            return self.mask.get_at((relative_x, relative_y))

        return False
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def draw_hover(self, screen):
        screen.blit(self.image_hover, self.hover_rect)

end_turn_button = Button((assets_folder / ui_elements_folder / buttons_folder / "end_turn_button.png"), 
                         (assets_folder / ui_elements_folder / buttons_folder / "end_turn_button_highlight.png"),
                         (width - 282),
                         (height - 117),
                        )





