"""Markable box class"""
from arcade import create_text_image, create_text_sprite, Sprite, Texture
from abstracts.multi_sprite import MultiSprite


class MarkableBox(MultiSprite):
    """Class for boxes that can be marked"""

    def __init__(self, center_x, center_y, text=""):
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

        self.sub_sprites.append(self.text_sprite)

    def mark_box(self):
        """Mark or unmark the box"""
        self.marked = not self.marked
        if self.marked:
            self.sub_sprites.append(self.mark)
        else:
            self.mark.remove_from_sprite_lists()

    def update_text(self, new_text):
        """Update the text displayed in the box"""
        self.text = new_text
        self.text_sprite.texture = Texture(
            name=new_text,
            image=create_text_image(
                new_text,
                text_color=(0, 0, 0),
            ),
            hit_box_algorithm="None",
        )
