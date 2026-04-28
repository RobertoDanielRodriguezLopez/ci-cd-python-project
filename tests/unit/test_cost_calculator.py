from app.shopping.cost_calculator import get_total


def test_get_total_with_existing_items():
    costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
    items = ['socks', 'shoes']
    tax = 0.09

    result = get_total(costs, items, tax)

    assert result == 70.85


def test_get_total_ignores_non_existing_items():
    costs = {'socks': 5}
    items = ['socks', 'shoes']
    tax = 0.10

    result = get_total(costs, items, tax)

    assert result == 5.50


def test_get_total_with_no_items():
    costs = {'socks': 5}
    items = []
    tax = 0.20

    result = get_total(costs, items, tax)

    assert result == 0.00


def test_get_total_rounding():
    costs = {'item': 0.99}
    items = ['item']
    tax = 0.075

    result = get_total(costs, items, tax)

    assert result == 1.06
