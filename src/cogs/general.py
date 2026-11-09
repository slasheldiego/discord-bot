"""Comandos generales del bot."""
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(description="Responde con Pong! y la latencia del bot")
    async def ping(self, ctx: commands.Context) -> None:
        """Funciona como /ping y como !ping."""
        await ctx.send(f"Pong! 🏓 Latencia: {round(self.bot.latency * 1000)} ms")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(General(bot))
