def add(left, right):
    return left + right


def subtract(left, right):
    return left - right


def test_add():
    assert add(3, 4) == 7


def test_subtract():
    assert subtract(3, 4) == -1


def test_subtract_positive_result():
    assert subtract(4, 3) == 1
