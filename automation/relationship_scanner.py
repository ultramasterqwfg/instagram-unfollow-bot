import csv
import json
from pathlib import Path
from typing import Any, Dict, List

from utils.logger import setup_logger

logger = setup_logger(__name__)

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)

DEFAULT_OUT = DATA_DIR / "relationships.json"

def load_relationships(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Relationship file not found: {path}")

    if path.suffix.lower() == ".json":
        return json.loads(path.read_text(encoding="utf-8"))

    if path.suffix.lower() == ".csv":
        rows: List[Dict[str, Any]] = []
        with path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for r in reader:
                if r.get("username"):
                    rows.append({"username": r["username"]})
        return {"followers": [], "following": rows}

    raise ValueError("Unsupported file type. Use .json or .csv")

def save_relationships(data: Dict[str, Any], out: Path = DEFAULT_OUT) -> Path:
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    logger.info("Saved relationships snapshot: %s", out)
    return out
