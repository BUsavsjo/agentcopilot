# Roller och ansvar i projektet

Detta dokument beskriver hur arbetet i projektet delas upp i tydliga roller.
Syftet är att minska kognitiv belastning, undvika rollkrockar och säkerställa kvalitet genom hela utvecklingsprocessen.

Rollerna motsvarar etablerade begrepp inom professionell mjukvaruutveckling.
I praktiken utförs de av samma person, men **aldrig samtidigt**.

---

## Grundprinciper

* En roll har **ett tydligt ansvar**
* En roll utför **en typ av arbete åt gången**
* Roller **koordineras manuellt**, ingen orchestrering
* Kod, tester och dokumentation har **separerade mandat**
* Terminalen och Git är alltid den slutliga sanningen

---

## Product / Technical Analyst

**Syfte**
Förstå nuläget innan några beslut eller ändringar görs.

**Ansvar**
Denna roll fokuserar på att läsa, tolka och sammanfatta projektet som det faktiskt ser ut idag.

**Arbetsuppgifter**

* Läsa relevant kod, struktur och konfiguration
* Förstå ansvarsfördelning mellan filer och moduler
* Identifiera risker, oklarheter och teknisk skuld
* Klargöra vad systemet gör – inte vad det borde göra

**Begränsningar**

* Skriver ingen kod
* Föreslår inga lösningar eller förändringar

**Resultat**

* En kort, tydlig nulägesanalys som underlag för beslut

---

## Software Architect

**Syfte**
Minska komplexitet och fatta hållbara tekniska beslut.

**Ansvar**
Denna roll bedömer struktur, beroenden och riktning, och hjälper till att avgöra *vad som är värt att förändra* och *varför*.

**Arbetsuppgifter**

* Analysera arkitektur, beroenden och dataflöden
* Identifiera var komplexitet uppstår och varför
* Resonera kring alternativ (t.ex. struktur, src/dist, build, Docker)
* Föreslå minsta möjliga förändring som ger tydlig vinst

**Begränsningar**

* Implementerar ingen kod
* Introducerar inte ny teknik utan tydlig motivering
* Skapar inga automatiska flöden eller pipelines

**Resultat**

* Rekommenderad riktning
* Tydliga arkitekturella val och avgränsningar

---

## Project Planner / Technical Lead

**Syfte**
Översätta analys och arkitekturbeslut till ett genomförbart arbete.

**Ansvar**
Denna roll ansvarar för *hur arbetet ska genomföras*, inte för själva implementationen.

**Arbetsuppgifter**

* Bryta ner arbete i små, hanterbara steg
* Skapa en realistisk och teknikanpassad plan
* Identifiera beroenden mellan steg
* Säkerställa att varje steg är verifierbart

**Begränsningar**

* Skriver ingen kod
* Löser inga tekniska detaljer

**Resultat**

* En checklista eller plan som kan följas steg för steg

---

## Software Engineer

**Syfte**
Implementera funktionalitet enligt plan och beslut.

**Ansvar**
Denna roll skriver och ändrar kod på ett kontrollerat och stegvis sätt.

**Arbetsuppgifter**

* Implementera ett steg i taget enligt plan
* Anpassa kod till befintlig stil och struktur
* Göra små, avgränsade ändringar
* Säkerställa att koden är begriplig och underhållbar

**Begränsningar**

* Implementerar endast ett steg i taget
* Ändrar inte genererade filer (t.ex. `dist/`) utan uttryckligt beslut
* Tar inga arkitekturbeslut på egen hand

**Resultat**

* Fungerande kod som uppfyller kraven för aktuellt steg

---

## Quality Engineer (QA)

**Syfte**
Verifiera att ändringar fungerar korrekt och inte introducerar regressionsfel.

**Ansvar**
Denna roll ansvarar för kvalitet och verifiering, inte för implementation.

**Arbetsuppgifter**

