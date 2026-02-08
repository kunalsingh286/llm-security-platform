from backend.app.security.scanner import RuleScanner


class SecurityManager:

    def __init__(self):
        self.scanner = RuleScanner()

    def validate_prompt(self, prompt: str) -> None:

        if not self.scanner.scan_prompt(prompt):
            raise ValueError("Prompt blocked by security rules")

    def validate_output(self, output: str) -> None:

        if not self.scanner.scan_output(output):
            raise ValueError("Output blocked by security rules")
