"""
Memory utilities for managing project state and history.

This module provides functions to read, write, and manage the project memory
stored in project.memory.json. It supports tracking current state, history
entries, milestones, and todos.

Example usage:
    from utils.memory_utils import read_memory, append_to_history
    
    # Read current memory state
    memory = read_memory()
    print(f"Current step: {memory['now']['current_step']}")
    
    # Append a history entry
    entry = {
        "date": "2026-01-19T12:00:00Z",
        "type": "change",
        "summary": "Implemented feature X."
    }
    append_to_history(entry)
"""

import json
from typing import Any, Dict

MEMORY_FILE = 'project.memory.json'

# Why: Ensures the memory file is read safely and provides a consistent structure for project state.
def read_memory() -> Dict[str, Any]:
    """Read the memory JSON file and return its contents.
    
    Returns:
        Dict[str, Any]: The memory data structure containing 'now', 'rules',
                       'commands', 'todos', 'milestones', and 'history'.
    
    Raises:
        FileNotFoundError: If project.memory.json is not found.
        ValueError: If the file contains invalid JSON.
    """
    try:
        with open(MEMORY_FILE, 'r') as memory_file:
            return json.load(memory_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Memory file '{MEMORY_FILE}' not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Memory file '{MEMORY_FILE}' is not a valid JSON file.")

# Why: Guarantees that updates to the memory file are atomic and error-checked.
def write_memory(data: Dict[str, Any]) -> None:
    """Write the given data to the memory JSON file.
    
    Args:
        data: The complete memory structure to write to file.
    
    Raises:
        IOError: If writing to the file fails.
    """
    try:
        with open(MEMORY_FILE, 'w') as memory_file:
            json.dump(data, memory_file, indent=4)
    except Exception as e:
        raise IOError(f"Failed to write to memory file '{MEMORY_FILE}': {e}")

# Why: Maintains a fixed history size to prevent memory bloat while preserving recent changes.
def append_to_history(entry: Dict[str, Any]) -> None:
    """Append an entry to the history in the memory file.
    
    Automatically manages history size according to max_history rule.
    When the limit is reached, removes the oldest entry before adding new one.
    
    Args:
        entry: A dictionary containing 'date', 'type', and 'summary' fields.
               Example: {"date": "2026-01-19T12:00:00Z", "type": "change", 
                        "summary": "Updated feature X."}
    
    Note:
        Expected entry format:
        - date: ISO 8601 date string
        - type: One of 'change', 'qa', or 'review'
        - summary: Brief description (1-2 sentences)
    """
    memory = read_memory()
    if len(memory['history']) >= memory['rules']['max_history']:
        memory['history'].pop(0)  # Remove oldest entry
    memory['history'].append(entry)
    write_memory(memory)

# Why: Updates the current state to reflect the latest project step, ensuring accurate tracking.
def update_current_state(new_state: Dict[str, Any]) -> None:
    """Update the current state in the memory file.

    Args:
        new_state: A dictionary representing the new state to set.

    Raises:
        KeyError: If 'now' key is missing in the memory structure.
        IOError: If writing to the file fails.
    """
    memory = read_memory()
    if 'now' not in memory:
        raise KeyError("The memory structure is missing the 'now' key.")

    memory['now'] = new_state
    write_memory(memory)

# Why: Allows for dynamic updates to the todos section, enabling task management directly through memory file edits.
def update_todos(memory_file_path, new_todo):
    """
    Update the todos section in the memory file with a new todo.

    Args:
        memory_file_path (str): Path to the memory file (project.memory.json).
        new_todo (dict): The new todo to add, with keys 'id', 'status', and 'title'.

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    # Helper function to validate the new_todo structure
    def is_valid_todo(todo):
        required_keys = {"id", "status", "title"}
        if not required_keys.issubset(todo.keys()):
            return False, "Missing required fields."
        if not isinstance(todo["id"], int):
            return False, "Invalid type for 'id'. Expected int."
        if not isinstance(todo["status"], str):
            return False, "Invalid type for 'status'. Expected str."
        if not isinstance(todo["title"], str):
            return False, "Invalid type for 'title'. Expected str."
        return True, None

    try:
        # Validate the new_todo structure
        is_valid, error_message = is_valid_todo(new_todo)
        if not is_valid:
            print(f"Error: {error_message}")
            return False

        # Read the current memory file
        with open(memory_file_path, 'r') as file:
            memory = json.load(file)

        # Ensure the todos list exists
        todos = memory.setdefault("todos", [])

        # Check for duplicate IDs
        if any(todo["id"] == new_todo["id"] for todo in todos):
            print("Error: Duplicate ID detected in new_todo.")
            return False

        # Add the new todo to the todos list
        todos.append(new_todo)

        # Write the updated memory back to the file
        with open(memory_file_path, 'w') as file:
            json.dump(memory, file, indent=4)

        return True
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from memory file.")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False