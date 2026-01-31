import os
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv()

# Get API key from environment or Streamlit secrets
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    try:
        import streamlit as st
        api_key = st.secrets.get("OPENAI_API_KEY")
    except:
        pass

llm = ChatOpenAI(api_key=api_key) if api_key else None

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    if llm is None:
        return {"messages": [BaseMessage(content="Error: OPENAI_API_KEY not configured", type="ai")]}
    response = llm.invoke(messages)
    return {"messages": [response]}

# Checkpointer
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)