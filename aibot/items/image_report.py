from aibot.items.base_item import BaseItem

class ImRep(BaseItem):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.description: str = "Image Report Maker"

    @property
    def command(self):
        com = app_commands.commands.Command(name="imrep", description="Create an image report", callback=self.interact)
        return com

    async def interact(self, interaction, prompt):
        self.incomings.append(interaction)
        await interaction.response.send_message("ImRep has not been created yet")