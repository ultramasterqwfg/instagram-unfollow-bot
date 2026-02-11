import yaml
from pathlib import Path

from automation.relationship_scanner import load_relationships
from automation.unfollow_queue_builder import Rules, build_queue, save_queue

ROOT = Path(__file__).resolve().parents[1]
REL = ROOT / "data" / "relationships.json"

RULES_FILE = ROOT / "config" / "filter_rules.yaml"
LIMITS_FILE = ROOT / "config" / "session_limits.yaml"

def main():
    relationships = load_relationships(REL)
    rules_cfg = yaml.safe_load(RULES_FILE.read_text(encoding="utf-8"))["rules"]
    limits_cfg = yaml.safe_load(LIMITS_FILE.read_text(encoding="utf-8"))["queue"]

    rules = Rules(
        non_reciprocal_only=bool(rules_cfg.get("non_reciprocal_only", True)),
        min_days_since_last_interaction=int(rules_cfg.get("min_days_since_last_interaction", 30)),
        exclude_verified=bool(rules_cfg.get("exclude_verified", True)),
        exclude_whitelist_usernames=list(rules_cfg.get("exclude_whitelist_usernames", [])),
        keyword_flags=list(rules_cfg.get("keyword_flags", [])),
        max_items=int(limits_cfg.get("max_items", 500)),
    )

    queue = build_queue(relationships, rules)
    out = save_queue(queue)
    print(f"Saved {out}")

if __name__ == "__main__":
    main()
