import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

class DiscordClient(discord.Client):

    def __init__(self, *, intents: discord.Intents, guild_id):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.guild = discord.Object(id=guild_id)

    @property
    def add_command(self):
        return self.tree.add_command

    async def sync_tree(self):
        await self.tree.sync(guild=self.guild)

    async def setup_hook(self):

        self.tree.copy_global_to(guild=self.guild)
        await self.tree.sync(guild=self.guild)

