"""Entry point for the TheronAI DND engine demo."""

from engine import Character, InventoryItem, GameEngine


def main() -> None:
    hero = Character(name="Theron")
    hero.add_item(InventoryItem(name="Sword", quantity=1, description="A sharp blade"))
    engine = GameEngine(hero)

    # Example prompt to start the game
    prompt = "The hero enters a dark dungeon. Respond with JSON describing the scene."
    try:
        response = engine.run_turn(prompt)
        print(response)
    except Exception as exc:  # noqa: BLE001
        print(f"Failed to contact ChatGPT: {exc}")


if __name__ == "__main__":
    main()
