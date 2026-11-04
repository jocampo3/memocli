import json
from pathlib import Path

DATA_DIR = Path.home() / '.memocli'
DATA_FILE = DATA_DIR / 'global.json'

def init():
    DATA_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        with open(DATA_FILE, 'w') as f:
            json.dump({"memos": []}, f, indent=2)


def load_memos():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def write_memos(data):
    with open(DATA_FILE, 'w') as f:
        f.seek(0) # reposition pointer
        json.dump(data, f, indent=2)
        f.truncate()
