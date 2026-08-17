# Zadatci za seminarski rad — OMRiUS 2025/26

> **Kolegij:** Optimizacijske metode u razvoju i upravljanju sustava
> **Student:** Krešimir Hartl
> **Zadatak zadan:** Siječanj 2026.
> **Rok predaje rada:** Lipanj 2027.
> **Mentor:** Prof.dr.sc. Andrej Jokić

---

## Zadatak 1. (QP, konveksnost, KKT, dualnost)

### Opis problema

Zadan je optimizacijski problem:

$$
\min_{x} \quad x_1^2 + 2x_2^2 - 0.3x_1 x_2 + 2x_1 - 3x_2 \tag{1a}
$$

uz ograničenja:

$$
a_{11}x_1 + a_{12}x_2 \leq -10, \tag{1b}
$$

$$
a_{21}x_1 + a_{22}x_2 \leq 3, \tag{1c}
$$

gdje su numeričke vrijednosti koeficijenata:

$$
a_{11} = -1, \quad a_{12} = -1, \quad a_{21} = 1, \quad a_{22} = -1.
$$

### Podzadatci i koraci rješavanja

#### a) Konveksnost — Obrazložiti odgovor

> **Pitanje:** Je li ovo konveksan optimizacijski problem? Obrazložiti odgovor.

**Koraci:**

1. Zapisati funkciju cilja u matričnom obliku: $f(x) = \frac{1}{2} x^T Q x + c^T x$
2. Odrediti Hessian matricu $Q$ iz funkcije cilja
3. Provjeriti pozitivnu semi-definitnost matrice $Q$ (svojstvene vrijednosti ≥ 0)
4. Provjeriti linearnost ograničenja (linearna ograničenja su konveksna)
5. Zaključiti o konveksnosti problema

#### b) KKT uvjeti — Odrediti optimum

> **Pitanje:** Postavite KKT uvjete optimalnosti i riješite ih (odredite vrijednosti projektnih varijabli i Lagrangeovih množitelja koji zadovoljavaju te uvjete).

**Koraci:**

1. Zapisati Lagrangian: $\mathcal{L}(x, \lambda) = f(x) + \lambda_1 g_1(x) + \lambda_2 g_2(x)$
2. Postaviti KKT uvjete:
   - **Stacionarnost:** $\nabla_x \mathcal{L} = 0$
   - **Primarna dopustivost:** $g_i(x) \leq 0$
   - **Dualna dopustivost:** $\lambda_i \geq 0$
   - **Komplementarnost:** $\lambda_i g_i(x) = 0$
3. Riješiti sustav jednadžbi (razmotriti sve kombinacije aktivnih/neaktivnih ograničenja)
4. Odrediti optimalne $x_1^*, x_2^*$ i $\lambda_1^*, \lambda_2^*$

#### c) Grafički prikaz

> **Pitanje:** Nacrtajte dozvoljeni skup, nivo krivulje funkcije cilja te izračunajte i skicirajte gradijente ograničenja i funkcije cilja u točki koja zadovoljava KKT uvjete.

**Koraci:**

1. Nacrtati dozvoljeni skup (feasible region) — područje definirano ograničenjima (1b) i (1c)
2. Nacrtati nivo-krivulje (contour lines) funkcije cilja
3. Izračunati gradijent funkcije cilja: $\nabla f(x^*)$
4. Izračunati gradijente ograničenja: $\nabla g_1(x^*)$, $\nabla g_2(x^*)$
5. Skicirati sve gradijente u KKT točki
6. Verificirati grafički da KKT uvjeti vrijede (gradijent cilja kao linearna kombinacija gradijenata aktivnih ograničenja)

#### d) Numeričko rješenje u MATLAB-u

> **Pitanje:** Riješite problem u MATLABu (quadprog i/ili yalmip) — odredite primarne i dualne varijable u optimumu te ih usporedite s rezultatima (Lagrangeovim množiteljima) iz (b).

