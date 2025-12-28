Sure! Here's the entire `README.md` content in one go:

````markdown
# Goal-Based Job Application Assistant

This project demonstrates a **goal-based conversational AI assistant** that collects a user's **name, email, and skills** through natural conversation. The system is designed with strict state control to avoid repetition, hallucination, or infinite questioning.

## Core Concept

The assistant follows a **goal-based architecture**:
- The application controls the goal state.
- The LLM is used only for understanding and extraction.
- Once a field is collected, it is treated as immutable.
- The assistant asks only for missing information.

This mirrors how production AI systems are built and avoids common agent-loop issues.

## Project Structure

- **Streamlit UI Version** – User-facing web application using Gemini API
- **CLI Prototype (Gemini API)** – Initial console-based implementation
- **Local Ollama Version** – Offline implementation using a local LLM

## 1. Streamlit UI (Gemini API)

This is the main production-style interface.

- Built using Streamlit
- User enters Gemini API key via secure popup
- Chat-based interaction
- Goal-based flow control
- No repeated questions
- State preserved across messages

The UI clearly displays both user and assistant messages and shows a structured summary once the application is complete.

## 2. CLI Prototype (Gemini API)

This version was created to understand the core logic before adding a UI.

- Runs entirely in the terminal
- Uses LangChain with Gemini API
- Demonstrates memory and tool usage
- Stops automatically once the goal is reached

This file serves as a learning and debugging reference.

## 3. Local Ollama Version

This version removes all external API dependencies.

- Uses Ollama with a local model (e.g., phi3)
- No internet required
- Same goal-based logic
- Suitable for privacy-sensitive environments

## Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini API
- Ollama (local LLM)
- Regular Expressions for controlled extraction

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

## Key Design Takeaways

* LLMs should not control application state
* Goals must be evaluated outside the agent
* Once extracted, data should not be revalidated
* Regex boundaries must handle real-world punctuation

## Use Cases

* Job application intake bots
* HR screening assistants
* Form-free data collection
* Conversational onboarding systems

## Author

Developed as a practical exploration of goal-based AI agents using modern LLM tooling.

```

This is a complete `README.md` formatted in one block. Let me know if you need any further adjustments!
```
