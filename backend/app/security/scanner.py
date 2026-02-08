class RuleScanner:

    def scan(self, text: str, rules: dict) -> bool:
        """
        Returns True if safe
        """

        if not rules.get("enabled", True):
            return True

        content = text.lower()

        blocklist = rules.get("blocklist", [])

        for pattern in blocklist:
            if pattern in content:
                return False

        return True
