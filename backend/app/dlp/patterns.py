import re


# Regular expressions for sensitive data

EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

PHONE_REGEX = re.compile(r"\b\d{10}\b")

CREDIT_CARD_REGEX = re.compile(r"\b(?:\d[ -]*?){13,16}\b")

API_KEY_REGEX = re.compile(r"(sk-[a-zA-Z0-9]{20,}|AIza[0-9A-Za-z\\-_]{35})")

IP_ADDRESS_REGEX = re.compile(
    r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
)

AADHAR_REGEX = re.compile(r"\b\d{4}\s?\d{4}\s?\d{4}\b")
