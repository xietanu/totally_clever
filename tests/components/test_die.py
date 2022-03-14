"""Tests for the Die component"""
from abstracts.coords import Coords
from abstracts.colours import Colours
from components.die import Die


def test_die_center_x_0():
    """Test for setting x coord to 0"""
    die = Die(center=Coords(0, 0))

    assert die.center_x == 0


def test_die_center_x_10():
    """Test for setting x coord to 10"""
    die = Die(center=Coords(10, 20))

    assert die.center_x == 10


def test_die_center_y_0():
    """Test for setting y coord to 0"""
    die = Die(center=Coords(0, 0))

    assert die.center_y == 0


def test_die_center_x_15():
    """Test for setting y coord to 15"""
    die = Die(center=Coords(25, 15))

    assert die.center_y == 15


def test_die_width():
    """Test the die's width is set correctly"""
    die = Die(center=Coords(0, 0))

    assert die.width == 64


def test_die_height():
    """Test the die's height is set correctly"""
    die = Die(center=Coords(0, 0))

    assert die.height == 64


def test_colour_sapphire():
    """Test the colour is set correctly to sky blue"""
    die = Die(center=Coords(0, 0), colour=Colours.SKY.value)

    assert die.color == Colours.SKY.value


def test_colour_flame():
    """Test the colour is set correctly to alabaster white"""
    die = Die(center=Coords(0, 0), colour=Colours.ALABASTER.value)

    assert die.color == Colours.ALABASTER.value
