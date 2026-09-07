# POGLAVLJE 3: Lagrangeova dualnost i analiza osjetljivosti (Shadow Prices)

> **Sadržaj poglavlja:**  
> 3.1 Koncept Lagrangeove dualnosti: Dualna funkcija, slaba i jaka dualnost  
> 3.2 Analitičko izvođenje Lagrangeovog duala za Kvadratni Program (QP)  
> 3.3 Numeričko rješavanje dualnog problema u MATLAB-u (`quadprog` vs. `fmincon`)  
> 3.4 Teorija perturbacija i analiza osjetljivosti: Fizikalno značenje "cijena u sjeni"  
> 3.5 Analiza rezerve (Slack) i lokalna priroda osjetljivosti u Zadatku 1  
> 3.6 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori  

---

## 3.1 Koncept Lagrangeove dualnosti: Dualna funkcija, slaba i jaka dualnost

Lagrangeova dualnost jedan je od najdubljih i najljepših koncepata u matematičkoj optimizaciji. Ona nam omogućuje da težak optimizacijski problem s ograničenjima transformiramo u komplementaran problem koji često ima jednostavnija ograničenja ili daje zajamčene donje granice optimalne vrijednosti (prof. Jokić, Predavanje 4).

### Minimax formulacija primarnog problema
Promotrimo primarni problem optimizacije:
$$p^* = \min_{x \in \mathbb{R}^n} \quad f(x) \quad \text{uz} \quad g_i(x) \leq 0, \quad i = 1, \dots, m. \tag{3.1}$$
Prisjetimo se Lagrangeove funkcije:
$$\mathcal{L}(x, \mu) = f(x) + \sum_{i=1}^m \mu_i g_i(x) = f(x) + \mu^{\mathsf{T}} g(x), \qquad \mu \geq 0.$$

Što se događa ako za fiksni vektor $x$ potražimo supremum Lagrangiana po svim dopustivim multiplikatorima $\mu \geq 0$?
$$\max_{\mu \geq 0} \mathcal{L}(x, \mu) = \max_{\mu \geq 0} \left[ f(x) + \sum_{i=1}^m \mu_i g_i(x) \right] = \begin{cases} f(x), & \text{ako je } g_i(x) \leq 0, \; \forall i \\ +\infty, & \text{ako postoji } i \text{ takav da je } g_i(x) > 0 \end{cases} \tag{3.2}$$
- Ako je točka $x$ **dopustiva** ($g_i(x) \leq 0$), član $\mu_i g_i(x)$ je nepozitivan za sve $\mu_i \geq 0$. Maksimum se postiže odabirom $\mu_i = 0$, pa je vrijednost točno $f(x)$.
- Ako je točka $x$ **nedopustiva** (npr. $g_k(x) > 0$), tada možemo poslati $\mu_k \to +\infty$, čime čitav izraz teži u $+\infty$.

Dakle, primarni problem možemo zapisati u ekvivalentnom bezuvjetnom obliku:
$$p^* = \min_{x \in \mathbb{R}^n} \left[ \max_{\mu \geq 0} \mathcal{L}(x, \mu) \right]. \tag{3.3}$$

### Lagrangeova dualna funkcija
Lagrangeova dualna funkcija $\theta: \mathbb{R}^m \to \mathbb{R} \cup \{-\infty\}$ nastaje jednostavnom **zamjenom redoslijeda minimizacije i maksimizacije**:
$$\theta(\mu) := \inf_{x \in \mathbb{R}^n} \mathcal{L}(x, \mu) = \inf_{x \in \mathbb{R}^n} \left[ f(x) + \mu^{\mathsf{T}} g(x) \right]. \tag{3.4}$$

> **Teorem 3.1 (Konkavnost dualne funkcije):**  
> Dualna funkcija $\theta(\mu)$ je **uvijek konkavna**, čak i ako je polazni primarni problem (funkcija $f$ ili funkcije $g_i$) izrazito nekonveksan!  
> *Dokaz:* Za svaku fiksnu točku $x$, funkcija $\mu \mapsto \mathcal{L}(x, \mu) = f(x) + \mu^{\mathsf{T}} g(x)$ je afina (dakle i konkavna) po $\mu$. Po definiciji, infimum proizvoljne familije afinih funkcija uvijek je konkavna funkcija.

