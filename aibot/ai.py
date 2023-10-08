from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from pathlib import Path

from .inventory import Inventory


template = """Acting as a helpful assistant, how best can you respond in the most fulfilling way to the following prompt?
{prompt}
"""

class AI:

    def __init__(self, openai_api_key, discord_client, inventory_dir=None, callback_manager=None):
        self.llm = OpenAI(openai_api_key=openai_api_key, temperature=0)
        self.llm_chain = LLMChain(llm=self.llm, prompt=PromptTemplate(input_variables=['prompt'], template=template))
        self.incoming = []
        self.discord_client = discord_client

        if not Path(inventory_dir).is_dir():
            #inventory_dir = Path(__file__).parent.parent / "inventory" # For usage to assign a default inventory
            inventory_dir.mkdir(parents=True)

        self.inventory = Inventory(inventory_dir, callback_manager=callback_manager)

    async def interact(self,message):

        if message.author == self.discord_client.user:
            return

        self.incoming.append(message)

        if message.content.startswith('.'):

            command = message.content.split()[0][1:]

            if command not in self.inventory.item_names:
                await message.reply(f"Command({command}) does not comply.")
                return

            await self.inventory[command].interact(message)
            return

        else:
            await message.channel.send(self.llm_chain.run(message.content))