# POGLAVLJE 2: Karush-Kuhn-Tucker (KKT) uvjeti optimalnosti i geometrija problema

> **Sadržaj poglavlja:**  
> 2.1 Geometrija optimalnosti: Dozvoljeni smjerovi i stožac normala  
> 2.2 Izvod Lagrangeove funkcije i četiri stupa KKT sustava  
> 2.3 Sustavno analitičko rješavanje Zadatka 1b seminara (svih $2^m = 4$ kombinacija)  
> 2.4 Fatalna ispitna zamka: Zašto se točka na sjecištu oba ograničenja odbacuje?  
> 2.5 Geometrijski prikaz i ravnoteža gradijenata (Slika 2.1 seminara)  
> 2.6 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori  

---

## 2.1 Geometrija optimalnosti: Dozvoljeni smjerovi i stožac normala

Kako bismo razumjeli zašto KKT uvjeti imaju upravo onakav oblik kakav imaju, moramo napustiti čisto algebarsko pamćenje formula i sagledati **fizikalnu i geometrijsku sliku** (prof. Jokić, Predavanje 3).

### Problem bez ograničenja (Fermateov teorem)
Kada minimiziramo diferencijabilnu funkciju $f(x)$ na cijelom prostoru $\mathbb{R}^n$, točka $x^*$ je lokalni minimum ako u njoj ne postoji smjer duž kojeg funkcija opada. Budući da je smjer najbržeg pada $-\nabla f(x)$, nužan uvjet je da je nagib jednak nuli:
$$\nabla f(x^*) = 0.$$

### Problem s ograničenjima: Dozvoljeni smjerovi
Kada je kretanje ograničeno na dopustivi skup $\mathcal{F} = \{x \mid g_i(x) \leq 0\}$, točka minimuma $x^*$ često se nalazi **na samom rubu** skupa $\mathcal{F}$. U toj točki gradijent $\nabla f(x^*)$ **u pravilu nije nula**! Funkcija bi rado nastavila padati, ali joj to ne dopuštaju granice skupa.

> **Definicija 2.1 (Dozvoljeni smjer - Feasible direction):**  
> Vektor $d \in \mathbb{R}^n$ ($d \neq 0$) naziva se dozvoljenim smjerom u točki $x \in \mathcal{F}$ ako postoji korak $\alpha_0 > 0$ takav da točka ostaje unutar skupa za sve male pomake:
> $$x + \alpha d \in \mathcal{F}, \quad \forall \alpha \in [0, \alpha_0].$$

Skup svih dozvoljenih smjerova u točki $x$ čini konus dozvoljenih smjerova. Ako je ograničenje $g_i$ aktivno u točki $x$ (tj. $g_i(x) = 0$), Taylorov razvoj prvog reda daje:
$$g_i(x + \alpha d) \approx g_i(x) + \alpha \nabla g_i(x)^{\mathsf{T}} d = \alpha \nabla g_i(x)^{\mathsf{T}} d \leq 0.$$
Dakle, smjer $d$ je dozvoljen ako zatvara tupi kut (ili pravi kut) s vanjskom normalom ograničenja:
$$\nabla g_i(x)^{\mathsf{T}} d \leq 0, \quad \forall i \in \mathcal{A}(x),$$
gdje je $\mathcal{A}(x) = \{i \mid g_i(x) = 0\}$ **aktivni skup ograničenja**.

> **Nužan uvjet optimalnosti prvog reda:**  
> Da bi točka $x^* \in \mathcal{F}$ bila lokalni minimum, funkcija cilja ne smije opadati ni duž jednog dozvoljenog smjera:
> $$\nabla f(x^*)^{\mathsf{T}} d \geq 0, \quad \forall d \in \mathcal{F}(x^*).$$
> Geometrijski: vektor $-\nabla f(x^*)$ ne smije biti dozvoljeni smjer. On mora "udarati u zid" ograničenja, odnosno mora ležati unutar **stožca vanjskih normala** aktivnih ograničenja.

