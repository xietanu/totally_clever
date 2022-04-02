"""Class for holding and drawing multi-part sprites"""
import arcade

import sprites


class MultiSpriteList(arcade.SpriteList):
    """A subclass of SpriteList for containing and drawing MultiSprites"""

    def draw(self, **kwargs):
        """Draw all the contained Sprites, and subsprites for MultiSprites"""
        super().draw(**kwargs)
        for sprite in self:
            if isinstance(sprite, sprites.MultiSprite):
                sprite.sub_sprites.draw()
