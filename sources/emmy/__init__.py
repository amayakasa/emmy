import os

import discord
import wavelink

from .commands import healthcheck

__all__ = ["client"]

intents = discord.Intents.default()

client = discord.Client(intents=intents)

commands = discord.app_commands.CommandTree(
    client=client,
    fallback_to_global=True,
)
commands.add_command(healthcheck)


async def setup_wavelink(self: discord.Client) -> None:
    node = wavelink.Node(
        uri=os.getenv("LAVALINK_URI", "127.0.0.1:2333"),
        password=os.getenv("LAVALINK_PASSWORD", "youshallnotpass"),
    )
    await wavelink.NodePool.connect(client=self, nodes=[node])


client.setup_hook = setup_wavelink.__get__(  # type: ignore[method-assign]
    client,
    discord.Client,
)


@client.event
async def on_ready() -> None:
    await commands.sync()
