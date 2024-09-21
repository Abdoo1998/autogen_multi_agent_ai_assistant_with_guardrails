# AutoGen Multi-Agent AI Assistant with Guardrails 🤖

## Overview

This project is a **multi-agent AI assistant** designed to handle queries in three key domains: **Legal, Financial**, and **General Knowledge**. The system leverages the **AutoGen** library to orchestrate responses from specialized agents. Each agent is guided by **Guardrails** to ensure responses are safe, policy-compliant, and aligned with ethical standards. The application uses **Streamlit** for the frontend interface.

## Key Features

- **Multi-Agent Architecture**: The assistant is powered by domain-specific agents:
  - 🏛️ **Legal Agent**: Handles queries related to laws, regulations, and legal matters.
  - 💰 **Financial Agent**: Provides financial advice and handles queries about money management, investments, and economics.
  - 🌐 **General Knowledge Agent**: Handles a broad range of topics outside legal and financial domains.
  
- **Guardrails Integration**: Ensures safe and compliant interactions by blocking inappropriate or harmful requests and responses.
  
- **Orchestrator**: Routes user queries to the most relevant agent based on the input.
  
- **Streamlit Interface**: A simple, user-friendly interface to interact with the AI assistant, download conversation logs, and reset the chat session.

## Technology Stack

- **Python 3.x**
- **Streamlit**: Web framework for the frontend interface.
- **AutoGen Library**: Used for building the multi-agent architecture.
- **NemoGuardrails**: Provides safety and compliance guardrails for agent responses.
- **LLMs (Large Language Models)**: Used to generate intelligent and contextual responses in each domain.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/autogen_multi_agent_ai_assistant.git
cd autogen_multi_agent_ai_assistant


### 2. Install Required Libraries
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

## Project Structure
```bash
├── agents/
│   ├── legal_agent.py  # Handles legal queries
│   ├── financial_agent.py  # Handles financial queries
│   ├── general_knowledge_agent.py  # Handles general knowledge queries
│   └── orchestrator.py  # Orchestrates between the agents
├── configs/
│   ├── legal/  # Guardrails configuration for the legal agent
│   ├── financial/  # Guardrails configuration for the financial agent
│   └── general/  # Guardrails configuration for the general knowledge agent
├── utils.py  # Utility functions including LLM initialization
├── main.py  # Main Streamlit app
├── requirements.txt  # List of dependencies
└── README.md  # This file
```
# How to Use

	1.	Type your question in the chat input box.
	2.	The AI will automatically route your question to the most appropriate agent.
	3.	Read the response, which will include which agent provided the information.
	4.	Continue the conversation or ask new questions as needed.
	5.	Use the “Download Conversation” button to save your chat history.
	6.	Click “Reset Conversation” to start over.

# Download and Reset Functionality

	•	Download Conversation: You can download the entire chat history as a JSON file.
	•	Reset Conversation: Clears the chat history and starts a new conversation.

# Disclaimer

 ⚠️ Disclaimer: This AI Assistant provides general information only. It should not be considered as professional legal, financial, or expert advice. Always consult with qualified professionals for specific advice
