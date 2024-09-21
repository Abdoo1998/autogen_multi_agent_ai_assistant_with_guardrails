import os
import streamlit as st
from datetime import datetime
import json
from agents import LegalAgent, FinancialAgent, GeneralKnowledgeAgent, Orchestrator
from utils import get_llm
from configs import initialize_rails
import nest_asyncio

nest_asyncio.apply()

# Set page config at the top of the script
st.set_page_config(page_title="AutoGen Multi-Agent AI Assistant With guardrails ", page_icon="🤖", layout="wide")

# Initialize components
llm = get_llm()
rails = initialize_rails(llm)

# Initialize agents
legal_agent = LegalAgent(rails["legal"])
financial_agent = FinancialAgent(rails["financial"])
general_knowledge_agent = GeneralKnowledgeAgent(rails["general"])
orchestrator = Orchestrator()

# Streamlit app
st.title("🤖 EXLNemoGDemoBot")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.header("Chat with Your AI Assistant")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    if message["role"] == "assistant" and "agent" in message:
        st.caption(f"Responded by: {message['agent']} Agent")

# Accept user input
if prompt := st.chat_input("What would you like to ask?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Determine the appropriate agent
                agent_type = orchestrator.generate_reply([{"role": "user", "content": prompt}], None, None)

                # Get response from the appropriate agent
                if agent_type == "legal":
                    agent_name = "Legal"
                    assistant_response = legal_agent.generate_reply([{"role": "user", "content": prompt}], None, None)
                elif agent_type == "financial":
                    agent_name = "Financial"
                    assistant_response = financial_agent.generate_reply([{"role": "user", "content": prompt}], None, None)
                elif agent_type == "general":
                    agent_name = "General Knowledge"
                    assistant_response = general_knowledge_agent.generate_reply([{"role": "user", "content": prompt}], None, None)
                else:
                    agent_name = "Orchestrator"
                    assistant_response = "I'm not sure how to categorize this question. Could you please provide more context or rephrase it?"

                # Extract the content, handling both string and dictionary responses
                if isinstance(assistant_response, dict):
                    response_text = assistant_response.get('content', 'Sorry, no response found.')
                else:
                    response_text = assistant_response

                st.markdown(response_text)
                st.caption(f"Responded by: {agent_name} Agent")

                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response_text, "agent": agent_name})

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Add a download button for the conversation
if st.button("Download Conversation"):
    conversation = json.dumps(st.session_state.messages, indent=2)
    st.download_button(
        label="Download JSON",
        data=conversation,
        file_name=f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
        mime="application/json"
    )

if st.button("Reset Conversation", type="secondary"):
    st.session_state.messages = []
    st.rerun()

# Sidebar content
st.sidebar.title("About the AI Assistant")
st.sidebar.info(
    "This AI Assistant uses multiple specialized agents to provide information on various topics. "
    "The Orchestrator determines which agent is best suited to answer your question:\n\n"
    "🏛️ **Legal Agent**: For questions about laws, regulations, and legal concepts.\n"
    "💰 **Financial Agent**: For questions about finance, economics, and money management.\n"
    "🌐 **General Knowledge Agent**: For a wide range of topics not specific to law or finance."
)

st.sidebar.title("How to Use")
st.sidebar.info(
    "1. Type your question in the chat input box.\n"
    "2. The AI will automatically route your question to the most appropriate agent.\n"
    "3. Read the response, which will include which agent provided the information.\n"
    "4. Continue the conversation or ask new questions as needed.\n"
    "5. Use the 'Download Conversation' button to save your chat history.\n"
    "6. Click 'Reset Conversation' to start over."
)

# Footer
st.sidebar.markdown("---")
st.sidebar.info(
    "⚠️ **Disclaimer**: This AI Assistant provides general information only. "
    "It should not be considered as professional legal, financial, or expert advice. "
    "Always consult with qualified professionals for specific advice."
)