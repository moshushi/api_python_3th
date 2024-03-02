import pytest

from Figure import Figure


def test_type():
    with pytest.raises(TypeError):
        Figure()


def test_negative():
    with pytest.raises(ValueError, match="Отрицательный аргумент"):
        Figure(-1)


def test_add_area():
    ob1 = Figure(1)
    ob2 = Figure(16)
    assert ob1.add_area(ob2) == ob1.area + ob2.area
