from pathlib import Path

import discord

from aibot import Config , AI, CallbackManager, DiscordClient

# Main settings loaded
config = Config.from_yaml()
callbacks = CallbackManager()
inventory_directory = Path(__file__).parent / config.INVETORY_PATH

# Discord Client Intents
intents = discord.Intents.default()
intents.message_content = True

# Instance the Client and the AI
client = DiscordClient(intents=intents, guild_id=config.DISCORD_GUILD_ID, callback_manager=callbacks)
ai = AI(config=config, inventory_dir=inventory_directory, callback_manager=callbacks)

# Run the Client
client.run(config.DISCORD_BOT_TOKEN)