### Teorem slabe dualnosti (Weak Duality)
> **Teorem 3.2 (Slaba dualnost):**  
> Za svaki vektor $\mu \geq 0$ i za svaku dopustivu točku $x \in \mathcal{F}$ vrijedi:
> $$\theta(\mu) \leq p^*.$$
> Drugim riječima, dualna funkcija daje **zajamčenu donju granicu** optimalne vrijednosti primarnog problema.  
> 
> *Dokaz (u tri retka):*  
> Neka je $x \in \mathcal{F}$ (dakle $g(x) \leq 0$) i neka je $\mu \geq 0$. Tada je $\mu^{\mathsf{T}} g(x) \leq 0$.  
> Po definiciji infimuma vrijedi:
> $$\theta(\mu) = \inf_{\tilde{x}} \mathcal{L}(\tilde{x}, \mu) \leq \mathcal{L}(x, \mu) = f(x) + \mu^{\mathsf{T}} g(x) \leq f(x).$$
> Budući da nejednakost $\theta(\mu) \leq f(x)$ vrijedi za svaku dopustivu točku $x \in \mathcal{F}$, uzimanjem infimuma po $x \in \mathcal{F}$ slijedi:
> $$\theta(\mu) \leq \inf_{x \in \mathcal{F}} f(x) = p^*.$$

### Lagrangeov dualni problem i jaka dualnost
Budući da $\theta(\mu) \leq p^*$ vrijedi za svaki $\mu \geq 0$, prirodno je potražiti **najbolju (najveću moguću) donju granicu**:
$$d^* := \max_{\mu \geq 0} \quad \theta(\mu). \tag{3.5}$$
To je **Lagrangeov dualni problem**.

Razlika $p^* - d^* \geq 0$ naziva se **dualni procjep** (*duality gap*).
- Ako je $p^* - d^* > 0$, imamo slabu dualnost s procjepom.
- Ako je $p^* - d^* = 0$, imamo **jaku dualnost** (*strong duality*).

Kao što smo dokazali u Poglavlju 1, budući da je naš Zadatak 1 konveksan i zadovoljava Slaterov uvjet kvalifikacije ograničenja ($x_{\mathrm{test}} = [7, 6]^{\mathsf{T}} \implies g_1 < 0, g_2 < 0$), **vrijedi jaka dualnost ($d^* = p^*$) i dualni procjep je točno nula**.

---

## 3.2 Analitičko izvođenje Lagrangeovog duala za Kvadratni Program (QP)

Izvedimo sada korak-po-korak dualnu funkciju $\theta(\mu)$ za kvadratni program iz Zadatka 1 seminara.

Polazni primarni problem:
$$f(x) = \frac{1}{2} x^{\mathsf{T}} Q x + c^{\mathsf{T}} x, \qquad g(x) = Gx - h \leq 0.$$
Lagrangian glasi:
$$\mathcal{L}(x, \mu) = \frac{1}{2} x^{\mathsf{T}} Q x + c^{\mathsf{T}} x + \mu^{\mathsf{T}} (Gx - h) = \frac{1}{2} x^{\mathsf{T}} Q x + (c + G^{\mathsf{T}} \mu)^{\mathsf{T}} x - \mu^{\mathsf{T}} h. \tag{3.6}$$

### Korak 1: Rješavanje unutrašnjeg infimuma po $x$
Kako bismo odredili $\theta(\mu) = \inf_{x} \mathcal{L}(x, \mu)$, promatramo $\mathcal{L}(x, \mu)$ kao funkciju po $x$ uz fiksni parametar $\mu$.  
Budući da je matrica $Q \succ 0$ strogo pozitivno definitna, funkcija $x \mapsto \mathcal{L}(x, \mu)$ je strogo konveksna kvadratna funkcija na cijelom $\mathbb{R}^n$. Njezin globalni minimum nalazi se izjednačavanjem gradijenta s nulom:
$$\nabla_x \mathcal{L}(x, \mu) = Q x + c + G^{\mathsf{T}} \mu = 0.$$
Množenjem s inverzom $Q^{-1}$ dobivamo eksplicitnu točku minimuma u ovisnosti o $\mu$:
$$x(\mu) = -Q^{-1} (c + G^{\mathsf{T}} \mu). \tag{3.7}$$

