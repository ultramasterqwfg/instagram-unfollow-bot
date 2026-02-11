from pathlib import Path
import json
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from automation.relationship_scanner import load_relationships
from automation.unfollow_queue_builder import Rules, build_queue

app = FastAPI(title="Instagram Follow Hygiene (Data-Only)", version="1.0.0")

DATA_DIR = Path(__file__).resolve().parent / "data"
REL_FILE = DATA_DIR / "relationships.json"

class QueueRequest(BaseModel):
    non_reciprocal_only: bool = True
    min_days_since_last_interaction: int = 30
    exclude_verified: bool = True
    exclude_whitelist_usernames: List[str] = []
    keyword_flags: List[str] = []
    max_items: int = 500

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/relationships")
def relationships():
    if not REL_FILE.exists():
        raise HTTPException(status_code=404, detail="data/relationships.json not found")
    return json.loads(REL_FILE.read_text(encoding="utf-8"))

@app.post("/queue")
def queue(req: QueueRequest):
    if not REL_FILE.exists():
        raise HTTPException(status_code=404, detail="data/relationships.json not found")
    rel = load_relationships(REL_FILE)
    rules = Rules(
        non_reciprocal_only=req.non_reciprocal_only,
        min_days_since_last_interaction=req.min_days_since_last_interaction,
        exclude_verified=req.exclude_verified,
        exclude_whitelist_usernames=req.exclude_whitelist_usernames,
        keyword_flags=req.keyword_flags,
        max_items=req.max_items,
    )
    q = build_queue(rel, rules)
    return {"count": len(q), "items": q}
