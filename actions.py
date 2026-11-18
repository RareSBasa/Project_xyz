from characters_properties import characters
from grid import map, grid
from characters_properties import chars_id_and_rects


def move(char_id, old_pos, new_pos, grid):
	map[new_pos] = char_id
	map[old_pos] = 0
	characters[char_id].pos = new_pos
	if characters[char_id].stamina > 0:
		new_coord = list(grid[new_pos])
		new_coord[1] = new_coord[1] + 10
		chars_id_and_rects[map[new_pos]].midbottom = tuple(new_coord)
		characters[char_id].stamina -= (4 - characters[char_id].speed)								# made it so for each time a char moves it loses 1 stamina
	else:
		old_coord = list(grid[old_pos])
		old_coord[1] = old_coord[1] + 10
		chars_id_and_rects[map[new_pos]].midbottom = tuple(old_coord)	

def character_add_on_map(char_id, pos, grid):
	map[pos] = char_id
	coord = list(grid[pos])
	coord[1] = coord[1] + 10
	chars_id_and_rects[char_id].midbottom = tuple(coord)

def remove_char_from_map(char_id):
	character = characters[char_id]
																		# used to remove chars when the assets is removed due to Death :>
	if map.get(character.pos) == char_id:
		map[character.pos] = 0
   
def attack(char_id_attacker, char_id_defender, skill, turn_manager):					# made it so when an attack is initiated it does damage and uses stamina 
	attacker = characters[char_id_attacker]
	defender = characters[char_id_defender]
	if attacker.stamina >= skill["stamina_cost"]:
		damage = skill["damage"]

		if defender.braced == True and damage > 0:
			damage = round(damage * .75)
	
		defender.take_damage(damage, turn_manager)
		attacker.stamina -= skill["stamina_cost"]

		if skill["status_effect"] != None and skill["status_effect"] not in defender.status_effect_list:
			
				defender.apply_status_effect(skill["status_effect"])
				if "Braced" in defender.status_effect_list:
					brace(defender.char_id)
				print(f"This char: {defender}, has been affliced with the following effect: {defender.status_effect_list}")
			
		if defender.status == "Dead":
			remove_char_from_map(defender.char_id)
			turn_manager.remove_character(defender.char_id)
			attacker.exp += 10
	print(f"THis char {attacker.char_id}, damages {defender.char_id}")

def brace(char_id):
	character = characters[char_id]

	if character.braced == False:
		character.braced = True 