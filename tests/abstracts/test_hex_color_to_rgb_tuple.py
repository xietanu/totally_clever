"""Tests for hex_colour_to_rgb_tuple"""
from abstracts.hex_color_to_rgb_tuple import hex_colour_to_rgb_tuple


def test_hex_colour_to_rgb_tuple_black():
    """Test for a basic black"""
    assert hex_colour_to_rgb_tuple("000000") == (0, 0, 0)


def test_hex_colour_to_rgb_tuple_white():
    """Test for a basic white"""
    assert hex_colour_to_rgb_tuple("FFFFFF") == (255, 255, 255)


def test_hex_colour_to_rgb_tuple_grey():
    """Test for a basic grey"""
    assert hex_colour_to_rgb_tuple("808080") == (128, 128, 128)


def test_hex_colour_to_rgb_tuple_light_red():
    """Test for light red"""
    assert hex_colour_to_rgb_tuple("FF4040") == (255, 64, 64)


def test_hex_colour_to_rgb_tuple_dark_green():
    """Test for dark green"""
    assert hex_colour_to_rgb_tuple("008020") == (0, 128, 32)
