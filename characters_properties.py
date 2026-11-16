# All about the Characters and their behaviour 
import loading_assets

width = 1920

(_, _, manu_asset, manu_rect, ion_asset, ion_rect, hori_asset, hori_rect,
 enemy_1_asset, enemy_1_rect, enemy_2_asset, enemy_2_rect) = loading_assets.load_game_objects()

([manu_turn_box_asset, manu_turn_box_rect], [ion_turn_box_asset, 
  ion_turn_box_rect], [hori_turn_box_asset, hori_turn_box_rect], [enemy_1_turn_box_asset, 
  enemy_1_turn_box_rect], [enemy_2_turn_box_asset, enemy_2_turn_box_rect]) = loading_assets.load_turn_box_assets()

class Character:

    def __init__(self, char_id, name, team, max_health, max_stamina, speed, position, skills, status, level, exp):

        self.char_id = char_id
        self.name = name
        self.level = level
        self.exp = exp
        self.team = team
        self.max_health = max_health
        self.health = max_health
        self.max_stamina = max_stamina
        self.stamina = max_stamina
        self.speed = speed 
        self.pos = position
        self.skills = skills 
        self.status = status
        self.turn = 0

    def take_damage(self, amount, turn_manager):
        
        self.health = max(0, self.health - amount)
        print(self.health)

        if self.health == 0:
            self.status = "Dead"
            turn_manager.turn_order.remove(self.char_id)    
            print("Status: ", self.status)

    def level_up(self):
        self.max_health *= 1.05
        self.max_stamina += .5
        self.exp -= 100  
        self.level += 1

Manu = Character(
    char_id = "pc_swordsman",
    name = "Manu",
    level = 1,
    exp = 0,
    team = "Friendly",
    max_health = 100,
    max_stamina = 12,
    speed = 2,
    position = (1, 1),
    skills = [
        {"name": "Thrust", "stamina_cost": 3, "damage": 10, "range": 1},
        {"name": "Slash", "stamina_cost": 2, "damage": 3, "range": 1}
    ],
    status = "Alive"

)
Hori = Character(
    char_id = "pc_archer",
    name = "Hori",
    level = 1,
    exp = 0,
    team = "Friendly",
    max_health = 80,
    max_stamina = 14,
    speed = 3,
    position = (2, 1),
    skills = [
        {"name": "Arrow_Shot", "stamina_cost": 5, "damage": 12, "range": 3},
        {"name": "Precision_Shot", "stamina_cost": 10, "damage": 25, "range": 4}
    ],
    status = "Alive"

)
Ion = Character(
    char_id = "pc_spearman",
    name = "Ion",
    level = 1,
    exp = 0,    
    team = "Friendly",
    max_health = 120,
    max_stamina = 10,
    speed = 1,
    position = (3, 1),
    skills = [
        {"name": "Spear Thrust", "stamina_cost": 3, "damage": 10, "range": 2},
        {"name": "Rod Boink", "stamina_cost": 4, "damage": 5, "range": 2}
    ],
    status = "Alive"
)

enemy_1 = Character(
    char_id = "en_swordsman_1",
    name = "Marcus",
    level = 1,
    exp = 0,
    team = "Enemy",    
    max_health = 80,
    max_stamina = 8,
    speed = 1,
    position = (1, 5),
    skills = [
        {"name": "Thrust", "stamina_cost": 3, "damage": 10, "range": 1},
        {"name": "Slash", "stamina_cost": 2, "damage": 3, "range": 1}
    ],
    status = "Alive"
)
enemy_2 = Character(
    char_id = "en_swordsman_2",
    name = "Darius",
    level = 1,
    exp = 0,
    team = "Enemy",
    max_health = 20,
    max_stamina = 8,
    speed = 1,
    position = (2, 5),
    skills = [
        {"name": "Thrust", "stamina_cost": 3, "damage": 10, "range": 1},
        {"name": "Slash", "stamina_cost": 2, "damage": 3, "range": 1}
    ],
    status = "Alive"
)

char_draw = {
    Manu.char_id: [manu_asset, manu_rect], 
    Ion.char_id: [ion_asset, ion_rect],
    Hori.char_id: [hori_asset, hori_rect],
    enemy_1.char_id: [enemy_1_asset, enemy_1_rect],
    enemy_2.char_id: [enemy_2_asset, enemy_2_rect]
}

characters = {
    Manu.char_id: Manu,
    Hori.char_id: Hori,
    Ion.char_id: Ion,
    
    enemy_1.char_id: enemy_1,
    enemy_2.char_id: enemy_2   
}

chars_id_and_rects = {
    Manu.char_id: manu_rect,
    Hori.char_id: hori_rect,
    Ion.char_id: ion_rect,
    
    enemy_1.char_id: enemy_1_rect,
    enemy_2.char_id: enemy_2_rect
}

chars_turn_box_items = {

    Manu.char_id: [manu_turn_box_asset, manu_turn_box_rect], 
    Ion.char_id: [ion_turn_box_asset, ion_turn_box_rect],
    Hori.char_id: [hori_turn_box_asset, hori_turn_box_rect],
    enemy_1.char_id: [enemy_1_turn_box_asset, enemy_1_turn_box_rect],
    enemy_2.char_id: [enemy_2_turn_box_asset, enemy_2_turn_box_rect]   

    }

def set_icon_order(turn_order):
    
    start_point = (width // 2) - ((len(turn_order) // 2) * 92)

    if len(turn_order) % 2 == 0:
        for index in range (0, len(turn_order)):
            chars_turn_box_items[turn_order[index]][1].x = 7 + start_point + (index * 92)
            chars_turn_box_items[turn_order[index]][1].y = 0

    elif len(turn_order) % 2 == 1:
        for index in range (0, len(turn_order)): 
            chars_turn_box_items[turn_order[index]][1].x = start_point + (index * 92) - 39
            chars_turn_box_items[turn_order[index]][1].y = 0

