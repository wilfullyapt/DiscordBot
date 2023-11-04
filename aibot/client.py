import discord
from discord import app_commands

class DiscordClient(discord.Client):

    def __init__(self, *, intents: discord.Intents, guild_id, callback_manager):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.guild = discord.Object(id=guild_id)
        self.callbacks = callback_manager
        self.callbacks.register_callback("inventory.add_command", self.add_command)

    def add_command(self, command):
        self.tree.add_command(command)
        return

    async def sync_tree(self):
        await self.tree.sync(guild=self.guild)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=self.guild)
        await self.tree.sync(guild=self.guild)

    async def on_message(self, message):
        if "client.on_message" in self.callbacks:
            await self.callbacks.async_invoke_callbacks("client.on_message", message)

    async def on_ready(self):
        print(f' -::> Successful login as {self.user}!\n\n')