---

## 2.2 Izvod Lagrangeove funkcije i četiri stupa KKT sustava

Kako bismo geometrijski uvjet preveli u algebarski sustav jednadžbi i nejednakosti prikladan za analitičko i numeričko računanje, uvodimo **Lagrangeovu funkciju (Lagrangian)**.

Za problem:
$$\min_{x \in \mathbb{R}^n} f(x) \quad \text{uz} \quad g_i(x) \leq 0, \quad i = 1, \dots, m,$$
Lagrangian glasi (oznaka množitelja $\mu \in \mathbb{R}^m$ s predavanja i vježbi):
$$\mathcal{L}(x, \mu) := f(x) + \sum_{i=1}^m \mu_i g_i(x) = f(x) + \mu^{\mathsf{T}} g(x). \tag{2.1}$$

### Fizikalna analogija (Mehanika sustava)
Zamislimo česticu koja se giba u potencijalnom polju $f(x)$. Čestica teži prema minimumu potencijala pod djelovanjem sile polja $F_{\mathrm{polje}} = -\nabla f(x)$.  
Granice $g_i(x) \leq 0$ predstavljaju neprobojne krute zidove. Kada čestica udari u $i$-ti zid, zid djeluje na česticu **reakcijom podloge** $F_{\mathrm{reakcija}} = -\mu_i \nabla g_i(x)$.  
- Vektor $\nabla g_i(x)$ je vanjska normala na zid (pokazuje prema nedopuštenom području).
- Sila reakcije mora gurati česticu natrag u dopušteno područje $\implies$ sila mora biti suprotna normali, što znači da intenzitet reakcije mora biti **nenegativan** ($\mu_i \geq 0$). Zid može samo gurati česticu, ne može je privlačiti (zid nije ljepljiv!).

U točki statičke ravnoteže (minimuma) zbroj svih sila mora biti nula:
$$F_{\mathrm{polje}} + \sum_{i=1}^m F_{\mathrm{reakcija}, i} = 0 \iff -\nabla f(x^*) - \sum_{i=1}^m \mu_i^* \nabla g_i(x^*) = 0 \iff \nabla f(x^*) + \sum_{i=1}^m \mu_i^* \nabla g_i(x^*) = 0.$$

To je upravo **uvjet stacionarnosti** Lagrangiana!

### Četiri stupa Karush-Kuhn-Tuckerovih (KKT) uvjeta
U točki optimuma $(x^*, \mu^*)$ moraju biti zadovoljena četiri skupa uvjeta:

1. **Uvjet stacionarnosti $(\star)$:**
   $$\nabla_x \mathcal{L}(x^*, \mu^*) = \nabla f(x^*) + \sum_{i=1}^m \mu_i^* \nabla g_i(x^*) = 0. \tag{2.2a}$$
2. **Uvjet primarne dopustivosti $(g)$:**
   $$g_i(x^*) \leq 0, \quad \forall i \in \{1, \dots, m\}. \tag{2.2b}$$
   (Točka $x^*$ mora ležati unutar fizikalno dozvoljenog područja).
3. **Uvjet dualne dopustivosti $(\star\star\star)$:**
   $$\mu_i^* \geq 0, \quad \forall i \in \{1, \dots, m\}. \tag{2.2c}$$
   (Multiplikatori nejednakosti smiju samo pružati otpor / gurati unutra).
4. **Uvjet komplementarnog popuštanja (*Complementary Slackness*) $(\star\star)$:**
   $$\mu_i^* \cdot g_i(x^*) = 0, \quad \forall i \in \{1, \dots, m\}. \tag{2.2d}$$

