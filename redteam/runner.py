import json
import datetime

from redteam.attacks.generator import AttackGenerator
from redteam.client import GatewayClient
from redteam.scorer import RedTeamScorer


class RedTeamRunner:

    def __init__(self):

        self.generator = AttackGenerator()
        self.client = GatewayClient()
        self.scorer = RedTeamScorer()

    def run(self, n=20):

        attacks = self.generator.generate(n)

        results = []

        for attack in attacks:

            res = self.client.send(attack["prompt"])

            results.append({
                "id": attack["id"],
                "type": attack["type"],
                "prompt": attack["prompt"],
                "status": res["status"],
                "response": res["response"]
            })

        score = self.scorer.score(results)

        report = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "summary": score,
            "results": results
        }

        filename = f"redteam/reports/report_{int(datetime.datetime.utcnow().timestamp())}.json"

        with open(filename, "w") as f:
            json.dump(report, f, indent=2)

        return filename, report


if __name__ == "__main__":

    runner = RedTeamRunner()

    file, report = runner.run()

    print("Red Team Report Saved:", file)
    print("Defense Score:", report["summary"]["defense_score"], "%")
