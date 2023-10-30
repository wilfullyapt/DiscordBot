import json
from pathlib import Path

from .items import BaseItem, get_item, get_item_identifier
from .callbacks import CallbackManager
from .utils import write_default_manifest

class Inventory:
    def __init__(self, root_dir, llm, callback_manager=None, verbose=True):
        self.root_dir = Path(root_dir)
        self.manifest_filepath = self.root_dir / "manifest.json"
        self._llm = llm
        if callback_manager is None:
            callback_manager = CallbackManager()
        self.callback_manager = callback_manager
        self.verbose = verbose
        self.items = {}

        if not self.manifest_filepath.is_file():
            write_default_manifest(self.manifest_filepath)

        self.load_manifest(self.manifest_filepath)
    
    def __getitem__(self, key):
        return self.items.get(key)

    def __setitem__(self, key, value):
        self.items[key] = value

    def get(self, key: str, default_return=None):
        if key not in self.items.keys():
            return default_return
        return self[key]

    @property
    def item_names(self):
        return list(self.items.keys())

    @property
    def describe(self):
        for key, value in self.items.items():
            print(f" {key}: {value}")

    @property
    def llm(self):
        return self._llm

    def add(self, item) -> None:
        if not isinstance(item, BaseItem):
            raise TypeError(f"Expected 'item' to be an instance of {BaseItem.__name__}")
        item.callbacks = self.callback_manager

        self.items[item.name] = item
        self.callback_manager.invoke_callbacks("add_command", item.command)

        self.save_manifest()

    def save_manifest(self) -> None:
        manifest = { name: get_item_identifier(type(item)) for name, item in self.items.items() }
        with open(self.manifest_filepath, 'w') as f:
            json.dump(manifest, f)

    def load_manifest(self, manifest_filepath):
        try:
            with open(manifest_filepath) as file:
                items = json.load(file)

            load_items = { name: get_item(value) for name, value in items.items() }
            
            for name, item in load_items.items():
                self.add(item(manifest_filepath.parent / name))

            if self.verbose:
                print(f"Manifest loaded successfully from {manifest_filepath}")
        
        except IOError as e:
            print(f"Error loading manifest: {e}")