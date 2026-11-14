import loading_assets, characters_properties

screen = width, height = 1920, 1080

max_health = 160.0
health = 49.0

h_bar_x = 135  
h_bar_y = 624
h_bar_height = 30
h_bar_width = 300
h_bar_max_width = 300

s_bar_x = 161
s_bar_y = 664 
s_bar_height = 20   
s_bar_width = 246
s_bar_max_width = 246

def set_width(amount, max_amount, bar_max_width):
    amount_precentage = amount / max_amount
    bar_width = bar_max_width * amount_precentage
    bar_width = int(bar_width)
    return bar_width

def get_bars(): # [[h_bar_x, h_bar_y, h_bar_height, h_bar_width, h_bar_max_width], [s_bar_x, s_bar_y, s_bar_height, s_bar_width, s_bar_max_width]]
    bars = []
    h_bar_max_width = 211
    s_bar_max_width = 211
    
    for index, character in enumerate(characters_properties.characters.values()):       # made use of indexing for the hp and stamina bars to work for each individual character

        h_bar_x = 1560
        h_bar_y = 106 + (index * 165) 
        h_bar_height = 20
        h_bar_width = set_width(character.health, character.max_health, h_bar_max_width)

        s_bar_x = 1560
        s_bar_y = 136 + (index * 165)
        s_bar_height = 20
        s_bar_width = set_width(character.stamina, character.max_stamina, s_bar_max_width)
        bars.append([[h_bar_x, h_bar_y, h_bar_height, h_bar_width, h_bar_max_width], [s_bar_x, s_bar_y, s_bar_height, s_bar_width, s_bar_max_width]])

    return bars

def get_turn_box_hp_bars(turn_manager):
    bars = []
    turn_order = turn_manager.turn_order
    h_bar_max_width = 78
    char_nr = len(turn_order)
    start_point = (width // 2) - ((char_nr//2) * 92) + 7

    for index in range(0, len(turn_order)):
        
        if char_nr % 2 == 0:
            h_bar_x = start_point + (index * 92)
            h_bar_y = 99
            h_bar_height = 8
            h_bar_width = set_width(characters_properties.characters[turn_order[index]].health, characters_properties.characters[turn_order[index]].max_health, h_bar_max_width)
            bars.append([h_bar_x, h_bar_y, h_bar_height, h_bar_width, h_bar_max_width])

        if char_nr % 2 == 1:
            h_bar_x = start_point + (index * 92)  - 46
            h_bar_y = 99
            h_bar_height = 8
            h_bar_width = set_width(characters_properties.characters[turn_order[index]].health, characters_properties.characters[turn_order[index]].max_health, h_bar_max_width)
            bars.append([h_bar_x, h_bar_y, h_bar_height, h_bar_width, h_bar_max_width])
    
    return bars













