import requests
import os


class OllamaClient:

    def __init__(self):

        self.base_url = os.getenv(
            "OLLAMA_URL",
            "http://localhost:11434"
        )

        # Long timeout for large models
        self.timeout = int(
            os.getenv("OLLAMA_TIMEOUT", "300")
        )

    def generate(self, model: str, prompt: str) -> str:

        url = f"{self.base_url}/api/generate"

        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }

        try:

            response = requests.post(
                url,
                json=payload,
                timeout=self.timeout
            )

            response.raise_for_status()

            data = response.json()

            return data.get("response", "")

        except requests.exceptions.RequestException as e:

            raise RuntimeError(
                f"Ollama request failed: {str(e)}"
            )
