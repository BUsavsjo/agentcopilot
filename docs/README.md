# Dokumentation — Index

En landningssida för projektets dokumentation och arbetsflöde.

---

## 🔍 Börja här — Välj rätt roll

**Osäker på vilken roll du ska ta?** Använd denna guide:

- [**Router — Välj rätt roll**](../.github/prompts/router.prompt.md) ← Börja här!

Router hjälper dig att diagnostisera situationen och rekommendera nästa steg.

---

## Roller och ansvar

- [docs/ROLES.md](ROLES.md)
- [docs/ROLES_ONE_PAGER.md](ROLES_ONE_PAGER.md)

## Arbetsflöde

- [docs/WORKFLOW.md](WORKFLOW.md)
- [docs/QA_CHECKLIST.md](QA_CHECKLIST.md) — QA-roll kontrollista
- [docs/RELEASE_NOTES.md](RELEASE_NOTES.md) — Release-process och mall
- [docs/MIGRATION_CHECKLIST.md](MIGRATION_CHECKLIST.md) — Anpassa mallen för nytt projekt

## Prompts och chat

- Rollspecifika promptmallar: [docs/COPILOT_PROMPTS.md](COPILOT_PROMPTS.md)
- Repo‑prompts (för Copilot Chat): [\.github/prompts](../.github/prompts)

## Användning

- **Första steget:** Börja med [Router](../.github/prompts/router.prompt.md) om du är osäker på vilken roll att välja
- **Sedan:** Följ rollen-ordningen: Analyst → Architect → Planner → Engineer → QA → Reviewer → Writer
- **Efter varje roll:** Kör Router igen för att välja nästa steg, eller meddela Copilot Chat `/router` för rekommendation
- **Fullständig guide:** Se [README.md](../README.md) för snabbstart och arbetsflöde

---

## Tips

- Länka alltid till specifika filer eller sektioner i chatten för fokus.
- Håll varje steg litet och verifierbart.
- Terminalen och Git är den slutliga sanningen.
