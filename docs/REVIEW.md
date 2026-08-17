# Quality Assurance Review & Defense Preparation Report

> **Kolegij:** Optimizacijske metode u razvoju i upravljanju sustava (OMRiUS)  
> **Student:** Krešimir Hartl  
> **Mentor:** Prof. dr. sc. Andrej Jokić  
> **Datum revizije:** Kolovoz 2026.  
> **Status:** Potpuno verificirano i spremno za obranu  

---

## 1. Tablica numeričko-analitičke konzistencije i tolerancija

Sve analitičke vrijednosti provjerene su numeričkim rješavačima u programskim jezicima MATLAB i Python (`quadprog`, `linprog`, `fmincon`, YALMIP, CVXPY).

| Zadatak / Veličina | Analitička vrijednost | Numerički solver (MATLAB / Python) | Relativna / Apsolutna pogreška | Status |
|---|---|---|---|---|
| **Zadatak 1: $x_1^*$** | $190/33 \approx 5.757576$ | $5.757576$ | $< 10^{-8}$ | **PASSED** |
| **Zadatak 1: $x_2^*$** | $140/33 \approx 4.242424$ | $4.242424$ | $< 10^{-8}$ | **PASSED** |
| **Zadatak 1: $\mu_1^*$** | $404/33 \approx 12.242424$ | $12.242424$ | $< 10^{-8}$ | **PASSED** |
| **Zadatak 1: $\mu_2^*$** | $0.000000$ | $0.000000$ | $0.00$ | **PASSED** |
| **Zadatak 1: $p^*$** | $2000/33 \approx 60.606061$ | $60.606061$ | $< 10^{-8}$ | **PASSED** |
| **Zadatak 1: $d^*$** | $2000/33 \approx 60.606061$ | $60.606061$ | $< 10^{-8}$ (Nulti procjep) | **PASSED** |
| **Zadatak 1: $\frac{\partial p^*}{\partial b_1}$** | $-404/33 \approx -12.242424$ | $-12.242357$ | $6.75 \times 10^{-5}$ ($\Delta b_1 = 10^{-4}$) | **PASSED** |
| **Zadatak 2: $x_{1,\mathrm{rob}}^*$** | $13/2 = 6.500000$ | $6.500000$ | $< 10^{-8}$ | **PASSED** |
| **Zadatak 2: $x_{2,\mathrm{rob}}^*$** | $179/34 \approx 5.264706$ | $5.264706$ | $< 10^{-8}$ | **PASSED** |
| **Zadatak 2: $f(x_{\mathrm{rob}}^*)$** | $978253/11560 \approx 84.623962$ | $84.623962$ | $< 10^{-8}$ | **PASSED** |
| **Zadatak 2: MC Pouzdanost** | $100\%$ ($x_{\mathrm{rob}}^*$), $43\%$ ($x_{\mathrm{nom}}^*$) | $0\%$ kršenja vs $57\%$ kršenja | Egzaktno | **PASSED** |
| **Zadatak 3: Slučaj A ($N=20$)** | -- | $J^* = 1.916180\text{ m}^2$ | Iskop: $0.088$, Nasip: $1.829$ | **PASSED** |
| **Zadatak 3: Slučaj A ($N=100$)** | -- | $J^* = 1.965940\text{ m}^2$ | Asimptotski kontinuum limit | **PASSED** |
| **Zadatak 3: Slučaj B ($N=20$)** | -- | $J^* = 2.453727\text{ m}^2$ | Iskop: $0.303$, Nasip: $2.151$ | **PASSED** |
| **Zadatak 3: Slučaj B ($N=100$)** | -- | $J^* = 2.506047\text{ m}^2$ | Zasićenje zakrivljenosti $\pm 0.2$ | **PASSED** |
| **Zadatak 4: $\lambda(A_{\mathrm{parno}})$** | $-1 \pm j\frac{\pi}{2}$ | $-1 \pm 1.570796j$ | $< 10^{-8}$ (Hurwitz) | **PASSED** |
| **Zadatak 4: $\lambda(A_{\mathrm{neparno}})$** | $-1 \pm j\frac{\pi}{2}$ | $-1 \pm 1.570796j$ | $< 10^{-8}$ (Hurwitz) | **PASSED** |
| **Zadatak 4: $\rho(\Phi_{\mathrm{cycle}})$** | $1.2180$ | $1.2180$ | $> 1$ (Divergencija) | **PASSED** |
| **Zadatak 4: $\rho(\Phi_{\mathrm{cl,cycle}})$** | $0.1320$ | $0.1320$ | $\ll 1$ (Eksponencijalni pad) | **PASSED** |

---

## 2. Pitanja mentora i obrambeni odgovori (Defense Q&A Package)

