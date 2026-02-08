from backend.app.security.scanner import RuleScanner
from backend.app.security.policy_loader import PolicyLoader
from backend.app.ml.security_engine import MLSecurityEngine


class SecurityManager:

    def __init__(self):

        self.scanner = RuleScanner()
        self.policy_loader = PolicyLoader()
        self.ml_engine = MLSecurityEngine()

    def reload_policies(self):

        self.policy_loader.reload_if_changed()

    def validate_prompt(self, prompt: str) -> None:

        self.reload_policies()

        # Rule check
        rules = self.policy_loader.get_prompt_rules()

        if not self.scanner.scan(prompt, rules):
            raise ValueError("Prompt blocked by policy rules")

        # ML check
        analysis = self.ml_engine.analyze_prompt(prompt)

        if analysis["final_risk"]:
            raise ValueError("Prompt blocked by ML security engine")

    def validate_output(self, output: str) -> None:

        self.reload_policies()

        rules = self.policy_loader.get_output_rules()

        if not self.scanner.scan(output, rules):
            raise ValueError("Output blocked by policy rules")
