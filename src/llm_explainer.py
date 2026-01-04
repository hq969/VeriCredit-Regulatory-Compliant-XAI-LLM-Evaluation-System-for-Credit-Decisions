from openai import OpenAI

client = OpenAI()

def generate_llm_explanation(features, decision):
    prompt = f"""
    Explain the loan decision below in neutral, compliant language.
    Do NOT mention protected attributes.
    Decision: {"Rejected" if decision == 0 else "Approved"}
    Features: {features}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content
