import inspect
from abc import ABC
from enum import Enum
from pathlib import Path

class BaseItem(ABC):
    def __init__(self):
        self.name = "MUST INHERIT"
        self.description = "MUST INHERIT"
        self._callbacks = None
        self._path = None

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
     
    @path.setter 
    def path(self, value):
        self._path = Path(value)
        if not self._path.is_dir() and self._path.parent.is_dir():
            self._path.mkdir()

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
        self.name: str = "aidoc"
        self.description: str = "Document loader for chatting with documents"

    async def interact(self, message):
        if message.attachments:

            for attachment in message.attachments:
                await attachment.save(self.path/attachment.filename)
            await message.reply("All attachments saved!")

        else:

            await message.reply("No attachments provided!")

        return

    def doc_loader_method(self, doc_loader=None):
      pass

class Personality(BaseItem):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name: str = "Personality"
        self.description: str = "Personalityof the AI is stored here"

    def personality(self, filesystem=None):
      pass



class Items(Enum):
    AI_DOCUMENT_LOADER  = AIDoc
    PERSONAITY          = Personality

def get_item(item_string_identifier):
    for item in Items:
        if item.name == item_string_identifier:
            return item.value
        else:
            return None
    raise ValueError("Invalid class string")