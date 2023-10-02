from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import tool
from pydantic import BaseModel


template = """Acting as a helpful assistant, how best can you respond in a helpful way to the following prompt?
{prompt}
"""

class AI:

    def __init__(self, openai_api_key):
        self.llm = OpenAI(openai_api_key=openai_api_key, temperature=0)
        self.llm_chain = LLMChain(llm=self.llm, prompt=PromptTemplate(input_variables=['prompt'], template=template))
        self.dot_commands = []
        self.messages = []

    def dot_command(self, message):
        self.dot_commands.append(message)
        return "observation mode: Dot command preserved"

    def converse(self, message):
        self.messages.append(message)
        response = self.llm_chain.run(message.content)
        return response
