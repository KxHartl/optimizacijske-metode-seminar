# STATE

## Projekt

- **Naziv**: Optimizacijske metode u razvoju i upravljanju sustava — Seminarski rad
- **Tip**: Seminar (FSB)
- **Kolegij**: Optimizacijske metode u razvoju i upravljanju sustava (OMRiUS)
- **Student**: Krešimir Hartl
- **Mentor**: Prof. dr. sc. Andrej Jokić
- **LaTeX format**: FSB Seminar (`fsb-seminar`)
- **Trenutna verzija**: v1.2 — `dist/v1.2/OMRiUS_seminar_Kresimir_Hartl.pdf`, 27 stranica

## Trenutni fokus

- [x] Verzija v1.0 (38 str.) i šest neovisnih recenzija u `for_validator/`.
- [x] **v1.2 — pročišćavanje rada** (rujan 2026.):
  - [x] MATLAB je jedini izvor rezultata i slika; Python implementacija uklonjena.
  - [x] YALMIP instaliran u `~/Documents/MATLAB/YALMIP` uz `startup.m`; SDPT3 dolazi s R2025b.
  - [x] Iz `task4` uklonjena hardkodirana zamjenska vrijednost $K$; LMI se stvarno rješava.
  - [x] `run_all.m` zapisuje konzolni ispis u `docs/code/task*_output.txt` — jedini referentni izvor brojki.
  - [x] Poglavlja prepisana po podzadacima (a)–(f), u notaciji s vježbi ($Gx-h\leq0$, $\theta(\mu)$, vektor $v$).
  - [x] Uklonjeno što zadatak ne traži: taksonomija, cijena robusnosti, smjernice za praksu, 5 od 12 slika.
  - [x] MATLAB kod i stvarni ispis priloženi uz svaki zadatak.
  - [x] `for_validator/`, `docs/REVIEW.md`, `BENCHMARK_RESULTS.md` i `DEFENSE_QA_PACKAGE.md` sinkronizirani.

## Preostalo prije predaje

- [ ] **JMBAG** — `\authorid` u `docs/main.tex` je zamjenski tekst `0035 XXX XXX`.

## Bilješke

- **Notacija** je usklađena s profesorovim materijalima: Vježbe 3 (isti tip zadatka
  a)–f), `Gx - h ≤ 0`, `θ(μ)`, tablica svih $2^m$ kombinacija aktivnosti,
  perturbacijski vektor `v`), Vježbe 4 ($\ell_1$-aproksimacija za Zadatak 3),
  Predavanje 7 (kvadratna stabilnost, `Q = P⁻¹`, `Y = KP⁻¹`), Predavanje 8
  (robusno optimiranje nad poliedarskim skupovima nesigurnosti).
- **Zadatak 1**: naš rezultat `x* = (190/33, 140/33)` je točan; u tuđem seminaru
  koji je poslužio kao usporedba (`data/sources/matija/`) rezultat
  `(5.4762, 4.5238)` ne zadovoljava uvjet stacionarnosti — nije preuzet.
- **Zadatak 2**: Monte Carlo pod MATLAB-ovim `rng(42)` daje **54/100** kršenja za
  nominalnu točku (ne 57/100 kao u v1.0, gdje je brojka bila iz Pythona).
- **Zadatak 3**: podjela `J*` na iskop i nasip nije jedinstvena — LP je
  degeneriran, pa su ti stupci uklonjeni iz tablice.
- **Zadatak 4**: LMI se rješava uz normalizaciju `Q ⪰ I`, `M_i ⪯ -I` i kriterij
  `min ‖Y‖₂`, što daje `K = [-3.424629, -0.104650]`, `α = 0.288374 s⁻¹`.
- **MATLAB R2025b gotcha**: u `-batch` načinu figure se crtaju prema tamnoj temi
  bez obzira na `Figure.Color`, pa `src/common/config_plot.m` eksplicitno
  postavlja sve boje na svijetle.
