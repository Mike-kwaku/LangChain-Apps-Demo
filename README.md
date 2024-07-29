# LangChain-Apps-Demo   
![alt text](https%3A%2F%2Fpython.langchain.com%2Fv0.2%2Fimg%2Fbrand%2Fwordmark.png&imgrefurl=https%3A%2F%2Fpython.langchain.com%2Fv0.2%2Fdocs%2Fintroduction%2F&docid=1DZgWlJxiFBvTM&tbnid=G6BjQMbxf0XAVM&vet=12ahUKEwj9w6r2xcyHAxWLUkEAHSmdJ8gQM3oECG0QAA..i&w=1586&h=251&hcb=2&ved=2ahUKEwj9w6r2xcyHAxWLUkEAHSmdJ8gQM3oECG0QAA)

This repository contains the following AI applications developed using Langchain components:

1. [Language Translator]()    :

## Quickstart to Langchain 

The following commands install `langchain` framework and `langchain-openai`. `langchain-openai` is an embedding model by OpenAI integrated into langchain. 

```
pip install langchain
pip install -qU langchain-openai
```

## Set Environmental Variables 

Setting `LANGCHAIN_TRACING_V2` starts logging traces.

```
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_API_KEY="..."
```

## Build a simple language translator with ChatOpenAI   

Copy and paste the following into a file.    

```
import getpass
import os

os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4")

messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

model.invoke(messages)

parser = StrOutputParser()

result = model.invoke(messages)

parser.invoke(result)
```