### Korak 2: Uvrštavanje $x(\mu)$ natrag u Lagrangian
Uvrstimo $x(\mu)$ u izraz (3.6):
$$\theta(\mu) = \frac{1}{2} \left[ -Q^{-1} (c + G^{\mathsf{T}} \mu) \right]^{\mathsf{T}} Q \left[ -Q^{-1} (c + G^{\mathsf{T}} \mu) \right] + (c + G^{\mathsf{T}} \mu)^{\mathsf{T}} \left[ -Q^{-1} (c + G^{\mathsf{T}} \mu) \right] - \mu^{\mathsf{T}} h.$$
Iskoristimo simetričnost matrice $Q$ (pa je i $(Q^{-1})^{\mathsf{T}} = Q^{-1}$):
- Prvi član: $\frac{1}{2} (c + G^{\mathsf{T}} \mu)^{\mathsf{T}} Q^{-1} Q Q^{-1} (c + G^{\mathsf{T}} \mu) = \frac{1}{2} (c + G^{\mathsf{T}} \mu)^{\mathsf{T}} Q^{-1} (c + G^{\mathsf{T}} \mu)$.
- Drugi član: $-(c + G^{\mathsf{T}} \mu)^{\mathsf{T}} Q^{-1} (c + G^{\mathsf{T}} \mu)$.

Zbrajanjem prvog i drugog člana dobivamo $-\frac{1}{2}(c + G^{\mathsf{T}} \mu)^{\mathsf{T}} Q^{-1} (c + G^{\mathsf{T}} \mu)$, pa dualna funkcija postaje:
$$\theta(\mu) = -\frac{1}{2} (c + G^{\mathsf{T}} \mu)^{\mathsf{T}} Q^{-1} (c + G^{\mathsf{T}} \mu) - \mu^{\mathsf{T}} h. \tag{3.8}$$

### Korak 3: Raspisivanje na kvadratni, linearni i konstantni član
Razvijmo kvadratni izraz:
$$(c + G^{\mathsf{T}} \mu)^{\mathsf{T}} Q^{-1} (c + G^{\mathsf{T}} \mu) = \mu^{\mathsf{T}} G Q^{-1} G^{\mathsf{T}} \mu + 2 c^{\mathsf{T}} Q^{-1} G^{\mathsf{T}} \mu + c^{\mathsf{T}} Q^{-1} c.$$
Uvrštavanjem u (3.8) dobivamo kanonski oblik Lagrangeove dualne funkcije:
$$\theta(\mu) = -\frac{1}{2} \mu^{\mathsf{T}} \left( G Q^{-1} G^{\mathsf{T}} \right) \mu + \left( -c^{\mathsf{T}} Q^{-1} G^{\mathsf{T}} - h^{\mathsf{T}} \right) \mu - \frac{1}{2} c^{\mathsf{T}} Q^{-1} c. \tag{3.9}$$

> **Ključno svojstvo:** Dualna funkcija $\theta(\mu)$ je kvadratna funkcija po $\mu$.  
> Budući da je $Q \succ 0$, matrica $G Q^{-1} G^{\mathsf{T}}$ je pozitivno semidefinitna (i pozitivno definitna ako $G$ ima puni redak), što znači da je vodeći član $-\frac{1}{2} \mu^{\mathsf{T}} (G Q^{-1} G^{\mathsf{T}}) \mu$ negativno definitan.  
> Prema tome, $\theta(\mu)$ je **strogo konkavna kvadratna funkcija**, a maksimizacija konkavne funkcije uz $\mu \geq 0$ je ponovno **Kvadratni Program (QP)**!

### Numeričke vrijednosti matrica dualnog problema (Zadatak 1):
Uvrstimo numeričke vrijednosti iz seminara:
$$Q^{-1} = \frac{1}{7.91} \begin{bmatrix} 4 & 0.3 \\ 0.3 & 2 \end{bmatrix}, \quad G = \begin{bmatrix} -1 & -1 \\ 1 & -1 \end{bmatrix}, \quad c = \begin{bmatrix} 2 \\ -3 \end{bmatrix}, \quad h = \begin{bmatrix} -10 \\ 3 \end{bmatrix}.$$

