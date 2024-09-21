import autogen
from utils.llm_utils import get_llm

class Orchestrator(autogen.AssistantAgent):
    def __init__(self):
        super().__init__(
            name="Orchestrator",
            system_message="""You are an intelligent orchestrator designed to analyze user queries and determine whether they are primarily legal, financial, or general in nature. Your role is crucial in directing users to the most appropriate specialized agent. When evaluating queries:

1. Carefully analyze the core subject matter of the query.
2. Identify key terms or concepts that indicate a legal, financial, or general knowledge focus.
3. Consider the context and potential implications of the query.
4. If a query contains multiple elements, determine which aspect is more prominent or central to the user's question.
5. Be prepared to route general knowledge questions to the General Knowledge Agent.
6. In cases of ambiguity, consider which specialized agent would be best equipped to provide the most relevant and helpful information.
7. Be prepared to ask for clarification if the nature of the query is unclear.

Your goal is to ensure that users receive the most accurate and relevant information by connecting them with the appropriate specialized agent.""",
            llm_config={"config_list": [{"model": "gpt-4o", "api_key": "YOUR_API_KEY"}], "temperature": 0},
        )

    def generate_reply(self, messages, sender, config):
        user_message = messages[-1]['content']
        llm = get_llm()
        prompt = f"""Analyze the following query and determine whether it is primarily legal, financial, or general in nature:

Query: {user_message}

Consider the following agent descriptions:

1. Legal Agent: Expertise in legal matters, including laws, regulations, legal concepts, and general legal information.
2. Financial Agent: Expertise in financial matters, including economics, investments, budgeting, and financial planning.
3. General Knowledge Agent: Broad expertise in various fields including science, history, culture, technology, and current events.

Based on these descriptions and the query, determine which agent would be best suited to answer the question.

Respond with either 'legal', 'financial', or 'general', followed by a brief explanation of your reasoning."""
        
        response = llm.invoke([{"role": "user", "content": prompt}])
        classification = response.content.strip().lower().split()[0]
        return classification