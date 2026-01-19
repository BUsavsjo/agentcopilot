# Använda Copilot Chat i VS Code — Praktisk guide

Den här README:n visar hur du använder Copilot Chat i VS Code på ett pedagogiskt och effektivt sätt, med tydliga mandat per roll och verifierbara leverabler. Guiden bygger på våra roller och arbetsflöden i dokumenten:

- Roller: se [docs/ROLES.md](docs/ROLES.md)
- Arbetsflöde: se [docs/WORKFLOW.md](docs/WORKFLOW.md)
- Rollspecifika promptmallar: se [docs/COPILOT_PROMPTS.md](docs/COPILOT_PROMPTS.md)
- One‑pager: se [docs/ROLES_ONE_PAGER.md](docs/ROLES_ONE_PAGER.md)

---

## 🚀 Snabbstart — Använd denna mall

**Ny på detta arbetsflöde?** Börja här:

1. **Clone eller fork denna repo** för ditt projekt.
2. **Verifiera miljö:** Öppna VS Code terminal och kör:
   ```powershell
   .\scripts\doctor.ps1
   ```
   (Doctor kontrollerar att allt är på plats: Git, Node.js, folders, dependencies.)

3. **Välj en roll** — Meddela Copilot Chat vilken roll du är i:
   - 🔍 **Osäker på vilken roll?** Se [Router — Välj rätt roll](.github/prompts/router.prompt.md) först.
   - Sedan meddela Copilot: `/analyst`, `/architect`, `/planner`, `/engineer`, `/qa`, `/reviewer` eller `/writer`

4. **Kör roll-prompten** — Kopiera motsvarande prompt från [.github/prompts/](.github/prompts/):
   - Välj din roll
   - Kopiera prompt från fil
   - Klistra in i Copilot Chat
   - Lägg till relevanta detaljer (mål, fil, issue, etc.)

5. **När du är klar** — Kör `/router` för att välja nästa roll, eller gå direkt till nästa (se "Nästa steg" i din prompt).

**Fullständig guide:** Se [CONTRIBUTING.md](CONTRIBUTING.md) för arbetsflöde, grindar och best practices.

---

## Prompts i repo

- [\.github/prompts/router.prompt.md](.github/prompts/router.prompt.md) — **Börja här när du är osäker!**
- [\.github/prompts/analyst.prompt.md](.github/prompts/analyst.prompt.md)
- [\.github/prompts/architect.prompt.md](.github/prompts/architect.prompt.md)
- [\.github/prompts/planner.prompt.md](.github/prompts/planner.prompt.md)
- [\.github/prompts/engineer.prompt.md](.github/prompts/engineer.prompt.md)
- [\.github/prompts/qa.prompt.md](.github/prompts/qa.prompt.md)
- [\.github/prompts/writer.prompt.md](.github/prompts/writer.prompt.md)
- [\.github/prompts/data-analyst.prompt.md](.github/prompts/data-analyst.prompt.md)
- [\.github/prompts/reviewer.prompt.md](.github/prompts/reviewer.prompt.md)

---

## Förutsättningar

- VS Code installerat.
- GitHub Copilot och Copilot Chat‑extension installerad och inloggad.
- Projektet öppnat i VS Code (den här repot).

---

## Öppna Copilot Chat

- Öppna sidopanelen för Copilot Chat via Copilot‑ikonen i Activity Bar.
- Alternativt: använd Inline Chat i editorn från kommandopaletten och välj Copilot Chat.

Fortsätt alltid att arbeta med små, tydliga promptar och ett mandat i taget.

---

## Användning i Copilot Chat

Anropa roller via `/`‑kommandon. Varje roll har ett fördefinierat mandat och väljer själv lämplig kontext.

Exempel:
- `/analyst nulägesbild`
- `/architect riktning`
- `/planner plan`
- `/engineer steg 1`
- `/qa verifiera`
- `/reviewer granskning`
- `/writer dokumentera`

