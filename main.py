import discord
from aibot import Config , AI

config = Config.from_yaml()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

ai = AI(config.OPENAI_API_KEY)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.'):
        response = ai.dot_command(message)
        await message.channel.send(response)
    else:
        response = ai.converse(message)
        await message.channel.send(response)

client.run(config.DISCORD_BOT_TOKEN)