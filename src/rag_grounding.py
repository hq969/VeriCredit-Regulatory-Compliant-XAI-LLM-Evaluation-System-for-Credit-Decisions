def grounding_score(llm_text, policy_text):
    matches = sum(
        1 for word in llm_text.lower().split()
        if word in policy_text.lower()
    )
    return round(matches / len(llm_text.split()), 2)
