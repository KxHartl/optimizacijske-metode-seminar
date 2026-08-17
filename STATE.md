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
- [x] Kreiranje sveobuhvatnog inženjerskog plana i radnog registra (`TODO.md`).
- [x] Postavljanje kostura LaTeX dokumenta u `docs/` (`latex_architect`).
- [x] Implementacija i verifikacija numeričkih i analitičkih rješenja u `src/`:
  - [x] Zadatak 1: QP, konveksnost, KKT 4-slučajna analiza, grafički prikaz, dualnost, osjetljivost.
  - [x] Zadatak 2: Robustan QP (egzaktna metoda najgoreg slučaja iz 8. predavanja + Monte Carlo verifikacija na 100 uzoraka).
  - [x] Zadatak 3: Optimizacijska nivelacija ceste (LP formulacija, slučaji A i B, $N=20, 100$).
  - [x] Zadatak 4: Switching sustav, stabilnost modova, monodromijska matrica, LMI sinteza robusnog regulatora stanja i Lyapunov simulacija.
- [x] Pisanje kompletnih LaTeX poglavlja seminara na akademskom hrvatskom jeziku (`docs/chapters/`).
- [x] Recenzija i verifikacija rada (`docs/REVIEW.md` s tablicom tolerancija i paketom pitanja za obranu).
- [x] Finalni release build u `dist/v1.0/OMRiUS_seminar_Kresimir_Hartl.pdf` (38 stranica, $\le 45$ stranica limit zadovoljen).

## Bilješke

- **Zadatak 2**: Egzaktni deterministički robusni ekvivalent uspješno riješen s 8 nejednakosti; analitičko i numeričko rješenje podudaraju se uz odstupanje $< 10^{-8}$.
- **Zadatak 4**: LMI sustav riješen semidefinitnim programiranjem (SDP), eksponencijalna stabilnost zatvorenog kruga verificirana duž svih trajektorija.
- **Kompilacija**: Tectonic XeTeX engine uspješno generira finalni PDF u `dist/v1.0/` bez grešaka.
