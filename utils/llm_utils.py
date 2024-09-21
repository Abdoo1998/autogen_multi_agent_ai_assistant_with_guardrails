import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from nemoguardrails import LLMRails, RailsConfig

load_dotenv()
OPENAPI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def get_llm():
    return ChatOpenAI(model="gpt-4o", api_key=OPENAPI_API_KEY)

def get_response(rails, user_input: str, agent_type: str) -> str:
    try:
        response = rails[agent_type].generate(messages=[{"role": "user", "content": user_input}])
        return response.bot_message
    except Exception as e:
        return f"Error generating response: {str(e)}"