from agents.search_agent import search_hotels
from agents.ranking_agent import rank_hotels
from agents.presenter_agent import present_hotels

def main():
    user_query = "Find budget hotels in Hinjewadi under $150 per night with good reviews"

    search_results = search_hotels(user_query)
    top_hotels = rank_hotels(search_results)
    response = present_hotels(user_query, top_hotels)

    print("\nFINAL RECOMMENDATIONS:\n")
    print(response)

if __name__ == "__main__":
    main()
