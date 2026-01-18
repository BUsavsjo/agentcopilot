# QA Checklist

En generisk kontrollista för Quality Assurance och verifiering av ändringar.

---

## Innan du börjar

Säkerställ att du har:
- [ ] Tillgång till senaste branch/PR
- [ ] Acceptanskriterier från Planner-steg
- [ ] Tidigare tester/lint-resultat för jämföring
- [ ] Test- och produktionsmiljö tillgänglig

---

## 1. Funktionalitet — Acceptanskriterier

- [ ] **Alla acceptanskriterier från steg är uppfyllda** — Jämför PR mot Planner-plan
- [ ] **Huvudflödet fungerar** — Testa det primära användarflödet
- [ ] **Kantfall är hanterade** — Testa gränsvärden och felscenarier
- [ ] **Indata valideras** — Dålig indata hanteras gracefullt
- [ ] **Felmeddelanden är tydliga** — Användare förstår vad som gick fel

**Verifiering:**
```
Local: npm test
CI: [Se PR-checks]
```

---

## 2. Regression — Befintlig funktionalitet

- [ ] **Befintlig funktionalitet fungerar** — Kör tidigare testsaker igen
- [ ] **Systemet startar utan fel** — Ingen "breaking change" från setup/config
- [ ] **Användar gränssnitt är oförändrat** (om relevant) — UI-layout brustit någonstans?
- [ ] **Databasen/API:er svarar som tidigare** — Samma response-format?
- [ ] **Performance är densamma eller bättre** — Ingen märkbar slowdown?

**Verifiering:**
```
Local: npm test (befintliga tester)
Staging/Prod: Smoke test av huvudflöden
```

---

## 3. Kodkvalitet — Stil och Lint

- [ ] **Linter-fel är 0** — `npm run lint` eller motsvarande
- [ ] **Kod följer projektets konventioner** — Indenting, namngivning, etc.
- [ ] **Ingen oanvänd kod eller imports** — `npm run lint` eller manual review
- [ ] **Kommentarer är klara och "varför"-fokuserade** — Inte "vad"-kommentarer
- [ ] **Länge på funktioner/metoder är rimlig** — Inte över 50–100 rader

**Verifiering:**
```
Local: npm run lint
```

---

## 4. Syntax och Type-checking

- [ ] **Ingen syntax-fel** — Koden är válid JavaScript/TypeScript/Python/etc.
- [ ] **Type-checking passar** (om TypeScript/mypy) — `npm run type-check` eller motsvarande
- [ ] **Inga deprecated API:er används** — Använd senaste stabila version
- [ ] **Importer är korrekta** — Inga "cannot find module"-fel

**Verifiering:**
```
Local: npm run type-check
Local: npm test (syntax-check inbyggd)
```

---

## 5. Dokumentation och Metadata

- [ ] **PR-mallen är ifylld korrekt** — Alla sektioner är besvarade
- [ ] **Commit-meddelanden är tydliga** — "Vad" och "Varför", inte bara "fix bug"
- [ ] **Ändringsloggen är uppdaterad** (om relevant) — CHANGELOG eller Release Notes
- [ ] **Länkar i dokumentation fungerar** — Inga 404:or
- [ ] **README uppdaterat** (om relevant) — Nya features dokumenterade?

**Verifiering:**
```
Manual: Läs PR description + commits
Manual: Klicka på alla docs-länkar
```

---

## 6. Säkerhet

- [ ] **Ingen secrets läckade** — Inga API-nycklar, lösenord, tokens i kod
- [ ] **Input-validering är på plats** — User input sanifieras (om relevant)
- [ ] **SQL Injection-säkerhet** (om databasanslutning) — Använd prepared statements
- [ ] **XSS-skydd** (om web-app) — HTML escapat, CSP header satt
- [ ] **CORS-konfiguration är korrekt** — Inte för öppen

**Verifiering:**
```
Manual: Läs kod för känslig data
Manual: Testa med ondskefull indata
Security scan: npm audit (om Node.js projekt)
```

---

## 7. Regressionsriskbedömning

Bedöm sannolikhet × påverkan för varje risk:

| Risk | Sannolikhet | Påverkan | Mitigation |
|------|-------------|----------|-----------|
| Att API ändras och bryter clients | Låg | Högt | Backtests, versioning |
| Att database-schema missmatchas | Låg | Högt | Migration-test |
| Att ny dependency skapar konflikt | Låg | Medel | npm audit, lock-file |
| Att performance degraderas | Låg | Låg | Profiling, benchmarks |

**Övergripande risk-nivå:**
- [ ] 🟢 **Låg risk** — Go för merge
- [ ] 🟡 **Medel risk** — Go med mitigering eller ytterligare testning
- [ ] 🔴 **Högt risk** — No-go, kräver ändringar innan merge

---

## 8. Recommendation: Go/No-go

**Baserat på all testning ovan:**

### Go ✅
- Alla acceptanskriterier uppfyllda
- Ingen regression detekterad
- Linter och type-check passar
- Låg regressionsrisk
- **Nästa steg: Reviewer** för kod-granskning

### No-go ❌
- Ett eller flera acceptanskriterier INTE uppfyllda
- Regression detekterad
- Linter-fel eller type-fel
- Högt regressionsrisk utan mitigering
- **Nästa steg: Engineer** för åtgärd

### Go with caveats ⚠️
- Acceptanskriterier uppfyllda men med begränsningar
- Medel regressionsrisk med dokumenterad mitigering
- **Nästa steg: Reviewer** + notering om caveat

---

## QA-rapport template

Kopiera denna sektion och fyll i din QA-rapport som PR-kommentar:

```markdown
## QA-rapport

**Datum:** [idag]
**Branch:** [branch-namn]
**Testad av:** [din namn]

### Sammanfattning
[1–2 meningar om vad som testades och resultat]

### Testning
- [ ] Funktionalitet: PASS / FAIL
- [ ] Regression: PASS / FAIL
- [ ] Kodkvalitet: PASS / FAIL
- [ ] Säkerhet: PASS / FAIL

### Regressionsrisk
- **Nivå:** 🟢 Låg / 🟡 Medel / 🔴 Högt
- **Motivering:** [kort beskrivning av risker identifierade]

### Rekommendation
**Go** / **No-go** / **Go with caveats**

[Eventuella noteringar eller begärda åtgärder]
```

---

Se även:
- [qa.prompt.md](../.github/prompts/qa.prompt.md) — QA-roll definition
- [.github/pull_request_template.md](../.github/pull_request_template.md) — PR-mall
- [ROLES.md](ROLES.md) — QA-rollen i detalj
