from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from pydantic import BaseModel

from pathlib import Path

from .inventory import Inventory


template = """Acting as a helpful assistant, how best can you respond in a helpful way to the following prompt?
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

    async def ai_document_loader(self, message):
        if message.attachments:
            savepath = self.inventory.get("aidoc").path

            await message.attachments[0].save(savepath)
            await message.reply("attachment saved!")
                
        else:
            await message.reply("No attachments provided!")

    async def interact(self,message):

        if message.author == self.discord_client.user:
            return

        self.incoming.append(message)

        if message.content.startswith('.'):
            if message.content.lower() == ".aidoc":
                await self.ai_document_loader(message)
        else:
            await message.channel.send(self.llm_chain.run(message.content))