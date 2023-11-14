from .base_item import BaseItem
from .aidoc import AIDoc
from .image_generator import ImGen

from enum import Enum

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