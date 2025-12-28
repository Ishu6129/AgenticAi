from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.memory import ConversationBufferMemory
import streamlit as st
import os
import re
import fitz  # PyMuPDF

# Initialize llm model
load_dotenv()
llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)


st.set_page_config(page_title="🎯 Job Application Agent", layout="centered")

if "application_info" not in st.session_state:
    st.session_state.application_info = {
        "name": None,
        "email": None,
        "skills": None
    }

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

if "chat_ui" not in st.session_state:
    st.session_state.chat_ui = []

def extract_application_info(text: str) -> str:
    info = st.session_state.application_info
    name = re.search(
        r"(?:my name is|i am)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)",
        text, re.I
    )
    email = re.search(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", text)
    skills = re.search(
        r"(?:skills are|i know|i can use)\s+(.+)",
        text, re.I
    )
    if name:
        info["name"] = name.group(1).title()
    if email:
        info["email"] = email.group(0)
    if skills:
        info["skills"] = skills.group(1).strip()
    return "Information extracted."

def check_application_goal(_: str) -> str:
    info = st.session_state.application_info
    missing = [k for k, v in info.items() if not v]

    if not missing:
        return (
            f"✅ Application complete!\n"
            f"Name: {info['name']}\n"
            f"Email: {info['email']}\n"
            f"Skills: {info['skills']}"
        )

    return f"⏳ Missing: {', '.join(missing)}. Ask user for this."


# Creating tools
tools = [
    Tool(
        name="extract_application_info",
        func=extract_application_info,
        description="Extract name, email, and skills from user message or resume text"
    ),
    Tool(
        name="check_application_goal",
        func=check_application_goal,
        description="Check whether all application fields are collected"
    )
]

# System Prompt
SYSTEM_PROMPT = """
You are a job application assistant.
Rules:
1. ALWAYS extract information using tools.
2. After extracting, ALWAYS check if the application is complete.
3. If something is missing, politely ask ONLY for missing fields.
4. If complete, confirm and stop.
Do not invent data.
"""

# Initialize Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=st.session_state.memory,
    verbose=False,
    agent_kwargs={"system_message": SYSTEM_PROMPT}
)


    
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "".join(page.get_text() for page in doc)
    
# Streamlit UI
st.title("🧠 Goal-Based Job Application Agent")
st.markdown("I will collect your **name**, **email**, and **skills**.")
    
# Resume
st.sidebar.header("📤 Upload Resume (Optional)")
resume = st.sidebar.file_uploader("Upload PDF resume", type=["pdf"])
if resume:
    resume_text = extract_text_from_pdf(resume)
    agent.invoke({"input": resume_text})
    st.sidebar.success("Resume processed by agent")

# User Input 
user_input = st.chat_input("Type here...")

if user_input:
    st.session_state.chat_ui.append(("user", user_input))
    with st.spinner("🤖 Thinking..."):
        response = agent.invoke({"input": user_input})
    st.session_state.chat_ui.append(("bot", response["output"]))



# Display Chat
for sender, msg in st.session_state.chat_ui:
    if sender == "user":
        with st.chat_message("user"):
            st.markdown(f"🧑 {msg}")
    else:
        with st.chat_message("assistant"):
            st.markdown(f"🤖 {msg}")


#Final Output
final_status = check_application_goal("check")
if final_status.startswith("✅"):
    st.success("🎉 Application Completed!")

    info = st.session_state.application_info
    summary = f"""
Name: {info['name']}
Email: {info['email']}
Skills: {info['skills']}
"""
    st.download_button(
        "📥 Download Application Summary",
        summary,
        "application_summary.txt"
    )
#Reset
if st.sidebar.button("🔄 Reset"):
    st.session_state.clear()
    st.rerun()