import loading_assets
from characters_properties import characters
from characters_properties import Manu, Ion, Hori, enemy_1, enemy_2
from grid import map, grid
from characters_properties import chars_id_and_rects

def move(char_id, old_pos, new_pos, grid):
	map[new_pos] = char_id
	map[old_pos] = 0
	characters[char_id].pos = new_pos
	if characters[char_id].stamina > 0:
		chars_id_and_rects[map[new_pos]].topleft = grid[new_pos]
		characters[char_id].stamina -= 1							# made it so for each time a char moves it loses 1 stamina
	else:
		chars_id_and_rects[map[new_pos]].topleft = grid[old_pos]		

def character_add_on_map(char_id, pos, grid):
    map[pos] = char_id
    chars_id_and_rects[char_id].topleft = grid[pos]

def attack(char_id_attacker, char_id_defender):					# made it so when an attack is initiated it does damage and uses stamina 
	attacker = characters[char_id_attacker]
	defender = characters[char_id_defender]
	if attacker.stamina >= attacker.skills[0]["stamina_cost"]:
		defender.take_damage(attacker.skills[0]["damage"])
		attacker.stamina -= attacker.skills[0]["stamina_cost"]