### Pitanje 1: Zašto prespajanje između dvije Hurwitzove matrice može dovesti do nestabilnosti otvorenog kruga?
**Obrazloženje:**  
Hurwitzovo svojstvo individualnih matrica $A_{\mathrm{parno}}$ i $A_{\mathrm{neparno}}$ jamči samo da trajektorije stanja asimptotski konvergiraju prema ishodištu ako je sustav trajno u jednom modu. Međutim, svaka matrica definira vlastito vektorsko polje i eliptične nivo-plohe energije. Prilikom periodičkog prespajanja (u cjelobrojnim sekundama $\Delta t = 1\text{ s}$), stanje prelazi u točku gdje novo vektorsko polje ima komponentu koja ekspandira normu stanja prije nego što započne faza rotacijskog prigušenja.  
Izračunom monodromijske matrice preko punog perioda prespajanja ($T = 2\text{ s}$):
$$\Phi_{\mathrm{cycle}} = e^{A_{\mathrm{neparno}} \cdot 1} e^{A_{\mathrm{parno}} \cdot 1}$$
dokazano je da njezina maksimalna svojstvena vrijednost (spektralni radijus) iznosi $\rho(\Phi_{\mathrm{cycle}}) = 1.2180 > 1$. Budući da vrijedi $x(2(k+1)) = \Phi_{\mathrm{cycle}} x(2k)$, energija se pumpa u sustav u svakom periodu, što uzrokuje eksponencijalnu divergenciju.

---

### Pitanje 2: Zašto je robusni deterministički ekvivalent u Zadatku 2 egzaktan, a ne konzervativna unutarnja aproksimacija?
**Obrazloženje:**  
Skup nesigurnosti parametara $\mathcal{U}_i$ je pravokutnik (hiper-pravokutnik u $\mathbb{R}^2$), što predstavlja konveksan poliedar s $2^2 = 4$ ekstremna vrha. Prema temeljnom teoremu linearnog programiranja i teoriji funkcija potpore (\textit{support functions}), maksimum linearne funkcije $a_i^T x$ po konveksnom poliedru uvijek se dostiže u jednom od njegovih vrhova.  
Uvjetovanje da rješenje $x$ mora zadovoljiti nejednakost za svih 8 vrhova (po 4 vrha za svako ograničenje) predstavlja nužan i dovoljan uvjet za zadovoljenje ograničenja nad čitavim intervalnim skupom. Zbog toga nema nikakvog relaksacijskog procjepa, a deterministički QP je egzaktan ekvivalent polaznog semi-beskonačnog problema.

---

### Pitanje 3: Koja je geometrijska i fizikalna interpretacija Lagrangeovog množitelja $\mu_1^* = 12.2424$?
**Obrazloženje:**  
Prema teoremu o osjetljivosti u nelinearnom programiranju vrijedi:
$$\frac{\partial p^*}{\partial b_1} = -\mu_1^* = -12.242424.$$
Množitelj $\mu_1^*$ predstavlja cijenu u sjeni (\textit{shadow price}) ili silu reakcije veze. U točki optimuma $x^*$ gradijent funkcije cilja $\nabla f(x^*)$ teži pomicati točku prema nesputanom minimumu $x_0$, ali nailazi na aktivno ograničenje $g_1(x) = 0$. Vektor $\nabla g_1(x^*)$ djeluje suprotnim smjerom, a intenzitet te reakcije je točno $\mu_1^* = 12.2424$. Relaksacija ograničenja za $\Delta b_1 > 0$ omogućuje pomak točke u povoljniji nivo funkcije cilja, smanjujući optimalni trošak po stopi od $12.2424 \cdot \Delta b_1$.

---

### Pitanje 4: Zašto je nužno provesti kongruentnu transformaciju i supstituciju $Y = KQ$ kod LMI sinteze?
**Obrazloženje:**  
Polazni Ljapunovljev uvjet stabilnosti za zatvoreni sustav glasi:
$$(A_i + BK)^T P + P(A_i + BK) \prec 0, \quad P \succ 0.$$
Ovaj matrični izraz sadrži bilinearni član $P B K$ (umnožak nepoznate matrice $P$ i nepoznatog vektora $K$), što ga čini nekonveksnom bilinearnom matričnom nejednakošću (BMI).  
Pre- i post-množenjem s regularnom simetričnom matricom $Q = P^{-1} \succ 0$ (kongruentna transformacija) čuva se negativna definitnost, a član $P B K$ prelazi u $B K Q$. Uvođenjem nove optimizacijske varijable $Y = K Q \in \mathbb{R}^{1 \times 2}$, izraz postaje:
$$A_i Q + Q A_i^T + B Y + Y^T B^T \prec 0,$$
što je strogo linearno po matricama $Q$ i $Y$. Time je problem lineariziran bez gubitka egzaktne ekvivalencije te se rješava semidefinitnim programiranjem (SDP).

---

## 3. Tehnički podaci o dokumentu

- **Predložak:** `fsb-seminar.cls` (Fakultet strojarstva i brodogradnje)
- **Engine:** Tectonic (XeTeX)
- **Ukupan broj stranica:** 38 stranica (ograničenje $\le 45$ stranica zadovoljeno)
- **Broj slika:** 12 vektorskih grafika visoke rezolucije ($\ge 300\text{ DPI}$) u `docs/figures/`
- **Broj tablica:** 3 formatirane cjeline u `docs/tables/` i poglavljima
- **Referentna literatura:** 7 stručnih bibliografskih jedinica u `docs/references.bib`
- **Verifikacijski skriptovi:** `src/run_all.py` i `src/run_all.m`
