import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import streamlit as st

os.environ["OPENAI_API_KEY"] = api_key 

symptoms_memory = ConversationBufferMemory(input_key='symptoms', memory_key='chat_history')
medications_memory = ConversationBufferMemory(input_key='condition', memory_key='medication_history')

llm = OpenAI(temperature=0.8)

symptoms_prompt = PromptTemplate(
    input_variables=['symptoms'],
    template="List 2 possible conditions for these symptoms: {symptoms}. Summarize."
)

symptoms_chain = LLMChain(
    llm=llm, prompt=symptoms_prompt, verbose=True, output_key='condition', memory=symptoms_memory
)

medications_prompt = PromptTemplate(
    input_variables=['condition'],
    template="Provide 2 first aid medications for {condition}. Summarize."
)

medications_chain = LLMChain(
    llm=llm, prompt=medications_prompt, verbose=True, output_key='medications', memory=medications_memory
)




