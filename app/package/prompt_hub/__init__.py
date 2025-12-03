from pathlib import Path

class PromptHub:
    base_dir = Path(__file__).parent

    @staticmethod
    def bro_andy():
        return (PromptHub.base_dir / "bro-andy.md").read_text(encoding='utf-8')

    @staticmethod
    def intent_classifier():
        return (PromptHub.base_dir / "intent_classifier.md").read_text(encoding='utf-8')