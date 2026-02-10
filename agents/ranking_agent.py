def rank_hotels(search_results: list):
    ranked = []

    for r in search_results:
        score = 0
        text = (r["title"] + " " + r["snippet"]).lower()

        if "budget" in text or "affordable" in text:
            score += 2
        if "4" in text or "excellent" in text or "great reviews" in text:
            score += 2
        if "hotel" in text:
            score += 1

        ranked.append({
            "name": r["title"],
            "url": r["url"],
            "score": score,
            "snippet": r["snippet"]
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked[:3]
