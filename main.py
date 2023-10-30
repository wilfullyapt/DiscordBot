import discord

from aibot import Config , AI, CallbackManager, DiscordClient
from aibot.items import Items
from pathlib import Path

config = Config.from_yaml()

intents = discord.Intents.default()
intents.message_content = True
client = DiscordClient(intents=intents, guild_id=config.DISCORD_GUILD_ID)

callbacks = CallbackManager()
callbacks.register_callback("add_command", client.add_command)


inventory_directory = Path(__file__).parent / config.INVETORY_PATH

ai = AI(config=config, inventory_dir=inventory_directory, callback_manager=callbacks)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

TS_FLAG = 1
RUN_FLAG = 1

# Current Troubleshooting Setup   
if (False, True)[TS_FLAG]:
    f = list(ai.inventory['aidoc'].path.glob('*'))
    z = ai.inventory['aidoc']
    q = ai.inventory['aidoc'].create_embeddings_file
    a = ai.inventory['aidoc'].source_directory / "bitcoin.pdf"

if (False, True)[RUN_FLAG]:
    client.run(config.DISCORD_BOT_TOKEN)
else:
    print(" -> Client Run disabled!")

e = ai.inventory['aidoc'].incomings[0].interaction

# See testing.py for other work


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
 [ ] Visualize the embeddings, maybe a manifest.json file or config.ymal file
 [ ] Load embedding based on the `manifest.json` file or `config.yaml` file
 [ ] Query embeddings
 [ ] Confirm all functionality through Discord Bot
 [ ] Squash Merge and Push

"""