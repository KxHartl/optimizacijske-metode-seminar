# Paket za neovisnu provjeru

> **Kolegij:** Optimizacijske metode u razvoju i upravljanju sustava (OMRiUS)
> **Student:** Krešimir Hartl
> **Mentor:** Prof. dr. sc. Andrej Jokić
> **Ustanova:** Sveučilište u Zagrebu, Fakultet strojarstva i brodogradnje
> **Verzija rada:** v1.2 (29 stranica: naslovnica, 2 stranice skena zadatka, 26 stranica rada)

---

## Sadržaj

```
for_validator/
├── 01_TASK/                              tekst zadatka
│   ├── zadatak_omrius.md                 transkripcija s koracima rješavanja
│   └── Zadatak_OMRiUS_Kresimir_Hartl.pdf izvorni PDF
├── 02_REPORT_PDF/
│   └── OMRiUS_seminar_Kresimir_Hartl.pdf gotov rad
├── 03_LATEX_SOURCE/                      LaTeX izvor
│   ├── main.tex
│   ├── references.bib
│   ├── chapters/                         5 poglavlja + zaključak
│   ├── figures/                          7 vektorskih PDF slika
│   └── zadatak/                          sken zadatka koji se umeće iza naslovnice
├── 04_SOURCE_CODE/matlab/                MATLAB skripte (jedini izvor rezultata)
│   ├── run_all.m                         pokreće sve i zapisuje ispis
│   ├── task1_qp_analysis.m
│   ├── task2_robust_qp.m
│   ├── task3_road_leveling.m
│   ├── task4_lmi_switched_stabilization.m
│   └── common/                           config_plot.m, fig_dir.m
├── 05_VERIFICATION_AND_BENCHMARKS/
│   ├── BENCHMARK_RESULTS.md              usporedba analitičkih i numeričkih vrijednosti
│   ├── DEFENSE_QA_PACKAGE.md             12 pitanja za obranu i odgovori
│   └── matlab_output/                    doslovan konzolni ispis sva 4 zadatka
└── omrius_recenzija_*.md                 ranije neovisne recenzije verzije v1.0
```

## Reprodukcija

Potreban je MATLAB (razvijano na R2025b) s Optimization Toolboxom. Za zadatak 4
dodatno je potreban YALMIP; rješavač SDPT3 dolazi s MATLAB-om.

```matlab
addpath(genpath(fullfile(userpath, 'YALMIP')));   % ako YALMIP nije na path-u
cd 04_SOURCE_CODE/matlab
run_all
```

`run_all.m` provjerava `exitflag` svakog rješavača i prekida se na prvoj grešci.
Ispis se zapisuje u `docs/code/task*_output.txt` (kopije u `matlab_output/`).

Slike se izvoze kao vektorski PDF u `docs/figures/`. Nema Python koda: cijeli je
rad izračunat i iscrtan u MATLAB-u, kako zadatak i traži.

## Što je promijenjeno u odnosu na v1.0

Ranije recenzije u ovoj mapi odnose se na verziju v1.0 (38 stranica). U v1.2:

- **Sve je izračunato u MATLAB-u.** Python implementacija je uklonjena, a iz
  skripte za zadatak 4 maknuta je hardkodirana zamjenska vrijednost pojačanja
  $K$; LMI se stvarno rješava u YALMIP-u sa SDPT3.
- **Ispravljene su matrice prijelaza** u zadatku 4 (blokirajuća greška iz v1.0);
  sada su ispisane u zatvorenom obliku $e^{-1}[0, -1/3; 3, 0]$ itd.
- **Jedan $K$** kroz cijeli rad, uz $P$, obje provjere $\lambda_{\max}$ i
  izvedenu stopu $\alpha$.
- **Struktura prati podzadatke** (a)–(f) redom, u notaciji s vježbi
  ($Gx - h \leq 0$, $\theta(\mu)$, tablica kombinacija aktivnosti, vektor $v$).
- **Uklonjeno je što zadatak ne traži:** taksonomija optimizacijskih problema,
  odjeljak o cijeni robusnosti, smjernice za praksu, generički uvodi poglavlja i
  pet slika (12 → 7).
- **Zatvorene su logičke rupe** iz recenzija: pretpostavka $x \geq 0$ u zadatku 2
  sada se izriče i provjerava, prikazane su sve tri nejednakosti; Monte Carlo je
  označen kao ilustracija, a ne dokaz.
- **Uklonjeni su stupci iskop/nasip** iz tablice zadatka 3 jer ta podjela nije
  jedinstvena (LP je degeneriran).
- **MATLAB kod i stvarni ispis** priloženi su uz svaki zadatak u tijelu rada.
- Ispravljeno pet mjesta na kojima je Markdown `**bold**` u LaTeX-u davao
  doslovne zvjezdice.
