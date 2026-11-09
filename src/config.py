"""Carga y valida la configuración desde el archivo .env."""
import os
import sys

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID") or None
PREFIX = os.getenv("COMMAND_PREFIX", "!")

if not TOKEN:
    sys.exit("Falta DISCORD_TOKEN. Revisa tu archivo .env")

if GUILD_ID is not None:
    GUILD_ID = int(GUILD_ID)
