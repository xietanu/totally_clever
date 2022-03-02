"""A subclass of SpriteList for containing and drawing MultiSprites"""
from arcade import Sprite
import abstracts.multi_sprite_list as msl


class MultiSprite(Sprite):
    """A subclass of Sprite that includes ability to draw multiple Sprites"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sub_sprites = msl.MultiSpriteList(use_spatial_hash=False)
