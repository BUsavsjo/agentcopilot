# Agent Reference — Roller & Workflow

Denna guide dokumenterar de 8 agentroller, deras status i arbetsflödet, nästa steg, körkommandon och quality gates.

Använd detta som referens när du byter roll eller behöver förstå vad en specifik agent bör göra.

---

## 1. Product / Technical Analyst

**STATUS**  
*Startrollen. Alltid först.*

Analyserar nuläget för att förstå kodbas, struktur, risker och oklarheter. Skriver ingen kod, föreslår ingen lösning.

**NÄSTA STEG**  
→ Software Architect (när Analyst-rapporten är klar)

**KÖR SÅ HÄR**

Använd denna prompt i Copilot Chat:

```
/analyst Analysera denna repo: vilken är nuläget, vilka risker finns, vad är oklart?
```

Alternativt, från terminalen:

```powershell
# Läs relevant dokumentation
Get-Content README.md
Get-ChildItem docs/ | ForEach-Object { Write-Host "=== $($_.Name) ===" ; Get-Content $_.FullName -Head 20 }

# Lisera projektstruktur
tree /F /L 2
```

**GATE A — Analyst-rapport godkänd?**

- ✓ Rapport identifierar minst 3 risker eller oklarheter
- ✓ Rapport baseras på faktisk kodbas (inte antaganden)
- ✓ Ingen kod skrivs i denna fas

*Gå vidare till Architect om Gate A är uppfylld.*

---

## 2. Software Architect

**STATUS**  
*Andra rollen. Inväntar Analyst-rapport.*

Väljer minsta hållbara förändring, definierar arkitekturella val och avgränsar scope baserat på Analyst-rapporten.

**NÄSTA STEG**  
→ Project Planner (när arkitekturplan är klar)

**KÖR SÅ HÄR**

Använd denna prompt i Copilot Chat:

```
/architect Baserat på denna analys: [klistra in Analyst-rapport], vad är den minsta förändring som löser det? Ge motivering och scope.
```

Alternativt, analysera befintlig arkitektur:

```powershell
# Undersök modulberoenden
Get-ChildItem -Recurse *.md, *.json | Where-Object { $_.Name -match "config|setup" }

# Kontrollera befintliga grindar/policies
Get-Content CONTRIBUTING.md -Head 50
```

**GATE B — Arkitekturplan godkänd?**

- ✓ Plan baseras på Analyst-rapport (inte ny idé)
- ✓ Scope är tydligt avgränsat
- ✓ Motivering för varje arkitekturellt val
- ✓ Ingen implementering gjord än

*Gå vidare till Planner om Gate B är uppfylld.*

---

## 3. Project Planner / Technical Lead

**STATUS**  
*Tredje rollen. Inväntar arkitekturplan.*

Bryter ner arkitekturplanen i små, verifierbara steg med beroenden, mål och verifieringsmetoder.

**NÄSTA STEG**  
→ Software Engineer (när plan är klar)

**KÖR SÅ HÄR**

Använd denna prompt i Copilot Chat:

```
/planner Bryt ner denna arkitekturplan: [klistra in Architect-plan] i 5–10 små steg. Varje steg ska ha: mål, in/utdata, beroenden, verifiering.
```

Alternativt, planera lokalt:

```powershell
# Granska befintlig plan/checklist om den finns
Get-Content .github/pull_request_template.md -ErrorAction SilentlyContinue

# Lista potentiella steg baserat på filstruktur
Get-ChildItem -Recurse -Include *.md, *.json | Select-Object FullName
```

**GATE C — Plan godkänd?**

- ✓ Minst 5–10 tydligt avgränsade steg
- ✓ Varje steg har mål, in/utdata och verifieringsmetod
- ✓ Beroenden är tydliga
- ✓ Ingen kod skrivs än

*Gå vidare till Engineer om Gate C är uppfylld.*

---

## 4. Software Engineer

**STATUS**  
*Fjärde rollen. Inväntar godkänd plan.*

Implementerar ett steg i taget enligt planen. Små, avgränsade ändringar. Följer befintlig stil. Inga arkitekturella extraval.

**NÄSTA STEG**  
→ Quality Engineer / QA (när ett steg är implementerat)

**KÖR SÅ HÄR**

Använd denna prompt i Copilot Chat:

```
/engineer Implementera endast steg N av denna plan: [klistra in Planner-plan]. Gör små ändringar, följ befintlig stil. Vilka filer ändras?
```

Alternativt, starta implementering lokalt:

```powershell
# Skapa branch för steg N
git checkout -b feature/step-N

# Gör ändringar enligt plan
# Verifiera lokalt enligt steg-beskrivningen
# Commit när steg är klart

git add .
git commit -m "Steg N: [kort beskrivning]"
git push origin feature/step-N
```

**GATE D — Implementation godkänd?**

- ✓ Endast ett steg implementerat
- ✓ Ändringar följer befintlig kodstil
- ✓ Inga arkitekturella extraval
- ✓ Branch är pushad och PR är öppen
- ✓ Lokalt verifierat enligt steg-checklist

