import discord
from aibot import Config , AI, BaseCallbackManager
from aibot.items import Items
from pathlib import Path

config = Config.from_yaml()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

ai = AI(
    openai_api_key= config.OPENAI_API_KEY,
    discord_client=client,
    inventory_dir=Path(__file__).parent / 'inventory',
    callback_manager=BaseCallbackManager()
)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    await ai.interact(message)

# Current Troubleshooting Setup
if (True, False)[0]:
    f = list(ai.inventory['aidoc'].path.glob('*'))[0]
    q = ai.inventory['aidoc'].create_embeddings_file

client.run(config.DISCORD_BOT_TOKEN)