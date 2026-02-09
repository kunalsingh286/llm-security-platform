import os

from backend.app.ml.injection_classifier import InjectionClassifier
from backend.app.ml.llm_judge import LLMJudge
from backend.app.ml.intent_classifier import IntentClassifier


class MLSecurityEngine:

    def __init__(self):

        self.enable_ml = os.getenv("ENABLE_ML", "true") == "true"

        self.injector = None
        self.intent = None

        if self.enable_ml:
            try:
                self.injector = InjectionClassifier()
                self.intent = IntentClassifier()
            except Exception:
                self.enable_ml = False

        self.judge = LLMJudge()

    def analyze_prompt(self, prompt: str) -> dict:

        risk_score = 0.0
        ml_flag = False
        safe_intent = True

        if self.enable_ml and self.injector and self.intent:

            try:
                risk_score = self.injector.risk_score(prompt)
                ml_flag = self.injector.is_malicious(prompt)
                safe_intent = self.intent.is_safe(prompt)

            except Exception:
                pass

        llm_flag = self.judge.judge(prompt)

        final_risk = False

        if risk_score >= 0.6:
            final_risk = True

        elif ml_flag and llm_flag:
            final_risk = True

        elif llm_flag and not safe_intent:
            final_risk = True

        return {
            "risk_score": risk_score,
            "ml_flag": ml_flag,
            "llm_flag": llm_flag,
            "safe_intent": safe_intent,
            "final_risk": final_risk
        }