*Gå vidare till QA om Gate D är uppfylld.*

---

## 5. Quality Engineer (QA)

**STATUS**  
*Femte rollen. Inväntar implementering.*

Verifierar att ändringen fungerar, inte skadar befintlig funktionalitet och uppfyller acceptanskriterier.

**NÄSTA STEG**  
→ Code Reviewer (när QA är godkänd)

**KÖR SÅ HÄR**

Använd denna prompt i Copilot Chat:

```
/qa Verifiera denna implementation: [länk till PR eller steg-beskrivning]. Vad ska testas? Vilka regressionsrisker finns?
```

Alternativt, testa lokalt:

```powershell
# Checkout feature branch
git checkout feature/step-N

# Kör tests/lint
npm test
npm run lint

# Manuell verifiering enligt steg-checklist
# Dokumnentera resultat i PR-kommentar
```

**GATE E — QA godkänd?**

- ✓ Acceptanskriterier från steg är uppfyllda
- ✓ Ingen regression i befintlig funktionalitet
- ✓ Tester/lint körda och godkända
- ✓ Risker identifierade och dokumenterade
- ✓ Rekommendation: Go/No-go för Review

*Gå vidare till Reviewer om Gate E är uppfylld.*

---

## 6. Code Reviewer

**STATUS**  
*Sjätte rollen. Inväntar QA-godkännande.*

Granskar kod mot stil, arkitektur, säkerhet och best practices. Slutgiltig kvalitetsgrind innan merge.

**NÄSTA STEG**  
→ Technical Writer (om Reviewer godkänner) ELLER tillbaka till Engineer (om ändringar behövs)

**KÖR SÅ HÄR**

Använd denna prompt i Copilot Chat:

```
/reviewer Granska denna PR: [länk]. Kontrollera: kodstil, arkitektur, säkerhet, best practices. Go/No-go för merge?
```

Alternativt, granska manuellt:

```powershell
# Visa ändringar
git diff main feature/step-N

# Checka mot CONTRIBUTING.md
Get-Content CONTRIBUTING.md

# Lämna feedback i GitHub PR-UI eller lokalt
# Godkänn eller begär ändringar
```

**GATE F — Review godkänd?**

- ✓ Kod följer projektets stil och konventioner
- ✓ Inga säkerhetsproblem identifierade
- ✓ Arkitektur överensstämmer med plan
- ✓ PR-mallen är ifylld korrekt
- ✓ Godkännande eller begäring om ändringar är dokumenterad

*Gå vidare till Writer om Gate F är godkänd. Om ändringar behövs, tillbaka till Engineer.*

---

## 7. Technical Writer

**STATUS**  
*Sjunde rollen. Inväntar Review-godkännande.*

Uppdaterar dokumentation, README, inline-kommentarer och releases notes för att hålla projektet förståeligt.

**NÄSTA STEG**  
→ Merge till dev/main (när Writer är klar)

**KÖR SÅ HÄR**

Använd denna prompt i Copilot Chat:

```
/writer Uppdatera dokumentation för denna ändring: [länk till PR]. Vilka filer ska uppdateras? Vad ska skriva?
```

Alternativt, uppdatera dokumentation lokalt:

```powershell
# Granska ändring
git show feature/step-N

# Uppdatera relevanta docs
# Exempel: README.md, docs/, inline-kommentarer

# Commit dokumentation
git add docs/ README.md
git commit -m "Docs: Uppdatera för steg N"

# Push och uppdatera PR
git push origin feature/step-N
```

**GATE G — Documentation godkänd?**

- ✓ README eller docs/ uppdaterad om relevant
- ✓ Inline-kommentarer är tydliga och uppdaterade
- ✓ Release notes eller CHANGELOG uppdaterade
- ✓ Externa beroenden eller setup-ändringar dokumenterade
- ✓ Länka är funktionella och uppdaterade

*Nästa steg: Merge till dev/main när alla grindar är godkända.*

---

## 8. Data Analyst (Optional)

**STATUS**  
*Valfri, parallell roll. Kan köras efter Engineer eller separat.*

Analyserar effekt av ändring (performance, användarmönster, fel) för validering och lärande.

**NÄSTA STEG**  
→ Integreras i nästa cykel eller rapporteras som feedback

**KÖR SÅ HÄR**

Använd denna prompt i Copilot Chat:

```
/data-analyst Analysera effekten av denna ändring: [länk eller beskrivning]. Vilka KPIS påverkas? Vad säger data?
```

Alternativt, manuell analys:

```powershell
# Samla metrics från prod/staging (om tillgängligt)
# Jämför före/efter ändringen
# Dokumentera fynd i issues eller wiki

# Exempel:
Get-Content ./metrics.json | ConvertFrom-Json
```

**GATE (Optional)** — Data-rapport?

- ✓ Effektanalys är baserad på faktiska data
- ✓ Jämförelse före/efter är dokumenterad
- ✓ Resultat är åtgärdsbara för nästa iteration

---

## Snabbkolla — Status-matrix

