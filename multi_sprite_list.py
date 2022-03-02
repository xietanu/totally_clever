"""A subclass of SpriteList for containing and drawing MultiSprites"""
from arcade import SpriteList
import multi_sprite as ms


class MultiSpriteList(SpriteList):
    """A subclass of SpriteList for containing and drawing MultiSprites"""

    def draw(self, **kwargs):
        super().draw(**kwargs)
        for sprite in self:
            if isinstance(sprite, ms.MultiSprite):
                sprite.sub_sprites.draw()
