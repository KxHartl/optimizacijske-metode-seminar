# Provjera brojčanih rezultata

> **Kolegij:** Optimizacijske metode u razvoju i upravljanju sustava (OMRiUS)
> **Student:** Krešimir Hartl
> **Mentor:** Prof. dr. sc. Andrej Jokić
> **Verzija rada:** v1.6

---

## 1. Kako su brojke dobivene

Svi rezultati u radu proizlaze iz **jednog** pokretanja MATLAB skripti (MATLAB R2025b):

```matlab
cd src
run_all
```

`run_all.m` pokreće četiri skripte i zapisuje njihov konzolni ispis u
`docs/code/task1_output.txt` … `task4_output.txt`. Kopije tih ispisa nalaze se u
mapi `matlab_output/` uz ovaj dokument. **Svaka brojka u tekstu, tablici ili
potpisu slike mora se doslovno podudarati s jednim retkom tih datoteka.**

Korišteni rješavači:

| Zadatak | Rješavač | Napomena |
|---|---|---|
| 1 | `quadprog` (primal i dual), `interior-point-convex` | dual QP-a je opet QP u $\mu$ |
| 2 | `quadprog` | 8 vršnih nejednakosti |
| 3 | `linprog`, `dual-simplex` | 4 slučaja |
| 4 | YALMIP + SDPT3 | SDPT3 dolazi s R2025b; YALMIP se dodaje na path |

Za zadatak 4 potreban je YALMIP na MATLAB path-u. Skripta se prekida s jasnom
porukom ako ga nema — nema zamjenske ("hardkodirane") vrijednosti pojačanja.

---

## 2. Zadatak 1 — analitičko nasuprot numeričkom

| Veličina | Analitički | MATLAB | Odstupanje |
|---|---|---|---|
| $\lambda(Q)$ | $\lambda_{1,2} = 3 \mp \sqrt{1.09}$ | $1.955969$, $4.044031$ | $< 10^{-10}$ |
| $x^0$ (bez ogr.) | $(-710/791,\ 540/791)$ | $(-0.897598,\ 0.682680)$ | $< 10^{-10}$ |
| $x^*$ | $(190/33,\ 140/33)$ | $(5.757576,\ 4.242424)$ | $7.16 \cdot 10^{-11}$ |
| $\mu^*$ | $(404/33,\ 0)$ | $(12.242424,\ 0.000000)$ | $< 10^{-10}$ |
| $p^*$ | $2000/33$ | $60.606061$ | $< 10^{-10}$ |
| $d^*$ | $2000/33$ | $60.606061$ | procjep $2.48 \cdot 10^{-10}$ |
| $\partial p^*/\partial v_1$ | $-404/33 = -12.242424$ | $-12.242364$ | $5.99 \cdot 10^{-5}$ ($\delta = 10^{-4}$) |
| $\partial p^*/\partial v_2$ | $0$ | $0.000000$ | $0$ |

Odbačeni slučajevi: slučaj 1 ($g_1(x^0) = 10.214918 > 0$), slučaj 3
($\mu_2 = -3623/540 = -6.709259 < 0$), slučaj 4 ($\mu_2 = -2.45 < 0$).

## 3. Zadatak 2 — robusni QP

| Veličina | Analitički | MATLAB |
|---|---|---|
| $x_{\mathrm{rob}}^*$ | $(13/2,\ 179/34)$ | $(6.500000,\ 5.264706)$ |
| $f(x_{\mathrm{rob}}^*)$ | $978253/11560$ | $84.623962$ |
| $\max(G_{\mathrm{rob}}x - h_{\mathrm{rob}})$ | $0$ (dva aktivna vrha) | $-2.793 \cdot 10^{-11}$ |
| množitelji aktivnih vrhova | — | $(17.607439,\ 1.344118) > 0$ |
| porast prema nominalnom | — | $+24.017901$ ($+39.63\%$) |

Aktivni su vrhovi $k = 1$, tj. $(-0.85, -0.85)$, i $k = 7$, tj. $(1.15, -0.85)$;
preostalih šest ima rezervu $\geq 1.5794$.

**Monte Carlo (`rng(42)`, 100 realizacija):** nominalna točka krši ograničenje u
**54** realizacije, robusna ni u jednoj. Brojka 54 vrijedi za MATLAB-ov generator
uz to sjeme; ona je ilustracija, a ne dokaz — dopustivost na cijelom skupu
nesigurnosti slijedi iz osam vršnih nejednakosti.

## 4. Zadatak 3 — nivelacija ceste (LP)

