"""Tests for the ScoreCategory component"""
from arcade import SpriteList
from abstracts.coords import Coords

from components.score_categories.score_category import ScoreCategory, ScoreModes


def test_center_x():
    """Test the center of the sprite calculated correctly - x"""
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(0, 0))
    assert score_cat.center_x == 250
    score_cat = ScoreCategory("images/green_icon.png", Coords(100, 100))
    assert score_cat.center_x == 116


def test_center_y():
    """Test the center of the sprite calculated correctly - y"""
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(0, 0))
    assert score_cat.center_y == 40
    score_cat = ScoreCategory("images/green_icon.png", Coords(100, 100))
    assert score_cat.center_y == 116


def test_score_trackers_created():
    """Test that score trackers are being initialised when appropriate"""
    score_cat = ScoreCategory(
        "images/GreenCategoryBox.png", Coords(0, 0), score_mode=ScoreModes.SUM
    )
    assert score_cat.score_trackers is None
    score_cat = ScoreCategory(
        "images/GreenCategoryBox.png", Coords(0, 0), score_mode=ScoreModes.MATCHED
    )
    assert isinstance(score_cat.score_trackers, SpriteList)
    score_cat = ScoreCategory(
        "images/GreenCategoryBox.png", Coords(0, 0), score_mode=ScoreModes.COUNT
    )
    assert isinstance(score_cat.score_trackers, SpriteList)


def test_add_box_added_to_boxes():
    """Test that when we add boxes, they are added to the boxes list"""
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(0, 0))
    score_cat.add_box(Coords(0, 0))
    assert len(score_cat.boxes) == 1
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(0, 0))
    score_cat.add_box(Coords(0, 0))
    score_cat.add_box(Coords(10, 0))
    assert len(score_cat.boxes) == 2


def test_add_box_added_to_subsprites():
    """Test that when we add boxes, they are added to the subsprite list"""
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(0, 0))
    score_cat.add_box(Coords(0, 0))
    assert len(score_cat.sub_sprites) == 1
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(0, 0))
    score_cat.add_box(Coords(0, 0))
    score_cat.add_box(Coords(10, 0))
    assert len(score_cat.sub_sprites) == 2


def test_add_box_boxes_matches_subsprites():
    """Test that the box added to the sub_sprite list is the same as the one added to the box"""
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(0, 0))
    score_cat.add_box(Coords(0, 0))
    assert score_cat.boxes[-1] is score_cat.sub_sprites[-1]
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(0, 0))
    score_cat.add_box(Coords(0, 0))
    score_cat.add_box(Coords(10, 0))
    assert score_cat.boxes[0] is score_cat.sub_sprites[0]
    assert score_cat.boxes[1] is score_cat.sub_sprites[1]


def test_add_box_position_x():
    """Test that when a box is added, its new position is calculated correctly (x)"""
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(0, 0))
    score_cat.add_box(Coords(0, 0))
    assert score_cat.boxes[0].center_x == 0
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(100, 50))
    score_cat.add_box(Coords(50, 10))
    assert score_cat.boxes[0].center_x == 150


def test_add_box_position_y():
    """Test that when a box is added, its new position is calculated correctly (y)"""
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(0, 0))
    score_cat.add_box(Coords(0, 0))
    assert score_cat.boxes[0].center_y == 0
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(100, 50))
    score_cat.add_box(Coords(20, 10))
    assert score_cat.boxes[0].center_y == 60


def test_add_box_text_default():
    """Test that when a box is added, by default it is given no text"""
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(0, 0))
    score_cat.add_box(Coords(0, 0))
    assert score_cat.boxes[0].text == ""


def test_add_box_text_set():
    """Test that when a box is added, the specified text is set correctly"""
    score_cat = ScoreCategory("images/GreenCategoryBox.png", Coords(0, 0))
    score_cat.add_box(Coords(0, 0), "Test")
    assert score_cat.boxes[0].text == "Test"