Izračunajmo matricu $H_{\mathrm{dual}} = G Q^{-1} G^{\mathsf{T}}$:
$$G Q^{-1} = \begin{bmatrix} -1 & -1 \\ 1 & -1 \end{bmatrix} \frac{1}{7.91} \begin{bmatrix} 4 & 0.3 \\ 0.3 & 2 \end{bmatrix} = \frac{1}{7.91} \begin{bmatrix} -4.3 & -2.3 \\ 3.7 & -1.7 \end{bmatrix},$$
$$H_{\mathrm{dual}} = G Q^{-1} G^{\mathsf{T}} = \frac{1}{7.91} \begin{bmatrix} -4.3 & -2.3 \\ 3.7 & -1.7 \end{bmatrix} \begin{bmatrix} -1 & 1 \\ -1 & -1 \end{bmatrix} = \frac{1}{7.91} \begin{bmatrix} 4.3 + 2.3 & -4.3 + 2.3 \\ -3.7 + 1.7 & 3.7 + 1.7 \end{bmatrix} = \frac{1}{7.91} \begin{bmatrix} 6.6 & -2.0 \\ -2.0 & 5.4 \end{bmatrix}.$$
Matrica je simetrična i pozitivno definitna ($\det H_{\mathrm{dual}} = \frac{6.6 \cdot 5.4 - 4.0}{7.91^2} = \frac{31.64}{62.5681} > 0$).

Izračunajmo linearni vektor $f_{\mathrm{dual}} = G Q^{-1} c + h$:
$$G Q^{-1} c = \frac{1}{7.91} \begin{bmatrix} -4.3 & -2.3 \\ 3.7 & -1.7 \end{bmatrix} \begin{bmatrix} 2 \\ -3 \end{bmatrix} = \frac{1}{7.91} \begin{bmatrix} -8.6 + 6.9 \\ 7.4 + 5.1 \end{bmatrix} = \frac{1}{7.91} \begin{bmatrix} -1.7 \\ 12.5 \end{bmatrix} = \begin{bmatrix} -0.214918 \\ 1.580278 \end{bmatrix},$$
$$f_{\mathrm{dual}} = \begin{bmatrix} -0.214918 \\ 1.580278 \end{bmatrix} + \begin{bmatrix} -10 \\ 3 \end{bmatrix} = \begin{bmatrix} -10.214918 \\ 4.580278 \end{bmatrix}.$$

Konstantni član iznosi:
$$-\frac{1}{2} c^{\mathsf{T}} Q^{-1} c = -\frac{1}{2} \cdot \frac{1}{7.91} \begin{bmatrix} 2 & -3 \end{bmatrix} \begin{bmatrix} 4 & 0.3 \\ 0.3 & 2 \end{bmatrix} \begin{bmatrix} 2 \\ -3 \end{bmatrix} = -\frac{1}{2} \cdot \frac{1}{7.91} (16 - 3.6 + 18) = -\frac{30.4}{15.82} = -1.921618.$$

---

## 3.3 Numeričko rješavanje dualnog problema u MATLAB-u (`quadprog` vs. `fmincon`)

Kako bismo maksimizirali $\theta(\mu)$ uz $\mu \geq 0$, pretvaramo problem u standardni format minimizacije za solver:
$$\min_{\mu \geq 0} \quad \left[ -\theta(\mu) \right] \iff \min_{\mu \geq 0} \quad \frac{1}{2} \mu^{\mathsf{T}} H_{\mathrm{dual}} \mu + f_{\mathrm{dual}}^{\mathsf{T}} \mu. \tag{3.10}$$

### MATLAB implementacija (`quadprog`):
```matlab
% Matrice dualnog problema
H_dual = G * (Q \ G');
f_dual = G * (Q \ c) + h;
lb = [0; 0]; % Ograničenje dualne dopustivosti mu >= 0

opts = optimoptions('quadprog', 'Display', 'none');
[mu_opt, fval_dual, exitflag] = quadprog(H_dual, f_dual, [], [], [], [], lb, [], [], opts);

% Rekonstrukcija optimalne vrijednosti dualne funkcije d*
d_opt = -fval_dual - 0.5 * (c' * (Q \ c));
```

### Zašto koristiti `quadprog`, a ne opći nelinearni rješavač `fmincon`?
U datoteci `task1_output.txt` i seminaru v1.2 jasno je istaknuto:
1. **`quadprog`** je namjenski rješavač za kvadratne programe s linearnim ograničenjima. On koristi egzaktni algoritam aktivnog skupa (*active-set*) ili metodu unutrašnje točke (*interior-point-convex*) i pronalazi rješenje do strojne točnosti uz status:
   $$\texttt{exitflag = 1} \quad \text{(Function converged to a solution)}.$$
