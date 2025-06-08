import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine import Character, attack


def test_attack_damage():
    attacker = Character(name="Attacker")
    defender = Character(name="Defender", stats=attacker.stats.__class__(health=10))
    result = attack(attacker, defender, damage_die="1d4")
    # After attack, defender health should not be greater than starting health
    assert result["defender_health"] <= 10
    assert result["defender_health"] >= 0
