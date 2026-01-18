# WORKFLOW

Detta dokument beskriver ett praktiskt, verifierbart arbetsflöde som följer rollerna i projektet. Flödet minskar kontextbyten, ger tydliga beslutspunkter och säkerställer kvalitet utan att blanda mandat.

---

## Översikt

Arbetet sker i tydliga faser där varje fas har ett specifikt mål, in-/utdata och kvalitetsgrind. Samma person kan byta roll mellan faserna, men aldrig utföra flera roller samtidigt.

---

## Ordning och leverabler

1. Product / Technical Analyst
   - Mål: Nulägesanalys av kodbas, struktur, konfiguration.
   - Leverabel: Kort, tydlig sammanfattning av vad systemet gör idag, identifierade risker och oklarheter.

2. Software Architect
   - Mål: Välja minsta hållbara förändring som ger tydlig vinst.
   - Leverabel: Rekommenderad riktning, arkitekturella val och avgränsningar (motivering + scope).

3. Project Planner / Technical Lead
   - Mål: Göra arbetet genomförbart.
   - Leverabel: Nedbruten plan i små, verifierbara steg med beroenden och tydliga mål per steg.

4. Software Engineer
   - Mål: Implementera ett steg i taget enl. plan.
   - Leverabel: Små, avgränsade kodändringar som följer befintlig stil; inga arkitekturella extraval.

5. Quality Engineer (QA)
   - Mål: Säkerställa att ändringen fungerar och inte skapar regressioner.
   - Leverabel: Verifieringslista + körda tester/lint/syntax; bedömning av risk.

6. Code Reviewer
   - Mål: Kvalitetsgrind innan merge.
   - Leverabel: Feedback samt Go/No-go för merge till dev/main.

7. Technical Writer
   - Mål: Göra projektet begripligt och körbart för andra.
   - Leverabel: Uppdaterad README/Dokumentation: körinstruktioner, designval, dataflöden.

8. Data Analyst (vid behov)
   - Mål: Dra korrekta slutsatser från data.
   - Leverabel: Observationer, mönster, avvikelser, antaganden och nästa analyssteg.

---

## Kvalitetsgrindar (gates)

- Gate A (efter Analyst): Finns en tydlig och korrekt nulägesbild? Om inte, stoppa.
- Gate B (efter Architect): Är riktningen minimal, motiverad och spårbar? Om inte, revidera.
- Gate C (efter Planner): Är planen verifierbar med små steg? Om inte, bryt ner mer.
- Gate D (efter Engineer): Uppfyller ändringen målet för just det steget? Om inte, iterera.
- Gate E (efter QA): Är risk acceptabel och kontrollerad av tester/lint? Om inte, åtgärda.
- Gate F (Reviewer): Är ändringen redo för merge enligt repo-policy? Om inte, justera.
- Gate G (Writer): Är docs uppdaterat och användbart? Om inte, komplettera.

---

## Branch- och commit-policy

- Branch: Skapa en feature-branch per plansteg; små PRs är standard.
- Commits: Små, atomiska commits med tydlig beskrivning ("why" först, sedan "what").
- PR: Inkludera mål, scope, förändringar och verifiering; länka till plansteg.

---

## Verifiering per steg

- Lint: Kör statiska kontroller och formattering där det är relevant.
- Tester: Starta med smala enhetstester nära ändringen; utöka vid behov.
- Bygge/Körning: Testa bygg/körning lokalt för påverkat område.
- Dokumentation: Uppdatera endast efter arkitektur/plan är klara och ändringen är verifierad.

---

## Snabbchecklista

- Gör bara en roll i taget.
- Håll ändringar små och spårbara.
- Mät mot tydligt mål per steg.
- Stoppa vid otydlighet – gå tillbaka till Analyst/Architect.
- Terminalen och Git är den slutliga sanningen.
