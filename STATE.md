# STATE

## Projekt

- **Naziv**: Optimizacijske metode u razvoju i upravljanju sustava — Seminarski rad
- **Tip**: Seminar (FSB)
- **Kolegij**: Optimizacijske metode u razvoju i upravljanju sustava (OMRiUS)
- **Student**: Krešimir Hartl
- **Mentor**: Prof. dr. sc. Andrej Jokić
- **LaTeX format**: FSB Seminar (`fsb-seminar`)
- **Trenutna verzija**: v1.6 — `dist/v1.6/OMRiUS_seminar_Kresimir_Hartl.pdf`, 30 fizičkih stranica
  (naslovnica, 2 stranice skena zadatka, sadržaj i 26 numeriranih stranica seminara)

## Trenutni fokus

- [x] **v1.6 — završna akademska i tehnička revizija** (8. rujna 2026.):
  - Zatvoreni su nalazi F01–F11 iz `docs/REVIEW.md`; tvrdnje o LMI kriteriju,
    profinjenju mreže, lokalnoj osjetljivosti, intervalima nesigurnosti,
    izvandijagonalnom umnošku i rastu sklopnog sustava sada su ograničene na ono
    što je izravno dokazano.
  - Robusni QP prikazuje 12 reprezentativnih parova granica i jasno zasjenjen
    robusni presjek; `rng(42)`, regulator i svi numerički rezultati ostali su
    nepromijenjeni.
  - MATLAB R2025b ponovno je izvršio `src/run_all.m` i prijenosnu kopiju u
    `for_validator/`; oba pokretanja završila su bez pogreške. Referentni ispisi
    ostaju u `docs/code/`.
  - Bibliografija sadrži samo četiri provjerena lokalna nastavna PDF-a iz
    `data/sources/lectures/`; uklonjeni su nedostupni knjižni izvori.
  - Tectonic build daje 30-stranični A4 PDF; log nema `Overfull`, `Underfull`,
    nedefinirane reference/citate, nedostajuće znakove ni nedefinirane naredbe.
    Sve su stranice renderirane i vizualno pregledane.
  - `for_validator/` je sinkroniziran s v1.6, uključujući PDF, LaTeX, MATLAB,
    slike, ispise, benchmarke i paket pitanja za obranu.

- [x] **Udžbenik v2 — LaTeX, vođen zadacima, s okvirima izvora** (`docs/udzbenik/`):
  - Nastao jer Markdown verzija nije pokazivala **odakle koja tvrdnja dolazi** —
    pandoc daje samo obične citatne blokove, pa su slajdovi s predavanja, tekst
    zadatka i rješenje iz seminara izgledali identično.
  - **Boja označava isključivo podrijetlo teksta**: crveno = doslovni slajd s
    predavanja/vježbi (citiran i brojem slajda i brojem PDF stranice, jer ih
    beamer overlayi razdvajaju), sivo = doslovni tekst zadatka sa skena,
    plavo = doslovni izvadak iz seminara v1.2, žuto = definicija ili formula.
    Sve ostalo je bez ispune, da četiri boje ostanu jedini glasan signal.
  - **Gotovo u cijelosti**: Dio 0 (rječnik svakog simbola s izgovorom, računski
    alat, čitanje i crtanje grafova), sva četiri zadatka po istom predlošku od
    devet koraka, svaki s modulom za obranu, i završni podsjetnik za dan obrane.
    **188 stranica**, `dist/v1.2/OMRiUS_udzbenik_v2.pdf`.
  - **Provjereno programski**: 49 referenci na slajdove usporedbom s podnožjem
    stvarnog slajda u PDF-u; 67 brojčanih tvrdnji prema `docs/code/task*_output.txt`;
    log bez `Missing character`, `Undefined control sequence` i `Overfull`.
  - **Zabilježene nijanse gdje seminar tvrdi više nego što je dokazano** (svaka s
    formulacijom za obranu): porast `J*` s gušćom mrežom ima dva uzroka, a ne samo
    kvadraturu, i dvije mreže nisu dokaz reda konvergencije (Z3); `min ||Y||` ne
    daje regulator najmanje norme jer je `K = Y Q^-1` (Z4); umnožak
    izvandijagonalnih elemenata je `-pi^2/4`, a u karakterističnu jednadžbu ulazi
    s minusom (Z4).
  - Build: `python src/build_udzbenik.py` (Tectonic; sam renderira slike koje
    nedostaju). Slajdovi: `python src/extract_slides.py` iz manifesta u gitu;
    PNG-ovi su izvedeni i gitignorirani.
  - Za odabir slajdova postoji indeks teksta svih 535 slajdova u
    `data/processed/lectures_text_07092026_185942/` (`INDEX.md`, `find.py`).
  - Detalji i pravila: `docs/udzbenik/README.md`.

