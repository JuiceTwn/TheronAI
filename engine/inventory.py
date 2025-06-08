"""Inventory system for the DND engine."""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class InventoryItem:
    """Represents a single item in an inventory."""

    name: str
    quantity: int = 1
    description: str = ""

    def to_dict(self) -> Dict[str, str]:
        """Return a JSON-serializable representation of this item."""
        return {
            "name": self.name,
            "quantity": self.quantity,
            "description": self.description,
        }


@dataclass
class Inventory:
    """Container for inventory items."""

    items: List[InventoryItem] = field(default_factory=list)

    def add_item(self, item: InventoryItem) -> None:
        self.items.append(item)

    def remove_item(self, item_name: str) -> None:
        self.items = [i for i in self.items if i.name != item_name]

    def to_dict(self) -> Dict[str, List[Dict[str, str]]]:
        return {"items": [item.to_dict() for item in self.items]}
