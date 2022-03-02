"""Markable box class"""
from arcade import Sprite, create_text_sprite, SpriteList


class MarkableBox(Sprite):
    """Class for boxes that can be marked"""

    def __init__(self, center_x, center_y, text="", scale=1):
        super().__init__(filename="images/mark_box.png")
        self.marked = False
        self.center_x = center_x
        self.center_y = center_y
        self.mark = Sprite(
            filename="images/mark_box_mark.png",
            center_x=self.center_x,
            center_y=self.center_y,
            hit_box_algorithm="None",
        )
        self.text = text
        self.text_sprite = create_text_sprite(
            text,
            start_x=center_x,
            start_y=center_y,
            color=(0, 0, 0),
            anchor_x="center",
            anchor_y="center",
        )
        self.sub_sprites = SpriteList(use_spatial_hash=False)
        self.sub_sprites.append(self.text_sprite)

    def mark_box(self):
        """Mark or unmark the box"""
        self.marked = not self.marked
        if self.marked:
            self.sub_sprites.append(self.mark)
        else:
            self.mark.remove_from_sprite_lists()

    def draw_sub_sprites(self):
        """Draw sub sprites"""
        self.sub_sprites.draw()
