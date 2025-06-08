"""Persistence helpers for saving and loading game state."""

from __future__ import annotations

import json
from pathlib import Path

from .character import Character, InventoryItem, Stats


def save_character(character: Character, path: str | Path) -> None:
    """Save a :class:`Character` to ``path`` in JSON format."""
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(character.to_dict(), fh, indent=2)


def load_character(path: str | Path) -> Character:
    """Load a :class:`Character` from a JSON file."""
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    char = Character(
        name=data.get("name", "Hero"),
        race=data.get("race", "Human"),
        char_class=data.get("class", "Fighter"),
        level=data.get("level", 1),
    )

    stats_data = data.get("stats", {})
    char.stats = Stats(**{k: int(v) for k, v in stats_data.items()})

    inv_items = data.get("inventory", {}).get("items", [])
    for item in inv_items:
        char.add_item(
            InventoryItem(
                name=item.get("name", ""),
                quantity=int(item.get("quantity", 1)),
                description=item.get("description", ""),
            )
        )
    return char


__all__ = ["save_character", "load_character"]
