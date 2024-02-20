import pytest

from Figure import Figure

def test_raise():
    with pytest.raises(ValueError):
        Figure()

def test_match():
    with pytest.raises(ValueError, match="Количество аргументов меньше 1"):
        Figure()

def test_perimeter_figure():
    assert Figure(1,2,3,4).perimeter == 10
    assert Figure(2,2,3,3).perimeter == 10

def test_figura_add_area():
    A = Figure(1)
    A.area = 10
    B = Figure(2)
    B.area = 12
    assert B.add_area(A) == 22