| Roll | Ordning | In-data | Out-data | Nästa roll |
|------|---------|---------|----------|-----------|
| **Analyst** | 1 | Kodbas | Nulägesanalys + risker | Architect |
| **Architect** | 2 | Nulägesanalys | Arkitekturplan | Planner |
| **Planner** | 3 | Arkitekturplan | Steg-för-steg plan | Engineer |
| **Engineer** | 4 | Plan | Kod-ändringar + branch | QA |
| **QA** | 5 | Branch + PR | Test-rapport + rekommendation | Reviewer |
| **Reviewer** | 6 | PR + tester | Godkännande/ändringar | Writer (eller Engineer) |
| **Writer** | 7 | Godkänd PR | Uppdaterad dokumentation | Merge |
| **Data Analyst** | (opt) | Prod-metrics | Effektanalys | Nästa cykel |

---

## Vanliga arbetsmönster

### Pattern 1: En loop (En person, alla roller)

```
Person X → Analyst → Architect → Planner → Engineer → QA → Reviewer → Writer → Merge
```

**Använd när:** Du jobbar själv eller i litet team.  
**Fördel:** Enkel överblick.  
**Risk:** Burnout om loops är för stora.

### Pattern 2: Specialisering (Olika personer)

```
Analyst Team → Architect Team → Planner → Engineer Team → QA Team → Reviewer → Writer → Merge
```

**Använd när:** Större projekt eller team.  
**Fördel:** Fokusering per expertis.  
**Risk:** Kommunikations-overhead.

### Pattern 3: Parallell QA + Writer

```
Engineer → QA (parallell) ─┐
                           ├→ Reviewer → Merge
         Writer (parallal) ─┘
```

**Använd när:** PR är stort och kräver parallell testning + dokumentation.  
**Fördel:** Snabbare iteration.  
**Risk:** Koordinations-overhead.

---

## Tips

- **Alltid samma ordning (1–7).** Inga hoppa över eller omordningar.
- **En person, en roll åt gången.** Byt roll mellan steg, men aldrig samtidigt.
- **Gates är inflexibla.** Om en gate inte är uppfylld, gå tillbaka och fixa.
- **Använd Copilot Chat.** Meddela agenten vilken roll du är i. Prompt-filerna finns i `.github/prompts/`.
- **Dokumentera allt.** Commit-meddelanden, PR-kommentarer, checklist — allt är data för nästa iteration.

---

Se även:
- [ROLES.md](ROLES.md) — Detaljerade rolldefinitioner
- [WORKFLOW.md](WORKFLOW.md) — Processöversikt och grindar
- [COPILOT_PROMPTS.md](COPILOT_PROMPTS.md) — Prompt-templates
- [.github/prompts/](../.github/prompts/) — Prompt-filer för varje roll
- [CONTRIBUTING.md](../CONTRIBUTING.md) — Bidragarguide

---

# Memory Policy

## History Rules
- **Maximum Size:** The `history` array in `project.memory.json` is limited to 50 entries.
- **Entry Format:** Each entry in `history` must follow this format:
  - `date`: ISO 8601 date string.
  - `type`: One of `change`, `qa`, or `review`.
  - `summary`: A brief description (1–2 sentences).
- **Roles Allowed to Write:**
  - `Engineer`: Logs changes made to the system.
  - `QA`: Logs verification results and identified risks.
  - `Reviewer`: Logs feedback or code review notes.

## Writer Responsibility
- The Writer role is responsible for performing a **Memory Sweep** after each completed step:
  - Compress the `history` array into a `milestone`.
  - Clear the `history` array after compression.

### Example Workflow
1. **Before Memory Sweep:**
   ```json
   "history": [
     {
       "date": "2026-01-19T12:00:00Z",
       "type": "change",
       "summary": "Updated the memory policy documentation."
     },
     {
       "date": "2026-01-19T13:00:00Z",
       "type": "qa",
       "summary": "Verified memory policy implementation."
     }
   ]
   ```

2. **After Memory Sweep:**
   ```json
   "milestones": [
     {
       "summary": "Compressed milestone from history.",
       "details": [
         {
           "date": "2026-01-19T12:00:00Z",
           "type": "change",
           "summary": "Updated the memory policy documentation."
         },
         {
           "date": "2026-01-19T13:00:00Z",
           "type": "qa",
           "summary": "Verified memory policy implementation."
         }
       ]
     }
   ]
   ```

3. **Cleared History:**
   ```json
   "history": []
   ```

## Memory System Interactions

#### Example: Engineer Role
- Reads the current state from memory:
  ```python
  from utils.memory_utils import read_memory
  memory = read_memory()
  print(memory['now'])
  ```
- Appends a history entry:
  ```python
  from utils.memory_utils import append_to_history
  entry = {"type": "change", "summary": "Implemented feature X."}
  append_to_history(entry)
  ```

#### Example: Writer Role
- Reads memory to compress history into milestones:
  ```python
  memory = read_memory()
  milestones = memory['milestones']
  ```
- Clears history after creating a milestone:
  ```python
  memory['history'] = []
  ```
