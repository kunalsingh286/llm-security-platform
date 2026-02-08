import json
import random


class AttackGenerator:

    def __init__(self, path="redteam/attacks/base_attacks.json"):

        with open(path, "r") as f:
            self.attacks = json.load(f)

    def generate(self, n: int = 10):

        results = []

        for _ in range(n):

            attack = random.choice(self.attacks)

            results.append({
                "id": attack["id"],
                "type": attack["type"],
                "prompt": attack["prompt"]
            })

        return results
