"""Class for holding and drawing multi-part sprites"""
import copy

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

    def __add__(self, sprite_list: arcade.SpriteList):
        new_sprite_list = copy.copy(self)
        new_sprite_list.sprite_list += sprite_list.sprite_list
        return new_sprite_list
