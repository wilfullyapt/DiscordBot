from dataclasses import dataclass


@dataclass
class Interaction:

    def __init__(self, interaction):
        self.user = interaction.user
        self.message = interaction.message
        self.response = interaction.response
        self.server = interaction.server
        self.interaction = interaction
        
    @classmethod
    def from_context(cls, context):
        return cls(context)

    @classmethod
    def from_message(cls, message):
        return cls(message)