# LangChain-Apps-Demo   
![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtCcKxc1zpF_tiC83xEnHC07fS_LqqknIJ-g&s)

This repository contains the following AI applications developed using Langchain components:

1. [Language Translator](https://github.com/Mike-kwaku/LangChain-Apps-Demo/tree/main/LanguageTranslator): This program translates "a message/text" from one language to another.
   
2. [Health Assitant]() : This AI powered health assistant provides relevant response to health-related questions. 
   
3. [Devops Assistant](https://github.com/Mike-kwaku/LangChain-Apps-Demo/tree/main/Devops%20Assistant): This AI powered assistant retrieves related response to Devops questions. 

## Quickstart to Langchain 

The following commands install `langchain` framework and `langchain-openai`. `langchain-openai` is an embedding model by OpenAI integrated into langchain. 

```
pip install langchain
pip install -qU langchain-openai
pip install "langserve[all]"
```

## Set Environmental Variables 

Setting `LANGCHAIN_TRACING_V2` starts logging traces.

```
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_API_KEY="insert_your_key_here"
export OPENAI_API_KEY="insert_your_key_here"
```

## Build a simple language translator with ChatOpenAI   

Copy and paste the following into a file.    

```
import getpass
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

model= ChatOpenAI(model="gpt-4")

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

model.invoke(messages)

parser = StrOutputParser()

result = model.invoke(messages)

parser.invoke(result)
```
