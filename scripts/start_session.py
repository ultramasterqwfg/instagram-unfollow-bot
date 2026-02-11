import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    cmd = ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", os.getenv("PORT", "8000")]
    subprocess.run(cmd, cwd=str(ROOT), check=False)

if __name__ == "__main__":
    main()
