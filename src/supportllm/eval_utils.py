REQUIRED_TONE_WORDS = ["sorry", "help", "please"]

def has_helpful_tone(text: str) -> bool:
    lower = text.lower()
    return any(word in lower for word in REQUIRED_TONE_WORDS)

def too_short(text: str, min_words: int = 12) -> bool:
    return len(text.split()) < min_words

def evaluate_response(text: str) -> dict:
    return {
        "helpful_tone": has_helpful_tone(text),
        "too_short": too_short(text),
        "word_count": len(text.split()),
    }
