def stability_score(explanations):
    base = explanations[0]
    similarity = sum(
        1 for e in explanations if e == base
    ) / len(explanations)

    return round(similarity, 2)
