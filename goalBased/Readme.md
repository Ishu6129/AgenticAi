# Goal-Based Job Application Assistant

This project demonstrates a **goal-based conversational AI assistant** that collects a user's **name, email, and skills** through natural conversation. The system is designed with strict state control to avoid repetition, hallucination, or infinite questioning.

Unlike prompt-driven agents, this system uses **external goal evaluation and immutable state**, reflecting how production-grade conversational systems are built.

---

## Live Demo

🚀 **Try the live Streamlit app here:**  
https://goalbased-apl-extr.streamlit.app/

---

## Core Concept

The assistant follows a **goal-based architecture**:

- The application controls the goal state
- The LLM is used only for understanding and extraction
- Once a field is collected, it is treated as immutable
- The assistant asks only for missing information

This approach prevents:
- Infinite questioning loops
- Hallucinated state changes
- Re-validation of already collected data

---

## Project Structure

- **Streamlit UI Version** – User-facing web application using Gemini API
- **CLI Prototype (Gemini API)** – Initial console-based implementation
- **Local Ollama Version** – Offline implementation using a local LLM

---

## 1. Streamlit UI (Gemini API)

This is the primary production-style interface.

- Built using Streamlit
- Gemini API key entered via secure input
- Chat-based conversational UI
- Goal-based flow control
- No repeated questions
- State preserved across messages

Once all required fields are collected, the UI displays a **structured summary** of the extracted data.

---

## 2. CLI Prototype (Gemini API)

This version was created to validate logic before adding a UI.

- Runs entirely in the terminal
- Uses LangChain with Gemini API
- Demonstrates controlled memory usage
- Automatically terminates when the goal is achieved

This version serves as a **learning and debugging reference**.

---

## 3. Local Ollama Version

This version removes all external API dependencies.

- Uses Ollama with a local model (e.g., `phi3`)
- Fully offline execution
- Same goal-based logic
- Suitable for privacy-sensitive or air-gapped environments

---

## Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini API
- Ollama (local LLM)
- Regular Expressions for controlled extraction

---

## Dependencies

```bash
langchain==0.2.14
langchain-core==0.2.33
langchain-google-genai==1.0.8
langchain-community
streamlit
python-dotenv
PyMuPDF
````

---

## How to Run

### Streamlit UI

```bash
streamlit run app.py
```

### CLI Gemini Prototype

```bash
python gemini_cli.py
```

### Local Ollama Version

```bash
ollama run phi3
python ollama_cli.py
```

---

## Key Design Takeaways

* LLMs should never control application state
* Goals must be evaluated outside the agent
* Extracted data should not be revalidated or mutated
* Regex boundaries must account for real-world punctuation

---

## Use Cases

* Job application intake bots
* HR screening assistants
* Form-free data collection
* Conversational onboarding systems

---

## Author

Developed as a practical exploration of **goal-based AI agents** using modern LLM tooling and production-oriented design principles.
