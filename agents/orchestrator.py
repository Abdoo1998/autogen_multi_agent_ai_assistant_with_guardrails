import autogen
from utils.llm_utils import get_llm

class Orchestrator(autogen.AssistantAgent):
    def __init__(self):
        super().__init__(
            name="Orchestrator",
            system_message="""You are an advanced orchestrator responsible for analyzing user queries and determining if they are primarily legal, financial, or general in nature. Your primary role is to route users to the most suitable specialized agent.
            Your goal is to ensure users receive relevant information by directing them to the correct specialized agent. When uncertain, carefully consider the query's main focus and context before making a decision. If the query spans multiple domains, prioritize the most dominant aspect.""",
            llm_config={"config_list": [{"model": "gpt-4", "api_key": "YOUR_API_KEY"}], "temperature": 0},
        )

    def generate_reply(self, messages, sender, config):
        user_message = messages[-1]['content']
        llm = get_llm()
        prompt = f"""Analyze the following query and determine whether it is primarily legal, financial, or general in nature:

Query: {user_message}

Consider the following detailed agent descriptions:

1. Legal Agent: 
   Expertise in a wide range of legal matters, including but not limited to:
   - Constitutional, criminal, civil, corporate, and international law
   - Legal rights and responsibilities
   - Contract law and interpretation
   - Intellectual property rights
   - Employment and labor laws
   - Real estate and property laws
   - Family law and divorce proceedings
   - Immigration law
   - Environmental regulations
   - Legal procedures and court processes
   - Legal terminology and concepts
   - Historical legal precedents and their implications
   Can handle questions about legal implications, rights, obligations, and provide general legal information.

2. Financial Agent: 
   A comprehensive finance expert with deep knowledge in:
   - Economics (micro and macro)
   - Investments and portfolio management
   - Personal and corporate finance
   - Budgeting and financial planning
   - Banking systems and operations
   - Credit and loans (personal, mortgage, business)
   - Tax planning and implications
   - Insurance (life, health, property)
   - Retirement planning and pensions
   - Financial markets and instruments
   - Cryptocurrencies and blockchain technology
   - International finance and forex
   - Financial regulations and compliance
   - Accounting principles and financial statements analysis
   Capable of answering questions on market trends, economic indicators, and money management strategies. Provides clear, objective advice on complex financial concepts while emphasizing confidentiality and professional standards.

3. General Knowledge Agent: 
   Broad expertise across various subjects including but not limited to:
   - Science (physics, chemistry, biology, astronomy)
   - History and archaeology
   - Culture and anthropology
   - Technology and computer science
   - Current events and geopolitics
   - Arts and literature
   - Philosophy and ethics
   - Psychology and cognitive sciences
   - Environmental studies and sustainability
   - Health and medicine (non-professional advice)
   - Education and learning theories
   - Sports and recreation
   - Geography and world cultures
   Can handle a wide range of questions that don't specifically fall under legal or financial categories.

Based on these descriptions and the query, determine which agent would be best suited to answer the question. If the query spans multiple domains, prioritize the most dominant aspect. If you are truly uncertain, choose the General Knowledge Agent as the fallback option.

Respond with 'legal', 'financial', or 'general', followed by a brief explanation of your reasoning."""

        response = llm.invoke([{"role": "user", "content": prompt}])
        classification = response.content.strip().lower().split('\n')[0]
        
        # Extract the first word as the classification
        classification = classification.split()[0]
        
        # Fallback to General Agent if the classification is uncertain
        if classification not in ['legal', 'financial', 'general']:
            classification = 'general'
        
        return classification