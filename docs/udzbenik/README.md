# Udžbenik za pripremu obrane — v2 (LaTeX)

Samostalan udžbenik koji vodi kroz seminarski rad **zadatak po zadatak**, tako da
se uz svaku tvrdnju vidi odakle dolazi. Nasljeđuje `docs/textbook/` (Markdown),
koji ostaje netaknut.

## Build

```powershell
python src\build_udzbenik.py
```

Izlaz: `docs/udzbenik/build/udzbenik.pdf` → `dist/v1.2/OMRiUS_udzbenik_v2.pdf`.
Skripta sama renderira slike koje nedostaju, pa je ovo jedina naredba koja treba.

Namjerno je odvojena od `.ai/scripts/helpers/build-docs.ps1`: ondje vrijedi
`max_pages: 30` iz `project.yaml`, što je ograničenje seminara, a ne udžbenika.

## Sustav okvira

Boja označava **isključivo podrijetlo teksta**. Sve ostalo je bez ispune, samo
tanka crta lijevo — da četiri boje ostanu jedini glasan signal na stranici.

| Okvir | Boja | Sadržaj |
|---|---|---|
| `izvor` | crvena | doslovni slajd s predavanja/vježbi + transkripcija |
| `zadatak` | siva | doslovni tekst zadatka, ništa dodano |
| `seminar` | plava | doslovni izvadak iz seminara v1.2 |
| `pojam`, `formula` | žuta | definicija ili formula koju treba znati napamet |

Tihi elementi: `predznanje`, `korak`, `zamka`, `pitanje`, `ploca`, `izgovor`.
Definicije su u `preambula/okviri.tex`.

**Pravilo za crveni okvir**: referenca uvijek nosi broj slajda ispisan u podnožju
slajda *i* broj PDF stranice — beamer overlayi ih razdvajaju (npr. `Vjezbe 3`
str. 23 = slajd 18/36).

**Pravilo za sivi okvir**: unutra ide samo profesorova formulacija. Numerirani
„Koraci rješavanja" iz `TASK/zadatak_omrius.md` dopisani su naknadno i **nisu**
dio zadatka — stoje izvan okvira, označeni kao izvedena uputa.

## Predložak podzadatka

Svaki podzadatak ide istim redom: što se traži → sivi okvir → predznanje →
crveni okvir → žuti okviri → izvod korak po korak → plavi okvir → graf s
uputama za crtanje rukom → MATLAB i stvarni ispis. Na kraju zadatka: modul za
obranu.

## Slike

`slides/manifest.tsv` i `zadatak/manifest.tsv` su u gitu; PNG-ovi su izvedeni i
u `.gitignore`. Regeneriraju se s:

```powershell
python src\extract_slides.py
```

`page` u manifestu je **PDF stranica**, ne broj slajda. Za pronalaženje prave
stranice postoji indeks teksta svih 535 slajdova u
`data/processed/lectures_text_<ts>/` (`INDEX.md` + `find.py`).

## Provjere prije predaje

- log bez `Missing character`, `Undefined control sequence`, `Overfull`;
- svaka referenca crvenog okvira provjerena prema podnožju stvarnog slajda;
- svaki broj u plavom okviru provjeren prema `docs/code/task*_output.txt`
  (jedini referentni izvor rezultata, vidi `STATE.md`);
- nijedan `\cite` ključ nije izmišljen.

## Stanje

| Dio | Poglavlja | Status |
|---|---|---|
| Dio 0 — rječnik, alat, čitanje grafa | 4 | gotovo |
| Zadatak 1 — QP, KKT, dualnost, osjetljivost | 9 | gotovo |
| Zadatak 2 — robusni QP | 6 | gotovo |
| Zadatak 3 — nivelacija ceste, LP | 6 | gotovo |
| Zadatak 4 — LMI stabilizacija | 6 | gotovo |
| Podsjetnik za dan obrane | 1 | gotovo |

Ukupno 188 stranica, 49 doslovnih isječaka s predavanja i vježbi.
