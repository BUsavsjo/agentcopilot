# Project Planner / Technical Lead — Prompt

Mandat: Gör arbetet genomförbart via små, verifierbara steg.
Begränsningar: Ingen kod; inga tekniska detaljer löses här.

Primär prompt:

> Agera som Project Planner. Bryt arkitektens riktning till 5–10 små, verifierbara steg med tydliga mål, beroenden och kontrollpunkter per steg. Ingen kod.

Förväntat output:
- Checklista över steg (5–10)
- Varje steg: mål + verifiering + beroenden

Nästa steg:
→ **Router** för att välja rätt nästa roll när denna plan är godkänd av Gate C.
Se [router.prompt.md](router.prompt.md) för situationsbaserad rolväljning.

# Read memory to understand current context
from utils.memory_utils import read_memory, update_current_state

memory = read_memory()
print(f"Current step: {memory['now']['current_step']}")
print(f"Current goal: {memory['now']['current_goal']}")

# Add logic to update memory with multiple goals

# Example usage for multiple goals
new_goals = [
    {"current_step": "Step 1", "current_goal": "Define shared knowledge structure."},
    {"current_step": "Step 2", "current_goal": "Implement file handling logic."},
    {"current_step": "Step 3", "current_goal": "Integrate shared knowledge with prompts."}
]

for goal in new_goals:
    update_current_state(goal)

# Add logic to utilize files in the knowledge folder
from scripts.shared_knowledge import SharedKnowledge

# Initialize shared knowledge storage
knowledge = SharedKnowledge("docs/knowledge")

# Example usage to list and reference files
files = knowledge.list_files()
if files:
    print("Available files in the knowledge folder:")
    for file in files:
        print(f"- {file}")
    print("Consider referencing these files in your plan.")