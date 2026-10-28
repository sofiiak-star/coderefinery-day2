import pytest

# Тема: Покупки

def calc_subtotal(prices):
    if not prices:
        raise ValueError("Prices list cannot be empty")
    if any(not isinstance(p, (int, float)) or isinstance(p, bool) or p < 0 for p in prices):
        raise ValueError("All prices must be positive numbers")
    return sum(prices)

def calc_discount(subtotal, discount_rate):
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")
    if not (0 <= discount_rate <= 1):
        raise ValueError("Discount rate must be between 0 and 1")
    return subtotal * discount_rate

def calc_delivery(subtotal, free_delivery_from=100, delivery_fee=20):
    if subtotal < 0 or free_delivery_from < 0 or delivery_fee < 0:
        raise ValueError("Values must be non-negative")
    if subtotal >= free_delivery_from:
        return 0
    return delivery_fee

def calc_total(prices, discount_rate=0, free_delivery_from=100, delivery_fee=20):
    subtotal = calc_subtotal(prices)
    discount = calc_discount(subtotal, discount_rate)
    delivery = calc_delivery(subtotal - discount, free_delivery_from, delivery_fee)
    return subtotal - discount + delivery

def print_receipt(prices, discount_rate=0, free_delivery_from=100, delivery_fee=20):
    subtotal = calc_subtotal(prices)
    discount = calc_discount(subtotal, discount_rate)
    delivery = calc_delivery(subtotal - discount, free_delivery_from, delivery_fee)
    total = subtotal - discount + delivery

    print("Receipt:")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Delivery: +${delivery:.2f}")
    print(f"Total: ${total:.2f}")

# Тести

@pytest.mark.parametrize("prices, expected", [
    ([100, 200, 50], 350),
    ([19.99, 10.1], 30.09),
    ([0.25, 0.5], 0.75),
],
)
def test_calc_subtotal(prices, expected):
    assert calc_subtotal(prices) == pytest.approx(expected)

@pytest.mark.parametrize("subtotal, rate, expected", [
    (1000, 0.10, 100),
    (200, 0.15, 30),
    (80, 0, 0),
],
)
def test_calc_discount(subtotal, rate, expected):
    assert calc_discount(subtotal, rate) == pytest.approx(expected)

@pytest.mark.parametrize("subtotal, expected", [
    (50, 20),
    (99, 20),
    (150, 0)
],
)
def test_calc_delivery(subtotal, expected):
    assert calc_delivery(subtotal) == pytest.approx(expected)

@pytest.mark.parametrize("subtotal, rate",[
    (100, 1.5),
    (100, -0.1),
],
)
def test_calc_discount_invalid(subtotal, rate):
    with pytest.raises(ValueError):
        calc_discount(subtotal, rate)

@pytest.mark.parametrize("prices",[
    [],
    [-10, 20],
    [-30, 5],
    [10, "двадцять"],
],
)

def test_calc_subtotal_invalid(prices):
    with pytest.raises(ValueError):
        calc_subtotal(prices)

if __name__ == "__main__":
    cart = [349.99, 199.50, 120.00]
    print_receipt(cart, discount_rate=0.10)
