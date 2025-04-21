import streamlit as st
import os
import string
import random
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.tools import StructuredTool
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# LangChain LLM
llm = ChatOpenAI(temperature=0, openai_api_key=openai_key)

# Password Strength Checker
def password_strength_checker(password: str) -> str:
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if strength == 4:
        return "Strong password 💪"
    elif strength == 3:
        return "Moderately strong password."
    elif strength == 2:
        return "Weak password."
    else:
        return "Very weak password. Consider improving it."

# Password Generator
def password_generator(length: int = 12, include_symbols: bool = True, include_numbers: bool = True, include_uppercase: bool = True) -> str:
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Define tools
tools = [
    Tool(
        name="password_strength_checker_tool",
        func=password_strength_checker,
        description="Check how secure a password is. Input should be a single string representing the password."
    ),
    StructuredTool.from_function(
        func=password_generator,
        name="password_generator_tool",
        description="Generate a strong password with optional length, symbols, numbers, and uppercase letters."
    )
]

# Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=False,
    agent_kwargs={
        "system_message": "You are a helpful assistant skilled in evaluating and generating secure passwords. Choose the right tool based on user intent."
    }
)

# Streamlit UI
st.set_page_config(page_title="🔐 Password Agent", layout="centered")
st.title("🔐 Password Assistant")

st.markdown("Ask anything related to passwords: check strength or generate one!")

query = st.text_input("💬 Your request", placeholder="e.g., Is 'password123' secure?")

if st.button("🔍 Run Agent"):
    if query:
        with st.spinner("Thinking..."):
            response = agent.run(query)
        st.success(response)
    else:
        st.warning("Please enter a request first.")
