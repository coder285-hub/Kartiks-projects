from um import count


def test_single_um():
    assert count("hello, um, world") == 1


def test_no_um():
    assert count("yummy") == 0


def test_multiple_um():
    assert count("um um um um um") == 5


def test_case_insensitivity():
    assert count("Um UM uM um") == 4
