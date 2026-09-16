import json
import shlex
import subprocess
from pathlib import Path

DEFAULT_CONFIG = Path("config/providers/providers.local.json")
EXAMPLE_CONFIG = Path("config/providers/providers.example.json")

def load_config():
    path = DEFAULT_CONFIG if DEFAULT_CONFIG.exists() else EXAMPLE_CONFIG
    return json.loads(path.read_text(encoding="utf-8"))

def choose_provider(role_name, requested=None):
    cfg = load_config()
    providers = cfg["providers"]

    if requested:
        if requested not in providers:
            raise ValueError(f"Unknown provider: {requested}")
        return requested

    for name in cfg.get("routing", {}).get(role_name, []):
        if providers.get(name, {}).get("enabled"):
            return name
    return "manual"

def execute(provider, prompt, output_path):
    cfg = load_config()
    item = cfg["providers"].get(provider, {})

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if provider == "manual" or not item.get("command"):
        output_path.write_text(prompt, encoding="utf-8")
        return {
            "mode": "manual",
            "provider": provider,
            "prompt_file": str(output_path)
        }

    # Command must be explicitly configured locally.
    command = item["command"]
    if isinstance(command, str):
        command = shlex.split(command)

    proc = subprocess.run(
        command,
        input=prompt,
        text=True,
        capture_output=True,
        check=False
    )
    output_path.write_text(proc.stdout or proc.stderr, encoding="utf-8")
    return {
        "mode": "executed",
        "provider": provider,
        "returncode": proc.returncode,
        "output_file": str(output_path)
    }
