import loading_assets, characters_properties

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
    index = 0
    for keys in characters_properties.characters:
        h_bar_x = 1560
        h_bar_y = 106 + (index * 165) 
        h_bar_height = 20
        h_bar_width = set_width(characters_properties.characters[keys].health,characters_properties.characters[keys].max_health, h_bar_max_width)
        s_bar_x = 1560
        s_bar_y = 136 + (index * 165)
        s_bar_height = 20
        s_bar_width = set_width(characters_properties.characters[keys].stamina,characters_properties.characters[keys].max_stamina, s_bar_max_width)
        bars.append([[h_bar_x, h_bar_y, h_bar_height, h_bar_width, h_bar_max_width], [s_bar_x, s_bar_y, s_bar_height, s_bar_width, s_bar_max_width]])

    return bars













