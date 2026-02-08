from backend.app.dlp import patterns


class Redactor:

    def redact(self, text: str) -> str:

        text = patterns.EMAIL_REGEX.sub("[REDACTED_EMAIL]", text)

        text = patterns.PHONE_REGEX.sub("[REDACTED_PHONE]", text)

        text = patterns.CREDIT_CARD_REGEX.sub("[REDACTED_CARD]", text)

        text = patterns.API_KEY_REGEX.sub("[REDACTED_KEY]", text)

        text = patterns.IP_ADDRESS_REGEX.sub("[REDACTED_IP]", text)

        text = patterns.AADHAR_REGEX.sub("[REDACTED_AADHAAR]", text)

        return text
