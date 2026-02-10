from core.llm import get_llm

def present_hotels(user_query: str, hotels: list):
    llm = get_llm()

    prompt = f"""
You are a hotel recommendation assistant.

User request:
{user_query}

Selected hotels:
{hotels}

Explain briefly why each hotel is recommended.
"""

    return llm.invoke(prompt)