| Slučaj | $N$ | $\Delta x$ | $J^*$ [m²] | $\max\lvert\nabla y\rvert$ | $\max\lvert\nabla^2 y\rvert$ [m⁻¹] | varijable / nejed. | `exitflag` |
|---|---|---|---|---|---|---|---|
| A | 20 | 0.50 | 1.916180 | 0.5000 | 0.5000 | 42 / 120 | 1 |
| A | 100 | 0.10 | 1.965940 | 0.5000 | 0.5000 | 202 / 600 | 1 |
| B | 20 | 0.50 | 2.453727 | 0.5000 | 0.2000 | 42 / 120 | 1 |
| B | 100 | 0.10 | 2.506047 | 0.5000 | 0.2000 | 202 / 600 | 1 |

Kriterij je $J = \Delta x \sum_i z_i$, dakle površina uzdužnog presjeka [m²]. Za
trasu širine $w$ pripadni je volumen $V=wJ$ [m³]; pri $w=1\ \mathrm{m}$ brojčane
su vrijednosti jednake, ali jedinice nisu. Pri prijelazu s $N=20$ na $N=100$
$J^*$ raste za 2.60 % u slučaju A i 2.13 % u slučaju B. To je opažanje za dvije
diskretne mreže, ne dokaz uzroka promjene, reda konvergencije ili predznaka
pogreške prema kontinuiranom problemu.

> **Opseg rezultata:** zadatak traži ukupni $J$; podjela na iskop i nasip nije
> posebno analizirana, pa se o njezinoj jednoznačnosti ne donosi zaključak.

## 5. Zadatak 4 — sklopni sustav i LMI

| Veličina | Analitički | MATLAB |
|---|---|---|
| $\lambda(A_{\mathrm{parno}})$, $\lambda(A_{\mathrm{neparno}})$ | $-1 \pm j\pi/2$ | $-1.000000 \pm 1.570796 j$ |
| $\Phi_{\mathrm{parno}}$ | $e^{-1}\begin{bmatrix}0 & -1/3\\ 3 & 0\end{bmatrix}$ | $\begin{bmatrix}0 & -0.122626\\ 1.103638 & 0\end{bmatrix}$ |
| $\Phi_{\mathrm{cikl}}$ | $e^{-2}\,\mathrm{diag}(-9,\ -1/9)$ | $\mathrm{diag}(-1.218018,\ -0.015037)$ |
| $\det \Phi_{\mathrm{cikl}}$ | $e^{-4}$ | $0.018316$ |
| $\rho(\Phi_{\mathrm{cikl}})$ | $9e^{-2}$ | $1.218018 > 1$ |

Sinteza (YALMIP + SDPT3, normalizacija $\mathcal{Q} \succeq I$,
$A_i\mathcal{Q} + \mathcal{Q}A_i^{\mathsf{T}} + BY + Y^{\mathsf{T}}B^{\mathsf{T}} \preceq -I$, kriterij $\min \lVert Y \rVert_2$ za odabir jednog dopustivog rješenja, ne za minimizaciju $\lVert K\rVert_2$):

| Veličina | Vrijednost |
|---|---|
| $\mathcal{Q}$ | $\begin{bmatrix}1.354304 & -0.385757\\ -0.385757 & 1.420003\end{bmatrix}$ |
| $Y$ | $[-4.597618,\ 1.172472]$ |
| $P = \mathcal{Q}^{-1}$ | $\begin{bmatrix}0.800314 & 0.217413\\ 0.217413 & 0.763286\end{bmatrix}$, $\lambda(P) = 0.563600,\ 1.000000$ |
| $K = YP$ | $[-3.424629,\ -0.104650]$ |
| $\lambda(A_{\mathrm{parno}} + BK)$ | $-2.712315 \pm 0.168908 j$ |
| $\lambda(A_{\mathrm{neparno}} + BK)$ | $-3.352491$, $-2.072138$ |
| $\lambda_{\max}\!\left(M_{\mathrm{parno}}\right)$ | $-0.910478 < 0$ |
| $\lambda_{\max}\!\left(M_{\mathrm{neparno}}\right)$ | $-0.329090 < 0$ |
| $\rho(\Phi_{\mathrm{cikl}}^{\mathrm{zk}})$ | $0.069720 \ll 1$ |
| $\alpha$ (iz $\dot V \leq -2\alpha V$) | $0.288374\ \mathrm{s}^{-1}$ |

Simulacija za $x(0)=[1,0]^{\mathsf T}$ (`ode45`, `RelTol` $10^{-9}$, po segmentima od 1 s):
otvoreni krug $\lVert x(20)\rVert = 7.1868$; zatvoreni krug
$\lVert x(5)\rVert = 1.5176 \cdot 10^{-3}$, $\lVert x(20)\rVert = 4.7232 \cdot 10^{-12}$.

> **Napomena o jednoznačnosti:** LMI je problem dopustivosti i nema jedinstveno
> rješenje. Bez normalizacije, ili s drugim rješavačem, dobiva se drugi $K$ koji
> također stabilizira zatvoreni krug. Sve brojke i sve slike u radu odgovaraju
> gore navedenom $K$.
