import json
from pathlib import Path

from .items import AIDoc, get_item
from .utils import write_default_manifest

class Inventory:
    def __init__(self, root_dir, callback_manager=None, verbose=True):
        self.root_dir = Path(root_dir)
        self.manifest = self.root_dir / "manifest.json"
        self.callbacks = callback_manager
        self.verbose = verbose

        if not self.manifest.is_file():
            write_default_manifest(self.manifest)

        self.items = {}
        self.load_manifest(self.manifest)

        if not hasattr(self, "items"):
            raise Exception("ERROR")
    
    def __getitem__(self, key):
        return self.items.get(key)

    def __setitem__(self, key, value):
        self.items[key] = value

    @property
    def describe(self):
        for key, value in self.items.items():
            print(f" {key}: {value}")

    def add(self, item) -> None:
        #if not isinstance(item, Item): raise TypeError("Invalid item")     # uncomment to work on Exception handling
        item.callbacks = self.callbacks
        item.path = self.root_dir / item.name

        self.items[item.name] = item

    def get(self, key: str, default_return=None):
        if key not in self.items.keys():
            return default_return
        return self[key]

    def save(self) -> None:
        with open(self.manifest, 'w') as f:
            json.dump({key: {'name': item.name,
                             'quantity': item.quantity}
                       for key, item in self.items.items()}, f)

    def load_manifest(self, manifest_filepath):
        try:
            with open(manifest_filepath) as file:
                items = json.load(file)
                self.i = items

            load_items = [ get_item(value) for _, value in items.items() ]
            
            for item in load_items:
                self.add(item())

            if self.verbose:
                print(f"Manifest loaded successfully from {manifest_filepath}")
        
        except IOError as e:
            print(f"Error loading manifest: {e}")