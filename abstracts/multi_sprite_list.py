"""A subclass of SpriteList for containing and drawing MultiSprites"""
from arcade import SpriteList
import abstracts.multi_sprite as ms


class MultiSpriteList(SpriteList):
    """A subclass of SpriteList for containing and drawing MultiSprites"""

    def draw(self, **kwargs):
        """Draw all the contained Sprites, and subsprites for MultiSprites"""
        super().draw(**kwargs)
        for sprite in self:
            if isinstance(sprite, ms.MultiSprite):
                sprite.sub_sprites.draw()
