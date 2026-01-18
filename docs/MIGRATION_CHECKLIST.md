# Migration Checklist — Använda denna mall i nya projekt

En steg-för-steg checklist för att anpassa denna agent-workflow-mall för ett nytt projekt.

---

## Förutsättningar

Innan du börjar, se till att du har:
- [ ] **Git installerat** — `git --version`
- [ ] **GitHub konto** — För att hoosta repot
- [ ] **VS Code installerat** — Editor
- [ ] **GitHub Copilot + Copilot Chat extension** — Installerad i VS Code
- [ ] **Node.js (valfritt)** — Om projektet behöver npm/JavaScript
- [ ] **PowerShell 5.1+ (Windows)** eller **sh/bash (Unix)** — För scripts

---

## Steg 1: Clone eller fork denna repo

**Option A: Fork på GitHub (rekommenderat för eget projekt)**
```
1. Gå till https://github.com/BUsavsjo/agentcopilot
2. Klicka "Fork" (övre höger)
3. Välj din Github-konto som destination
4. Clone din fork lokalt:
   git clone https://github.com/[din-user]/agentcopilot.git
   cd agentcopilot
```

**Option B: Clone direkt (om du bara vill testa)**
```
git clone https://github.com/BUsavsjo/agentcopilot.git
cd agentcopilot
```

---

## Steg 2: Uppdatera projekt-metadata

Anpassa för ditt projekt:

### Uppdatera README.md
- [ ] Byt rubrik från "Använda Copilot Chat..." till ditt projekt-namn
- [ ] Uppdatera första paragrafen med ditt projekts syfte
- [ ] Lägg till eller ta bort relevanta roller (t.ex. Data Analyst är valfri)

### Uppdatera package.json (om Node.js projekt)
```json
{
  "name": "ditt-projekt-namn",
  "version": "0.1.0",
  "description": "Din projektbeskrivning",
  "author": "Din namn",
  "license": "MIT"
}
```

### Uppdatera index.html
- [ ] Byt rubrik från "agentcopilot" till ditt projekt-namn
- [ ] Uppdatera subtitle om relevant

---

## Steg 3: Anpassa doctor.ps1 för ditt projekt

Uppdatera `scripts/doctor.ps1` för din miljö:

```powershell
# Redigera dessa variabler:

# Rad ~7: Minsta PowerShell-version
$PowerShellMinVersion = "5.1"

# Rad ~8: Erforderliga mappar
$RequiredFolders = @("docs", ".github", ".vscode", "src")  # Lägg till "src" om du behöver

# Rad ~9: Valfria mappar
$OptionalFolders = @("output", "data", "scripts", "tests")  # Anpassa för ditt projekt

# Rad ~10: Erforderliga filer
$RequiredFiles = @("README.md", "LICENSE", "CONTRIBUTING.md")  # Lägg till/ta bort efter behov
```

Spara och test:
```powershell
.\scripts\doctor.ps1
```

---

## Steg 4: Anpassa .vscode/tasks.json

Uppdatera VS Code tasks för ditt projekt-setup:

```json
{
  "tasks": [
    {
      "label": "Doctor",
      "command": "${workspaceFolder}/scripts/doctor.ps1"
      // Ändra inte detta, det är default
    },
    {
      "label": "Test",
      "command": "npm",  // Byt till "python -m pytest" om Python projekt
      "args": ["test"]   // Anpassa för din test-runner
    },
    {
      "label": "Lint",
      "command": "npm",  // Byt till "pylint" eller "black" om Python
      "args": ["run", "lint"]
    },
    // Lägg till fler tasks för ditt projekt-specifika behov
  ]
}
```

---

## Steg 5: Uppdatera CONTRIBUTING.md

Anpassa bidragarguiden:

- [ ] Byt länk från detta repo till ditt repo i "se även"-sektionen
- [ ] Lägg till eller ta bort roller om relevant (t.ex. om du inte använder Data Analyst)
- [ ] Uppdatera exempel för ditt projekt-teknostack

