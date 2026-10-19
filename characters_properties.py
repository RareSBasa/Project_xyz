# All about the Characters and their behaviour 
import loading_assets

(_, _, manu_asset, manu_rect, ion_asset, ion_rect, hori_asset, hori_rect,
 enemy_1_asset, enemy_1_rect, enemy_2_asset, enemy_2_rect) = loading_assets.load_game_objects()

class Character:

    def __init__(self, char_id, name, team, max_health, max_stamina, position, skills):

        self.char_id = char_id
        self.name = name
        self.team = team
        self.max_health = max_health
        self.health = max_health
        self.max_stamina = max_stamina
        self.stamina = max_stamina
        self.pos = position
        self.skills = skills 

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        print(self.health)

   # def move(self, new_pos):    

Manu = Character(
    char_id = "pc_swordsman",
    name = "Manu",
    team = "Friendly",
    max_health = 100,
    max_stamina = 120,
    position = (1, 1),
    skills = [
        {"name": "Thrust", "stamina_cost": 3, "damage": 10, "range": 1},
        {"name": "Slash", "stamina_cost": 2, "damage": 3, "range": 1}
    ]

)
Hori = Character(
    char_id = "pc_archer",
    name = "Hori",
    team = "Friendly",
    max_health = 80,
    max_stamina = 140,
    position = (2, 1),
    skills = [
        {"name": "Arrow_Shot", "stamina_cost": 5, "damage": 12, "range": 3},
        {"name": "Precision_Shot", "stamina_cost": 10, "damage": 25, "range": 4}
    ]

)
Ion = Character(
    char_id = "pc_spearman",
    name = "Ion",
    team = "Friendly",
    max_health = 120,
    max_stamina = 100,
    position = (3, 1),
    skills = [
        {"name": "Thrust", "stamina_cost": 3, "damage": 10, "range": 2},
        {"name": "Rod Boink", "stamina_cost": 4, "damage": 5, "range": 2}
    ]
)

enemy_1 = Character(
    char_id = "en_swordsman_1",
    name = "Marcus",
    team = "Enemy",
    max_health = 800,
    max_stamina = 8,
    position = (1, 5),
    skills = [
        {"name": "Thrust", "stamina_cost": 3, "damage": 10, "range": 1},
        {"name": "Slash", "stamina_cost": 2, "damage": 3, "range": 1}
    ]
)
enemy_2 = Character(
    char_id = "en_swordsman_2",
    name = "Marcus",
    team = "Enemy",
    max_health = 800,
    max_stamina = 8,
    position = (2, 5),
    skills = [
        {"name": "Thrust", "stamina_cost": 3, "damage": 10, "range": 1},
        {"name": "Slash", "stamina_cost": 2, "damage": 3, "range": 1}
    ]
)

char_draw = [
             [manu_asset, manu_rect], 
             [ion_asset, ion_rect],
             [hori_asset, hori_rect],
             [enemy_1_asset, enemy_1_rect],
             [enemy_2_asset, enemy_2_rect]
]

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

char_boxes = loading_assets.get_char_boxes(len(characters))     # creates char_boxes as many as existing chars

chars_huds = dict(zip(characters, char_boxes))      # creates a dictionary with chars and their huds 

#print (Manu.skills)
# print (str(characters))
# print (str(characters["pc_swordsman"]))
# print ("this is: " + str(enemy_1))
print (chars_huds)
