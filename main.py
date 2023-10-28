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
    f = list(ai.inventory['aidoc'].path.glob('*'))
    z = ai.inventory['aidoc']
    q = ai.inventory['aidoc'].create_embeddings_file
    a = ai.inventory['aidoc'].source_directory / "bitcoin.pdf"

if True:
    print(" Client Run disabled!")
else:
    client.run(config.DISCORD_BOT_TOKEN)


"""

Use 'git diff' to see changes.

GOALS:

 [x] Formalize the filestructure for AIDoc, Enum -> config file (local or global)
 [x] File structure is now predicated upon config file
 [x] Item.path is provided by virture of the Invetory.manifest
 [x] q(a) now works to create embedding and append to z.embeddings list | WORKING = ai.inventory['aidoc'].create_embeddings_file( ai.inventory['aidoc'].source_directory / "bitcoin.pdf" )
 [ ] Switch to discord slah commands
 [ ] Visualize the embeddings, maybe a manifest.json file or config.ymal file
 [ ] Load embedding based on the `manifest.json` file or `config.yaml` file
 [ ] Query embeddings
 [ ] Confirm all functionality through Discord Bot
 [ ] Squash Merge and Push

"""