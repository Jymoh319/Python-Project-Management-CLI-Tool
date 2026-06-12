import os
import json
from models.user import User
from models.project import Project
from models.task import Task

DB_PATH = os.path.join(os.path.dirname(__file__), "../data/db.json")

def load_database():
    """Reads structural disk files safely while returning stateful object maps."""
    if not os.path.exists(DB_PATH):
        return {"users": {}, "projects": {}, "tasks": {}}
    
    try:
        with open(DB_PATH, "r") as f:
            raw_data = json.load(f)
    except (json.JSONDecodeError, IOError):
        # Graceful fallback initialization on read errors
        return {"users": {}, "projects": {}, "tasks": {}}

    # Normalize base dictionaries
    users = {name: User.from_dict(d) for name, d in raw_data.get("users", {}).items()}
    projects = {title: Project.from_dict(d) for title, d in raw_data.get("projects", {}).items()}
    tasks = {tid: Task.from_dict(d) for tid, d in raw_data.get("tasks", {}).items()}
    
    return {"users": users, "projects": projects, "tasks": tasks}

def save_database(state):
    """Converts working runtime objects back into static disk data frames."""
    try:
        serialized = {
            "users": {name: obj.to_dict() for name, obj in state["users"].items()},
            "projects": {title: obj.to_dict() for title, obj in state["projects"].items()},
            "tasks": {tid: obj.to_dict() for tid, obj in state["tasks"].items()}
        }
        with open(DB_PATH, "w") as f:
            json.dump(serialized, f, indent=2)
    except IOError as e:
        print(f"Critical File System Failure: Unable to persist data stream. Detail: {e}")
