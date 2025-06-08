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
    experience: int = 0
    stats: Stats = field(default_factory=Stats)
    inventory: Inventory = field(default_factory=Inventory)

    def gain_experience(self, amount: int) -> bool:
        """Add experience and level up when thresholds are reached."""
        self.experience += int(amount)
        leveled = False
        while self.experience >= self.level * 100:
            self.experience -= self.level * 100
            self.level_up()
            leveled = True
        return leveled

    def level_up(self) -> None:
        """Increase level and improve basic stats."""
        self.level += 1
        self.stats.modify(health=5)

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
            "experience": self.experience,
            "stats": self.stats.to_dict(),
            "inventory": self.inventory.to_dict(),
        }
