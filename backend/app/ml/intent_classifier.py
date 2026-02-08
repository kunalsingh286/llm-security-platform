from transformers import pipeline


class IntentClassifier:

    def __init__(self):

        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )

        self.labels = [
            "educational",
            "general knowledge",
            "harmless question",
            "malicious intent",
            "system bypass",
            "jailbreak"
        ]

    def is_safe(self, text: str, threshold: float = 0.6) -> bool:

        result = self.classifier(text, self.labels)

        scores = dict(
            zip(result["labels"], result["scores"])
        )

        safe_score = max(
            scores.get("educational", 0),
            scores.get("general knowledge", 0),
            scores.get("harmless question", 0)
        )

        return safe_score >= threshold
