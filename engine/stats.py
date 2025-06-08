"""Character statistics and utilities."""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Stats:
    """Represents standard DND statistics."""

    strength: int = 10
    dexterity: int = 10
    constitution: int = 10
    intelligence: int = 10
    wisdom: int = 10
    charisma: int = 10
    health: int = 10

    def to_dict(self) -> Dict[str, int]:
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma,
            "health": self.health,
        }

    def modify(self, **kwargs: int) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, getattr(self, key) + int(value))
