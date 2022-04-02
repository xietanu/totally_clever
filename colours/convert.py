"""Functions to convert between colour types"""


def hex_colour_to_rgb_tuple(hex_colour: str) -> tuple[int, int, int]:
    """
    Converts a hex value (e.g. #FF8000) and to an RGB tuple (e.g. (255,128,0))

    Args:
        hex_colour (str): Hex colour, # at start is optional.

    Returns:
        tuple[int, int, int]: RGB tuple colour equivalent.
    """
    hex_colour = hex_colour[-6:]
    return tuple(int(hex_colour[i : i + 2], 16) for i in range(0, 6, 2))
