import argparse
import json
from pathlib import Path

from .state_machine import Lifecycle
from .work_package import load, save, append_history
from .prompt_builder import build_prompt
from .providers import choose_provider, execute

def cmd_status(args):
    wp = load(args.work_package)
    lifecycle = Lifecycle()
    state = wp["state"]
    info = lifecycle.state(state)
    print(json.dumps({
        "id": wp["id"],
        "title": wp["title"],
        "state": state,
        "role": info.get("role"),
        "human_gate": info.get("human_gate"),
        "allowed_next": info.get("next", [])
    }, indent=2))

def cmd_transition(args):
    path = Path(args.work_package)
    wp = load(path)
    lifecycle = Lifecycle()
    current = wp["state"]

    if not lifecycle.can_transition(current, args.target):
        raise SystemExit(f"Invalid transition: {current} -> {args.target}")

    if lifecycle.requires_human_gate(current) and not args.human_approved:
        raise SystemExit(
            f"State '{current}' requires --human-approved before transition."
        )

    wp["state"] = args.target
    append_history(wp, "state_transition", {
        "from": current,
        "to": args.target,
        "human_approved": bool(args.human_approved)
    })
    save(path, wp)
    print(f"{current} -> {args.target}")

def cmd_dispatch(args):
    path = Path(args.work_package)
    wp = load(path)
    lifecycle = Lifecycle()
    role = lifecycle.next_role(wp["state"])

    if role in (None, "none", "human"):
        raise SystemExit(f"State '{wp['state']}' is not dispatchable to an AI role.")

    provider = choose_provider(role, requested=args.provider)
    prompt = build_prompt(wp, role)
    run_dir = Path("runs") / wp["id"]
    output_path = run_dir / f"{wp['state']}--{role}--{provider}.md"
    result = execute(provider, prompt, output_path)

    append_history(wp, "agent_dispatch", {
        "role": role,
        "provider": provider,
        "result": result
    })
    save(path, wp)
    print(json.dumps(result, indent=2))

def main():
    parser = argparse.ArgumentParser(description="ServiceNow home-lab orchestrator")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("status")
    p.add_argument("work_package")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("transition")
    p.add_argument("work_package")
    p.add_argument("target")
    p.add_argument("--human-approved", action="store_true")
    p.set_defaults(func=cmd_transition)

    p = sub.add_parser("dispatch")
    p.add_argument("work_package")
    p.add_argument("--provider")
    p.set_defaults(func=cmd_dispatch)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
