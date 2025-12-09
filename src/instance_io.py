import json
from pathlib import Path

CONFIG_PATH = Path("configs/instances.json")

def load_instances() -> list[dict]:

    """
    Load existing VM instances from configs/instances.json.
    If the file doesn't exist or invalid, return an empty list.
    """

    if not CONFIG_PATH.exists():
        return[]
    
    try:
        with CONFIG_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        print("[WARN] instances.json is not a list.")
        return[]
    except json.JSONDecodeError:
        print("[WARN] invalid JSON format - resetting.")
        return[]
    
def save_instances(instances: list[dict]) -> None:

    """
    Save the provided list of VM instances into configs/instances.json.
    Overwrites the file completely.
    """

    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with CONFIG_PATH.open("w", encoding="utf-8") as f:
        json.dump(instances, f, indent=2)
