import discord
from aibot import Config , AI, InvetoryItemCallbackManager
from aibot.items import Personality
from pathlib import Path

config = Config.from_yaml()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

ai = AI(
    openai_api_key= config.OPENAI_API_KEY,
    discord_client=client,
    inventory_dir=Path(__file__).parent / 'inventory',
    callback_manager=InvetoryItemCallbackManager()
)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    await ai.interact(message)

client.run(config.DISCORD_BOT_TOKEN)


"""
AI should load itself from a manifest file upon instantiation
    [ ] filepath args must be bulletproof
    [x] write default manifest file if missing, then load

AI shouls automatically save itself when the inventory or item is changed
    [x] Callback should be loaded with the Invetory
    [x] Callbacks should be added to items when the item is added to the inventory
    [ ] Callback should be implemented into the events within the items

GOAL: AI should be able to download an attachement from discord

"""