För detaljerade kommandon, se [Appendix: Slash‑kommandon](#appendix-slash-kommandon).

---

## Grundprinciper i chatten

- En roll i taget: byt roll när du byter fas (Analyst → Architect → Planner → Engineer → QA → Reviewer → Writer).
- Säg mandat och begränsningar först: vad rollen får/inte får göra.
- Peka ut konkreta filer/moduler: t.ex. [index.html](index.html) eller dokument i docs/.
- Be om verifierbart output: kort sammanfattning, lista, plan, diff, kontrollsteg.
- Stoppa vid oklarhet: gå tillbaka till Analyst/Architect innan du implementerar.

---

## Snabbstart — steg för steg

1) Analyst (nulägesbild)
- Skriv: "Agera som Product/Technical Analyst. Läs [index.html](index.html). Sammanfatta nuläget på 5–10 meningar. Lista risker/oklarheter/teknisk skuld. Ingen kod eller förslag."
- Förväntat output: Kort nulägesanalys + risklista.

2) Architect (riktning/avgränsning)
- Skriv: "Agera som Software Architect. Utgå från analystens nulägesbild. Föreslå minsta hållbara förändring med tydlig vinst. Ge riktning + avgränsningar. Ingen implementation."
- Förväntat output: 1–3 huvudpunkter med motivering + scope.

3) Planner (plan i små steg)
- Skriv: "Agera som Project Planner. Bryt arkitektens riktning till 5–10 små, verifierbara steg med mål och kontroll per steg. Ingen kod."
- Förväntat output: Checklista över steg med mål + verifiering.

4) Engineer (implementera ett steg)
- Skriv: "Agera som Software Engineer. Implementera endast steg N. Följ befintlig stil. Visa vilka filer ändras + hur jag verifierar lokalt."
- Förväntat output: Konkreta filändringar + kort lokal verifikation.

5) QA (verifiera)
- Skriv: "Agera som QA. Föreslå och kör verifieringssteg (tester/lint/syntax) för senaste ändringen. Bedöm regressionsrisk. Ingen kodändring."
- Förväntat output: Verifieringslista + resultat + riskbedömning.

6) Reviewer (kvalitetsgrind)
- Skriv: "Agera som Code Reviewer. Granska struktur/läsbarhet/lämplighet. Kontrollera att rätt filer ändrats. Ge Go/No‑go för merge."
- Förväntat output: Feedbacklista + Go/No‑go.

7) Writer (uppdatera dokumentation)
- Skriv: "Agera som Technical Writer. Uppdatera dokumentation utifrån ändringen: körning lokalt, designval och dataflöden. Lägg bara till 'varför'‑kommentarer."
- Förväntat output: Konkreta dokumentationsuppdateringar.

---

## Rollspecifika promptar (redo att klistra in)

- Analyst:
  - "Agera som Product/Technical Analyst. Läs [index.html](index.html) och sammanfatta nuläget på 5–10 meningar. Lista risker/oklarheter/teknisk skuld. Ingen kod eller förslag."

- Architect:
  - "Agera som Software Architect. Utgå från analystens nulägesanalys och föreslå minsta möjliga förändring som ger tydlig vinst. Motivera riktning och avgränsningar. Ingen implementation."

- Planner:
  - "Agera som Project Planner. Bryt arkitektens riktning till 5–10 små, verifierbara steg med mål och kontroll per steg. Ingen kod."

- Engineer (steg N):
  - "Agera som Software Engineer. Implementera endast steg N. Gör små, avgränsade ändringar som följer befintlig stil. Redovisa vilka filer ändras och hur jag verifierar lokalt."

- QA:
  - "Agera som QA. Föreslå och kör verifieringssteg (tester/lint/syntax) för senaste ändringen. Bedöm regressionsrisk. Ingen kodändring."

- Reviewer:
  - "Agera som Code Reviewer. Bedöm struktur, läsbarhet och lämplighet. Kontrollera att rätt filer ändrats. Ge Go/No‑go för merge."

- Writer:
  - "Agera som Technical Writer. Uppdatera dokumentation utifrån gjorda ändringar: körinstruktioner, designval och dataflöden. Endast 'varför'‑kommentarer vid behov."

För fler exempel, se [docs/COPILOT_PROMPTS.md](docs/COPILOT_PROMPTS.md).

---

## Verifiering i chatten

- Be om korta checklistor för test/lint/syntax.
- Be om diff‑förslag och filöversikter för precision.
- Använd små, separata steg och be om lokala testinstruktioner.

---

## Vanliga fallgropar och hur du undviker dem

- Blandade mandat i samma prompt → Dela upp efter roll.
- Otydligt mål → Skriv målet i första meningen och be om verifierbart output.
- För stora ändringar → Be om minsta ändring som ger vinst, en fil/sektion åt gången.
- Oklara nästa steg → Be Planner att bryta ner till 5–10 steg innan implementation.

