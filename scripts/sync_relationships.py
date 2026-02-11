from pathlib import Path
from automation.relationship_scanner import load_relationships, save_relationships

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
SRC = DATA_DIR / "relationships.json"

def main():
    data = load_relationships(SRC)
    save_relationships(data)

if __name__ == "__main__":
    main()
