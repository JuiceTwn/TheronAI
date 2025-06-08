# TheronAI DND Engine

This repository contains a minimal skeleton for a ChatGPT-powered Dungeons & Dragons game engine written in Python. The project is intentionally light-weight and is meant as a starting point for further development.

## Features

- **Inventory system** – classes for items and managing player inventory
- **Stat tracker** – representation of common DND attributes
- **Character model** – combines stats and inventory
- **ChatGPT integration** – communicate with OpenAI's API and parse JSON replies
- **Dice rolling** – helper to roll dice with ``XdY`` notation
- **Game state persistence** – save and load characters from JSON
- **Basic combat** – simple attack resolution using dice rolls

## Usage

1. Install dependencies (mainly `openai`):
   ```bash
   pip install openai
   ```
2. Set your OpenAI API key when constructing `GameEngine` or via the `OPENAI_API_KEY` environment variable.
3. Run the example:
   ```bash
   python main.py
   ```
   The engine attempts to contact ChatGPT. Without an API key or network access it will fail gracefully.

## Saving and Loading Characters

Use ``save_character`` and ``load_character`` to persist your hero between sessions:

```python
from engine import save_character, load_character

save_character(hero, "hero.json")
reloaded = load_character("hero.json")
```

## Rolling Dice

The ``roll_dice`` helper parses standard notation:

```python
from engine import roll_dice
damage = roll_dice("2d6+1")
```

This is only a starting point; feel free to expand the mechanics, add combat logic, or build a full campaign framework on top of it.
