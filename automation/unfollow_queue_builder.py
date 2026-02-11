import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Set

from utils.logger import setup_logger
from utils.validators import safe_int

logger = setup_logger(__name__)

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)

@dataclass
class Rules:
    non_reciprocal_only: bool = True
    min_days_since_last_interaction: int = 30
    exclude_verified: bool = True
    exclude_whitelist_usernames: List[str] = None
    keyword_flags: List[str] = None
    max_items: int = 500

def build_queue(relationships: Dict[str, Any], rules: Rules) -> List[Dict[str, Any]]:
    followers = relationships.get("followers", []) or []
    following = relationships.get("following", []) or []

    follower_set: Set[str] = set((u.get("username") or "").lower() for u in followers if u.get("username"))
    whitelist: Set[str] = set((u or "").lower() for u in (rules.exclude_whitelist_usernames or []))
    flags = [(k or "").lower() for k in (rules.keyword_flags or []) if (k or "").strip()]

    queue: List[Dict[str, Any]] = []

    for u in following:
        username = (u.get("username") or "").strip()
        if not username:
            continue

        uname = username.lower()
        if uname in whitelist:
            continue

        is_verified = bool(u.get("is_verified", False))
        if rules.exclude_verified and is_verified:
            continue

        last_days = safe_int(u.get("last_interaction_days"), default=9999)
        if last_days < rules.min_days_since_last_interaction:
            continue

        non_reciprocal = uname not in follower_set
        if rules.non_reciprocal_only and not non_reciprocal:
            continue

        bio = (u.get("bio") or "").lower()
        keyword_hit = any(k in bio for k in flags) if flags else False

        reason_parts = []
        if non_reciprocal:
            reason_parts.append("non_reciprocal")
        reason_parts.append(f"inactive_{last_days}d")
        if keyword_hit:
            reason_parts.append("keyword_flag")

        queue.append({
            "username": username,
            "reason": ",".join(reason_parts),
            "is_verified": is_verified,
            "last_interaction_days": last_days,
        })

        if len(queue) >= rules.max_items:
            break

    logger.info("Built review queue: %s items", len(queue))
    return queue

def save_queue(queue: List[Dict[str, Any]], out: Path = DATA_DIR / "review_queue.json") -> Path:
    out.write_text(json.dumps(queue, ensure_ascii=False, indent=2), encoding="utf-8")
    logger.info("Saved review queue: %s", out)
    return out
