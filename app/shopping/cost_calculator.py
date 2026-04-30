from typing import Dict, List


def get_total(costs: Dict[str, float], items: List[str], tax: float) -> float:
    total = 0.0
    for item in items:
        if item in costs:
            total += costs[item]
    return round(total * (1 + tax), 2)
