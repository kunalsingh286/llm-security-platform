import requests
import json


class OllamaClient:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url

    def generate(self, model: str, prompt: str) -> str:
        url = f"{self.base_url}/api/generate"

        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(url, json=payload, timeout=300)
            response.raise_for_status()

            data = response.json()
            return data.get("response", "")

        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Ollama request failed: {str(e)}")
