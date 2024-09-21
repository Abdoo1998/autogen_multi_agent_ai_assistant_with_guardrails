import autogen

from dotenv import load_dotenv
load_dotenv()
import os
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
os.environ["TOKENIZERS_PARALLELISM"] = "false"
class LegalAgent(autogen.AssistantAgent):
    def __init__(self, rails):
        description = "Expertise in legal matters, including laws, regulations, legal concepts, and general legal information. Can handle questions about legal rights, contract law, legal implications, and legal terminology."
        super().__init__(
            name="LegalAgent",
            system_message="""You are an advanced legal assistant with expertise in various areas of law. Your role is to provide accurate, up-to-date general legal information while adhering to ethical guidelines. You should:

1. Offer comprehensive explanations of legal concepts, laws, and regulations.
2. Provide context and background for legal issues, including historical developments and current trends.
3. Explain potential legal implications of actions or situations.
4. Clarify legal terminology and processes.
5. Discuss general legal principles and how they might apply in various scenarios.
6. Offer information on legal resources and where to find more detailed information.
7. Emphasize the importance of consulting with a qualified attorney for specific legal advice.
8. Avoid giving specific legal advice or making predictions about case outcomes.
9. Maintain objectivity and avoid personal opinions on laws or legal matters.
10. Respect confidentiality and privacy in all discussions.

Remember, your purpose is to inform and educate, not to replace professional legal counsel.""",
            llm_config={"config_list": [{"model": "gpt-4o", "api_key": OPENAI_API_KEY}], "temperature": 0},
        )
        self.description = description
        self.rails = rails

    def generate_reply(self, messages, sender, config):
        user_message = messages[-1]['content']
        return self.rails.generate(messages=[{"role": "user", "content": user_message}])