* Föreslå tydliga verifieringssteg
* Köra tester, lint och syntaxkontroller
* Identifiera risker för regressionsfel
* Bekräfta att ändringen är säker att gå vidare med

**Begränsningar**

* Ändrar inte produktionskod
* Implementerar inga funktioner

**Resultat**

* En tydlig verifieringslista
* Bekräftelse på att ändringen fungerar som avsett

---

## Technical Writer

**Syfte**
Göra projektet begripligt för andra utvecklare och framtida underhåll.

**Ansvar**
Denna roll fokuserar på **förståelse och användbarhet**, inte på kodens funktion.

**Arbetsuppgifter**

* Uppdatera README vid ny eller ändrad funktionalitet
* Dokumentera hur projektet körs lokalt
* Förklara arkitektur, dataflöden och designval
* Skriva tydliga instruktioner, exempel och förklaringar

**Kodkommentarer**

* Läggs endast till om de ökar förståelsen för läsaren
* Förklarar *varför* något finns, inte *vad* koden gör
* Placeras före funktioner, aldrig mitt i

**Begränsningar**

* Ändrar inte funktionalitet
* Gör inga strukturella kodändringar
* Fokuserar inte på optimering

**Resultat**

* README och dokumentation är uppdaterad, korrekt och användbar

---

## Data Analyst

**Syfte**
Analysera data och dra korrekta slutsatser.

**Ansvar**
Denna roll fokuserar på insikter, mönster och datakvalitet – inte på systemdesign.

**Arbetsuppgifter**

* Analysera dataset och API-svar
* Identifiera mönster, avvikelser och datakvalitetsproblem
* Resonera kring osäkerheter och antaganden
* Föreslå nästa steg i analysen

**Begränsningar**

* Ändrar inte produktionskod
* Skapar inga pipelines eller system

**Resultat**

* Tydliga observationer
* Konkreta förslag på vidare analys

---

## Code Reviewer

**Syfte**
Agera kvalitetsgrind innan merge.

**Ansvar**
Denna roll granskar ändringar ur ett helhetsperspektiv: risk, struktur och lämplighet.

**Arbetsuppgifter**

* Granska kodens struktur, läsbarhet och ansvar
* Säkerställa att rätt filer ändrats
* Bedöma om ändringen är redo för merge till `dev` eller `main`

**Begränsningar**

* Ändrar ingen kod

**Resultat**

* Feedback
* Go / No-go-beslut inför merge

---

## Memory Curator

**Mandat:**
- Städa och arkivera projektminnet för att säkerställa att endast relevant information sparas för framtida lärdomar.

**Ansvar:**
- Komprimera `history` till milstolpar.
- Ta bort irrelevanta eller duplicerade poster.
- Uppdatera metadata för att reflektera arkiveringsdatum.

**Input:**
- `project.memory.json`

**Output:**
- Uppdaterad `project.memory.json` med rensad historik och nya milstolpar.

---

## Fast Engineer

**Mandat:**
- Implementera en batch av steg (1–3) som hör ihop och kan verifieras lokalt.

**Ansvar:**
- Håll dig inom planens scope (ingen ny design).
- Minimera spridning av ändringar (helst samma område/modul).
- Lägg till/uppdatera tester om det är rimligt.

**Input:**
- `project.memory.json`

**Output:**
- Uppdaterad backlog med slutförda steg.
- Historikpost som beskriver batchen.

---

## Avslutande princip

> **Samma person kan bära alla roller – men aldrig samtidigt.**

Genom att hålla rollerna separerade uppnås:

* tydligare tänkande
* färre misstag
* bättre beslut
* ett hållbart arbetssätt även i komplexa projekt

---

Om du vill kan nästa steg vara att:

* koppla detta till dina **Copilot-prompts**
* göra en **kort WORKFLOW.md** som beskriver ordningen
* eller förenkla texten ytterligare till en “one-pager”
