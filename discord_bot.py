"""Example Discord bot interface for the TheronAI engine."""

import os

import discord
from discord.ext import commands

from engine import Character, GameEngine, attack, roll_dice


def create_bot(token: str) -> commands.Bot:
    bot = commands.Bot(command_prefix="!")

    hero = Character(name="Hero")
    engine = GameEngine(hero)

    @bot.command()
    async def roll(ctx, notation: str):
        try:
            result = roll_dice(notation)
            await ctx.send(f"Rolled {notation}: {result}")
        except ValueError as exc:
            await ctx.send(str(exc))

    @bot.command()
    async def attack_cmd(ctx):
        goblin = Character(name="Goblin", stats=hero.stats.__class__(health=5))
        result = attack(hero, goblin)
        await ctx.send(f"Attack result: {result}")

    @bot.command()
    async def scene(ctx, *, prompt: str):
        try:
            response = engine.run_turn(prompt)
            await ctx.send(str(response))
        except Exception as exc:  # pragma: no cover - network call
            await ctx.send(f"Error: {exc}")

    return bot


if __name__ == "__main__":
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_BOT_TOKEN environment variable not set")
    create_bot(token).run(token)
