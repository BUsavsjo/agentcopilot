# Använda Copilot Chat i VS Code — Praktisk guide

Den här README:n visar hur du använder Copilot Chat i VS Code på ett pedagogiskt och effektivt sätt, med tydliga mandat per roll och verifierbara leverabler. Guiden bygger på våra roller och arbetsflöden i dokumenten:

- Roller: se [docs/ROLES.md](docs/ROLES.md)
- Arbetsflöde: se [docs/WORKFLOW.md](docs/WORKFLOW.md)
- Rollspecifika promptmallar: se [docs/COPILOT_PROMPTS.md](docs/COPILOT_PROMPTS.md)
- One‑pager: se [docs/ROLES_ONE_PAGER.md](docs/ROLES_ONE_PAGER.md)

---

## Prompts i repo

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

## Appendix: Slash‑kommandon

De flesta VS Code Copilot Chat‑versioner stöder enkla slash‑kommandon kombinerat med kontext‑referenser.

**Vanliga kommandon:**
- `/explain`: Förklara
- `/fix`: Föreslå ändringar
- `/tests`: Generera/verifiera tester
- `/help`: Lista stödda kommandon

**Kontext‑referenser:**
- `@workspace`: Helhetskontxt om repo
- `@editor`: Aktuell fil (use `#selection` för markerad kod)
- `@terminal`: Senaste terminaloutput

### Exempel per roll

**Analyst:**
- `/explain @workspace Agera som Product/Technical Analyst. Sammanfatta nuläget och lista risker/oklarheter/teknisk skuld. Ingen kod.`

**Architect:**
- `/explain @workspace Agera som Software Architect. Föreslå minsta hållbara förändring med riktning + avgränsningar och motivering. Ingen implementation.`

**Planner:**
- `/explain @workspace Agera som Project Planner. Bryt riktningen till 5–10 små, verifierbara steg (Mål/Verifiering/Beroenden). Ingen kod.`

**Engineer:**
- `/fix @editor #selection Agera som Software Engineer. Implementera steg N. Föreslå minimal diff och lista filer som ändras + verifikationssteg.`

**QA:**
- `/tests @workspace Agera som QA. Föreslå verifieringsstep (tester/lint/syntax) och bedöm regressionsrisk. Ingen kodändring.`

**Reviewer:**
- `/explain @workspace Agera som Code Reviewer. Bedöm struktur/läsbarhet/lämplighet och ge Go/No‑go.`

**Writer:**
- `/explain @workspace Agera som Technical Writer. Föreslå dokumentationsuppdateringar baserat på senaste ändringen.`