> **Značenje komplementarnog popuštanja:**  
> Za svako pojedino ograničenje $i$ mora vrijediti barem jedno od dvoje:
> - Ili je ograničenje **neaktivno** u optimumu ($g_i(x^*) < 0$), što znači da čestica ne dodiruje zid, pa je reakcija zida nužno nula: $\mu_i^* = 0$.
> - Ili je množitelj strogo pozitivan ($\mu_i^* > 0$), što znači da zid aktivno sputava česticu, pa se čestica nužno nalazi točno na granici: $g_i(x^*) = 0$.
> Nikada ne može istovremeno biti $g_i(x^*) < 0$ i $\mu_i^* > 0$.

---

## 2.3 Sustavno analitičko rješavanje Zadatka 1b seminara (svih $2^m = 4$ kombinacija)

U Zadatku 1b zadan je kvadratni program s $m = 2$ ograničenja:
$$f(x) = x_1^2 + 2x_2^2 - 0.3 x_1 x_2 + 2x_1 - 3x_2,$$
$$g_1(x) = -x_1 - x_2 + 10 \leq 0, \qquad g_2(x) = x_1 - x_2 - 3 \leq 0.$$

Gradijent funkcije cilja po projektnim varijablama $x_1$ i $x_2$ iznosi:
$$\nabla f(x) = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\[4pt] \frac{\partial f}{\partial x_2} \end{bmatrix} = \begin{bmatrix} 2x_1 - 0.3x_2 + 2 \\[4pt] -0.3x_1 + 4x_2 - 3 \end{bmatrix}.$$

Gradijenti funkcija ograničenja su konstantni vektori normala:
$$\nabla g_1(x) = \begin{bmatrix} -1 \\ -1 \end{bmatrix}, \qquad \nabla g_2(x) = \begin{bmatrix} 1 \\ -1 \end{bmatrix}.$$

Uvjet stacionarnosti raspisan glasi:
$$\begin{bmatrix} 2x_1 - 0.3x_2 + 2 \\ -0.3x_1 + 4x_2 - 3 \end{bmatrix} + \mu_1 \begin{bmatrix} -1 \\ -1 \end{bmatrix} + \mu_2 \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}. \tag{2.3}$$

Zbog uvjeta komplementarnosti $\mu_1 g_1 = 0$ i $\mu_2 g_2 = 0$, imamo točno $2^2 = 4$ kombinacije aktivnosti ograničenja. Provest ćemo sustavno analitičko rješavanje za svaku kombinaciju, točno onako kako se to radi na Vježbama 3.

---

### Slučaj 1: Nijedno ograničenje nije aktivno ($\mu_1 = 0, \mu_2 = 0$)
Pretpostavimo da se optimum nalazi u unutrašnjosti dopustivog skupa. Tada su oba multiplikatora nula, pa se uvjet stacionarnosti svodi na slobodni minimum funkcije cilja:
$$\begin{aligned}
2x_1 - 0.3x_2 + 2 &= 0 \\
-0.3x_1 + 4x_2 - 3 &= 0
\end{aligned} \iff Q x = -c \implies x = -Q^{-1} c.$$

Inverz matrice $Q = \begin{bmatrix} 2 & -0.3 \\ -0.3 & 4 \end{bmatrix}$ uz $\det Q = 2 \cdot 4 - (-0.3)^2 = 7.91$ glasi:
$$Q^{-1} = \frac{1}{7.91} \begin{bmatrix} 4 & 0.3 \\ 0.3 & 2 \end{bmatrix}.$$
Uvrštavanjem $c = \begin{bmatrix} 2 \\ -3 \end{bmatrix}$:
$$x_{\mathrm{unc}} = -\frac{1}{7.91} \begin{bmatrix} 4 & 0.3 \\ 0.3 & 2 \end{bmatrix} \begin{bmatrix} 2 \\ -3 \end{bmatrix} = -\frac{1}{7.91} \begin{bmatrix} 8 - 0.9 \\ 0.6 - 6 \end{bmatrix} = -\frac{1}{7.91} \begin{bmatrix} 7.1 \\ -5.4 \end{bmatrix} = \begin{bmatrix} -0.897598 \\ 0.682680 \end{bmatrix}.$$

