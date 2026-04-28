def get_total(costs: dict, items: list, tax: float) -> float:
    """
    Calculate the total cost of the given items including tax.
    Items not found in the costs dictionary are ignored.
    """
    subtotal = 0.0

    for item in items:
        if item in costs:
            subtotal += costs[item]

    total = subtotal + (subtotal * tax)
    return round(total, 2)
