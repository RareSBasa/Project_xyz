import loading_assets
from characters_properties import characters
from characters_properties import Manu, Ion, Hori, enemy_1, enemy_2
from grid import map, grid
from characters_properties import chars_id_and_rects

def move(char_id, old_pos, new_pos, grid):
	map[new_pos] = char_id
	map[old_pos] = 0
	characters[char_id].pos = new_pos
	chars_id_and_rects[map[new_pos]].topleft = grid[new_pos]

def character_add_on_map(char_id, pos, grid):
    map[pos] = char_id
    chars_id_and_rects[char_id].topleft = grid[pos]


	
