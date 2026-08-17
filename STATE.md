# STATE

## Projekt

- **Naziv**: Optimizacijske metode u razvoju i upravljanju sustava — Seminarski rad
- **Tip**: Seminar (FSB)
- **Kolegij**: Optimizacijske metode u razvoju i upravljanju sustava (OMRiUS)
- **Student**: Krešimir Hartl
- **Mentor**: Prof. dr. sc. Andrej Jokić
- **LaTeX format**: FSB Seminar (`fsb-seminar`)

## Trenutni fokus

- [x] Inicijalizacija repozitorija, okruženja i RAG baze podataka.
- [x] Transkripcija i analiza specifikacije zadataka (`TASK/zadatak_omrius.md`).
- [ ] Postavljanje kostura LaTeX dokumenta u `docs/` (`latex_architect`).
- [ ] Implementacija i verifikacija numeričkih i analitičkih rješenja u `src/`:
  - Zadatak 1: QP, konveksnost, KKT, grafički prikaz, dualnost, osjetljivost.
  - Zadatak 2: Robustan QP (egzaktna metoda iz 8. predavanja + Monte Carlo verifikacija).
  - Zadatak 3: Optimizacijska nivelacija ceste (LP formulacija, slučaji A i B, $N=20, 100$).
  - Zadatak 4: Switching sustav, stabilnost modova, LMI sinteza robusnog regulatora stanja i simulacija.
- [ ] Pisanje LaTeX poglavlja seminara (`writer`).
- [ ] Recenzija i verifikacija rada (`qa_reviewer`).
- [ ] Finalni build u `dist/`.

## Bilješke

- **Zadatak 2 (Važno)**: Rješavati prema egzaktnoj formulaciji iz 8. predavanja (najgori slučaj za poliedarska/intervalna ograničenja), a ne diskretnim odabirom točaka.
- **RAG baza**: LanceDB baza je indeksirana s 14 PDF dokumenata (predavanja, vježbe, referentni seminar). Za sve citate koristiti `rag query`.
- **Kompilacija**: Koristi se `tectonic` / MiKTeX (`pdflatex`).

---

## Obavezno prije pozivanja agenta

Popuni `.ai/config/project.yaml` — `latex_architect` čita metapodatke za
naslovnicu odatle (ne iz ovog fajla):

```yaml
author_name: "Ime Prezime"
course_name: "NAZIV KOLEGIJA"
seminar_title: "Puni naslov seminara"
seminar_title_short: "Kratki naslov za header"
professor_title: "Prof. dr. sc."
professor_name: "Ime Prezime"
```

Agent neće nastaviti dok ta 4 obavezna polja nisu popunjena:
`author_name`, `course_name`, `seminar_title`, `professor_name`.