Sada provjeravamo primarnu dopustivost uvrštavanjem u ograničenja:
$$g_1(x_{\mathrm{unc}}) = -(-0.897598) - (0.682680) + 10 = 0.897598 - 0.682680 + 10 = +10.214918 > 0!$$
> **Zaključak za Slučaj 1:** Prvo ograničenje je drastično prekršeno ($g_1 > 0$). Slobodni minimum leži duboko u nedopuštenom području. **Slučaj 1 se odbacuje.**

---

### Slučaj 3: Samo je drugo ograničenje aktivno ($g_2 = 0, \mu_1 = 0$)
Pretpostavimo da ležimo na pravcu $g_2(x) = x_1 - x_2 - 3 = 0$, dok je prvo ograničenje neaktivno ($\mu_1 = 0$).  
Sustav stacionarnosti i aktivnosti glasi:
$$\begin{aligned}
2x_1 - 0.3x_2 + 2 + \mu_2 &= 0 \quad &(1) \\
-0.3x_1 + 4x_2 - 3 - \mu_2 &= 0 \quad &(2) \\
x_1 - x_2 - 3 &= 0 \quad &(3)
\end{aligned}$$

Zbrajanjem jednadžbi (1) i (2) eliminiramo $\mu_2$:
$$(2 - 0.3)x_1 + (-0.3 + 4)x_2 + (2 - 3) = 0 \implies 1.7x_1 + 3.7x_2 - 1 = 0.$$
Iz jednadžbe (3) izrazimo $x_1 = x_2 + 3$ i uvrstimo:
$$1.7(x_2 + 3) + 3.7x_2 - 1 = 0 \implies 5.4x_2 + 5.1 - 1 = 0 \implies 5.4x_2 = -4.1 \implies x_2 = -\frac{4.1}{5.4} = -\frac{41}{54} \approx -0.759259.$$
Tada je:
$$x_1 = -\frac{41}{54} + 3 = \frac{121}{54} \approx 2.240741.$$
Sada izračunajmo Lagrangeov množitelj $\mu_2$ iz jednadžbe (1):
$$\mu_2 = -2x_1 + 0.3x_2 - 2 = -2(2.240741) + 0.3(-0.759259) - 2 = -4.481481 - 0.227778 - 2 = -6.709259 < 0!$$
Također provjerimo i prvo ograničenje:
$$g_1(x) = -x_1 - x_2 + 10 = -2.240741 - (-0.759259) + 10 = -1.481481 + 10 = +8.518519 > 0!$$
> **Zaključak za Slučaj 3:** Narušeni su i dualna dopustivost ($\mu_2 < 0$) i primarna dopustivost ($g_1 > 0$). **Slučaj 3 se odbacuje.**

---

## 2.4 Fatalna ispitna zamka: Zašto se točka na sjecištu oba ograničenja odbacuje?

Razmotrimo sada **Slučaj 4**, koji predstavlja najčešću zamku na usmenom ispitu kod prof. Jokića!

### Slučaj 4: Oba ograničenja su aktivna ($g_1 = 0, g_2 = 0$)
Točka se nalazi na sjecištu pravaca oba ograničenja:
$$\begin{aligned}
-x_1 - x_2 + 10 &= 0 \implies x_1 + x_2 = 10 \\
x_1 - x_2 - 3 &= 0 \implies x_1 - x_2 = 3
\end{aligned}$$
Zbrajanjem ovih dviju jednadžbi dobivamo:
$$2x_1 = 13 \implies x_1 = 6.5.$$
Oduzimanjem dobivamo:
$$2x_2 = 7 \implies x_2 = 3.5.$$
Dakle, geometrijska točka sjecišta je točno $x = \begin{bmatrix} 6.5 \\ 3.5 \end{bmatrix}$.

