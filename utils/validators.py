from typing import Any, Dict, List

def require_keys(obj: Dict[str, Any], keys: List[str]) -> None:
    missing = [k for k in keys if k not in obj]
    if missing:
        raise ValueError(f"Missing required keys: {missing}")

def safe_int(v: Any, default: int = 0) -> int:
    try:
        return int(v)
    except Exception:
        return default
