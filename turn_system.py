import pygame, random 
from characters_properties import characters 

class Turn_manager:
    def __init__(self):
        self.turn_order = []            # Will store the turn order 
        self.initiative_rolls = {}      # Stores the initiative rolls for each char_id in a dict
        self.current_turn = 0           # The turn will change from 0 (1st char in order) to 1(2nd char in order) to 2...... and so on 
        self.round_number = 0           # this is the round after the chars complete their turns the round_number increases 

    def roll_initiative(self):
        #self.initiative_rolls.clear()                              # this clears the "rolls"
        
        for char_id, character in characters.items():
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
