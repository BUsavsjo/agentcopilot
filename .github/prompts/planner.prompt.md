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

## Plan to Verify Prompt Flow Delivery

### Checklist of Steps

1. **Define the expected flow**
   - **Goal**: Clearly outline the sequence of prompts and their expected outputs.
   - **Verification**: Ensure the flow aligns with the project requirements.
   - **Dependencies**: Understanding of the current prompt structure.

2. **Analyze existing prompts**
   - **Goal**: Review all current prompts to identify their roles and outputs.
   - **Verification**: Documented analysis of each prompt.
   - **Dependencies**: Access to all prompt files.

3. **Simulate the flow**
   - **Goal**: Test the sequence of prompts in a controlled environment.
   - **Verification**: Logs or outputs showing the flow execution.
   - **Dependencies**: Defined expected flow and prompt analysis.

4. **Identify gaps or issues**
   - **Goal**: Highlight any missing links or inconsistencies in the flow.
   - **Verification**: A list of identified issues with proposed solutions.
   - **Dependencies**: Results from the simulation.

5. **Iterate and refine**
   - **Goal**: Adjust the prompts to ensure seamless delivery.
   - **Verification**: Successful re-simulation with no issues.
   - **Dependencies**: Feedback from the previous step.

6. **Document the final flow**
   - **Goal**: Create a comprehensive guide for the prompt flow.
   - **Verification**: Approved documentation by stakeholders.
   - **Dependencies**: Finalized and verified prompt flow.