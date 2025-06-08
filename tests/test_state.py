import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine import Character, save_character, load_character


def test_save_and_load(tmp_path):
    hero = Character(name="TestHero")
    path = tmp_path / "hero.json"
    save_character(hero, path)
    loaded = load_character(path)
    assert loaded.name == hero.name
