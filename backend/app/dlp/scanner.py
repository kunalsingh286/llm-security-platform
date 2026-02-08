from backend.app.dlp import patterns


class DLPScanner:

    def scan(self, text: str) -> dict:

        findings = {}

        if patterns.EMAIL_REGEX.search(text):
            findings["email"] = True

        if patterns.PHONE_REGEX.search(text):
            findings["phone"] = True

        if patterns.CREDIT_CARD_REGEX.search(text):
            findings["credit_card"] = True

        if patterns.API_KEY_REGEX.search(text):
            findings["api_key"] = True

        if patterns.IP_ADDRESS_REGEX.search(text):
            findings["ip_address"] = True

        if patterns.AADHAR_REGEX.search(text):
            findings["aadhaar"] = True

        return findings
