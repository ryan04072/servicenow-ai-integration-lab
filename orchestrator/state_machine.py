import json
from pathlib import Path

DEFAULT_LIFECYCLE = Path("config/lifecycle/lifecycle.json")

class Lifecycle:
    def __init__(self, path=DEFAULT_LIFECYCLE):
        self.path = Path(path)
        self.data = json.loads(self.path.read_text(encoding="utf-8"))

    def state(self, name):
        try:
            return self.data["states"][name]
        except KeyError as exc:
            raise ValueError(f"Unknown lifecycle state: {name}") from exc

    def can_transition(self, current, target):
        return target in self.state(current).get("next", [])

    def next_role(self, current):
        return self.state(current).get("role")

    def requires_human_gate(self, current):
        return bool(self.state(current).get("human_gate", False))
