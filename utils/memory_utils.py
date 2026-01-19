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