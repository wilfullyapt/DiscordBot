import inspect
from abc import ABC
from enum import Enum
from pathlib import Path

from .callbacks import BaseCallbackManager
from aibot.utils import create_embeddings_from_pdf
from aibot.config import Config

class BaseItem(ABC):
    def __init__(self, item_path):
        if not item_path.is_dir():
            raise FileNotFoundError(f"The directory '{item_path.name}' does not exist! 'Item cannot be created!!")
        self.name = item_path.name
        self.description = "MUST INHERIT"
        self._callbacks = BaseCallbackManager()
        self._path = item_path

    def __repr__(self):
        return f"ITEM({self.name}) : {self.description}"

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
    def methods(self):
        methods = inspect.getmembers(type(self), predicate=inspect.isfunction)
        return [name for name, _ in methods if not name.startswith("__")]

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

    def create_embeddings_file(self, source_document):
        relitive_to_source = str(source_document).split(self.source_directory.name)[1]
        self.d = relitive_to_source
        embedding_path = self.embeddings_directory / source_document.name.split(".")[0]
        embeddings = create_embeddings_from_pdf(source_document, self.embeddings_directory / source_document.name)
        self.embeddings.append(embeddings)

    async def save_attachement(self, attachments):
        for attachment in message.attachments:
            filepath = self.source_directory() / attachment.filename
            await attachment.save(filepath)
            self.create_embeddings_file(filepath)

    #def query_documents(self, query):
    #    qa_chain = RetrievalQA.from_chain_type(llm="test", retriever= vectordb.as_retriever(search_kwargs={'k': 7}), return_source_documents=True)
    #    result = qa_chain({'query': 'Who is the CV about?'})
    #    print(result['result'])

    async def interact(self, message):
        if message.attachments:
            # If there are attachements, save and create embeddings for it
            await self.save_attachement(message.attachments)

        else:
            # TODO, implement question asking against embedding files
            await message.reply("No attachments provided!")

        return

    def doc_loader_method(self, doc_loader=None):
      pass

class Personality(BaseItem):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.description: str = "Personalityof the AI is stored here"

    def personality(self, filesystem=None):
      pass



class Items(Enum):
    """ Items Enum is the single refernce point for items that can be in the inventory

    """
    AI_DOCUMENT_LOADER  = AIDoc
    PERSONAITY          = Personality

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