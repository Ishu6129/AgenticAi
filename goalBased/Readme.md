<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Goal-Based Job Application Assistant</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
            margin: 40px;
            background-color: #ffffff;
            color: #222;
        }
        h1, h2, h3 {
            color: #1f2937;
        }
        code, pre {
            background-color: #f4f4f4;
            padding: 6px;
            border-radius: 4px;
            display: block;
            overflow-x: auto;
        }
        ul {
            margin-left: 20px;
        }
        .section {
            margin-bottom: 40px;
        }
    </style>
</head>
<body>

<h1>Goal-Based Job Application Assistant</h1>

<p>
This project demonstrates a <strong>goal-based conversational AI assistant</strong> that collects
a user's <strong>name, email, and skills</strong> through natural conversation.
The system is designed with strict state control to avoid repetition, hallucination,
or infinite questioning.
</p>

<div class="section">
    <h2>Core Concept</h2>
    <p>
        The assistant follows a <strong>goal-based architecture</strong>:
    </p>
    <ul>
        <li>The application controls the goal state.</li>
        <li>The LLM is used only for understanding and extraction.</li>
        <li>Once a field is collected, it is treated as immutable.</li>
        <li>The assistant asks only for missing information.</li>
    </ul>
    <p>
        This mirrors how production AI systems are built and avoids common agent-loop issues.
    </p>
</div>

<div class="section">
    <h2>Project Structure</h2>
    <ul>
        <li><strong>Streamlit UI Version</strong> – User-facing web application using Gemini API</li>
        <li><strong>CLI Prototype (Gemini API)</strong> – Initial console-based implementation</li>
        <li><strong>Local Ollama Version</strong> – Offline implementation using local LLM</li>
    </ul>
</div>

<div class="section">
    <h2>1. Streamlit UI (Gemini API)</h2>
    <p>
        This is the main production-style interface.
    </p>
    <ul>
        <li>Built using Streamlit</li>
        <li>User enters Gemini API key via secure popup</li>
        <li>Chat-based interaction</li>
        <li>Goal-based flow control</li>
        <li>No repeated questions</li>
        <li>State preserved across messages</li>
    </ul>
    <p>
        The UI clearly displays both user and assistant messages and shows
        a structured summary once the application is complete.
    </p>
</div>

<div class="section">
    <h2>2. CLI Prototype (Gemini API)</h2>
    <p>
        This version was created to understand the core logic before adding a UI.
    </p>
    <ul>
        <li>Runs entirely in the terminal</li>
        <li>Uses LangChain with Gemini API</li>
        <li>Demonstrates memory and tool usage</li>
        <li>Stops automatically once the goal is reached</li>
    </ul>
    <p>
        This file serves as a learning and debugging reference.
    </p>
</div>

<div class="section">
    <h2>3. Local Ollama Version</h2>
    <p>
        This version removes all external API dependencies.
    </p>
    <ul>
        <li>Uses Ollama with a local model (example: phi3)</li>
        <li>No internet required</li>
        <li>Same goal-based logic</li>
        <li>Suitable for privacy-sensitive environments</li>
    </ul>
</div>

<div class="section">
    <h2>Technologies Used</h2>
    <ul>
        <li>Python</li>
        <li>Streamlit</li>
        <li>LangChain</li>
        <li>Google Gemini API</li>
        <li>Ollama (local LLM)</li>
        <li>Regular Expressions for controlled extraction</li>
    </ul>
</div>

<div class="section">
    <h2>Dependencies</h2>
    <pre>
langchain==0.2.14
langchain-core==0.2.33
langchain-google-genai==1.0.8
langchain-community
streamlit
python-dotenv
PyMuPDF
    </pre>
</div>

<div class="section">
    <h2>How to Run</h2>

    <h3>Streamlit UI</h3>
    <pre>
streamlit run app.py
    </pre>

    <h3>CLI Gemini Prototype</h3>
    <pre>
python gemini_cli.py
    </pre>

    <h3>Local Ollama Version</h3>
    <pre>
ollama run phi3
python ollama_cli.py
    </pre>
</div>

<div class="section">
    <h2>Key Design Takeaways</h2>
    <ul>
        <li>LLMs should not control application state</li>
        <li>Goals must be evaluated outside the agent</li>
        <li>Once extracted, data should not be revalidated</li>
        <li>Regex boundaries must handle real-world punctuation</li>
    </ul>
</div>

<div class="section">
    <h2>Use Cases</h2>
    <ul>
        <li>Job application intake bots</li>
        <li>HR screening assistants</li>
        <li>Form-free data collection</li>
        <li>Conversational onboarding systems</li>
    </ul>
</div>

<div class="section">
    <h2>Author</h2>
    <p>
        Developed as a practical exploration of goal-based AI agents
        using modern LLM tooling.
    </p>
</div>

</body>
</html>
