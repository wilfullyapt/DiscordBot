from aibot.items.base_item import BaseItem

class ImGen(BaseItem):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.description: str = "Image Generator using AI"

    @property
    def command(self):
        com = app_commands.commands.Command(name="imgen", description="Create an image using AI", callback=self.interact)
        app_commands.commands._populate_description(com._params, { "prompt": "Input prompt for image generation" } )
        return com

    async def interact(self, interaction, prompt):
        self.incomings.append(interaction)
        await interaction.response.send_message("ImgGen has not been reated yet")