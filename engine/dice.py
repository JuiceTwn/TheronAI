"""Utility functions for rolling dice using standard DND notation."""

from __future__ import annotations

import random
import re

_DICE_RE = re.compile(r"(?P<num>\d*)d(?P<sides>\d+)(?P<bonus>[+-]\d+)?")


def roll_dice(notation: str) -> int:
    """Roll dice based on a notation string like ``'2d6+1'``.

    Parameters
    ----------
    notation:
        Dice notation in the form ``XdY`` or ``XdY+Z``.

    Returns
    -------
    int
        The result of the roll.
    """

    match = _DICE_RE.fullmatch(notation.replace(" ", ""))
    if not match:
        raise ValueError(f"Invalid dice notation: {notation}")

    num = int(match.group("num") or 1)
    sides = int(match.group("sides"))
    bonus = int(match.group("bonus") or 0)

    total = sum(random.randint(1, sides) for _ in range(num)) + bonus
    return total


__all__ = ["roll_dice"]
