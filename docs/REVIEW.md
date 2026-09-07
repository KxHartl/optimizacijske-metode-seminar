# Provjera rada prije predaje (v1.2)

> **Kolegij:** Optimizacijske metode u razvoju i upravljanju sustava (OMRiUS)
> **Student:** Krešimir Hartl
> **Mentor:** Prof. dr. sc. Andrej Jokić
> **Opseg:** 27 stranica, 7 slika, 5 tablica, 4 reference

---

## 1. Pokrivenost zadatka

Svaka podtočka iz `TASK/zadatak_omrius.md` ima svoje mjesto u radu:

| Podzadatak | Traženo | Gdje |
|---|---|---|
| 1a | Je li problem konveksan? Obrazložiti. | §2.2 |
| 1b | Postaviti i riješiti KKT uvjete | §2.3, tablica 2.1, 4 slučaja |
| 1c | Dopustivi skup, nivo-krivulje, gradijenti u KKT točki | §2.4, slika 2.1 |
| 1d | MATLAB (`quadprog`), usporedba s (b) | §2.5, tablica 2.2 |
| 1e | Dualni problem, usporedba s (d) i (b) | §2.6 |
| 1f | Osjetljivost $p^*$ na perturbacije $b_1$, $b_2$ | §2.7 |
| 2 | Robusni problem + slika s nizom realizacija i optimumom | §3.1–3.5, slika 3.1 |
| 3a | Formulacija i klasa problema | §4.1 (odgovor: LP) |
| 3b | Četiri slučaja, prikaz $y(x)$ uz $h(x)$ | §4.4, tablica 4.1, slike 4.1–4.2 |
| 4a | Jesu li matrice Hurwitzove? | §5.2 |
| 4b | Simulacija, $x(t)$, fazni portret, je li stabilan? | §5.3, slika 5.1 |
| 4c | LMI sinteza $K$, simulacija zatvorenog kruga | §5.4, slika 5.2 |

Na svako izravno pitanje iz zadatka odgovoreno je i u zaključku, jednom rečenicom
po zadatku.

## 2. Brojčana provjera

Sve brojke potječu iz jednog pokretanja `src/run_all.m` (MATLAB R2025b) i
zapisane su u `docs/code/task1_output.txt` … `task4_output.txt`. Detaljna tablica
usporedbe analitičkih i numeričkih vrijednosti je u
`for_validator/05_VERIFICATION_AND_BENCHMARKS/BENCHMARK_RESULTS.md`.

Ključni rezultati:

- Zadatak 1: $x^* = (190/33,\ 140/33)$, $\mu^* = (404/33,\ 0)$,
  $p^* = d^* = 2000/33 = 60.606061$, dualni procjep $2.48 \cdot 10^{-10}$.
- Zadatak 2: $x_{\mathrm{rob}}^* = (13/2,\ 179/34)$, $f = 978253/11560 = 84.623962$,
  dva aktivna vrha uz $\mu = (17.607439,\ 1.344118) > 0$.
- Zadatak 3: $J^* = 1.916180 / 1.965940 / 2.453727 / 2.506047\ \mathrm{m}^2$,
  `exitflag = 1` u sva četiri slučaja.
- Zadatak 4: $\rho(\Phi_{\mathrm{cikl}}) = 9e^{-2} = 1.218018 > 1$;
  $K = [-3.424629,\ -0.104650]$, $\lambda_{\max}(M_i) = -0.910478$ i $-0.329090$,
  $\rho(\Phi_{\mathrm{cikl}}^{\mathrm{zk}}) = 0.069720$.

## 3. Provjere prije predaje

| Provjera | Naredba | Status |
|---|---|---|
| Sve skripte prolaze | `matlab -batch "cd src; run_all"` | prolazi |
| Broj stranica $\leq 30$ | `pdfinfo dist/v1.2/*.pdf` | 27 |
| Nema spomena Pythona ni drugih alata | `grep -iE 'python\|cvxpy\|clarabel\|scipy\|highs' docs` | prazno |
| Nema Markdown `**` u LaTeX-u | `grep -F '**' docs/chapters/*.tex` | prazno |
| Nema pogrešnih termina | `grep -iE 'dupleks\|CQLF' docs` | prazno |
| Sve slike referencirane iz teksta | ručno | 7/7 |
| Sve tablice referencirane iz teksta | ručno | 5/5 |

## 4. Poznata ograničenja i svjesne odluke

- **LMI nema jedinstveno rješenje.** Prikazani $K$ dobiven je uz normalizaciju
  $\mathcal{Q} \succeq I$, $M_i \preceq -I$ i kriterij $\min\lVert Y\rVert_2$.
  To je u radu izrečeno, a ne prešućeno.
- **Podjela $J^*$ na iskop i nasip nije jedinstvena** jer je LP degeneriran; zato
  ti stupci nisu u tablici 4.1.
- **Monte Carlo je ilustracija, ne dokaz.** Brojka 54/100 vrijedi za MATLAB-ov
  generator uz `rng(42)`; jamstvo dopustivosti daje osam vršnih nejednakosti.
- **Zajamčena stopa $\alpha = 0.288374\ \mathrm{s}^{-1}$ je konzervativna** jer
  vrijedi za proizvoljno prespajanje; pri zadanom periodičkom prespajanju stvarna
  je kontrakcija znatno brža.
- **JMBAG na naslovnici je zamjenski tekst** (`\authorid` u `docs/main.tex`) i
  treba ga zamijeniti stvarnim brojem prije predaje.
