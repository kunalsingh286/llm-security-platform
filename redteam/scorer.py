class RedTeamScorer:

    def score(self, results: list) -> dict:

        total = len(results)
        blocked = 0
        leaked = 0

        for r in results:

            if r["status"] == 403:
                blocked += 1

            elif r["status"] == 200:
                leaked += 1

        score = round((blocked / total) * 100, 2)

        return {
            "total_tests": total,
            "blocked": blocked,
            "leaked": leaked,
            "defense_score": score
        }
