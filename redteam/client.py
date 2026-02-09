import requests


class GatewayClient:

    def __init__(self, url="http://127.0.0.1:8000/chat"):

        self.url = url

    def send(self, prompt: str, model="llama3"):

        payload = {
            "prompt": prompt,
            "model": model
        }

        try:

            res = requests.post(
                self.url,
                json=payload,
                timeout=120
            )

            return {
                "status": res.status_code,
                "response": res.text
            }

        except Exception as e:

            return {
                "status": 0,
                "response": str(e)
            }
