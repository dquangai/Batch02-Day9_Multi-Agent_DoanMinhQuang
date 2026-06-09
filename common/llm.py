"""Shared LLM factory for all agents.

Uses OpenRouter as an OpenAI-compatible API, so any provider's model
can be selected via the OPENROUTER_MODEL env var.
"""

import os

from langchain_openai import ChatOpenAI

RESPONSE_LANGUAGE_INSTRUCTION = (
    "IMPORTANT: Luôn trả lời bằng tiếng Việt. "
    "Viết rõ ràng, có cấu trúc, dễ hiểu với người dùng Việt Nam."
)


def get_llm() -> ChatOpenAI:
    """Return a ChatOpenAI client pointed at OpenRouter."""
    return ChatOpenAI(
        model=os.getenv("OPENROUTER_MODEL", "openai/gpt-3.5-turbo"),
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=float(os.getenv("OPENROUTER_TEMPERATURE", "0.3")),
        max_tokens=int(os.getenv("OPENROUTER_MAX_TOKENS", "512")),
    )