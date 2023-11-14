#######################################
##############
###
### This file
###     is slated for
###         completely deletaion and deprication
###
###
import inspect
from abc import ABC
from enum import Enum
from pathlib import Path
import datetime

from discord import app_commands ,ui, ButtonStyle, Interaction
from discord.app_commands.commands import Command

from aibot.callbacks import CallbackManager
from aibot.utils import create_embeddings_from_pdf, ContentTypes
from aibot.config import Config

class BaseItem(ABC):
    def __init__(self, item_path):
        if not item_path.is_dir():
            raise FileNotFoundError(f"The directory '{item_path.name}' does not exist! 'Item cannot be created!!")
        self.name = item_path.name
        self.description = "MUST INHERIT"
        self._callbacks = CallbackManager()
        self._path = item_path

    def __repr__(self):
        return f"<Item name='{self.name}' description='{self.description}'>"

    @property
    def describe(self):
        print(f"ITEM( {self.name} )")
        print(f"    description: {self.description}")
        print(f"    callbacks: {self.callbacks}")
        print(f"    path: {self.path}")

    @property
    def path(self):
        return self._path

    @property
    def callbacks(self):
        return self._callbacks

    @callbacks.setter
    def callbacks(self, value):
        if value is not None:
            self._callbacks = value

    @property
    def command(self):
        raise NotImplementedError("'Item.command' has not implemented the 'interact' method!")

    @property
    def methods(self):
        methods = inspect.getmembers(type(self), predicate=inspect.isfunction)
        return [name for name, _ in methods if not name.startswith("__")]

    def attach_command(self, add_command):
        add_command(self.interact)

    async def interact(self, message):
        raise NotImplementedError("'{self.name}' has not implemented the 'interact' method!")

    def validate_members(self):
        members = [self.name, self.description, self.callbacks, self.path]
        for member in members:
            if member is None:
                return False
        return True

class AIDoc(BaseItem):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.description: str = "Document loader for chatting with documents"
        self.prompt_template = """Use the following pieces of context to answer the question at the end.
            If you don't know the answer, just say that you don't know, don't try to
            make up an answer.

            {context}

            Question: {query}
            Helpful Answer:
        """
        self.config = Config.from_yaml(self.path / "config.yaml")
        self.embeddings = []
        self.incomings = []

    @property
    def command(self):
        com = app_commands.commands.Command(name="aidoc", description="Upload / Query the AI docuement loader", callback=self.interact)
        return com

    @property
    def embeddings_directory(self):
        embeddings_directory = self.path / self.config.EMBEDDINGS_DIRECTORY
        if not embeddings_directory.is_dir():
            embeddings_directory.mkdir(parents=False)
        return embeddings_directory
    @property
    def source_directory(self):
        source_directory = self.path / self.config.SOURCEFILES_DIRECTORY
        if not source_directory.is_dir():
            source_directory.mkdir(parents=False)
        return source_directory

    async def save_attachement(self, attachment):
        filepath = self.source_directory / attachment.filename
        await attachment.save(filepath)
        #self.create_embeddings(filepath)

    async def on_message(self, message, *args, **kwargs):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.content_type == ContentTypes.PDF.value:
                    await self.save_attachement(attachment)
                    await message.reply(f"`{attachment.filename}` saved under AI Document Loader!")

    #def query_documents(self, query):
    #    qa_chain = RetrievalQA.from_chain_type(llm="test", retriever= vectordb.as_retriever(search_kwargs={'k': 7}), return_source_documents=True)
    #    result = qa_chain({'query': 'Who is the CV about?'})
    #    print(result['result'])

    def load_embeddings(self, doc_loader=None):
        pass

    def create_embeddings(self, source_document):
        relitive_to_source = str(source_document).split(self.source_directory.name)[1]
        self.d = relitive_to_source
        embedding_path = self.embeddings_directory / source_document.name.split(".")[0]
        embeddings = create_embeddings_from_pdf(source_document, self.embeddings_directory / source_document.name)
        self.embeddings.append(embeddings)

    async def interact(self, interaction):
        self.incomings.append(interaction)
        await interaction.response.send_message(content="AI Document Loader Interaction", view=AIDocButtons(interaction.user,self))
        #try:
        #    await interaction.response.send_message("this is a second test")
        #except:
        #    await interaction.followup.send("Uh oh!")
        #    await interaction.followup.send("Spegetti Ohs!")

class AIDocButtons(ui.View):

    def __init__(self, author, aidoc):
        super().__init__()
        self.author = author
        self.aidoc = aidoc

    @ui.button(label='Create Embeddings', style=ButtonStyle.blurple)
    async def create_embeddings(self, interaction: Interaction, button: ui.Button):
        pass

    @ui.button(label='Load Vector Store', style=ButtonStyle.blurple)
    async def load_store(self, interaction: Interaction, button: ui.Button):
        pass

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

class Items(Enum):
    """ Items Enum is the single refernce point for items that can be in the inventory

    """
    AI_DOCUMENT_LOADER  = AIDoc
    IMAGE_GENERATOR     = ImGen

def get_item(item_string_identifier):
    for item in Items:
        if item.name == item_string_identifier:
            return item.value
        else:
            return None
    raise ValueError("Invalid class string")

def get_item_identifier(item_type):
    for item in Items:
        if item_type is item.value:
            return item.name
    return