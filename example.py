def add(left, right):
    """Return the sum of the left and right values.

    Args:
        left: The first value.
        right: The second value.

    Returns:
        The sum of the two values.

    Example:
        add(3, 4) -> 7
    """
    return left + right


def subtract(left, right):
    """Subtract the second value from the first.

    Args:
        left: The value to subtract from.
        right: The value to subtract.

    Returns:
        The difference between the two values.
    """
    return left - right


def test_add():
    assert add(3, 4) == 7


def test_subtract():
    assert subtract(3, 4) == -1
