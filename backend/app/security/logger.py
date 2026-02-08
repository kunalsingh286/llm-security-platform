import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename="security.log"
)


class SecurityLogger:

    @staticmethod
    def log_violation(source: str, message: str):

        logging.warning(f"[{source}] {message}")
