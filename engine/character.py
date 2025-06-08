"""Character representation for the DND engine."""

from dataclasses import dataclass, field
from typing import Dict

from .inventory import Inventory, InventoryItem
from .stats import Stats


@dataclass
class Character:
    """Represents a player or NPC character."""

    name: str
    race: str = "Human"
    char_class: str = "Fighter"
    level: int = 1
    stats: Stats = field(default_factory=Stats)
    inventory: Inventory = field(default_factory=Inventory)

    def add_item(self, item: InventoryItem) -> None:
        self.inventory.add_item(item)

    def remove_item(self, item_name: str) -> None:
        self.inventory.remove_item(item_name)

    def to_dict(self) -> Dict[str, object]:
        return {
            "name": self.name,
            "race": self.race,
            "class": self.char_class,
            "level": self.level,
            "stats": self.stats.to_dict(),
            "inventory": self.inventory.to_dict(),
        }
