import random 
from characters_properties import characters 

class Turn_manager:
    def __init__(self):
        self.turn_order = []            # Will store the turn order 
        self.initiative_rolls = {}      # Stores the initiative rolls for each char_id in a dict
        self.current_turn_index = 0     # The turn will change from 0 (1st char in order) to 1(2nd char in order) to 2...... and so on # so it knows who's turn it is 
        self.turn_number = 0            # this is the round after the chars complete their turns the round_number increases 
        self.battle_active = False      # If out of battle is False , if battle start it will change to True 

    def roll_initiative(self):
        self.initiative_rolls.clear()                                 # this clears the "rolls"
        
        for char_id, character in characters.items():
            if character.status != "Alive":
                continue
            minimum_roll = character.speed - 1
            maximum_roll = character.speed + 2

            initiative = random.randint(minimum_roll, maximum_roll)
            self.initiative_rolls[char_id] = initiative

        return self.initiative_rolls           

    def create_turn_order(self):
        self.turn_order = list(self.initiative_rolls.keys())          # creates list for turn order 

        self.turn_order.sort(
            key = self.get_sort_values,                               # sorts it so it's from highest to lowest initiate roll 
            reverse = True 
        )
        return self.turn_order

    def get_sort_values(self, char_id):
        character = characters[char_id]
        initiative = self.initiative_rolls[char_id]
        speed = character.speed
        if character.team == "Friendly":                              # used for the turn order sorting logic , what to priorities for ex : 
            friendly_priority = 1                                     # highest initiation roll -> highest speed value -) friendly chars -> enemy chars 
        else:
            friendly_priority = 0

        return initiative, speed, friendly_priority

    def start_battle(self):                                           # starts the battle duhh
        self.current_turn_index = 0
        self.turn_number = 1
        self.battle_active = True

        self.roll_initiative()
        self.create_turn_order()

    def get_active_char_id(self):                                     # will be used to select the char that has the turn
        if not self.battle_active:
            return None
        if not self.turn_order:
            return None

        return self.turn_order[self.current_turn_index]

    def end_turn(self):                                               # ends turn duhhh...
        if not self.battle_active:
            return None      
        if not self.turn_order:
            return None
        self.turn_number += 1
        checked_chars = 0

        while checked_chars < len(self.turn_order):                   # used to check if chars are alive, if not they will not be "shown" in the turn order
            
            self.current_turn_index += 1

            if self.current_turn_index >= len(self.turn_order):
                self.current_turn_index = 0

            active_char_id = self.turn_order[self.current_turn_index]
            active_character = characters[active_char_id]

            if active_character.status == "Alive":
                return
            
            checked_chars += 1
        

        self.end_battle()

    def end_battle(self):                   # ends the battle and resets turn order, initiation rolls, current turn index, turn number in order to be re initiated when next battle starts
        self.turn_order.clear()
        self.initiative_rolls.clear()
        self.current_turn_index = 0
        self.turn_number = 0
        self.battle_active = False