**Koraci:**

1. Formulirati QP u standardnom obliku za `quadprog`: $\min \frac{1}{2}x^T H x + f^T x$ uz $Ax \leq b$
2. Odrediti matrice $H$, $f$, $A$, $b$
3. Pozvati `[x_opt, fval, ~, ~, lambda] = quadprog(H, f, A, b)`
4. Alternativno: formulirati u YALMIP-u koristeći `sdpvar`, `optimize`
5. Usporediti numeričke rezultate s analitičkim iz (b)

#### e) Lagrangeov dualan problem

> **Pitanje:** Postavite i riješite Lagrangeov dualan problem (koristite MATLAB za numeričko rješavanje dualnog problema). Usporedite vrijednost izračunatih dualnih varijabli s onima dobivenima pod (d) i (b).

**Koraci:**

1. Zapisati dualnu funkciju: $g(\lambda) = \inf_x \mathcal{L}(x, \lambda)$
2. Riješiti minimizaciju po $x$ analitički (iz stacionarnosti)
3. Formulirati dualan problem: $\max_{\lambda \geq 0} g(\lambda)$
4. Riješiti dualan problem numerički u MATLAB-u
5. Usporediti dualne varijable s rezultatima iz (b) i (d)
6. Verificirati jaku dualnost (ako je problem konveksan)

#### f) Analiza osjetljivosti

> **Pitanje:** Što možete reći o osjetljivosti optimalne vrijednosti ($p^* =$ opt. vrijednost primarnog problema) na perturbacije u ograničenjima (na perturbacije koeficijenata $b_1$ i $b_2$)?

**Koraci:**

1. Koristiti teoriju osjetljivosti: $\frac{\partial p^*}{\partial b_i} = -\lambda_i^*$
2. Interpretirati značenje optimalnih Lagrangeovih množitelja
3. Analizirati kako se $p^*$ mijenja za male perturbacije $b_1$ i $b_2$
4. Dati numeričku verifikaciju (varirati $b_1$, $b_2$ i riješiti ponovo)

---

## Zadatak 2. (Robustan QP)

### Opis problema

Za optimizacijski problem iz Zadatka 1, pretpostavimo da su koeficijenti $a_{ij}$, $i = 1, 2$, $j = 1, 2$ nesigurni u sljedećem smislu. Jedino što znamo je da se njihove stvarne vrijednosti nalaze u intervalu od $\pm 15\%$ od numeričkih vrijednosti zadanih u Zadatku 1: stvarna vrijednost $a_{ij,\text{stvarno}}$ se nalazi u intervalu od $0.85 a_{ij}$ do $1.15 a_{ij}$, gdje je $a_{ij}$ numerička vrijednost iz Zadatka 1.

Riješite ovako zadan robustan optimizacijski problem. Nacrtajte dozvoljeni skup za niz slučajno izabranih koeficijenata iz dozvoljenih intervala te na istoj slici označite gdje se nalazi točka optimuma.

### Koraci rješavanja

1. **Definirati nesigurnost:** $a_{ij,\text{stvarno}} \in [0.85 \cdot a_{ij}, \; 1.15 \cdot a_{ij}]$
2. **Formulirati robusni QP** — ograničenja moraju vrijediti za **sve** moguće vrijednosti koeficijenata:
   - Za svako ograničenje, odrediti najgori slučaj (worst-case) unutar intervala nesigurnosti
   - Primjena: za $a_{ij} x_j \leq b$, najgori slučaj je $\max_{a_{ij} \in [\underline{a}_{ij}, \overline{a}_{ij}]} a_{ij} x_j$
3. **Prevesti robustan problem u deterministički QP** s pooštrenim ograničenjima
4. **Riješiti robustan QP** u MATLAB-u (quadprog ili YALMIP)
5. **Generirati nasumične koeficijente** iz dozvoljenih intervala (npr. 50-100 realizacija)
6. **Nacrtati dozvoljeni skup** za svaku realizaciju koeficijenata
7. **Označiti robusnu optimalnu točku** na grafu
8. **Usporediti** s nominalnim rješenjem iz Zadatka 1

