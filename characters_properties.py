# All about the Characters and their behaviour 
import loading_assets

(_, _, manu_asset, manu_rect, ion_asset, ion_rect, hori_asset, hori_rect) = loading_assets.load_game_objects()

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

   # def move(self, new_pos):    

Manu = Character(
    char_id = "pc_swordsman",
    name = "Manu",
    team = "Friendly",
    max_health = 100,
    max_stamina = 12,
    position = (1, 1),
    skills = [
        {"name": "Thrust", "type": "piercing", "stamina_cost": 3, "damage": 10, "range": 1},
        {"name": "Slash", "type": "slicing", "stamina_cost": 2, "damage": 3, "range": 1}
    ]

)
Hori = Character(
    char_id = "pc_archer",
    name = "Hori",
    team = "Friendly",
    max_health = 80,
    max_stamina = 14,
    position = (2, 1),
    skills = [
        {"name": "Arrow_Shot", "type": "piercing", "stamina_cost": 5, "damage": 12, "range": 3},
        {"name": "Precision_Shot", "type": "piercing", "stamina_cost": 10, "damage": 25, "range": 4}
    ]

)
Ion = Character(
    char_id = "pc_spearman",
    name = "Ion",
    team = "Friendly",
    max_health = 120,
    max_stamina = 10,
    position = (3, 1),
    skills = [
        {"name": "Thrust", "type": "piercing", "stamina_cost": 3, "damage": 10, "range": 2},
        {"name": "Rod Boink", "type": "blunt", "stamina_cost": 4, "damage": 5, "range": 2}
    ]
)

enemy_1 = Character(
    char_id = "en_swordsman",
    name = "Marcus",
    team = "Enemy",
    max_health = 80,
    max_stamina = 8,
    position = (1, 5),
    skills = [
        {"name": "Arrow_Shot", "type": "piercing", "stamina_cost": 5, "damage": 12, "range": 3},
        {"name": "Precision_Shot", "type": "piercing", "stamina_cost": 10, "damage": 25, "range": 4}
    ]
)
enemy_2 = Character(
    char_id = "en_swordsman",
    name = "Marcus",
    team = "Enemy",
    max_health = 80,
    max_stamina = 8,
    position = (2, 5),
    skills = [
        {"name": "Arrow_Shot", "type": "piercing", "stamina_cost": 5, "damage": 12, "range": 3},
        {"name": "Precision_Shot", "type": "piercing", "stamina_cost": 10, "damage": 25, "range": 4}
    ]
)

char_draw = [
             [manu_asset, manu_rect], 
             [ion_asset, ion_rect],
             [hori_asset, hori_rect]
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
    
    # enemy_1.char_id: enemy_1,
    # enemy_2.char_id: enemy_2
}

#print (Manu.skills)
print (str(characters))
print (str(characters["pc_swordsman"]))
print ("this is: " + str(enemy_1))