2. **`fmincon`** je opći rješavač za nelinearno programiranje. Budući da problem promatra kao opću crnu kutiju (*black-box*), on koristi numeričke procjene gradijenata i koraka. Zbog jednostavnih granica $\mu \geq 0$, `fmincon` često završava na kriteriju minimalne duljine koraka:
   $$\texttt{exitflag = 2} \quad \text{(Step size smaller than TolX)},$$
   što formalno označava raniji prekid bez jamstva strogog zadovoljenja stacionarnosti.

### Usporedba numeričkih rezultata primara i duala:
Iz ispisa MATLAB-a dobivamo:
- Primarni optimum: $x^* = [5.757576, 4.242424]^{\mathsf{T}}$, $p^* = 60.606061$.
- Dualni optimum: $\mu^* = [12.242424, 0.000000]^{\mathsf{T}}$, $d^* = 60.606061$.
- **Dualni procjep:** $|p^* - d^*| = 2.48 \times 10^{-10} \approx 0$.
- Razlika analitičkog KKT rješenja i numeričkog QP rješenja: $|x_{\mathrm{qp}} - x_{\mathrm{analiticki}}| = 7.155 \times 10^{-11}$.

Ovim je egzaktno verificirana **jaka dualnost**!

---

## 3.4 Teorija perturbacija i analiza osjetljivosti: Fizikalno značenje "cijena u sjeni"

Jedan od najvažnijih inženjerskih aspekata dualnosti je analiza što se događa s performansama sustava kada se promijene fizikalni uvjeti ili raspoloživi resursi.

### Perturbirani optimizacijski problem
Neka je zadan perturbirani problem:
$$\begin{aligned}
p^*(v) = \min_{x} \quad & f(x) \\
\text{uz} \quad & g_i(x) \leq v_i, \quad i = 1, \dots, m,
\end{aligned} \tag{3.11}$$
gdje je $v = [v_1, \dots, v_m]^{\mathsf{T}}$ vektor perturbacije desne strane ograničenja.  
- Ako je $v_i < 0$, dopustivo područje se sužava (zahtjevniji inženjerski uvjeti).
- Ako je $v_i > 0$, dopustivo područje se proširuje (popuštanje ograničenja).
- Za $v = 0$ imamo nominalni problem s optimalnom vrijednošću $p^*(0) = p^*$.

> **Teorem 3.3 (Lokalni teorem o osjetljivosti):**  
> Neka je nominalni problem konveksan i strogo zadovoljava Slaterov uvjet. Ako je funkcija perturbirane vrijednosti $p^*(v)$ diferencijabilna u točki $v = 0$, tada njezine parcijalne derivacije po komponentama perturbacije iznose:
> $$\frac{\partial p^*}{\partial v_i}(0) = -\mu_i^*, \quad i = 1, \dots, m, \tag{3.12}$$
> odnosno u vektorskom obliku:
> $$\nabla_v p^*(0) = -\mu^*. \tag{3.13}$$

### Inženjerski i ekonomski izvod:
Iz slabe dualnosti, za perturbirani problem s granicama $g(x) \leq v$ vrijedi:
$$p^*(v) \geq \theta_v(\mu) = \inf_x \left[ f(x) + \mu^{\mathsf{T}} (g(x) - v) \right] = \theta(\mu) - \mu^{\mathsf{T}} v.$$
Uvrstimo optimalni multiplikator nominalnog problema $\mu^*$. Kako vrijedi jaka dualnost za nominalni problem, imamo $\theta(\mu^*) = p^*(0)$, pa slijedi:
$$p^*(v) \geq p^*(0) - (\mu^*)^{\mathsf{T}} v \iff p^*(v) - p^*(0) \geq -(\mu^*)^{\mathsf{T}} v. \tag{3.14}$$
Ova nejednakost pokazuje da je vektor $-\mu^*$ **subgradijent** konveksne funkcije $p^*(v)$ u točki $v = 0$. Ako je funkcija $p^*(v)$ glatka u $v = 0$, subgradijent je jedinstven i jednak klasičnom gradijentu: $\nabla_v p^*(0) = -\mu^*$.

### Fizikalna interpretacija "cijene u sjeni" (*Shadow Price*):
- Predznak minus potječe od konvencije $g_i(x) \leq v_i$:
  - Ako **popuštamo** ograničenje ($v_i > 0$), dopustivi skup se širi, pa minimum $p^*$ može samo pasti ili ostati isti $\implies \Delta p^* \approx -\mu_i^* v_i \leq 0$.
  - Ako **pooštravamo** ograničenje ($v_i < 0$), dopustivi skup se smanjuje, pa trošak raste $\implies \Delta p^* \approx -\mu_i^* v_i \geq 0$.
