import random 
import characters_properties 


class Turn_manager:
    def __init__(self):
        self.turn_order = []            # Will store the turn order 
        self.initiative_rolls = {}      # Stores the initiative rolls for each char_id in a dict {char_id : initiative_roll }
        self.current_turn_index = 0     # The turn will change from 0 (1st char in order) to 1(2nd char in order) to 2...... and so on # so it knows who's turn it is 
        self.round_number = 0            # this is the round after the chars complete their turns the round_number increases 
        self.battle_active = False      # If out of battle is False , if battle start it will change to True 

    def roll_initiative(self):
        self.initiative_rolls.clear()                                 # this clears the "rolls"
        
        for char_id, character in characters_properties.characters.items():
            if character.status != "Alive":
                continue

            minimum_roll = character.speed - 1
            maximum_roll = character.speed + 2

            initiative = random.randint(minimum_roll, maximum_roll)
            self.initiative_rolls[char_id] = initiative

            print(
                    f"{character.name} | "
                    f"speed: {character.speed} | "
                    f"range: {minimum_roll}-{maximum_roll} | "          # To test if it work and it does :)
                    f"initiative: {initiative}"
                )    
        return self.initiative_rolls           

    def create_turn_order(self):
        self.turn_order = list(self.initiative_rolls.keys())          # creates list for turn order 

        self.turn_order.sort(
            key = self.get_sort_values,                               # sorts it so it's from highest to lowest initiate roll, speed , friendly  
            reverse = True 
        )
        print (self.turn_order)
        return self.turn_order

    def get_sort_values(self, char_id):                               # 2 (Enemey) , 4 , 1(Friendly), 2 (Friendly), 1 (Enemy) - > 4, 2(Friendly), 2(Enemy), 1(Friendly). 1(Enemy)
        character = characters_properties.characters[char_id]
        initiative = self.initiative_rolls[char_id]
        speed = character.speed
        if character.team == "Friendly":                              # used for the turn order sorting logic , what to priorities for ex : 
            friendly_priority = 1                                     # highest initiation roll -> highest speed value -) friendly chars -> enemy chars 
        else:
            friendly_priority = 0

        return initiative, friendly_priority, speed

    def start_battle(self):                                           # starts the battle duhh
        self.current_turn_index = 0
        self.round_number = 1
        self.battle_active = True

        self.roll_initiative()
        self.create_turn_order()
        
        
    def get_active_char_id(self):                                     # will be used to select the char that has the turn
        if not self.battle_active:
            return None
        if not self.turn_order:
            return None

        return self.turn_order[self.current_turn_index]

    def remove_character(self, char_id):                              # removes "Dead" chars from the turn order list and the index 
        if char_id not in self.turn_order:
            return

        removed_index = self.turn_order.index(char_id)
        self.turn_order.remove(char_id)

        if removed_index < self.current_turn_index:
            self.current_turn_index -= 1

        if not self.turn_order:
            self.end_battle()                                         # ff the list is now empty the battle will be ended 
            return 

        if self.current_turn_index >= len(self.turn_order):
            self.current_turn_index = 0

    def end_turn(self):                                               # ends turn duhhh...
        if not self.battle_active:
            return None      
        if not self.turn_order:
            return None
        
        self.round_number += 1
        self.current_turn_index += 1

        if self.current_turn_index >= len(self.turn_order):
            self.current_turn_index = 0

        active_char_id = self.turn_order[self.current_turn_index]
        active_character = characters_properties.characters[active_char_id]
        active_character.brace = False
        
        self.end_battle()

    def end_battle(self):                   # ends the battle and resets turn order, initiation rolls, current turn index, turn number in order to be re initiated when next battle starts
        self.turn_order.clear()
        self.initiative_rolls.clear()
        self.current_turn_index = 0
        self.turn_number = 0
        self.battle_active = False


def set_turn():
    for turn_number in range(0, len(Turn_manager.turn_order)):
        characters_properties.characters[Turn_manager.turn_order[turn_number]].turn = turn_number + 1

