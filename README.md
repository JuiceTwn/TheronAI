# TheronAI DND Engine

This repository contains a minimal skeleton for a ChatGPT-powered Dungeons & Dragons game engine written in Python. The project is intentionally light-weight and is meant as a starting point for further development.

## Features

- **Inventory system** – classes for items and managing player inventory
- **Stat tracker** – representation of common DND attributes
- **Character model** – combines stats and inventory
- **ChatGPT integration** – communicate with OpenAI's API and parse JSON replies

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

This is only a starting point; feel free to expand the mechanics, add combat logic, or build a full campaign framework on top of it.
