import pytest

from Figure import Figure


def test_raise():
    with pytest.raises(ValueError):
        Figure()


def test_match():
    with pytest.raises(ValueError, match="Количество аргументов меньше 1"):
        Figure()


def test_perimeter_figure():
    assert Figure(1, 2, 3, 4).perimeter == 10
    assert Figure(2, 2, 3, 3).perimeter == 10


def test_figura_add_area():
    a = Figure(10)
    b = Figure(12)
    assert b.add_area(a) == 22
