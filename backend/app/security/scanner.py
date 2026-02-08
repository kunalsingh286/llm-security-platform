from backend.app.security.rules import PROMPT_BLOCKLIST, OUTPUT_BLOCKLIST


class RuleScanner:

    def scan_prompt(self, prompt: str) -> bool:
        """
        Returns True if prompt is safe
        """
        text = prompt.lower()

        for pattern in PROMPT_BLOCKLIST:
            if pattern in text:
                return False

        return True

    def scan_output(self, output: str) -> bool:
        """
        Returns True if output is safe
        """
        text = output.lower()

        for pattern in OUTPUT_BLOCKLIST:
            if pattern in text:
                return False

        return True
