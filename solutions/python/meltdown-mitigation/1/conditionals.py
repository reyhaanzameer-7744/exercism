"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    temp = float(temperature)
    neutrns = float (neutrons_emitted)
    product = temp * neutrns
    return temp < 800 and neutrns> 500 and product < 500000
       
        
    """Verify criticality is balanced."""


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage*current
    percent = (generated_power/theoretical_max_power)*100
    if 80<= percent <= 100:
        return "green"
    elif 60<= percent <= 79.99:
        return "orange"
    elif 30 <= percent <= 59.99:
        return "red"
    return "black"
    
    """Assess reactor efficiency zone."""

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    percent_threshold = threshold*(10/100)
    product = temperature* neutrons_produced_per_second 
    if product < (threshold-(percent_threshold)):
        return "LOW"
    elif threshold-(percent_threshold) <= product <= threshold+(percent_threshold):
        return "NORMAL"
    return "DANGER"




    
    """Assess and return status code for the reactor.

    Parameters:
        temperature (int or float): The value of the temperature in kelvin.
        neutrons_produced_per_second (int or float): The neutron flux.
        threshold (int or float): The threshold for the category.

    Returns:
        str: One of ('LOW', 'NORMAL', 'DANGER').

    Note:
        1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
        2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
        3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    pass
