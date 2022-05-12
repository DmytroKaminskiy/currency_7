def add(x, y):
    return x + y


def test_add_first():
    assert add(4, 4) == 8

def test_add_second():
    assert add(5, 6) == 11

def test_add_third():
    assert add(2, 3) == 5
