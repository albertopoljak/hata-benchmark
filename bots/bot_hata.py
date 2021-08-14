from time import perf_counter

import hata

from stats import Stats
from config import TOKEN


class HataStats(Stats):
    def library_info(self) -> str:
        return f"hata {hata.__version__}"

    def server_count(self) -> int:
        return len(self.client.guilds)

    def total_users(self) -> int:
        return len(hata.USERS)


hata_client = hata.Client(TOKEN, intents=hata.IntentFlag(0).update_by_keys(guilds=True, guild_users=True, guild_messages=True, guild_reactions=True))
stats = HataStats(hata_client)
now = perf_counter()


@hata_client.events
async def message_create(client, message):
    if message.content == "hata pong":
        await client.message_create(message.channel, f"hata stats:\n{stats} shards {hata_client.shard_count}")


@hata_client.events
async def ready(client):
    print(f"{client:f} is connected, it took: {perf_counter()-now}")
    print(f"hata stats:\n{stats}")


def start():
    hata_client.start()