Studenti na ispitu često brzopleto kažu: *"Točka zadovoljava $g_1 = 0$ i $g_2 = 0$, dakle nalazi se unutar dopustivog skupa $\mathcal{F}$. Je li to optimum?"*

Da bismo saznali je li to optimum, **moramo provjeriti uvjet stacionarnosti i predznake multiplikatora** $\mu_1$ i $\mu_2$!  
Iz uvjeta stacionarnosti (2.3):
$$\begin{bmatrix} -1 & 1 \\ -1 & -1 \end{bmatrix} \begin{bmatrix} \mu_1 \\ \mu_2 \end{bmatrix} = -\nabla f(x) = -\begin{bmatrix} 2(6.5) - 0.3(3.5) + 2 \\ -0.3(6.5) + 4(3.5) - 3 \end{bmatrix} = -\begin{bmatrix} 13 - 1.05 + 2 \\ -1.95 + 14 - 3 \end{bmatrix} = -\begin{bmatrix} 13.95 \\ 9.05 \end{bmatrix}.$$

Raspisano po komponentama:
$$\begin{aligned}
-\mu_1 + \mu_2 &= -13.95 \quad &(A) \\
-\mu_1 - \mu_2 &= -9.05 \quad &(B)
\end{aligned}$$
Zbrojimo jednadžbe $(A)$ i $(B)$:
$$-2\mu_1 = -23.00 \implies \mu_1 = \frac{23.00}{2} = +11.50 > 0.$$
Oduzmemo jednadžbu $(B)$ od jednadžbe $(A)$:
$$2\mu_2 = -13.95 - (-9.05) = -4.90 \implies \mu_2 = -\frac{4.90}{2} = -2.45 < 0!$$

> 🔴 **KLJUČNI ISPITNI NALAZ:**  
> Multiplikator $\mu_2 = -2.45$ je **strogo negativan**!  
> Time je prekršen uvjet dualne dopustivosti ($\mu_2 \geq 0$).  
> **Točka $x = [6.5, 3.5]^{\mathsf{T}}$ NIJE optimum i Slučaj 4 se odbacuje!**

### Dubinska inženjerska i geometrijska interpretacija zašto $\mu_2 < 0$ odbacuje točku:
Zašto se točka odbacuje iako leži na rubu dopustivog skupa?
1. Predznak $\mu_2 < 0$ znači da bi ograničenje $g_2$ moralo **vući česticu prema van**, dakle ponašati se kao ljepljiva traka, a ne kao jednostrani kruti zid.
2. Normala drugog ograničenja je $\nabla g_2 = [1, -1]^{\mathsf{T}}$. Gradijent funkcije cilja $\nabla f(6.5, 3.5) = [13.95, 9.05]^{\mathsf{T}}$ ima skalarni produkt s unutarnjom normalom $-\nabla g_2 = [-1, 1]^{\mathsf{T}}$:
   $$\nabla f(x)^{\mathsf{T}} (-\nabla g_2) = 13.95(-1) + 9.05(1) = -13.95 + 9.05 = -4.90 < 0.$$
   To znači da pomakom s granice $g_2 = 0$ **prema unutrašnjosti skupa** ($g_2 < 0$), funkcija cilja $f(x)$ **strogo opada**!
3. Granica $g_2$ ne sprječava pad funkcije, već sustav "želi" pobjeći od granice $g_2 = 0$ dublje u područje $g_2 < 0$, krećući se duž pravca $g_1 = 0$. Zato optimum ne može biti u sjecištu!

---

### Slučaj 2: Samo je prvo ograničenje aktivno ($g_1 = 0, \mu_2 = 0$)
Pretpostavimo da je optimalna točka na pravcu $g_1(x) = -x_1 - x_2 + 10 = 0$, dok je drugo ograničenje neaktivno ($g_2(x) < 0 \implies \mu_2 = 0$).