---

## Steg 6: Uppdatera LICENSE

Anpassa copyright för ditt projekt:

```
MIT License

Copyright (c) 2026 [Ditt namn eller organisation]
```

Eller välj en annan licens från [choosealicense.com](https://choosealicense.com/) om du föredrar det.

---

## Steg 7: Installera dependencies och kör doctor

```powershell
# Om Node.js projekt:
npm install

# Kör doctor för att verifiera miljö:
.\scripts\doctor.ps1
```

Förväntat output: ✓ Alla checks passar (eller ⚠ med varningar).

---

## Steg 8: Gör första Analyst-analys

Analysera ditt nytt projekt innan någon utveckling:

```powershell
# I VS Code:
# 1. Öppna Copilot Chat (Copilot-ikonen i Activity Bar)
# 2. Kopiera prompt från .github/prompts/router.prompt.md
# 3. Eller använd /router direkt
# 4. Välj /analyst
# 5. Fyll i: "Analysera detta nytt projekt. Vad är nuläget, mål, risker?"
```

Resultat: En initial analysis issue som grund för nästa steg (Architect).

---

## Steg 9: Skapa GitHub Issues för första cykeln

Baserat på din Analyst-rapport, skapa GitHub Issues för:
- Architect-arbete
- Planner-arbete
- En eller två Engineer-steg för MVP

Använd issue-templatens:
- `.github/ISSUE_TEMPLATE/analyst.md`
- `.github/ISSUE_TEMPLATE/architect.md`
- `.github/ISSUE_TEMPLATE/planner.md`

---

## Steg 10: Publisera som GitHub Template (valfritt)

Om du vill att andra ska kunna använda ditt projekt som template:

1. **GitHub Settings** → Repository details
2. Checka "Template repository"
3. Spara

Nu kan andra klicka "Use this template" på din repo-sida.

---

## Verifiering — Är allting redo?

Kör denna kontroll:

- [ ] `./scripts/doctor.ps1` passar utan kritiska fel
- [ ] `README.md` är uppdaterad för ditt projekt
- [ ] `LICENSE` har korrekt copyright
- [ ] `.vscode/tasks.json` har rätt tasks för ditt setup
- [ ] Första Analyst-issue är skapad
- [ ] Prompt-filerna i `.github/prompts/` är tillgängliga
- [ ] index.html linkerar korrekt

---

## Nästa steg — Börja arbeta

1. **Välj roll via Router:**
   ```
   /router
   ```

2. **Följa arbetsflödet:**
   - Analyst → Architect → Planner → Engineer → QA → Reviewer → Writer

3. **Använd tasks i VS Code:**
   - `Ctrl+Shift+B` för default task (t.ex. Test eller Doctor)
   - `Ctrl+Shift+P` → "Tasks: Run Task" för att lista alla

4. **Öppna PRs med denna template:**
   ```
   `.github/pull_request_template.md`
   ```

---

## Troubleshooting

### Doctor-scriptet misslyckas
- **Fel:** PowerShell execution policy
- **Lösning:** `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process`

### Copilot Chat fungerar inte
- **Lösning:** Verifiera att GitHub Copilot och Copilot Chat är installerat i VS Code
- **Tips:** Öppna Command Palette (`Ctrl+Shift+P`) och sök "Copilot"

### Tasks.json körs inte
- **Lösning:** Verifiera att du är i rätt mapp (`${workspaceFolder}`)
- **Tips:** Öppna integrated terminal i VS Code: `Ctrl+` ` (backtick)

---

Se även:
- [ROLES.md](ROLES.md) — Roller definition
- [WORKFLOW.md](WORKFLOW.md) — Arbetsflöde
- [README.md](../README.md) — Huvudguide
- [CONTRIBUTING.md](../CONTRIBUTING.md) — Bidragarguide
- [Router](./.github/prompts/router.prompt.md) — Hjälp att välja roll
