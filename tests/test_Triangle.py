import pytest

from Triangle import Triangle


def test_type():
    with pytest.raises(TypeError):
        Triangle(1, 2)


def test_negatie():
    with pytest.raises(ValueError, match="Отрицательный аргумент"):
        Triangle(1, -2, 7)


def test_valid():
    with pytest.raises(ValueError, match="Не треугольник"):
        Triangle(1, 2, 16)


def test_perimeter():
    assert Triangle(6, 8, 10).perimeter == 24
    assert Triangle(1, 2, 3).perimeter == 6


def test_area():
    assert Triangle(6, 8, 10).area == 24


def test_add_area():
    tra = Triangle(6, 8, 10)
    assert tra.add_area(tra) == 48
