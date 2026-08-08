''' Implementing some rules from Pac-Man'''
def eat_ghost(power_pellet_active, touching_ghost):
    return bool(power_pellet_active and touching_ghost)

def score(touching_power_pellet, touching_dot):
    return bool(touching_power_pellet or touching_dot)
    
def lose(power_pellet_active, touching_ghost):
    return not power_pellet_active and touching_ghost
       
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    '''It tells that the Pac-man wins, if all conditions are satisifed'''
    if has_eaten_all_dots is True and power_pellet_active is True and touching_ghost is True:
        return True
    if has_eaten_all_dots is True and not lose(power_pellet_active, touching_ghost):
        return True
    return False
