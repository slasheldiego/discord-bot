"""Punto de entrada del bot. Ejecutar con: python -m src.bot"""
import logging
from pathlib import Path

import discord
from discord.ext import commands

from src import config

COGS_DIR = Path(__file__).parent / "cogs"

log = logging.getLogger("bot")


class Bot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True  # Necesario para leer mensajes y comandos con prefijo
        super().__init__(command_prefix=config.PREFIX, intents=intents)

    async def setup_hook(self) -> None:
        # Carga todos los cogs de src/cogs
        for file in sorted(COGS_DIR.glob("*.py")):
            if file.stem.startswith("_"):
                continue
            await self.load_extension(f"src.cogs.{file.stem}")
            log.info("Cog cargado: %s", file.stem)

        # Registra los slash commands en Discord
        if config.GUILD_ID:
            guild = discord.Object(id=config.GUILD_ID)
            self.tree.copy_global_to(guild=guild)
            synced = await self.tree.sync(guild=guild)
            log.info("%d comando(s) sincronizados en el servidor %s", len(synced), config.GUILD_ID)
        else:
            synced = await self.tree.sync()
            log.info("%d comando(s) sincronizados globalmente (puede tardar hasta 1 h)", len(synced))

    async def on_ready(self) -> None:
        log.info("Conectado como %s (ID: %s)", self.user, self.user.id)


def main() -> None:
    discord.utils.setup_logging(level=logging.INFO)
    Bot().run(config.TOKEN, log_handler=None)


if __name__ == "__main__":
    main()
