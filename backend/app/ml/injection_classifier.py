from transformers import pipeline


class InjectionClassifier:

    def __init__(self):

        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )

        self.labels = [
            "prompt injection",
            "jailbreak attempt",
            "malicious instruction",
            "normal request"
        ]

    def predict(self, text: str) -> dict:

        result = self.classifier(
            text,
            self.labels
        )

        scores = dict(
            zip(result["labels"], result["scores"])
        )

        return scores

    def is_malicious(self, text: str, threshold: float = 0.6) -> bool:

        scores = self.predict(text)

        risk_score = max(
            scores.get("prompt injection", 0),
            scores.get("jailbreak attempt", 0),
            scores.get("malicious instruction", 0)
        )

        return risk_score >= threshold