---

## Zadatak 3. (Formulacija opt. problema; opt. aproksimacija s ograničenjima)

### Opis problema

> **Pitanje:** Potrebno je izgraditi cestu na neravnom terenu. Trošak izrade ceste proporcionalan je količini materijala (zemlje) kojeg treba oduzeti (otkopati) ili dodati da bi se dobio donekle "poravnan" teren prikladan za izgradnju ceste.
>
> Neka je $L$ sveukupna duljina ceste (točnije projekcija duljine ceste na horizontalnu os $x$), a $h(x)$ je poznata visina terena u ovisnosti o koordinati $x \in [0, L]$ — vidjeti sliku za ilustraciju. Potrebno je odrediti visinu ceste $y(x)$ za $x \in [0, L]$ koja rezultira minimalnim troškovima izrade, s time da je nužno poštovati sljedeća ograničenja:
>
> - nagib ceste ne smije biti veći od $b_1$;
> - za ugodnu vožnju brzina promjene nagiba ceste ne smije biti veća od $b_2$;
> - rubni uvjeti $y(0) = a$ i $y(L) = b$ moraju biti zadovoljeni.

### Zadani parametri

$$
L = 10, \tag{2a}
$$

$$
h(x) = 0.0053x^4 - 0.095x^3 + 0.48x^2 - 0.3x + 1, \tag{2b}
$$

$$
a = h(0) = 1, \quad b = h(L) = 4. \tag{2c}
$$

$$
\text{slučaj A:} \quad b_1 = 0.5, \; b_2 = 0.5 \tag{2d}
$$

$$
\text{slučaj B:} \quad b_1 = 0.5, \; b_2 = 0.2 \tag{2e}
$$

### Upute za diskretizaciju

Koordinate $x$ na intervalu $[0, L]$ diskretizirati s $N + 1$ točaka $\{x_0, x_1, \ldots, x_N\}$, odnosno ovaj interval podijelite na $N$ podintervala od kojih je svaki duljine $\Delta h = L/N$ (uočite $x_0 = 0, x_N = L$). Tada visinu ceste računajte samo u točkama diskretizacije $\{y_0 = y(x_0), y_1 = y(x_1), \ldots, y_N = y(x_N)\}$.

Nagib ceste (derivaciju) aproksimirati prvom podijeljenom razlikom:

$$
y'(x_i) \approx \nabla y_i := \frac{1}{\Delta x}(y_i - y_{i-1}),
$$

a brzinu promjene nagiba (drugu derivaciju):

$$
y''(x_i) \approx \nabla^2 y_i := \frac{1}{\Delta x}(\nabla y_i - \nabla y_{i-1}).
$$

### Podzadatci i koraci rješavanja

#### a) Formulacija i klasifikacija problema

> **Pitanje:** Formulirajte problem kao optimizacijski problem. Kojoj klasi optimizacijskih problema pripada ovaj problem?

**Koraci:**

1. **Funkcija cilja** — minimizirati ukupni trošak (proporcionalan količini materijala):
   $$\min_y \sum_{i=0}^{N} |y_i - h(x_i)|$$
   ili ekvivalentni LP oblik s pomoćnim varijablama $t_i$:
   $$\min \sum t_i \quad \text{uz} \quad -t_i \leq y_i - h_i \leq t_i$$
2. **Ograničenja nagiba:** $|\nabla y_i| \leq b_1$ za sve $i$
3. **Ograničenja brzine promjene nagiba:** $|\nabla^2 y_i| \leq b_2$ za sve $i$
4. **Rubni uvjeti:** $y_0 = a$, $y_N = b$
5. Analizirati funkciju cilja i ograničenja
6. Prepoznati da je to **linearni program (LP)** nakon reformulacije s apsolutnim vrijednostima

