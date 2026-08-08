"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):#Verify criticality is balanced.
    temp = float(temperature)
    neutrns = float (neutrons_emitted)
    product = temp * neutrns
    return temp < 800 and neutrns> 500 and product < 500000
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage*current
    '''Assess reactor efficiency zone with all the given input values and tell the reactor efficiency'''
    percent = (generated_power/theoretical_max_power)*100
    if 80<= percent <= 100:
        return "green"
    if 60<= percent <= 79.99:
        return "orange"
    if 30 <= percent <= 59.99:
        return "red"
    return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    percent_threshold = threshold*(10/100)
    '''Assess and return status code for the reactor and tells the reactor status by return low,normal,danger'''
    product = temperature* neutrons_produced_per_second 
    if product < (threshold-(percent_threshold)):
        return "LOW"
    if threshold-(percent_threshold) <= product <= threshold+(percent_threshold):
        return "NORMAL"
    return "DANGER"