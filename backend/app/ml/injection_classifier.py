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
            "roleplay bypass",
            "system override",
            "normal request"
        ]

    def predict(self, text: str) -> dict:

        result = self.classifier(
            text,
            self.labels
        )

        return dict(
            zip(result["labels"], result["scores"])
        )

    def risk_score(self, text: str) -> float:

        scores = self.predict(text)

        return max(
            scores.get("prompt injection", 0),
            scores.get("jailbreak attempt", 0),
            scores.get("malicious instruction", 0),
            scores.get("roleplay bypass", 0),
            scores.get("system override", 0)
        )

    def is_malicious(self, text: str, threshold: float = 0.4) -> bool:

        return self.risk_score(text) >= threshold
