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
- [x] Implementacija i verifikacija numeričkih i analitičkih rješenja u `src/` i `for_validator/`:
  - [x] Zadatak 1: QP, konveksnost, KKT 4-slučajna analiza, grafički prikaz s neaktivnim vektorom $\nabla g_2$, dualnost, osjetljivost.
  - [x] Zadatak 2: Robustan QP (egzaktna metoda najgoreg slučaja nad 8 vrhova uz KKT verifikaciju + deterministička Monte Carlo verifikacija na 100 uzoraka sa seed 42).
  - [x] Zadatak 3: Optimizacijska nivelacija ceste (LP formulacija, jedinice površine/zakrivljenosti, dualni simpleks, slučaji A i B, $N=20, 100$).
  - [x] Zadatak 4: Sklopni sustav, egzaktne monodromijske matrice $\Phi_{\mathrm{even}}, \Phi_{\mathrm{odd}}, \Phi_{\mathrm{cycle}}$, determinantni i spektralni dokaz, LMI sinteza stanjskog regulatora, egzaktna Ljapunovljeva stopa disipacije $\beta = 0.0742\text{ s}^{-1}$ i simulacija.
- [x] Pisanje i inženjersko usavršavanje LaTeX poglavlja seminara (`docs/chapters/` i `for_validator/03_LATEX_SOURCE/`).
- [x] Recenzija i verifikacija rada (`for_validator/05_VERIFICATION_AND_BENCHMARKS/` s tablicom tolerancija i paketom pitanja za obranu).
- [x] Finalni release build u `dist/v1.0/OMRiUS_seminar_Kresimir_Hartl.pdf` (strogo unutar limita $\le 45$ stranica).

## Bilješke

- **Zadatak 1**: Figure 1.1 dopunjena vektorom $\nabla g_2(x^*)$ uz eksplicitno objašnjenje zašto je $\mu_2^* = 0$ u KKT ravnoteži; uklonjen pogrešan spomen YALMIP-a za Zadatak 1.
- **Zadatak 2**: KKT verifikacija nad 8 vrhova potvrđuje $\mu_1^* > 0, \mu_2^* > 0$ za dva najgora vrha i strogi slack ($\ge 1.5794$) za preostalih 6; Monte Carlo analiza precizno formulirana sa seed 42.
- **Zadatak 3**: Uvedena jedinična širina $w = 1\text{ m}$, diskretni integral $J_{\mathrm{disc}} = \Delta x \sum z_i$ usklađen s Riemannovom sumom površine, a terminologija usklađena s dualnim simpleksom.
- **Zadatak 4**: Ispravljene matrice prijelaza i monodromije ($\Phi_{\mathrm{cycle}} = e^{-2}\mathrm{diag}(-9, -1/9)$), popravljen MATLAB bug indeksiranja `eig(Acl_even)`, objašnjena nejedinstvenost LMI dobitka $K$ i izračunata egzaktna Ljapunovljeva stopa disipacije $\beta = 0.0742\text{ s}^{-1}$.
- **Naslovnica i stil**: Uklonjeno dvostruko ponavljanje naziva kolegija, formatiran "SEMINARSKI RAD", uklonjene generičke AI fraze iz zaključka.
