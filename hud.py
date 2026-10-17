import loading_assets

max_health = 160.0
health = 49.0

h_bar_x = 135  
h_bar_y = 624
h_bar_height = 30
h_bar_width = 300
h_bar_max_width = 300

def set_width(health, max_health):
    health_precentage = health / max_health
    h_bar_width = 300 * health_precentage
    h_bar_width = int(h_bar_width)
    return h_bar_width





