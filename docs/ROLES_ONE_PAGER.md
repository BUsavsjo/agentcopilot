# ROLES — ONE PAGER

En snabböversikt som sammanfattar roller, mandat och ordning.

---

## Grundprinciper

- En roll per fas; inga blandade mandat.
- Små, verifierbara steg; terminal och Git är sanningen.
- Kod, tester och dokumentation har separata ansvar.

---

## Ordning

1. Analyst: Nulägesbild
2. Architect: Minimal, motiverad riktning
3. Planner: Verifierbar plan
4. Engineer: Implementera ett steg
5. QA: Verifiera och bedöm risk
6. Reviewer: Go/No-go
7. Writer: Uppdatera dokumentation
8. Data Analyst (vid behov): Insikter från data

---

## Do / Don't per roll

- Analyst: Gör nulägesanalys / Gör inte förändringar
- Architect: Föreslå minimal förändring / Implementera inte
- Planner: Bryt ner i steg / Lös inte teknik
- Engineer: Små, avgränsade ändringar / Ta inte arkitekturbeslut
- QA: Verifiera kvalitet / Ändra inte produktionskod
- Reviewer: Bedöm helheten / Ändra ingen kod
- Writer: Uppdatera docs / Optimera inte
- Data Analyst: Dra slutsatser / Bygg inga pipelines

---

## Kvalitetsgrindar

- A: Nuläget är begripligt
- B: Riktning är minimal och motiverad
- C: Plan är verifierbar
- D: Steg levererar målet
- E: Risk acceptabel
- F: Merge-lämpligt
- G: Docs uppdaterat

---

## Snabb check

- Är målet för fasen mätbart?
- Är ändringen den minsta som fungerar?
- Är nästa steg tydligt?
