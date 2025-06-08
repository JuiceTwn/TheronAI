"""Entry point for the TheronAI DND engine demo."""

from engine import (
    Character,
    InventoryItem,
    GameEngine,
    roll_dice,
    save_character,
    load_character,
    attack,
)


def main() -> None:
    hero = Character(name="Theron")
    hero.add_item(InventoryItem(name="Sword", quantity=1, description="A sharp blade"))
    engine = GameEngine(hero)

    # Demonstrate dice rolling
    print(f"Rolling 2d6+1 for attack damage: {roll_dice('2d6+1')}")

    # Persist and reload the character
    save_character(hero, "hero.json")
    hero = load_character("hero.json")

    # Example combat round
    goblin = Character(name="Goblin", stats=hero.stats.__class__(health=5))
    result = attack(hero, goblin)
    print(f"Attack result: {result}")

    # Example prompt to start the game
    prompt = "The hero enters a dark dungeon. Respond with JSON describing the scene."
    try:
        response = engine.run_turn(prompt)
        print(response)
    except Exception as exc:  # noqa: BLE001
        print(f"Failed to contact ChatGPT: {exc}")


if __name__ == "__main__":
    main()
