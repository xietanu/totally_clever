"""Markable box class"""
import arcade
import sprites

from components import coords


class MarkableBox(sprites.MultiSprite):
    """Class for boxes that can be marked"""

    def __init__(
        self,
        parent_zone,
        center: coords.Coords,
        text: str = "",
        prereq=None,
    ):
        super().__init__(
            filename="images/mark_box.png",
            center_x=center.x_coord,
            center_y=center.y_coord,
        )
        self.marked = False
        self.markable = False

        self.prereq = prereq

        self.mark = arcade.Sprite(
            filename="images/mark_box_mark.png",
            center_x=self.center_x,
            center_y=self.center_y,
            hit_box_algorithm="None",
        )

        self.text = text
        self.text_sprite = arcade.create_text_sprite(
            text,
            start_x=center.x_coord,
            start_y=center.y_coord,
            color=(0, 0, 0),
            anchor_x="center",
            anchor_y="center",
        )
        self.parent_zone = parent_zone

        self.sub_sprites.append(self.text_sprite)

    def mark_box(self):
        """Mark or unmark the box"""
        if not self.markable:
            return False

        self.marked = True
        self.markable = False
        self.sub_sprites.append(self.mark)
        self.parent_zone.update_markables()
        return True

    def set_prereq(self, box):
        """
        Set the box required to be marked before this one can be marked.

        Args:
            box (MarkableBox)): Prerequisite box
        """
        self.prereq = box

    def update_text(self, new_text):
        """Update the text displayed in the box"""
        self.text = new_text
        self.text_sprite.texture = arcade.Texture(
            name=new_text,
            image=arcade.create_text_image(
                new_text,
                text_color=(0, 0, 0),
            ),
            hit_box_algorithm="None",
        )

    def update_markable(self):
        """Check any prerequisite conditions on being marked"""
        if (self.prereq is None or self.prereq.marked) and not self.marked:
            self.markable = True
        else:
            self.markable = False
