# All about the Characters and their behaviour 


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
Hari = Character(
    char_id = "pc_archer",
    name = "Hari",
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

print (Manu.skills)