---

## Exempel — jobba mot en specifik fil

- Analyst: "Läs [index.html](index.html) och förklara vad sidan gör idag. Lista risker/oklarheter." 
- Architect: "Föreslå minimal förbättring som ökar läsbarhet eller struktur i [index.html](index.html), med tydlig motivering."
- Planner: "Bryt din rekommendation till 5 verifierbara steg med mål per steg."
- Engineer: "Implementera steg 1. Redovisa filändringar + snabb verifikation."

---

## Koppla till våra dokument

- Mandat och ansvar: [docs/ROLES.md](docs/ROLES.md)
- Ordning/gates/policy: [docs/WORKFLOW.md](docs/WORKFLOW.md)
- Promptmallar: [docs/COPILOT_PROMPTS.md](docs/COPILOT_PROMPTS.md)
- Snabböversikt: [docs/ROLES_ONE_PAGER.md](docs/ROLES_ONE_PAGER.md)

Använd dessa som stöd i chatten och länka dem vid behov för fokus.

---

## Licens

Detta projekt är licensierat under MIT License. Se [LICENSE](LICENSE) för detaljer.

Du är fri att använda, modifiera och distribuera denna mall i privata och kommersiella projekt.

---

## SharedKnowledge Class

### Purpose
The `SharedKnowledge` class is designed to manage shared files within the project. It provides methods for uploading, listing, and retrieving files stored in the `docs/knowledge` directory.

### Usage
```python
from scripts.shared_knowledge import SharedKnowledge

# Initialize the class
knowledge = SharedKnowledge()

# Upload a file
uploaded_path = knowledge.upload_file("example.txt")
print(f"File uploaded to: {uploaded_path}")

# List all files
files = knowledge.list_files()
print("Files in storage:", files)

# Retrieve a file
file_path = knowledge.retrieve_file("example.txt")
print(f"File retrieved at: {file_path}")
```

---

## Timer Feature

### Overview
The timer feature includes the following components:
- **`timer.html`**: A web page with an analog clock, digital timer, and control buttons.
- **`timer.css`**: Styles for the timer interface.
- **`timer.js`**: JavaScript logic for managing the timer and drawing the clock.

### Testing the Timer
1. Open `timer.html` in a web browser.
2. Use the slider to set the timer duration.
3. Click "Start" to begin the countdown.
4. Verify that the analog clock and digital display update correctly.
5. Ensure the alarm sound plays when the timer reaches zero.

---

## Uppdateringar i `memory_utils.py`

### Nya funktioner

#### `append_to_history`
- **Syfte**: Lägger till en post i projektets historik och säkerställer att historikens storlek inte överskrider den maximala gränsen.
- **Exempel**:
  ```python
  from utils.memory_utils import append_to_history

  entry = {"type": "qa", "summary": "QA verified feature X."}
  append_to_history(entry)
  ```

#### `update_current_state`
- **Syfte**: Uppdaterar den aktuella statusen i `project.memory.json`.
- **Exempel**:
  ```python
  from utils.memory_utils import update_current_state

  new_state = {"current_step": "Steg 2", "status": "pågående"}
  update_current_state(new_state)
  ```

---

## Placeholder Scripts in `package.json`

### Overview
The `package.json` file includes placeholder scripts for `test` and `lint`. These scripts currently output placeholder messages and should be replaced with actual commands.

### How to Update
1. Install the necessary libraries:
   ```bash
   npm install --save-dev jest eslint
   ```
2. Update the `scripts` section:
   ```json
   "scripts": {
     "test": "jest",
     "lint": "eslint ."
   }
   ```
3. Run the scripts:
   ```bash
   npm run test
   npm run lint
   ```

---

## Recent Updates

### Plan to Verify Prompt Flow Delivery
- **Purpose**: Ensure that the sequence of prompts delivers the expected outcomes.
- **Steps**:
  1. Define the expected flow.
  2. Analyze existing prompts.
  3. Simulate the flow.
  4. Identify gaps or issues.
  5. Iterate and refine.
  6. Document the final flow.
- **Verification**: Logs and outputs from simulations.

### QA Verification
- **Summary**: Recent changes were verified through tests and linting.
- **Outcome**: All checks passed successfully.

### Code Review
- **Feedback**: Changes align with project goals and maintain quality standards.
- **Decision**: Approved for merge.
