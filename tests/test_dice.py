import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine.dice import roll_dice


def test_roll_dice_range():
    result = roll_dice("2d6")
    assert 2 <= result <= 12
