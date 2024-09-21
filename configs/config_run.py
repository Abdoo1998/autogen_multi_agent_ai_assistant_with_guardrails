import os
from nemoguardrails import LLMRails, RailsConfig
from dotenv import load_dotenv
load_dotenv()

def initialize_rails(llm):
    """
    Initialize the LLMRails objects for legal, financial, and general knowledge agents.
    """
    legal_config=RailsConfig.from_path("./configs/legal")
    financial_config=RailsConfig.from_path("./configs/financial")
    general_config=RailsConfig.from_path("./configs/general")
    return {
        "legal": LLMRails(legal_config, llm=llm),
        "financial": LLMRails(financial_config, llm=llm),
        "general": LLMRails(general_config, llm=llm)
    }
