from pathlib import Path

import discord

from aibot import Config , AI, CallbackManager, DiscordClient
from aibot.context import Context
from aibot.items import Items

config = Config.from_yaml()
callbacks = CallbackManager()
inventory_directory = Path(__file__).parent / config.INVETORY_PATH

intents = discord.Intents.default()
intents.message_content = True
client = DiscordClient(intents=intents, guild_id=config.DISCORD_GUILD_ID, callback_manager=callbacks)

ai = AI(config=config, inventory_dir=inventory_directory, callback_manager=callbacks)

TS_FLAG = 1
RUN_FLAG = 1

# Current Troubleshooting Setup   
if (False, True)[TS_FLAG]:
    z = ai.inventory['aidoc']

if (False, True)[RUN_FLAG]:
    client.run(config.DISCORD_BOT_TOKEN)
else:
    print(" -> Client Run disabled!")

"""

Use 'git diff' to see changes.

GOALS:

 [x] Formalize the filestructure for AIDoc, Enum -> config file (local or global)
 [x] File structure is now predicated upon config file
 [x] Item.path is provided by virture of the Invetory.manifest
 [x] q(a) now works to create embedding and append to z.embeddings list | WORKING = ai.inventory['aidoc'].create_embeddings_file( ai.inventory['aidoc'].source_directory / "bitcoin.pdf" )
 [x] Switch to discord slah commands
 [x] Dynamically add slash commands as the item is loaded tot he inventory
 [x] completely implement slash commands for `aidoc`
 [x] aidoc on_message method waits for .pdf files to be attached and saves them, responds with conformation
 [ ] /aidoc button interface to dictate interaction
    - Create embeddings / vector store      -> Choose source to embed
    - Load Vector store                     -> Choose Vector store to load
 [ ] Load embedding based on the `manifest.json` file or `config.yaml` file
 [ ] Query embeddings
    - `/aidoc query="What is the sound of one hand clapping?"
 [ ] Confirm all functionality through Discord Bot
    1. Upload a document
    2. create a vecor store from document
    3. query vector store
    4. load and query a differnent vector store
 [ ] Squash Merge and Push

"""