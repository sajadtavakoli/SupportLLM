def build_prompt(message: str, category: str = "general") -> str:
    return f"""### Instruction:
Write a polite, concise, and helpful customer support response.

### Category:
{category}

### Customer message:
{message}

### Response:
"""
