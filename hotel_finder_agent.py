from langchain_community.llms import Ollama
from duckduckgo_search import DDGS

# -------------------------
# 1. Initialize LLM (Ollama)
# -------------------------
llm = Ollama(
    model="mistral",
    temperature=0.2
)

# -------------------------
# 2. Hotel search function
# -------------------------
def hotel_search(query: str, max_results: int = 5):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title"),
                "url": r.get("href"),
                "snippet": r.get("body")
            })
    return results

# -------------------------
# 3. Agent logic (explicit)
# -------------------------
def hotel_finder_agent(user_query: str):
    search_results = hotel_search(user_query)

    prompt = f"""
You are a hotel recommendation agent.

Return ONLY valid JSON.
No markdown. No explanation outside JSON.

Schema:
{{
  "hotels": [
    {{
      "name": "string",
      "reason": "string",
      "source_url": "string"
    }}
  ]
}}

Rules:
- Exactly 3 hotels
- Budget under $150 per night
- Prefer good reviews

User request:
{user_query}

Search results:
{search_results}
"""

    return llm.invoke(prompt)


# -------------------------
# 4. Run
# -------------------------
if __name__ == "__main__":
    query = "Find budget hotels in Pune under $150 per night with good reviews"
    response = hotel_finder_agent(query)
    print(response)
