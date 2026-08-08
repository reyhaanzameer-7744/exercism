def eat_ghost(power_pellet_active, touching_ghost):
    return bool(power_pellet_active and touching_ghost)

def score(touching_power_pellet, touching_dot):
    return bool(touching_power_pellet or touching_dot)
    
def lose(power_pellet_active, touching_ghost):
    if power_pellet_active is False and  touching_ghost is True:
        return True
    else:
        return False
       
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots is True and power_pellet_active is True and touching_ghost is True:
        return True
    if has_eaten_all_dots is True and lose(power_pellet_active, touching_ghost) is False:
        return True
    else:
        return False