Sustav glasi:
$$\begin{aligned}
2x_1 - 0.3x_2 + 2 - \mu_1 &= 0 \quad &(1) \\
-0.3x_1 + 4x_2 - 3 - \mu_1 &= 0 \quad &(2) \\
-x_1 - x_2 + 10 &= 0 \quad &(3)
\end{aligned}$$

Izjednačimo $\mu_1$ iz prve dvije jednadžbe:
$$2x_1 - 0.3x_2 + 2 = -0.3x_1 + 4x_2 - 3 \implies 2.3x_1 - 4.3x_2 + 5 = 0.$$
Iz jednadžbe (3) uvrstimo $x_1 = 10 - x_2$:
$$2.3(10 - x_2) - 4.3x_2 + 5 = 0 \implies 23 - 2.3x_2 - 4.3x_2 + 5 = 0 \implies -6.6x_2 + 28 = 0.$$
Odavde slijedi egzaktna vrijednost u razlomku:
$$x_2^* = \frac{28}{6.6} = \frac{280}{66} = \frac{140}{33} \approx 4.242424.$$
Tada je $x_1^*$:
$$x_1^* = 10 - \frac{140}{33} = \frac{330 - 140}{33} = \frac{190}{33} \approx 5.757576.$$

Sada izračunajmo Lagrangeov množitelj $\mu_1^*$ iz jednadžbe (1):
$$\mu_1^* = 2\left(\frac{190}{33}\right) - 0.3\left(\frac{140}{33}\right) + 2 = \frac{380}{33} - \frac{42}{33} + \frac{66}{33} = \frac{380 - 42 + 66}{33} = \frac{404}{33} \approx 12.242424.$$
Budući da je $\mu_1^* = 12.242424 > 0$, **uvjet dualne dopustivosti je zadovoljen**!

Preostaje provjeriti primarnu dopustivost drugog ograničenja:
$$g_2(x^*) = x_1^* - x_2^* - 3 = \frac{190}{33} - \frac{140}{33} - 3 = \frac{50}{33} - \frac{99}{33} = -\frac{49}{33} \approx -1.484848 < 0.$$
Budući da je $g_2(x^*) = -1.484848 < 0$, **drugo ograničenje je strogo zadovoljeno s rezervom (slack) od $1.4848$**.

Izračunajmo optimalnu vrijednost funkcije cilja $p^* = f(x^*)$:
$$f(x^*) = \left(\frac{190}{33}\right)^2 + 2\left(\frac{140}{33}\right)^2 - 0.3\left(\frac{190}{33}\right)\left(\frac{140}{33}\right) + 2\left(\frac{190}{33}\right) - 3\left(\frac{140}{33}\right) = \frac{2000}{33} \approx 60.606061.$$

### Sažetak provjere svih 4 kombinacije:
Tablica 2.1 sažima rezultate rješavanja svih slučajeva (usklađeno s tablicom iz seminara v1.2 i MATLAB ispisom):

| Slučaj | Pretpostavka aktivnosti | Izračunata točka $x$ | Multiplikatori $\mu$ | Vrijednosti $g(x)$ | Status rješenja |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | $\mu_1 = 0, \mu_2 = 0$ | $(-0.8976, 0.6827)$ | $(0, 0)$ | $g_1 = +10.215, g_2 = -4.580$ | ❌ Odbačen ($g_1 > 0$) |
| **2** | $g_1 = 0, \mu_2 = 0$ | $(\frac{190}{33}, \frac{140}{33}) \approx (5.7576, 4.2424)$ | $\mu_1 = \frac{404}{33} \approx 12.2424, \mu_2 = 0$ | $g_1 = 0, g_2 = -1.4848$ |  **JEDINSTVENI OPTIMUM** |
| **3** | $\mu_1 = 0, g_2 = 0$ | $(2.2407, -0.7593)$ | $\mu_1 = 0, \mu_2 = -6.7093$ | $g_1 = +8.519, g_2 = 0$ | ❌ Odbačen ($\mu_2 < 0, g_1 > 0$) |
| **4** | $g_1 = 0, g_2 = 0$ | $(6.5000, 3.5000)$ | $\mu_1 = 11.50, \mu_2 = -2.45$ | $g_1 = 0, g_2 = 0$ | ❌ Odbačen ($\mu_2 < 0$) |

