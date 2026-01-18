# Bidra till projektet

Tack för att du vill bidra! Den här guiden förklarar hur du använder vårt rollbaserade arbetsflöde innan du öppnar en PR.

---

## Arbetsflödet

Allt arbete följer **en definierad sekvens av roller**, varje med ett tydligt mandat och verifieringsgates.

Se [docs/WORKFLOW.md](docs/WORKFLOW.md) för fullständig policy och gates.

### Ordning: Analyst → Architect → Planner → Engineer → QA → Reviewer → Writer

**Innan du öppnar PR, genomgår du dessa steg:**

1. **Analyst** — Nulägesbild
   - Läs relevant kod och sammanfatta nuläget.
   - Identifiera risker, oklarheter och teknisk skuld.
   - Implementera inget; föreslå inga lösningar.
   - Prompt: [\.github/prompts/analyst.prompt.md](.github/prompts/analyst.prompt.md)

2. **Architect** — Riktning och avgränsning
   - Föreslå minsta hållbara förändring med tydlig vinst.
   - Motivera riktning och avgränsning.
   - Implementera inget.
   - Prompt: [\.github/prompts/architect.prompt.md](.github/prompts/architect.prompt.md)

3. **Planner** — Nedbrytning i små steg
   - Bryt riktningen till 5–10 små, verifierbara steg.
   - Definiera mål, verifiering och beroenden per steg.
   - Skapa ingen kod.
   - Prompt: [\.github/prompts/planner.prompt.md](.github/prompts/planner.prompt.md)

4. **Engineer** — Implementera ett steg i taget
   - Implementera endast ett steg enligt planen.
   - Gör små, avgränsade ändringar.
   - Följ befintlig stil.
   - Ta inga arkitekturbeslut.
   - Prompt: [\.github/prompts/engineer.prompt.md](.github/prompts/engineer.prompt.md)

5. **QA** — Verifiera och bedöm risk
   - Föreslå verifieringssteg (tester, lint, syntax).
   - Kör relevanta kontroller.
   - Bedöm regressionsrisk.
   - Ändra ingen produktionskod.
   - Prompt: [\.github/prompts/qa.prompt.md](.github/prompts/qa.prompt.md)

6. **Reviewer** — Kvalitetsgrind
   - Bedöm struktur, läsbarhet och lämplighet.
   - Kontrollera att rätt filer ändrats.
   - Ge Go/No-go för merge.
   - Ändra ingen kod.
   - Prompt: [\.github/prompts/reviewer.prompt.md](.github/prompts/reviewer.prompt.md)

7. **Writer** — Uppdatera dokumentation
   - Uppdatera README och relevant dokumentation.
   - Förklara designval och dataflöden.
   - Lägg endast till "varför"-kommentarer där det behövs.
   - Ändra ingen funktionalitet.
   - Prompt: [\.github/prompts/writer.prompt.md](.github/prompts/writer.prompt.md)

---

## Använd Copilot Chat

Alla steg utfördes genom **Copilot Chat** i VS Code.

Anropa roller via slash-kommandon:
- `/analyst nulägesbild`
- `/architect riktning`
- `/planner plan`
- `/engineer steg 1`
- `/qa verifiera`
- `/reviewer granskning`
- `/writer dokumentera`

Se [README.md#användning-i-copilot-chat](README.md#användning-i-copilot-chat) för detaljerade kommandon.

---

## Öppna en PR

**Använd PR-mallen** ([\.github/pull_request_template.md](.github/pull_request_template.md)) som stöd.

Din PR bör innehålla:

- **Titel:** Kort, beskrivande (t.ex. "docs: add QA checklist").
- **Beskrivning:** Sammanfattning av vad som ändras och varför.
- **Checkboxar:** Bekräfta att du har genomgått alla 7 roller (eller relevant delmängd).
- **Länkar:** Referera till relevanta dokumenter och prompts.

---

## Kvalitets-gates

- **Gate A (Analyst):** Finns en tydlig nulägebild? Stoppa här om nej.
- **Gate B (Architect):** Är riktningen minimal och motiverad? Revidera om nej.
- **Gate C (Planner):** Är planen verifierbar med små steg? Bryt ner mer om nej.
- **Gate D (Engineer):** Uppfyller implementeringen stegets mål? Iterera om nej.
- **Gate E (QA):** Är risken acceptabel? Åtgärda om nej.
- **Gate F (Reviewer):** Är koden redo för merge? Go/No-go-beslut här.
- **Gate G (Writer):** Är dokumentation uppdaterad? Kompletta om nej.

Se [docs/WORKFLOW.md](docs/WORKFLOW.md) för mer detalj.

---

## Tips

- **En roll åt gången:** Byt roll mellan varje fas för tydlighet.
- **Håll ändringar små:** Be om minsta ändring som ger vinst.
- **Länka specifika filer:** T.ex. `[docs/ROLES.md](docs/ROLES.md)` för fokus.
- **Stoppa vid oklarhet:** Gå tillbaka till Analyst/Architect innan du implementerar.
- **Terminal och Git är sanningen:** Verifiera alla ändringar lokalt.

---

## Behöver du hjälp?

- Läs [README.md](README.md) för introduktion.
- Se [docs/README.md](docs/README.md) för dokumentationsindex.
- Kolla roller- och ansvarsdefinitionerna i [docs/ROLES.md](docs/ROLES.md).
- Använd promptmallarna under [\.github/prompts](.github/prompts).

---

## Licens

Genom att bidra till detta projekt godkänner du att dina bidrag licensieras under MIT License. Se [LICENSE](LICENSE).

---

**Tack för ditt bidrag!**
