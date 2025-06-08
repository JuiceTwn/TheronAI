"""Core game engine that interacts with ChatGPT."""

import json
from typing import Any, Dict, List

try:
    import openai
except ImportError:  # pragma: no cover - openai might not be installed in all envs
    openai = None

from .character import Character


class GameEngine:
    """Simple game engine using ChatGPT for narrative generation."""

    def __init__(self, character: Character, openai_api_key: str = "") -> None:
        self.character = character
        self.api_key = openai_api_key
        if openai and self.api_key:
            openai.api_key = self.api_key

    def chat_with_gpt(self, messages: List[Dict[str, str]]) -> str:
        """Call the ChatGPT API with the provided messages."""
        if not openai:
            raise RuntimeError("openai package is required for API calls")
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        return response["choices"][0]["message"]["content"]

    def request_action(self, prompt: str) -> Dict[str, Any]:
        """Send a prompt to ChatGPT and expect a JSON response."""
        system = {"role": "system", "content": "You are a DND game master."}
        user = {"role": "user", "content": prompt}
        content = self.chat_with_gpt([system, user])
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON", "content": content}

    def run_turn(self, prompt: str) -> Dict[str, Any]:
        """Example method for running a single turn using ChatGPT."""
        action = self.request_action(prompt)
        return action
