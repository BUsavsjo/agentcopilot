# Release Notes — Process & Mall

En guide för att dokumentera releases och uppdateringar.

---

## Vad är Release Notes?

Release Notes är en sammanfattning av vad som ändrats i en ny version:
- Nya funktioner
- Bugfixes
- Performance-förbättringar
- Beroende-uppdateringar
- **Breaking changes** och migreringsguider

Release Notes hjälper användare att:
- Förstå vad som är nytt
- Bestämma om de bör uppdatera
- Genomföra migreringar om nödvändigt

---

## Version Numbering (Semantic Versioning)

Använd [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (t.ex. 1.2.3)
- **MAJOR:** Breaking change
- **MINOR:** Ny feature, backwards-compatible
- **PATCH:** Bugfix, backwards-compatible

Exempel:
- 1.0.0 → 1.1.0 (ny feature)
- 1.1.0 → 1.1.1 (bugfix)
- 1.1.1 → 2.0.0 (breaking change)

---

## Release Notes Template

Kopiera denna mall för varje release:

```markdown
# Version X.Y.Z — YYYY-MM-DD

## 🎉 Highlights

En kort rad om huvudnyheten eller temat för denna release.

## ✨ Nya funktioner

### [Feature 1]
- **Vad:** Kort beskrivning av vad som är nytt
- **Varför:** Varför behövdes denna feature?
- **Användning:** Kort exempel eller länk till docs

### [Feature 2]
- ...

## 🐛 Bugfixes

- **[Issue #123](länk):** Beskrivning av buggen som åtgärdades
- **[Issue #124](länk):** ...

## 🚀 Performance

- Reducerad load-tid med 20% (från 500ms → 400ms)
- Optimerad database-query för stort dataset
- ...

## 📦 Beroenden (Dependencies)

- `dependency-name`: 1.0.0 → 1.1.0 (ny feature)
- `other-lib`: 2.0.0 → 2.0.1 (bugfix)

## ⚠️ Breaking Changes

Om denna release innehåller breaking changes (MAJOR version bump):

### [Breaking Change 1]
- **Vad ändrades:** Gamla API `foo()` → Nya API `bar()`
- **Varför:** Klarare API, bättre namngivning
- **Migration:** Se migreringsguide nedan

### Migreringsguide

Steg-för-steg instruktioner för att uppdatera från föregående version:

1. Uppdatera dependency: `npm install dependency@X.Y.Z`
2. Uppdatera anrop från `foo()` till `bar()` i din kod
3. Testa lokalt: `npm test`
4. Deploy och verifiera i staging

## 🔗 Länker

- [Fullständig changelog](CHANGELOG.md)
- [GitHub Release](länk)
- [Dokumentation](../README.md)
```

---

## Release Process

### 1. **Engineer/Writer** — Implementera ändringar
- Kod skrivs, testning, reviews (Gate D–F)
- Gränser för ny version bestäms

### 2. **Writer** — Uppdatera Release Notes
- Sammanfatta nya features, bugfixes, breaking changes
- Lägg till version-nummer och datum
- Skriv migreringsguide om breaking changes

### 3. **QA** — Verifiera Release
- Testa alla nya features från Release Notes
- Verifiera migreringsguide (om breaking changes)
- Godkänn innan publicering

### 4. **Maintainer** — Publisera Release
- Skapa Git tag: `git tag vX.Y.Z`
- Skapa GitHub Release med Release Notes
- Publicera paket (om npm/PyPI/etc)

### 5. **Communication** — Meddela användare
- Publicera på webbplats, blog, sociala medier
- Skicka email till abonnenter
- Uppdatera dokumentation

---

## Uppdatering av Changelog

Underhåll även en `CHANGELOG.md` i repo-roten för historia över alla releases:

```markdown
# Changelog

## [1.2.0] — 2026-01-18
### Added
- Feature A
- Feature B

### Fixed
- Bug 1

### Changed
- API improvement

## [1.1.0] — 2026-01-01
...
```

Se [keepachangelog.com](https://keepachangelog.com/) för mer detalj.

---

## Tips

- **Be concise:** 2–3 rader per feature, max
- **Använd enkelt språk:** Anta inte teknisk kunskap från läsaren
- **Länka:** Till relaterade issues, PRs, dokumentation
- **Testa innan publicering:** Se till att allt i Release Notes faktiskt fungerar
- **Migreringsguide:** Obligatorisk för breaking changes, valfri annars

---

Se även:
- [writer.prompt.md](../.github/prompts/writer.prompt.md) — Writer-roll definition
- [.github/pull_request_template.md](../.github/pull_request_template.md) — PR-mall
- [Semantic Versioning](https://semver.org/)
