from backend.app.dlp.scanner import DLPScanner
from backend.app.dlp.redactor import Redactor


class DLPManager:

    def __init__(self):

        self.scanner = DLPScanner()
        self.redactor = Redactor()

    def process(self, text: str) -> tuple:

        findings = self.scanner.scan(text)

        if findings:

            redacted = self.redactor.redact(text)

            return {
                "violations": findings,
                "redacted": True,
                "output": redacted
            }

        return {
            "violations": {},
            "redacted": False,
            "output": text
        }