#### b) Rješavanje za 4 različita slučaja

> **Pitanje:** Riješite problem za 4 različita slučaja: _i)_ za slučaj A (parametri zadani s (2d)) te s $N = 20$; _ii)_ za slučaj A s $N = 100$; _iii)_ za slučaj B (parametri zadani s (2e)) te s $N = 20$; _iv)_ za slučaj B s $N = 100$.

| Slučaj | Parametri     | $N$       |
| ------ | ------------- | --------- |
| i)     | Slučaj A (2d) | $N = 20$  |
| ii)    | Slučaj A (2d) | $N = 100$ |
| iii)   | Slučaj B (2e) | $N = 20$  |
| iv)    | Slučaj B (2e) | $N = 100$ |

**Koraci:**

1. Diskretizirati teren — izračunati $h(x_i)$ za sve točke
2. Formulirati LP u MATLAB-u (linprog ili YALMIP)
3. Riješiti i prikazati rješenje $y(x)$ zajedno s terenom $h(x)$
4. Analizirati utjecaj parametara $b_1$, $b_2$ i finoće diskretizacije $N$

---

## Zadatak 4. (Robusna stabilizacija)

### Opis problema

Promotrimo sljedeći vremenski promjenjiv sustav:

$$
\dot{x}(t) = A(t)x(t) + Bu(t) \tag{3}
$$

gdje je $x(t)$ varijabla stanja, a $u(t)$ je ulazni (upravljački) signal. Matrica $A(t)$ je vremenski promjenjiva ($t$ označava vrijeme) i to prema sljedećem pravilu:

$$
A(t) = \begin{cases} A_{\text{parno}} & \text{kad je } \lfloor t \rfloor \text{ paran broj} \\ A_{\text{neparno}} & \text{kad je } \lfloor t \rfloor \text{ neparan broj} \end{cases} \tag{4}
$$

gdje $\lfloor t \rfloor$ označava najveći cijeli broj koji je manji ili jednak $t$ (zaokruživanja broja $t$ na prvi manji cijeli broj). Imamo:

$$
A_{\text{parno}} = \begin{bmatrix} -1 & -\frac{1}{6}\pi \\ \frac{3}{2}\pi & -1 \end{bmatrix}, \qquad A_{\text{neparno}} = \begin{bmatrix} -1 & -\frac{3}{2}\pi \\ \frac{1}{6}\pi & -1 \end{bmatrix}. \tag{5}
$$

Ovdje se u biti radi o hibridnom sustavu sa "skokovitom" promjenom dinamike (_switching_) u diskretnim vremenskim trenucima. Između svaka dva trenutka u kojima se odvija ovo skokovita promjena, sustav je linearan vremenski invarijantan. Kažemo da ovaj sustav ima dva dinamička moda.

### Podzadatci i koraci rješavanja

#### a) Stabilnost pojedinih modova

> **Pitanje:** Jesu li matrice $A_{\text{parno}}$ i $A_{\text{neparno}}$ stabilne matrice (Hurwitzove matrice)? Odnosno, jesu li oba dinamička moda stabilna? _(Napomena: ovo možete provjeriti izračunom svojstvenih vrijednosti ovih matrica)._

**Koraci:**

1. Izračunati svojstvene vrijednosti matrice $A_{\text{parno}}$: $\text{eig}(A_{\text{parno}})$
2. Izračunati svojstvene vrijednosti matrice $A_{\text{neparno}}$: $\text{eig}(A_{\text{neparno}})$
3. Provjeriti imaju li sve svojstvene vrijednosti negativni realni dio ($\text{Re}(\lambda_i) < 0$)
4. Zaključiti o stabilnosti pojedinog moda

#### b) Simulacija vremenski promjenjivog sustava

