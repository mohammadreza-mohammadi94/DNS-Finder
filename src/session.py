import json
import os

SESSION_FILE = "dns_finder_session.json"

def save_session(data):
    with open(SESSION_FILE, "w") as f:
        json.dump(data, f)

def get_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def clear_session():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
