"""Tests for Coords"""
from abstracts.coords import Coords

def test_coords_addition_type():
    """Test addition returns Coords"""
    coords_1 = Coords(0,0)
    coords_2 = Coords(0,0)

    assert isinstance(coords_1 + coords_2,Coords)

def test_coords_addition_basic():
    """Basic addition test"""
    coords_1 = Coords(2,1)
    coords_2 = Coords(5,4)

    expected = Coords(7,5)

    assert coords_1 + coords_2 == expected

def test_coords_addition_negative():
    """Negative addition test"""
    coords_1 = Coords(2,1)
    coords_2 = Coords(-7,-2)

    expected = Coords(-5,-1)

    assert coords_1 + coords_2 == expected
    