
from enum import Enum

class InvetoryItemCallbackManager:
    def __init__(self):
        pass
    def on_modify(self):
        pass
    def on_add(self):
        pass
    def on_remove(self):
        pass


class Callbacks(Enum):
    BASICS = InvetoryItemCallbackManager