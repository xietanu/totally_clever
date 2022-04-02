"""Tests for Coords"""
import components


def test_coords_addition_type():
    """Test addition returns Coords"""
    coords_1 = components.Coords(0, 0)
    coords_2 = components.Coords(0, 0)

    assert isinstance(coords_1 + coords_2, components.Coords)


def test_coords_addition_basic():
    """Basic addition test"""
    coords_1 = components.Coords(2, 1)
    coords_2 = components.Coords(5, 4)

    expected = components.Coords(7, 5)

    assert coords_1 + coords_2 == expected


def test_coords_addition_negative():
    """Negative addition test"""
    coords_1 = components.Coords(2, 1)
    coords_2 = components.Coords(-7, -2)

    expected = components.Coords(-5, -1)

    assert coords_1 + coords_2 == expected
