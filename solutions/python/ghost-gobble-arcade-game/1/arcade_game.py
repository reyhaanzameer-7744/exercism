"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active and touching_ghost is True:
        return True 
    else:
        return False

def score(touching_power_pellet, touching_dot):
    if touching_power_pellet or touching_dot is True:
        return True
    else:
        return False

def lose(power_pellet_active, touching_ghost):
    if power_pellet_active is False and touching_ghost is True:
        return True
    else:
        return False
      
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots is True and power_pellet_active is True and touching_ghost is True:
        return True
    elif has_eaten_all_dots is True and lose(power_pellet_active, touching_ghost) is False:
        return True
    else:
        return False



    
    """Trigger the victory event when all dots have been eaten.

    Parameters:
        has_eaten_all_dots (bool): Has the player "eaten" all the dots?
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Has the player won the game?
    """

    pass
