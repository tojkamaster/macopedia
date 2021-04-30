# Own better algorithm
from typing import Dict


def calculate_packages(product_count: int) -> Dict[str, int]:
    """
    Function for calculating amount of specific cartons
    """
    carton_sizes = {'large': 9, 'medium': 6, 'small': 3}
    carton_definitions = {'small': 0, 'medium': 0, 'large': 0}

    rest = product_count
    for key, value in carton_sizes.items():
        while rest >= value:
            carton_definitions[key] += 1
            rest -= value

    if rest > 0:
        carton_definitions['small'] += 1
        rest = 0

    # Cost optimization - 1 medium instead of 2 small
    if carton_definitions['small'] == 2:
        carton_definitions['small'] -= 2
        carton_definitions['medium'] += 1

    # Cost optimization - 1 large instead of 2 (small + medium)
    if carton_definitions['small'] > 0 and carton_definitions['medium'] > 0:
        carton_definitions['small'] -= 1
        carton_definitions['medium'] -= 1
        carton_definitions['large'] += 1

    return carton_definitions
