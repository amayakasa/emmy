import logging
import os

from emmy import client

token = os.getenv("EMMY_BOT_TOKEN")

if not token:
    raise RuntimeError("Specify the bot token!")

client.run(
    token=token,
    log_level=logging.INFO,
    reconnect=True,
)
