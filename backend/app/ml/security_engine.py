from backend.app.ml.injection_classifier import InjectionClassifier
from backend.app.ml.llm_judge import LLMJudge


class MLSecurityEngine:

    def __init__(self):

        self.classifier = InjectionClassifier()
        self.judge = LLMJudge()

    def analyze_prompt(self, prompt: str) -> dict:

        ml_score = self.classifier.risk_score(prompt)
        ml_flag = self.classifier.is_malicious(prompt)

        llm_flag = self.judge.judge(prompt)

        # Voting logic
        votes = sum([
            1 if ml_flag else 0,
            1 if llm_flag else 0
        ])

        final_risk = votes >= 1   # Any one system can block

        return {
            "ml_score": ml_score,
            "ml_flag": ml_flag,
            "llm_flag": llm_flag,
            "votes": votes,
            "final_risk": final_risk
        }
