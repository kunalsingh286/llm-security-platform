import yaml
import os


class PolicyLoader:

    def __init__(self, policy_path: str = "policies/default.yaml"):
        self.policy_path = policy_path
        self._last_modified = None
        self.policy = None

        self.load()

    def load(self):

        if not os.path.exists(self.policy_path):
            raise FileNotFoundError("Policy file not found")

        with open(self.policy_path, "r") as f:
            self.policy = yaml.safe_load(f)

        self._last_modified = os.path.getmtime(self.policy_path)

    def reload_if_changed(self):

        current_mtime = os.path.getmtime(self.policy_path)

        if self._last_modified != current_mtime:
            self.load()

    def get_prompt_rules(self):

        return self.policy["security"]["prompt"]

    def get_output_rules(self):

        return self.policy["security"]["output"]

    def logging_enabled(self):

        return self.policy["logging"]["enabled"]