- Veličina $\mu_i^*$ predstavlja **granični trošak po jedinici ograničenja**. U mehanici, to je točno intenzitet reakcije podloge kojom se zid odupire gibanju.

---

## 3.5 Analiza rezerve (Slack) i lokalna priroda osjetljivosti u Zadatku 1

Primijenimo teorem o osjetljivosti na naš Zadatak 1f:
Optimalni Lagrangeovi multiplikatori su:
$$\mu_1^* = \frac{404}{33} \approx 12.242424, \qquad \mu_2^* = 0.$$

Prema teoremu o osjetljivosti:
$$\frac{\partial p^*}{\partial v_1} = -\mu_1^* = -12.242424, \qquad \frac{\partial p^*}{\partial v_2} = -\mu_2^* = 0. \tag{3.15}$$

### Numerička verifikacija pomoću MATLAB-a:
U MATLAB skripti provedena je konačna diferencijska aproksimacija s perturbacijom $\Delta v = 10^{-5}$:
- Za $v_1$: $\frac{p^*(\Delta v_1) - p^*(0)}{\Delta v_1} = -12.242364$.  
  Odstupanje od analitičke vrijednosti $-\mu_1^*$ iznosi svega $5.99 \times 10^{-5}$, što potvrđuje točnost izvoda.
- Za $v_2$: $\frac{p^*(\Delta v_2) - p^*(0)}{\Delta v_2} = 0.000000$.  
  Odstupanje je točno $0.00 \times 10^0$.

### Ključni inženjerski uvid: Zašto je $\frac{\partial p^*}{\partial v_2} = 0$ i koja su ograničenja te tvrdnje?
Drugo ograničenje $g_2(x) = x_1 - x_2 - 3 \leq 0$ u optimalnoj točki ima vrijednost:
$$g_2(x^*) = 5.757576 - 4.242424 - 3 = -1.484848 < 0.$$
To znači da imamo **rezervu (slack)** od točno $s_2 = 1.484848\,\mathrm{m}$.

1. **Lokalna valjanost:** Sve dok je perturbacija $v_2$ manja od rezerve (odnosno $v_2 \geq -1.484848$), pomicanje granice drugog ograničenja uopće ne dotiče točku optimuma $x^*$. Aktivni skup ostaje isti ($\mathcal{A} = \{1\}$), točka $x^*$ ostaje ista i $p^*$ se ne mijenja. Zato je derivacija jednaka nuli.
2. **Prijelaz aktivnog skupa (nelokalni efekt):** Ako pooštrimo drugo ograničenje za iznos veći od rezerve ($v_2 < -1.484848$), pravac $g_2$ će presjeći točku $x^*$. Od tog trenutka drugo ograničenje postaje aktivno, aktivni skup prelazi u $\mathcal{A} = \{1, 2\}$, točka optimuma se počinje pomicati duž pravca $g_1 = 0$, a derivacija $\frac{\partial p^*}{\partial v_2}$ prestaje biti nula i postaje strogo negativna!

---

## 3.6 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori

### ❓ Tipična ispitna pitanja profesora na obrani

#### Pitanje 3.1: Zašto ste dualni problem riješili funkcijom `quadprog`, a ne općom funkcijom `fmincon`?
*Kontekst:* Razumijevanje matematičke strukture dualnog problema i ponašanja solvera.
> **Modelski odgovor studenta:**  
> "Zato što je Lagrangeov dual kvadratnog programa s linearnim ograničenjima **ponovno kvadratni program**.  
> Analitičkim uvrštavanjem stacionarne točke $x(\mu) = -Q^{-1}(c + G^{\mathsf{T}}\mu)$ u Lagrangian, dobiva se funkcija $\theta(\mu)$ koja je strogo konkavna kvadratna forma po $\mu$. Problem $\max_{\mu \geq 0} \theta(\mu)$ ekvivalentan je minimizaciji konveksne kvadratne funkcije $-\theta(\mu)$ uz jednostavne donje granice $\mu \geq 0$.  
> Namjenski QP solver `quadprog` rješava takav problem egzaktno, iskorištava strukturu Hesseove matrice $H_{\mathrm{dual}} = G Q^{-1} G^{\mathsf{T}}$ i vraća `exitflag = 1` uz nultu toleranciju stacionarnosti. Opći rješavač `fmincon` ne prepoznaje kvadratnu strukturu, provodi skupe linijske pretrage i završava na kriteriju minimalnog koraka (`exitflag = 2`)."

