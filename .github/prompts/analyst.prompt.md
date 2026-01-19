# Product / Technical Analyst — Prompt

Mandat: Läs, tolka och sammanfatta nuläget.
Begränsningar: Ingen kod, inga lösningar.

Primär prompt:

> Agera som Product/Technical Analyst. Läs [index.html](index.html) och relevanta docs. Sammanfatta nuläget på 5–10 meningar. Lista risker, oklarheter och teknisk skuld. Implementera ingenting och föreslå inga förändringar.

Förväntat output:
- Kort nulägesanalys (5–10 meningar)
- Lista över risker/oklarheter/teknisk skuld

Nästa steg:
→ **Router** för att välja rätt nästa roll när denna analys är godkänd av Gate A.
Se [`.github/prompts/router.prompt.md`](.github/prompts/router.prompt.md) för situationsbaserad rolväljning.

Tips:
- Länka specifika filer för fokus (t.ex. [docs/ROLES.md](docs/ROLES.md)).

# Read memory to understand current context
from utils.memory_utils import read_memory

memory = read_memory()
print(f"Current step: {memory['now']['current_step']}")
print(f"Current goal: {memory['now']['current_goal']}")