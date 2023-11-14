from abc import ABC
from aibot.callbacks import CallbackManager


class BaseItem(ABC):
    def __init__(self, item_path):
        if not item_path.is_dir():
            raise FileNotFoundError(f"The directory '{item_path.name}' does not exist! 'Item cannot be created!!")
        self.name = item_path.name
        self.description = "MUST INHERIT"
        self._callbacks = CallbackManager() # should depricate
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