import datetime
import typing

import discord

__all__ = ["healthcheck"]

T = typing.TypeVar("T", bound=discord.Client)


@discord.app_commands.command(  # type: ignore[arg-type]
    name="healthcheck",
    description="Check if the bot is working",
    auto_locale_strings=False,
)
async def healthcheck(
    interaction: discord.Interaction[T],
) -> None:
    response = typing.cast(
        discord.InteractionResponse[T],
        interaction.response,
    )

    await response.send_message(
        content="I'm okay, just call **9-1-1**!",
        ephemeral=True,
        delete_after=datetime.timedelta(minutes=1).seconds,
    )
