import os
import json
import pytest
from utils.memory_utils import read_memory, write_memory, append_to_history

MEMORY_FILE = 'project.memory.json'

@pytest.fixture(scope="function")
def setup_memory_file():
    # Create a temporary memory file for testing
    test_memory = {
        "now": {"current_step": None, "current_goal": None},
        "rules": {
            "max_history": 3,
            "history_entry_format": {
                "date": "ISO 8601 date string",
                "type": "One of 'change', 'qa', 'review'",
                "summary": "A brief description (1–2 sentences)"
            }
        },
        "commands": {},
        "todos": [],
        "milestones": [],
        "history": []
    }
    with open(MEMORY_FILE, 'w') as f:
        json.dump(test_memory, f, indent=4)
    yield
    # Cleanup after test
    os.remove(MEMORY_FILE)

def test_read_memory(setup_memory_file):
    memory = read_memory()
    assert memory["now"] == {"current_step": None, "current_goal": None}

def test_write_memory(setup_memory_file):
    new_data = {"now": {"current_step": "step1", "current_goal": "goal1"}}
    write_memory(new_data)
    memory = read_memory()
    assert memory["now"] == {"current_step": "step1", "current_goal": "goal1"}

def test_append_to_history(setup_memory_file):
    entry1 = {"type": "qa", "summary": "QA verified feature X."}
    entry2 = {"type": "change", "summary": "Engineer updated feature Y."}
    entry3 = {"type": "review", "summary": "Reviewer approved changes."}
    entry4 = {"type": "qa", "summary": "QA verified feature Z."}

    append_to_history(entry1)
    append_to_history(entry2)
    append_to_history(entry3)
    memory = read_memory()
    assert len(memory["history"]) == 3

    append_to_history(entry4)
    memory = read_memory()
    assert len(memory["history"]) == 3  # Oldest entry should be removed
    assert memory["history"][0] == entry2