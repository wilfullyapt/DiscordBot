from dataclasses import dataclass


@dataclass
class Context:

    def __init__(self, context):
        #self.user = interaction.user
        #self.message = interaction.message
        #self.response = interaction.response
#        self.server = interaction.server
        self.context = context
        
    @classmethod
    def from_interaction(cls, interaction):
        print(interaction)
        return cls(context=interaction)

    @classmethod
    def from_message(cls, message):
        print(message)
        return cls(context=message)