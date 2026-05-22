import json
import os

DATA_DIR = "data"
VOTER_FILE = os.path.join(DATA_DIR, "voters.json")
CANDIDATE_FILE = os.path.join(DATA_DIR, "candidates.json")
VOTED_FILE = os.path.join(DATA_DIR, "voted.json")
ADMIN_FILE = os.path.join(DATA_DIR, "admin.json")

os.makedirs(DATA_DIR, exist_ok=True)

def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)