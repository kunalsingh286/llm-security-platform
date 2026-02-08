from backend.app.ml.injection_classifier import InjectionClassifier
from backend.app.ml.llm_judge import LLMJudge
from backend.app.ml.intent_classifier import IntentClassifier


class MLSecurityEngine:

    def __init__(self):

        self.injector = InjectionClassifier()
        self.judge = LLMJudge()
        self.intent = IntentClassifier()

    def analyze_prompt(self, prompt: str) -> dict:

        risk_score = self.injector.risk_score(prompt)
        ml_flag = self.injector.is_malicious(prompt)

        llm_flag = self.judge.judge(prompt)

        safe_intent = self.intent.is_safe(prompt)

        # Weighted decision
        final_risk = False

        # High confidence attack
        if risk_score >= 0.6:
            final_risk = True

        # Judge + ML agree
        elif ml_flag and llm_flag:
            final_risk = True

        # Judge says risky and not safe intent
        elif llm_flag and not safe_intent:
            final_risk = True

        return {
            "risk_score": risk_score,
            "ml_flag": ml_flag,
            "llm_flag": llm_flag,
            "safe_intent": safe_intent,
            "final_risk": final_risk
        }