> **Pitanje:** Simulirajte vremenski promjenjiv sustav (3) s početnim uvjetom $x(0) = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$, prikažite $x(t)$ (graf kako se varijable stanja mijenjaju s vremenom) i prikažite trajektoriju sustava u prostoru stanja. Je li ovaj sustav stabilan?

**Koraci:**

1. Implementirati simulaciju switching sustava u MATLAB-u (npr. `ode45` po segmentima ili diskretna simulacija)
2. Na svakom cijelom broju $t$, provjeriti parnost $\lfloor t \rfloor$ i odabrati odgovarajući $A(t)$
3. Simulirati za dovoljno dugo vrijeme (npr. $t \in [0, 20]$)
4. Nacrtati $x_1(t)$ i $x_2(t)$ u funkciji vremena
5. Nacrtati fazni portret (trajektoriju u prostoru stanja: $x_1$ vs $x_2$)
6. Analizirati stabilnost — konvergiraju li stanja prema nuli?

#### c) Dizajn robusnog regulatora — statička povratna veza

> **Pitanje:** U sustavu (3), neka je matrica $B = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$. Dizajnirajte statički regulator $u(t) = Kx(t)$ takav da je zatvoreni krug:
> $$\dot{x}(t) = (A(t) + BK)x(t) \tag{6}$$
> eksponencijalno stabilan, gdje je $A(t)$ zadana s (4). Simulirajte ovaj vremenski promjenjiv zatvoreni sustav s početnim uvjetom $x(0) = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$, prikažite $x(t)$ i prikažite trajektoriju sustava u prostoru stanja.

**Koraci:**

1. **Formulirati problem kao LMI (linearne matrične nejednakosti):**
   - Pronaći zajedničku Lyapunovu funkciju $V(x) = x^T P x$ ($P \succ 0$) takvu da:
     - $(A_{\text{parno}} + BK)^T P + P(A_{\text{parno}} + BK) \prec 0$
     - $(A_{\text{neparno}} + BK)^T P + P(A_{\text{neparno}} + BK) \prec 0$
2. **Supstitucija:** Uvesti $Y = KP^{-1}$ (ili ekvivalentnu) za linearizaciju LMI-ja
3. **Riješiti LMI** u MATLAB-u koristeći YALMIP + SDP solver (npr. SeDuMi, SDPT3, MOSEK)
4. **Izračunati pojačanje:** $K = Y P$
5. **Simulirati zatvoreni sustav** s $\dot{x} = (A(t) + BK)x$ i $x(0) = [1; 0]$
6. **Nacrtati grafove:** $x_1(t)$, $x_2(t)$ vs. vrijeme, te fazni portret
7. **Verificirati eksponencijalnu stabilnost** — stanja trebaju konvergirati prema nuli

---

## Sažetak koraka i alata

| Zadatak | Tema                  | Ključni alati / metode                                            |
| ------- | --------------------- | ----------------------------------------------------------------- |
| 1a      | Konveksnost           | Hessian, svojstvene vrijednosti                                   |
| 1b      | KKT uvjeti            | Analitičko rješavanje sustava jednadžbi                           |
| 1c      | Grafički prikaz       | MATLAB plotting (contour, quiver)                                 |
| 1d      | Numeričko rješenje    | `quadprog`, YALMIP                                                |
| 1e      | Dualan problem        | Dualna funkcija, MATLAB optimizacija                              |
| 1f      | Osjetljivost          | Teorija osjetljivosti, $\partial p^*/\partial b_i = -\lambda_i^*$ |
| 2       | Robustan QP           | Worst-case analiza, robusna optimizacija                          |
| 3       | Optimizacija ceste    | LP formulacija, `linprog`, diskretizacija                         |
| 4a      | Stabilnost            | Svojstvene vrijednosti, Hurwitz kriterij                          |
| 4b      | Simulacija            | `ode45`, switching sustav                                         |
| 4c      | Robusna stabilizacija | LMI, Lyapunov, YALMIP + SDP solver                                |
