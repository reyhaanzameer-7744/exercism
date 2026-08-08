"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Check whether the reactor criticality is balanced.

    Parameters:
        temperature (float): The reactor temperature in kelvin.
        neutrons_emitted (float): The number of neutrons emitted per second.

    Returns:
        bool: True if all criticality conditions are satisfied,
        otherwise False.
    """
    temp = float(temperature)
    neutrns = float(neutrons_emitted)
    product = temp * neutrns

    return temp < 800 and neutrns > 500 and product < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Calculate the reactor efficiency zone.

    Parameters:
        voltage (float): The reactor voltage.
        current (float): The reactor current.
        theoretical_max_power (float): The maximum possible reactor power.

    Returns:
        str: The efficiency zone: green, orange, red, or black.
    """
    generated_power = voltage * current

    percent = (generated_power / theoretical_max_power) * 100

    if 80 <= percent <= 100:
        return "green"

    if 60 <= percent <= 79.99:
        return "orange"

    if 30 <= percent <= 59.99:
        return "red"

    return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Determine the fail-safe status of the reactor.

    Parameters:
        temperature (float): The reactor temperature.
        neutrons_produced_per_second (float): The number of neutrons
            produced per second.
        threshold (float): The criticality threshold.

    Returns:
        str: The reactor status: LOW, NORMAL, or DANGER.
    """
    percent_threshold = threshold * (10 / 100)

    product = temperature * neutrons_produced_per_second

    if product < threshold - percent_threshold:
        return "LOW"

    if threshold - percent_threshold <= product <= threshold + percent_threshold:
        return "NORMAL"

    return "DANGER"