#### Pitanje 3.2: Zašto je derivacija optimalne vrijednosti po perturbaciji $v_2$ jednaka nuli? Znači li to da to ograničenje možemo trajno izbaciti iz modela?
*Kontekst:* Provjera razumijevanja komplementarnosti i lokalne prirode osjetljivosti.
> **Modelski odgovor studenta:**  
> "Derivacija je jednaka nuli jer je drugo ograničenje u optimumu strogo neaktivno ($g_2(x^*) = -1.4848 < 0$), pa je iz uvjeta komplementarnog popuštanja njegov multiplikator $\mu_2^* = 0$. Prema teoremu o osjetljivosti je $\frac{\partial p^*}{\partial v_2} = -\mu_2^* = 0$.  
> Međutim, to ograničenje **ne smijemo trajno izbaciti iz modela**. Derivacija jednaka nuli je **strogo lokalno svojstvo**. Rezerva iznosi točno $1.4848$. Ako se radni uvjeti sustava promijene ili dođe do veće perturbacije desne strane ($v_2 < -1.4848$), granica ograničenja $g_2$ presjeći će trenutni optimum, točka $x^*$ postat će nedopustiva, a ograničenje $g_2$ postat će aktivno i odredit će novi, skuplji optimum."

#### Pitanje 3.3: Može li Lagrangeova dualna funkcija $\theta(\mu)$ poprimiti vrijednost $-\infty$ i što to znači?
*Kontekst:* Dubinsko razumijevanje domene dualne funkcije (Predavanje 4).
> **Modelski odgovor studenta:**  
> "Da, dualna funkcija poprima vrijednost $-\infty$ na onim dijelovima prostora multiplikatora gdje funkcija $x \mapsto \mathcal{L}(x, \mu)$ nije odozdo ograničena.  
> U našem Zadatku 1 to se ne događa jer je $Q \succ 0$, pa je Lagrangian strogo konveksan po $x$ za svaki $\mu$, te infimum uvijek postoji kao konačan broj (efektivna domena dualne funkcije je čitav $\mathbb{R}^m$).  
> Međutim, kod Linearnog Programa (LP), gdje je funkcija cilja linearna ($c^{\mathsf{T}} x$), Lagrangian je afina funkcija po $x$. Infimum je konačan samo ako je koeficijent uz $x$ identički jednak nuli ($c + A^{\mathsf{T}} \mu = 0$). Za bilo koji $\mu$ gdje to nije ispunjeno, $\theta(\mu) = -\infty$. Točke u kojima je $\theta(\mu) = -\infty$ predstavljaju trivijalne donje granice i isključuju se iz dopustivog skupa dualnog problema."

---

### ⚠️ Fatalne zablude i zamke u izvođenju

1. **Zaboravljanje minusa u teoremu o osjetljivosti:** Pisanje $\frac{\partial p^*}{\partial v} = +\mu^*$ umjesto $-\mu^*$. Posljedica: student tvrdi da popuštanje ograničenja ($v > 0$) povećava trošak sustava, što se protivi osnovnim zakonima fizike i ekonomije (veći skup dopustivih rješenja nikada ne može povećati minimum!).
2. **Tvrdnja da je dualni problem konveksan samo ako je primar konveksan:** Česta zabluda. Dualna funkcija $\theta(\mu)$ je **uvijek konkavna**, pa je dualni problem $\max \theta(\mu)$ **uvijek konveksan problem optimizacije**, čak i ako je primarni problem grubo nekonveksan ili diskretan! Konveksnost primara i Slaterov uvjet potrebni su samo za **jaku dualnost** ($d^* = p^*$), a ne za konveksnost samog duala.
3. **Zanemarivanje konstante pri izračunu $d^*$:** Prilikom rješavanja dualnog QP-a u MATLAB-u, funkcija `quadprog` vraća vrijednost kvadratne i linearne forme. Student često zaboravi dodati slobodni konstantni član $-\frac{1}{2} c^{\mathsf{T}} Q^{-1} c = -1.9216$ i zatim se čudi zašto postoji prividni procjep između $p^*$ i $d^*$.
