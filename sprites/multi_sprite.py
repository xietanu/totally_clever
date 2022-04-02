"""Classes for handling multi-part sprites, derived from arcade.Sprite"""
import arcade

import sprites


class MultiSprite(arcade.Sprite):
    """A subclass of Sprite that includes ability to draw multiple Sprites"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sub_sprites = sprites.MultiSpriteList(use_spatial_hash=False)