- [x] **Sveučilišni udžbenik i vodič za pripremu usmene obrane i ispita (rujan 2026.)** — verzija v1, Markdown, ostaje netaknuta:
  - Samostalan udžbenik od 11 poglavlja (Poglavlja 0–10 u `docs/textbook/` i master verzija `docs/UDZBENIK_OMRIUS_PRIPREMA_OBRANE.md`, preko 250 kB teksta).
  - **Poglavlje 0 (Matematički rječnik i govorni vodič)**: detaljno objašnjenje svih simbola od nule ($\mathbb{R}^n, \langle x, y \rangle, \coloneqq, \succeq, \succ$), fizikalna značenja, vodič za govorno izražavanje pred ispitivačem i 10 doslovnih modela rečenica.
  - **Umetnute slike i vodiči za crtanje na ploči**: Umetnuto svih 7 slika seminara u visoko-kvalitetnom PNG formatu, uz detaljne dekonstrukcije elemenata i korak-po-korak vodiče s ASCII skicama i govornim predlošcima za crtanje na ploči (Zadatak 1 geometrija i nivo-elipse, Zadatak 2 robusna anvelopa i Monte Carlo, Zadatak 3 niveleta ceste i zasićenje zakrivljenosti, Zadatak 4 odmotavajuća spirala otvorenog kruga i Ljapunovljeva elipsoidna kontrakcija zatvorenog kruga).
  - **Kompajliran PDF udžbenika**: `docs/UDZBENIK_OMRIUS_PRIPREMA_OBRANE.pdf` i `dist/v1.2/OMRiUS_udzbenik_priprema_obrane_latest.pdf` (123 stranice, 1.3 MB, akademski format report s dvo-stupanjskim TOC-om, fancyhdr i microtype).

- [x] Dubinska komparativna recenzija v1.2 prema izvornom zadatku i seminarima Matije i Ivana (završena 2026-09-08).
  - Primarni artefakt: `dist/v1.2/OMRiUS_seminar_Kresimir_Hartl.pdf`; kopija u `for_validator` ima drugi SHA-256 i ne smatra se istom verzijom bez provjere.
  - Završni nalaz je u `docs/REVIEW.md`; provedeni su neovisna matematička provjera, RAG provjera izvora i usporedba stvarnih PDF-ova.
  - Glavni zaključak: nema potvrđene zajedničke numeričke pogreške; prije predaje preporučena je ciljana revizija nalaza F01–F11.
  - Recenzija ne mijenja sadržaj seminara, MATLAB kod ni grafove.

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

- [x] Sken izvornog zadatka umetnut odmah iza naslovnice; JMBAG uklonjen s naslovnice.

## Bilješke

- **Notacija** je usklađena s profesorovim materijalima: Vježbe 3 (isti tip zadatka
  a)–f), `Gx - h ≤ 0`, `θ(μ)`, tablica svih $2^m$ kombinacija aktivnosti,
  perturbacijski vektor `v`), Vježbe 4 ($\ell_1$-aproksimacija za Zadatak 3),
  Predavanje 7 (kvadratna stabilnost, `Q = P⁻¹`, `Y = KP⁻¹`), Predavanje 8
  (robusno optimiranje nad poliedarskim skupovima nesigurnosti).
- **Zadatak 1**: rezultat `x* = (190/33, 140/33)` je točan. Matijin stvarni PDF
  daje isti točan rezultat; pogrešna vrijednost `(5.4762, 4.5238)` pojavljuje se
  samo u starom Markdown prijepisu, koji nije autoritativan i nije sadržajni izvor.
- **Zadatak 2**: Monte Carlo pod MATLAB-ovim `rng(42)` daje **54/100** kršenja za
  nominalnu točku (ne 57/100 kao u v1.0, gdje je brojka bila iz Pythona).
- **Zadatak 3**: službeni zadatak traži ukupni kriterij `J`; odvojeni iskop i
  nasip nisu analizirani pa se o njihovoj jednoznačnosti ne iznosi tvrdnja.
  `J` je površina [m²], a za širinu trase `w` volumen je `V=wJ` [m³].
- **Zadatak 4**: LMI se rješava uz normalizaciju `Q ⪰ I`, `M_i ⪯ -I` i kriterij
  `min ‖Y‖₂`, kojim se bira jedno dopustivo rješenje, a ne regulator najmanje
  norme. Dobiva se `K = [-3.424629, -0.104650]`, `α = 0.288374 s⁻¹`.
- **MATLAB R2025b gotcha**: u `-batch` načinu figure se crtaju prema tamnoj temi
  bez obzira na `Figure.Color`, pa `src/common/config_plot.m` eksplicitno
  postavlja sve boje na svijetle.
- **Sken zadatka**: `docs/zadatak/zadatak_sken.pdf` je ravna kopija
  `TASK/Zadatak_OMRiUS_Kresimir_Hartl.pdf` dobivena s `pdftocairo -pdf`.
  Izvornik ruši `xdvipdfmx` (`pdf_link_obj(): passed invalid object`), pa se
  uključuje kopija. `.gitignore` ima iznimku `!docs/zadatak/*.pdf`.
