import discord

from .commands import healthcheck

__all__ = ["client"]

intents = discord.Intents.default()

client = discord.Client(intents=intents)

commands = discord.app_commands.CommandTree(
    client=client,
    fallback_to_global=True,
)
commands.add_command(healthcheck)


@client.event
async def on_ready() -> None:
    await commands.sync()