---

## 2.5 Geometrijski prikaz i ravnoteža gradijenata (Slika 2.1 seminara)

U podzadatku (c) traži se geometrijska verifikacija rješenja. Pogledajmo što se fizikalno događa u točki optimuma $x^* = (5.7576, 4.2424)$:

1. **Gradijent funkcije cilja u optimumu:**
   $$\nabla f(x^*) = \begin{bmatrix} 2(5.7576) - 0.3(4.2424) + 2 \\ -0.3(5.7576) + 4(4.2424) - 3 \end{bmatrix} = \begin{bmatrix} 12.242424 \\ 12.242424 \end{bmatrix}.$$
2. **Gradijent aktivnog ograničenja $g_1$:**
   $$\nabla g_1 = \begin{bmatrix} -1 \\ -1 \end{bmatrix}.$$
3. **Provjera uvjeta stacionarnosti:**
   $$\nabla f(x^*) + \mu_1^* \nabla g_1 = \begin{bmatrix} 12.242424 \\ 12.242424 \end{bmatrix} + 12.242424 \begin{bmatrix} -1 \\ -1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}.$$
   Odavde je:
   $$\nabla f(x^*) = -\mu_1^* \nabla g_1 = -12.242424 \begin{bmatrix} -1 \\ -1 \end{bmatrix} = 12.242424 \begin{bmatrix} 1 \\ 1 \end{bmatrix}.$$

### Geometrijsko značenje na Slici 2.1 (`fig1_1_qp_primal_geometry.pdf`):
- Nivo-krivulje funkcije cilja $f(x) = c$ su elipse nagnute u ravnini zbog mješovitog člana $-0.3 x_1 x_2$.
- Pravac aktivnog ograničenja $x_1 + x_2 = 10$ je tangenta na elipsu razine $f(x) = 60.606$ točno u točki $x^*$.
- Vektor gradijenta funkcije cilja $\nabla f(x^*)$ okomit je na tangentu elipse i usmjeren prema van (u smjeru rasta funkcije).
- Vektor gradijenta ograničenja $\nabla g_1 = [-1, -1]^{\mathsf{T}}$ okomit je na pravac ograničenja i usmjeren prema nedopuštenom području.
- Budući da su ti vektori antiparalelni ($\nabla f(x^*) = -\mu_1^* \nabla g_1$ uz $\mu_1^* > 0$), nivo-elipsa i pravac ograničenja se **glatko dodiruju**, a svako kretanje duž pravca vodi u elipse s većom vrijednošću funkcije cilja.

---

## 2.6 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori

### ❓ Tipična ispitna pitanja profesora na obrani

#### Pitanje 2.1: Zašto ste odbacili Slučaj 4, iako se točka nalazi na samom sjecištu granica oba ograničenja i formalno zadovoljava primarna ograničenja?
*Kontekst:* Glavno eliminacijsko pitanje za provjeru razumijevanja KKT uvjeta.
> **Modelski odgovor studenta:**  
> "Zato što je u toj točki narušen uvjet **dualne dopustivosti**.  
> Točka sjecišta $x_1 + x_2 = 10$ i $x_1 - x_2 = 3$ iznosi $x = (6.5, 3.5)$. Uvrštavanjem u uvjet stacionarnosti dobiva se $\mu_1 = 11.50$, ali $\mu_2 = -2.45 < 0$.  
> Fizikalno i geometrijski: negativan množitelj $\mu_2$ znači da bi ograničenje $g_2$ moralo djelovati kao privlačna sila (vući točku), dok nejednakost dopušta samo odbojne reakcije podloge. Skalarni produkt gradijenta cilja i unutarnje normale $-\nabla g_2$ je strogo negativan, što dokazuje da funkcija cilja opada kretanjem od granice $g_2 = 0$ prema unutrašnjosti dopustivog skupa duž pravca $g_1 = 0$. Prema tome, točka u sjecištu ne može biti točka minimuma."

