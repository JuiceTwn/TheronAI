"""Simple turn-based combat utilities."""

from __future__ import annotations

from typing import Dict

from .character import Character
from .dice import roll_dice


def attack(attacker: Character, defender: Character, damage_die: str = "1d6") -> Dict[str, int | bool]:
    """Resolve an attack from ``attacker`` against ``defender``.

    Attack roll is ``1d20 + strength`` versus ``10 + dexterity``. On hit,
    damage is rolled using ``damage_die`` and subtracted from defender's health.
    """

    attack_roll = roll_dice("1d20") + attacker.stats.strength
    defense = 10 + defender.stats.dexterity
    hit = attack_roll >= defense
    damage = roll_dice(damage_die) if hit else 0
    if hit:
        defender.stats.modify(health=-damage)

    return {
        "hit": hit,
        "attack_roll": attack_roll,
        "defense": defense,
        "damage": damage,
        "defender_health": defender.stats.health,
    }


__all__ = ["attack"]
