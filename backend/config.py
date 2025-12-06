"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers
# COUNCIL_MODELS = [
#     "openai/gpt-5.1",
#     "google/gemini-3-pro-preview",
#     "anthropic/claude-sonnet-4.5",
#     "x-ai/grok-4",
# ]
COUNCIL_MODELS = [
    "amazon/nova-2-lite-v1:free",
    "mistralai/mistral-7b-instruct:free",
    "google/gemini-2.0-flash-exp:free",
    "google/gemma-3-27b-it:free",
    "kwaipilot/kat-coder-pro:free",
    "tngtech/tng-r1t-chimera:free",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "google/gemini-2.0-flash-exp:free"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