#### Pitanje 2.2: Što fizikalno predstavlja uvjet komplementarnog popuštanja ($\mu_i g_i(x) = 0$)?
*Kontekst:* Povezivanje mehanike i matematičke optimizacije.
> **Modelski odgovor studenta:**  
> "Fizikalno, uvjet komplementarnosti izražava princip da pasivna veza ne može proizvoditi silu reakcije.  
> Ako je točka u unutrašnjosti dopustivog područja s obzirom na $i$-to ograničenje ($g_i(x) < 0$), sustav ne dodiruje granicu, pa je sila otpora jednaka nuli ($\mu_i = 0$).  
> Sila reakcije ($\mu_i > 0$) može postojati samo i jedino ako sustav fizički leži na samoj granici ($g_i(x) = 0$) i nastoji je probiti. Umnožak $\mu_i g_i(x) = 0$ matematički osigurava da nema 'djelovanja sile na daljinu'."

#### Pitanje 2.3: Kada su KKT uvjeti nužni, a kada dovoljni uvjeti optimalnosti?
*Kontekst:* Teoretska klasifikacija uvjeta optimalnosti (Predavanja 3 i 4).
> **Modelski odgovor studenta:**  
> "Za opće glatke nelinearne probleme, KKT uvjeti su samo **nužni** uvjeti lokalne optimalnosti, i to uz pretpostavku da vrijedi neka kvalifikacija ograničenja (npr. LICQ ili Slaterov uvjet). To znači da svaka točka lokalnog minimuma mora zadovoljavati KKT, ali svaka KKT točka ne mora biti minimum (može biti sedlasta točka ili lokalni maksimum).  
> Međutim, za **konveksne optimizacijske probleme** (konveksna funkcija cilja, konveksan dopustivi skup) uz zadovoljen Slaterov uvjet kvalifikacije ograničenja, KKT uvjeti postaju **nužni i dovoljni** za globalni optimum. To znači da je svaka točka koja zadovoljava KKT uvjete ujedno i globalni minimum problema."

---

### ⚠️ Fatalne zablude i zamke u izvođenju

1. **Proglašavanje stacionarne točke optimumom bez provjere multiplikatora:** Student nađe točku koja zadovoljava $Qx + c + G^{\mathsf{T}}\mu = 0$ i $Gx \leq h$, ali zaboravi provjeriti je li $\mu \geq 0$. To je najbrži put do pada na usmenom ispitu.
2. **Pogrešno tumačenje predznaka u Lagrangianu:** Ako se Lagrangian definira s plusom ($\mathcal{L} = f + \mu^{\mathsf{T}} g$), tada je uvjet stacionarnosti $\nabla f + G^{\mathsf{T}} \mu = 0$ uz $\mu \geq 0$. Ako student zabunom stavi minus ($\mathcal{L} = f - \mu^{\mathsf{T}} g$), cijeli sustav znakova se invertira, što unosi kaos u analizu aktivnosti. Uvijek se držati definicije s predavanja prof. Jokića!
3. **Zabluda o broju aktivnih ograničenja u $\mathbb{R}^2$:** Česta je zabluda da u dvodimenzionalnom problemu u optimumu uvijek moraju biti aktivna dva ograničenja. Kao što Zadatak 1 jasno pokazuje, optimum leži na glatkom dijelu pravca gdje je aktivno samo **jedno** ograničenje ($g_1 = 0$), dok je drugo neaktivno ($g_2 < 0$).
