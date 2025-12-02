from .registry import agent

@agent("text_processor", "Processes and transforms text input")
def process_text(text: str) -> str:
    return f"Processed: {text.upper()}"

@agent("calculator", "Performs basic arithmetic operations")
def calculate(expression: str) -> float:
    try:
        return eval(expression)  # Note: Use safe evaluation in production
    except:
        return 0.0

@agent("summarizer", "Summarizes text content")
def summarize_text(text: str) -> str:
    words = text.split()
    if len(words) <= 10:
        return text
    return " ".join(words[:10]) + "..."