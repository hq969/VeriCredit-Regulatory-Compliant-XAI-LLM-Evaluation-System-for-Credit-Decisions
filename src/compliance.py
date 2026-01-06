PROHIBITED_TERMS = [
    "gender", "male", "female",
    "race", "religion", "caste"
]

def compliance_check(text):
    violations = [t for t in PROHIBITED_TERMS if t in text.lower()]
    return 1 if violations else 0
