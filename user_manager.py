import json
import os

USER_DATA_FILE = "user_data.json"

def load_user_data():
    """Load user preferences and history from a JSON file."""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    return {"saved_topics": [], "search_history": []}

def save_user_data(data):
    """Save user preferences and history to a JSON file."""
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def save_topic(topic):
    """Save a topic of interest for the user."""
    data = load_user_data()
    if topic not in data["saved_topics"]:
        data["saved_topics"].append(topic)
        save_user_data(data)

def add_search_history(topic):
    """Add a topic to the user's search history."""
    data = load_user_data()
    data["search_history"].append(topic)
    save_user_data(data)

def view_saved_topics():
    """Retrieve saved topics."""
    return load_user_data().get("saved_topics", [])

def view_search_history():
    """Retrieve search history."""
    return load_user_data().get("search_history", [])
