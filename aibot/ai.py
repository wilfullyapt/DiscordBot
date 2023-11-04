from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from pathlib import Path

from .inventory import Inventory


template = """Acting as a helpful assistant, how best can you respond in the most fulfilling way to the following prompt?
{prompt}
"""

class AI:

    def __init__(self, config, inventory_dir=None, callback_manager=None):

        self._llm = OpenAI(openai_api_key=config.OPENAI_API_KEY, temperature=0)
        self.llm_chain = LLMChain(llm=self._llm, prompt=PromptTemplate(input_variables=['prompt'], template=template))

        self.incoming = []

        #self._llm = OpenAI(openai_api_key=openai_api_key, temperature=0)
        #self.llm_chain = LLMChain(llm=self._llm, prompt=PromptTemplate(input_variables=['prompt'], template=template))
        #self.incoming = []
        #self.discord_client = discord_client

        inventory_dir = Path(inventory_dir)

        if not inventory_dir.parent.is_dir():
            raise ValueError("Parent directory does not exist or is not a directory")

        if not inventory_dir.is_dir():
            try:
                inventory_dir.mkdir(parents=True)
            except OSError as e:
                raise ValueError(f"Failed to create the {inventory_dir} directory: {e}")

        self.inventory = Inventory(inventory_dir, callback_manager=callback_manager, llm=self.llm)

    @property
    def llm(self):
        return self._llm

    async def interact(self, message):

        if message.author == self.discord_client.user:
            return

        self.incoming.append(message)

        if message.content.startswith('.'):

            command = message.content.split()[0][1:]

            if command not in self.inventory.item_names:
                await message.reply(f"Command({command}) does not comply.")
                return

            await self.inventory[command].interact(message)

        else:
            await message.channel.send(self.llm_chain.run(message.content))

        return