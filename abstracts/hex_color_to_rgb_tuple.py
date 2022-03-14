"""hex_colour_to_rgb_tuple"""


def hex_colour_to_rgb_tuple(hex_colour: str) -> tuple[int, int, int]:
    """Takes a hex values (e.g. #FF8000) and returns an RGB tuple (e.g. (255,128,0))"""
    hex_colour = hex_colour[-6:]
    return tuple(int(hex_colour[i : i + 2], 16) for i in range(0, 6, 2))
