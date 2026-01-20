import os
import json
import pytest
from utils.memory_utils import read_memory, write_memory, append_to_history, update_todos

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

def test_update_todos():
    """Test the update_todos function with various scenarios."""
    import os
    import json
    from utils.memory_utils import update_todos

    # Create a temporary memory file for testing
    temp_memory_file = "temp_project.memory.json"
    initial_memory = {
        "todos": [
            {"id": 1, "status": "completed", "title": "Initial todo"}
        ]
    }

    # Write initial memory to the temporary file
    with open(temp_memory_file, "w") as file:
        json.dump(initial_memory, file, indent=4)

    try:
        # Test 1: Add a valid new todo
        new_todo = {"id": 2, "status": "pending", "title": "New valid todo"}
        assert update_todos(temp_memory_file, new_todo) is True

        # Verify the new todo was added
        with open(temp_memory_file, "r") as file:
            updated_memory = json.load(file)
        assert len(updated_memory["todos"]) == 2
        assert updated_memory["todos"][1] == new_todo

        # Test 2: Handle invalid input (missing fields)
        invalid_todo = {"id": 3, "status": "pending"}  # Missing 'title'
        assert update_todos(temp_memory_file, invalid_todo) is False

        # Verify the invalid todo was not added
        with open(temp_memory_file, "r") as file:
            updated_memory = json.load(file)
        assert len(updated_memory["todos"]) == 2  # No change

    finally:
        # Clean up the temporary file
        if os.path.exists(temp_memory_file):
            os.remove(temp_memory_file)

def test_update_todos_edge_cases():
    """Test the update_todos function for edge cases."""
    import os
    import json
    from utils.memory_utils import update_todos

    # Create a temporary memory file for testing
    temp_memory_file = "temp_project.memory.json"
    initial_memory = {
        "todos": [
            {"id": 1, "status": "completed", "title": "Initial todo"}
        ]
    }

    # Write initial memory to the temporary file
    with open(temp_memory_file, "w") as file:
        json.dump(initial_memory, file, indent=4)

    try:
        # Test 1: Duplicate ID
        duplicate_todo = {"id": 1, "status": "pending", "title": "Duplicate ID todo"}
        assert update_todos(temp_memory_file, duplicate_todo) is False

        # Test 2: Missing fields
        missing_fields_todo = {"id": 2, "status": "pending"}  # Missing 'title'
        assert update_todos(temp_memory_file, missing_fields_todo) is False

        # Test 3: Invalid data types
        invalid_types_todo = {"id": "two", "status": "pending", "title": "Invalid ID type"}
        assert update_todos(temp_memory_file, invalid_types_todo) is False

        # Test 4: Valid new todo
        valid_todo = {"id": 2, "status": "pending", "title": "Valid new todo"}
        assert update_todos(temp_memory_file, valid_todo) is True

        # Verify the valid todo was added
        with open(temp_memory_file, "r") as file:
            updated_memory = json.load(file)
        assert len(updated_memory["todos"]) == 2
        assert updated_memory["todos"][1] == valid_todo

    finally:
        # Clean up the temporary file
        if os.path.exists(temp_memory_file):
            os.remove(temp_memory_file)

# Example usage of the test function
if __name__ == "__main__":
    test_update_todos_edge_cases()