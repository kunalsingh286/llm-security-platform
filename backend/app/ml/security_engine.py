from backend.app.ml.injection_classifier import InjectionClassifier
from backend.app.ml.llm_judge import LLMJudge


class MLSecurityEngine:

    def __init__(self):

        self.classifier = InjectionClassifier()
        self.judge = LLMJudge()

    def analyze_prompt(self, prompt: str) -> dict:

        ml_result = self.classifier.predict(prompt)
        is_ml_risky = self.classifier.is_malicious(prompt)

        llm_verdict = self.judge.judge(prompt)

        final_risk = is_ml_risky or llm_verdict

        return {
            "ml_scores": ml_result,
            "ml_flag": is_ml_risky,
            "llm_flag": llm_verdict,
            "final_risk": final_risk
        }
