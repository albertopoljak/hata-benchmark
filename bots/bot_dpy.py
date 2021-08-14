from time import perf_counter

import discord

from stats import Stats
from config import TOKEN


class DpyStats(Stats):
    def library_info(self) -> str:
        return f"discord.py {discord.__version__}"

    def server_count(self) -> int:
        return len(self.client.guilds)

    def total_users(self) -> int:
        return len(self.client._connection._users)  # noqa users creates an entire list ...


dpy_client = discord.Client(intents=discord.Intents(guilds=True, members=True, messages=True, reactions=True))
stats = DpyStats(dpy_client)
now = perf_counter()


@dpy_client.event
async def on_message(message):
    if message.content == "dpy ping":
        await message.reply(f"dpy stats:\n{stats}")


@dpy_client.event
async def on_ready():
    print(f"{dpy_client.user.name} is connected, it took: {perf_counter()-now}")
    print(f"dpy stats:\n{stats}")


def start():
    dpy_client.run(TOKEN)
