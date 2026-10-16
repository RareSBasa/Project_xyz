import pygame, sys, random, characters_properties, loading_assets 

from grid import detect_pos, grid_create

pygame.init()
size = width, height = 1920, 1080
white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project Name TBD")
font = pygame.font.SysFont(None, 70)

(background, background_rect, manu_asset, manu_rect,
ion_asset, ion_rect, hori_asset, hori_rect) = loading_assets.load_game_objects(width, height)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def redraw():
    screen.fill(white)
    screen.blit(background, background_rect)
    screen.blit(manu_asset, manu_rect)
    screen.blit(ion_asset, ion_rect)
    screen.blit(hori_asset, hori_rect)

def try_things(): # Test things using this function
    grid = grid_create()
    manu_rect.topleft = grid[characters_properties.Manu.pos]
    ion_rect.topleft = grid[characters_properties.Ion.pos]
    hori_rect.topleft = grid[characters_properties.Hari.pos]

try_things()
    

while True:
    clock.tick(60)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Why tho? --- A: I like to exit the program with ESC :p
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:  #  - - - If the click button is being held, the program will take only one click and IGNORES the rest.
            print(str(detect_pos(event.pos)))
            print(str(event.pos))

        


    redraw()
    pygame.display.flip()
