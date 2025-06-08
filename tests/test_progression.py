import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine import Character


def test_gain_experience_level_up():
    hero = Character(name="Hero")
    leveled = hero.gain_experience(150)
    assert hero.level == 2
    assert hero.experience == 50
    assert leveled
