import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.memory import ConversationBufferMemory
import re

# Streamlit config
st.set_page_config(page_title="🎯 Job Application Assistant", layout="centered")

# API key handling
if "GOOGLE_API_KEY" not in st.session_state:
    st.session_state.GOOGLE_API_KEY = None

@st.dialog("🔐 Enter Gemini API Key")
def api_key_dialog():
    key = st.text_input("Gemini API Key", type="password")
    if st.button("Save Key"):
        if key.strip():
            st.session_state.GOOGLE_API_KEY = key.strip()
            st.rerun()
        else:
            st.error("API key cannot be empty")

if not st.session_state.GOOGLE_API_KEY:
    api_key_dialog()
    st.stop()

# Session state for application data
if "application_info" not in st.session_state:
    st.session_state.application_info = {
        "name": None,
        "email": None,
        "skills": None
    }

# Chat history for UI
if "chat_ui" not in st.session_state:
    st.session_state.chat_ui = []

# LangChain memory
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

# LLM initialization
llm = GoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=st.session_state.GOOGLE_API_KEY
)

# Tool to extract information
def extract_application_info(text: str) -> str:
    info = st.session_state.application_info

    if info["name"] is None:
        name_match = re.search(
            r"(?:my name is|i am|name is)\s+([A-Za-z ]+?)(?:[.,]|$)",
            text,
            re.IGNORECASE
        )
        if name_match:
            info["name"] = name_match.group(1).strip().title()

    if info["email"] is None:
        email_match = re.search(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)
        if email_match:
            info["email"] = email_match.group(0)

    if info["skills"] is None:
        skills_match = re.search(
            r"(?:skills are|i know|i can use|skills include)\s+(.+)",
            text,
            re.IGNORECASE
        )
        if skills_match:
            info["skills"] = skills_match.group(1).strip()

    return "Information processed."


# Register tools
tools = [
    Tool(
        name="extract_application_info",
        func=extract_application_info,
        description="Extract name, email, and skills from user input"
    )
]

# System prompt
SYSTEM_PROMPT = """
You are a job application assistant.
Extract information using tools.
Do not ask for information that is already collected.
Ask only for missing fields.
"""

# Agent initialization
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=st.session_state.memory,
    verbose=False,
    agent_kwargs={"system_message": SYSTEM_PROMPT}
)

# UI
st.title("🧠 Goal-Based Job Application Assistant")
st.markdown("Tell me your **name**, **email**, and **skills**.")

# Chat input
user_input = st.chat_input("Type here...")

if user_input:
    st.session_state.chat_ui.append(("user", user_input))

    with st.spinner("🤖 Thinking..."):
        agent.invoke({"input": user_input})

    info = st.session_state.application_info
    missing = [k for k, v in info.items() if not v]

    if not missing:
        bot_reply = (
            "🎉 **Application complete!**\n\n"
            f"- **Name:** {info['name']}\n"
            f"- **Email:** {info['email']}\n"
            f"- **Skills:** {info['skills']}"
        )
    else:
        bot_reply = f"⏳ Please tell me your **{missing[0]}**."


    st.session_state.chat_ui.append(("bot", bot_reply))

# Display chat
for sender, msg in st.session_state.chat_ui:
    if sender == "user":
        with st.chat_message("user"):
            st.markdown(msg)
    else:
        with st.chat_message("assistant"):
            st.markdown(msg)


# Reset without clearing API key
if st.button("🔄 Reset"):
    st.session_state.application_info = {
        "name": None,
        "email": None,
        "skills": None
    }
    st.session_state.chat_ui = []
    st.session_state.memory.clear()
    st.rerun()
