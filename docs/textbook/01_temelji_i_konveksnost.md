# POGLAVLJE 1: Temelji optimizacije, matematički aparat i konveksnost

> **Sadržaj poglavlja:**  
> 1.1 First Principles: Vektorski i matrični prostori, unutrašnji produkti i definitnost  
> 1.2 Anatomija optimizacijskog problema s ograničenjima  
> 1.3 Teorija konveksnih skupova i konveksnih funkcija  
> 1.4 Zadatak 1a seminara: Egzaktna formulacija Kvadratnog Programa (QP)  
> 1.5 Dokaz stroge konveksnosti, egzistencije i jedinstvenosti optimuma  
> 1.6 Slaterov uvjet kvalifikacije ograničenja  
> 1.7 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori  

---

## 1.1 First Principles: Vektorski i matrični prostori, unutrašnji produkti i definitnost

### Pristup od nule: Kako intuitivno zamisliti optimizaciju?
Zamislimo da se nalazimo u gustom planinskom krajoliku prekrivenom gustom maglom. Naš zadatak je pronaći najnižu točku u kotlini (minimum).
- **Projektne varijable $x = [x_1, x_2]^\mathsf{T}$:** To su naše GPS koordinate (npr. geografska širina i dužina). To su veličine koje inženjer slobodno bira ili podešava.
- **Funkcija cilja $f(x)$:** To je nadmorska visina terena na koordinatama $(x_1, x_2)$. Želimo se spustiti što je niže moguće ($f(x) \to \min$).
- **Ograničenja $g_i(x) \leq 0$:** To su ograde u prostoru (npr. provalija, minsko polje, granica parcele). Ne smijemo prijeći preko ograde.
- **Optimizacija:** Traženje one točke unutar dopuštenog dijela parcele na kojoj je nadmorska visina najniža moguća.

> [!TIP]
> **Referenca na rječnik:** Za detaljan popis svih simbola, logičkih operatora i njihovih izgovora pogledajte **Poglavlje 0: Matematički rječnik i govorni vodič za usmeni ispit**.

---

### Euklidski prostor $\mathbb{R}^n$ — Što je to zapravo?
U inženjerstvu promatramo realni $n$-dimenzionalni euklidski prostor označen sa $\mathbb{R}^n$.
- **Što znači simbol $\mathbb{R}$?** Simbol $\mathbb{R}$ označava skup svih realnih brojeva (brojevi poput $3$, $-5.2$, $\sqrt{2}$, $\pi$).
- **Što znači eksponent $n$?** Eksponent $n$ označava dimenziju prostora, odnosno broj koordinata.
  - Za $n = 1$: to je običan realni pravac ($\mathbb{R}$).
  - Za $n = 2$: to je ravnina (poput lista papira ili ploče) gdje svaka točka ima dvije koordinate: $x = [x_1, x_2]^\mathsf{T}$. To je prostor u kojem rješavamo Zadatke 1, 2 i 4!
  - Za $n = 3$: to je trodimenzionalni fizikalni prostor u kojem živimo ($x_1, x_2, x_3$).
  - Za $n > 3$: to je višedimenzionalni prostor parametara (u Zadatku 3 imamo $N+1 = 21$ ili $101$ koordinatu visine nivelete!).
- **Zašto se zove "euklidski"?** Zato što u njemu vrijedi Euklidska geometrija i Pitagorin poučak za udaljenost: udaljenost točke od ishodišta računa se preko korijena sume kvadrata.

Element tog prostora je vektor-stupac $x \in \mathbb{R}^n$:
$$x = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}, \qquad x_i \in \mathbb{R}, \quad i \in \{1, 2, \dots, n\}.$$

> **Govorni predložak (kako pročitati pred pločom):**  
> *"x je vektor-stupac iz n-dimenzionalnog realnog prostora r-n, čije su komponente x-1 do x-n projektne varijable sustava."*

---

### Što predstavlja simbol `:=` ?
U matematičkom tekstu često susrećemo simbol `:=` (dvotočka jednako).  
- **Značenje:** `:=` označava **jednakost po definiciji** (*equal by definition*).
- **Razlika od običnog `=`:** Običan znak jednakosti ($A = B$) tvrdi da su dvije prethodno poznate veličine jednake (npr. $2 + 2 = 4$ ili $f(x^*) = 60.6$). Znak `:=` uvodi **sasvim novu oznaku ili pojam** i definira ga pomoću izraza s desne strane (npr. $q(x) := x^\mathsf{T} A x$).
- **Govorni izgovor:** *"definirano kao"* ili *"jednako po definiciji"*.

---

### Skalarni (unutrašnji) produkt $\langle x, y \rangle$ i transponiranje $(\cdot)^\mathsf{T}$
Za dva vektora $x, y \in \mathbb{R}^n$, standardni euklidski skalarni produkt definiran je kao:
$$\langle x, y \rangle := x^{\mathsf{T}} y = \sum_{i=1}^n x_i y_i = x_1 y_1 + x_2 y_2 + \dots + x_n y_n.$$

- **Što je operacija transponiranja $(\cdot)^\mathsf{T}$?**  
  Ako je $x$ vektor-stupac dimenzije $n \times 1$, njegovo transponiranje $x^\mathsf{T}$ pretvara stupac u vektor-redak dimenzije $1 \times n$:
  $$x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \implies x^\mathsf{T} = \begin{bmatrix} x_1 & x_2 \end{bmatrix}.$$
  Kada pomnožimo redak dimenzije $1 \times n$ sa stupcem dimenzije $n \times 1$, matrično množenje daje skalar (jedan broj) dimenzije $1 \times 1$:
  $$x^\mathsf{T} y = \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = x_1 y_1 + x_2 y_2.$$
- **Što predstavlja oznaka $\langle x, y \rangle$?**  
  To su šiljaste zagrade (*angle brackets*) koje u naprednoj matematici označavaju unutrašnji produkt. U euklidskom prostoru $\mathbb{R}^n$ oznake $\langle x, y \rangle$ i $x^\mathsf{T} y$ su **potpuni sinonimi**.
- **Geometrijsko značenje skalarnog produkta:**  
  $$\langle x, y \rangle = \|x\|_2 \|y\|_2 \cos \varphi,$$
  gdje je $\varphi$ kut između vektora.
  - Ako je $\langle x, y \rangle > 0$, kut je šiljast ($\varphi < 90^\circ$). Vektori "djelomično pokazuju u istom smjeru".
  - Ako je $\langle x, y \rangle = 0$, kut je točno $90^\circ$ — **vektori su ortogonalni (okomiti)**!
  - Ako je $\langle x, y \rangle < 0$, kut je tupi ($\varphi > 90^\circ$). Vektori se "opiru" jedan drugome.

> **Govorni predložak:**  
> *"Skalarni produkt vektora x i y, označen kao x-transponirano puta y ili unutrašnji produkt x zarez y, jednak je sumi umnožaka odgovarajućih koordinata."*

---

### Euklidska norma i duljina vektora
Skalarni produkt inducira **euklidsku normu** ($\ell_2$-normu) koja predstavlja geometrijsku duljinu vektora u prostoru (udaljenost točke od ishodišta):
$$\|x\|_2 := \sqrt{\langle x, x \rangle} = \sqrt{x^{\mathsf{T}} x} = \sqrt{\sum_{i=1}^n x_i^2} = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}.$$
To je doslovno Pitagorin poučak u $n$ dimenzija!

Uz euklidsku normu, u inženjerstvu i kolegiju OMRiUS ključne su još dvije norme:
1. **$\ell_1$-norma (Manhattan ili taksi norma):**  
   $$\|x\|_1 := \sum_{i=1}^n |x_i| = |x_1| + |x_2| + \dots + |x_n|.$$
   U Zadatku 3 vidjet ćemo da $\ell_1$-norma točno mjeri fizikalni volumen zemljanih radova (iskopa i nasipa).
2. **$\ell_\infty$-norma (Chebyshevjeva norma):**  
   $$\|x\|_\infty := \max_{1 \leq i \leq n} |x_i|.$$
   Mjeri najveće vršno pojedinačno odstupanje među svim koordinatama.

---

### Simetrične matrice i Loewnerov parcijalni poredak ($\succeq$ i $\succ$)
Skup svih realnih simetričnih matrica dimenzija $n \times n$ označavamo sa $\mathbb{S}^n$:
$$\mathbb{S}^n := \{A \in \mathbb{R}^{n \times n} \mid A = A^{\mathsf{T}}\}.$$
Simetrična matrica je matrica koja je zrcalna s obzirom na glavnu dijagonalu ($A_{ij} = A_{ji}$).

Za simetričnu matricu $A \in \mathbb{S}^n$ promatramo **kvadratnu formu** $q(x) = x^{\mathsf{T}} A x$. 

> **Definicija 1.1 (Pozitivna semidefinitnost i definitnost):**
> Neka je $A \in \mathbb{S}^n$. Kažemo da je matrica $A$:
> 1. **Pozitivno semidefinitna**, u oznaci $A \succeq 0$, ako vrijedi:
>    $$x^{\mathsf{T}} A x \geq 0, \quad \forall x \in \mathbb{R}^n.$$
>    Ekvivalentno: sve svojstvene vrijednosti matrice $A$ su nenegativne ($\lambda_i(A) \geq 0, \, \forall i$).
> 2. **Pozitivno definitna**, u oznaci $A \succ 0$, ako vrijedi:
>    $$x^{\mathsf{T}} A x > 0, \quad \forall x \in \mathbb{R}^n \setminus \{0\}.$$
>    Ekvivalentno: sve svojstvene vrijednosti matrice $A$ su strogo pozitivne ($\lambda_i(A) > 0, \, \forall i$).

- **Što znače simboli $\succeq$ i $\succ$?**  
  To nisu obične skalarne nejednakosti ($\geq$ i $>$), već **matrične nejednakosti**.  
  Relacija $A \succeq B$ znači da je razlika matrica $(A - B)$ pozitivno semidefinitna.  
  Taj parcijalni poredak matrica naziva se **Loewnerov poredak**.  
  Linearna nejednakost u kojoj nepoznate matrice stoje u Loewnerovom poretku naziva se **Linearna matrična nejednakost (LMI - Linear Matrix Inequality)**, što je temelj Zadatka 4!

> **Govorni predložak:**  
> *"Matrica A je pozitivno definitna, u oznaci A strogo veće od nula u smislu Loewnera, ako je kvadratna forma x-transponirano A x strogo pozitivna za svaki vektor x različit od nul-vektora, što je ekvivalentno činjenici da su sve svojstvene vrijednosti matrice A strogo veće od nula."*

---

## 1.2 Anatomija optimizacijskog problema s ograničenjima

Standardni matematički oblik optimizacijskog problema u kontinuiranom prostoru glasi:

$$\begin{aligned}
\min_{x \in \mathbb{R}^n} \quad & f_0(x) \\
\text{uz ograničenja} \quad & f_i(x) \leq 0, \quad i = 1, \dots, m, \\
& h_j(x) = 0, \quad j = 1, \dots, p.
\end{aligned} \tag{1.1}$$

Pojmovnik i fizikalno značenje komponenata:
- **Funkcija cilja (kriterij optimalnosti) $f_0: \mathbb{R}^n \to \mathbb{R}$:** Funkcija koju želimo minimizirati. Predstavlja mjeru nepoželjnog stanja: energiju gubitaka, utrošeni materijal, financijski trošak, pogrešku vođenja ili vrijeme odziva.
- **Ograničenja nejednakosti $f_i(x) \leq 0$:** Predstavljaju fizikalna i tehnička ograničenja sustava: maksimalno dozvoljeno naprezanje materijala, geometrijske gabarite, granice hoda aktuatora, temperaturne limite.
- **Ograničenja jednakosti $h_j(x) = 0$:** Predstavljaju kinematičke veze, zakone očuvanja mase i energije, rubne uvjete na krajevima trajektorije ili statičku ravnotežu.
- **Dozvoljeni (dopustivi) skup $\mathcal{F}$:**
  $$\mathcal{F} := \{x \in \mathbb{R}^n \mid f_i(x) \leq 0, \; i = 1, \dots, m; \quad h_j(x) = 0, \; j = 1, \dots, p\}.$$
  Točka $x$ je **dopustiva** (*feasible*) ako leži u $\mathcal{F}$. Ako je $\mathcal{F} = \emptyset$, problem je nedopustiv.
- **Optimalna vrijednost $p^*$:**
  $$p^* := \inf \{f_0(x) \mid x \in \mathcal{F}\}.$$
  Ako je problem nedopustiv, po definiciji uzimamo $p^* = +\infty$. Ako funkcija nije odozdo ograničena na $\mathcal{F}$, $p^* = -\infty$.
- **Lokalni vs. Globalni minimum:**
  - Točka $x^* \in \mathcal{F}$ je **lokalni minimum** ako postoji okolina $B(x^*, \epsilon) = \{x \mid \|x - x^*\| < \epsilon\}$ takva da je $f_0(x^*) \leq f_0(x)$ za sve $x \in \mathcal{F} \cap B(x^*, \epsilon)$.
  - Točka $x^* \in \mathcal{F}$ je **globalni minimum** ako je $f_0(x^*) \leq f_0(x)$ za **sve** $x \in \mathcal{F}$.

---

## 1.3 Teorija konveksnih skupova i konveksnih funkcija

U općoj nelinearnoj optimizaciji pronalaženje globalnog optimuma je NP-težak problem jer algoritmi lako zapinju u lokalnim minimumima. Zato je u inženjerstvu najvažnija podjela na **konveksne** i **nekonveksne** probleme (prof. Jokić, Predavanje 2).

### Konveksni skupovi
> **Definicija 1.2 (Konveksan skup):**  
> Skup $C \subseteq \mathbb{R}^n$ je konveksan ako za bilo koje dvije točke $x_1, x_2 \in C$ dužina koja ih spaja u potpunosti leži unutar skupa $C$:
> $$\alpha x_1 + (1 - \alpha) x_2 \in C, \quad \forall \alpha \in [0, 1].$$

Fizikalno i geometrijsko značenje:
- **Hiperravnina** $H = \{x \in \mathbb{R}^n \mid a^{\mathsf{T}} x = b\}$ ($a \neq 0$) je konveksan skup.
- **Zatvoreni poluprostor** $H_- = \{x \in \mathbb{R}^n \mid a^{\mathsf{T}} x \leq b\}$ je konveksan skup.
- **Poliedar:** Presjek konačno mnogo poluprostora $\mathcal{P} = \{x \in \mathbb{R}^n \mid Gx \leq h\}$ je konveksan skup jer **presjek proizvoljne familije konveksnih skupova ostaje konveksan skup**.

### Konveksne funkcije
> **Definicija 1.3 (Konveksna funkcija):**  
> Funkcija $f: C \to \mathbb{R}$ definirana na konveksnom skupu $C \subseteq \mathbb{R}^n$ je konveksna ako za sve $x, y \in C$ i sve $\alpha \in [0, 1]$ vrijedi:
> $$f(\alpha x + (1 - \alpha) y) \leq \alpha f(x) + (1 - \alpha) f(y).$$
> Funkcija je **strogo konveksna** ako za sve $x \neq y$ i $\alpha \in (0, 1)$ vrijedi stroga nejednakost ($<$).

Geometrijski, to znači da sekanta koja spaja točke $(x, f(x))$ i $(y, f(y))$ leži iznad grafa funkcije. Ekvivalentno, epigraf funkcije $\mathrm{epi}(f) := \{(x, t) \in \mathbb{R}^{n+1} \mid f(x) \leq t\}$ je konveksan skup u $\mathbb{R}^{n+1}$.

### Kriteriji konveksnosti preko derivacija
Ako je funkcija dvaput neprekidno diferencijabilna ($f \in C^2$):
1. **Uvjet prvog reda (gradijentni uvjet):**
   $$f(y) \geq f(x) + \nabla f(x)^{\mathsf{T}} (y - x), \quad \forall x, y \in C.$$
   Graf funkcije leži iznad svoje tangencijalne hiperravnine u svakoj točki.
2. **Uvjet drugog reda (Hesseova matrica):**
   Hesseova matrica drugih parcijalnih derivacija definira se kao $[\nabla^2 f(x)]_{ij} := \frac{\partial^2 f(x)}{\partial x_i \partial x_j}$.
   - Funkcija $f$ je konveksna na konveksnom otvorenom skupu ako i samo ako je njezina Hesseova matrica pozitivno semidefinitna u svakoj točki:
     $$\nabla^2 f(x) \succeq 0, \quad \forall x \in C.$$
   - Ako vrijedi $\nabla^2 f(x) \succ 0$ za sve $x \in C$, funkcija $f$ je **strogo konveksna**.

> **Teorem 1.1 (Temeljni teorem konveksne optimizacije):**  
> Ako je optimizacijski problem konveksan (funkcija cilja $f_0$ je konveksna, dopustivi skup $\mathcal{F}$ je konveksan), tada:
> 1. Svaki lokalni minimum je ujedno i **globalni minimum**.
> 2. Skup točaka globalnog minimuma je konveksan skup.
> 3. Ako je funkcija cilja $f_0$ **strogo konveksna**, globalni minimum je **jedinstven**.

---

## 1.4 Zadatak 1a seminara: Egzaktna formulacija Kvadratnog Programa (QP)

U Zadatku 1 seminara Krešimira Hartla zadan je optimizacijski problem u dvodimenzionalnom prostoru ($n = 2$, varijable $x = [x_1, x_2]^{\mathsf{T}} \in \mathbb{R}^2$):

$$\min_{x \in \mathbb{R}^2} \quad f(x) = x_1^2 + 2x_2^2 - 0.3 x_1 x_2 + 2x_1 - 3x_2 \tag{1.2}$$

uz ograničenja nejednakosti:
$$\begin{aligned}
g_1(x) &= a_{11} x_1 + a_{12} x_2 \leq -10, \\
g_2(x) &= a_{21} x_1 + a_{22} x_2 \leq 3,
\end{aligned} \tag{1.3}$$
s numeričkim vrijednostima parametara:
$$a_{11} = -1, \quad a_{12} = -1, \quad a_{21} = 1, \quad a_{22} = -1.$$

### Svođenje na standardni kanonski matrični oblik
U teoriji optimizacije i MATLAB-u (`quadprog`, YALMIP) standardni zapis kvadratnog programa glasi:
$$\min_{x} \quad \frac{1}{2} x^{\mathsf{T}} Q x + c^{\mathsf{T}} x \quad \text{uz} \quad Gx - h \leq 0. \tag{1.4}$$

Pažljivo identificirajmo članove funkcije cilja $f(x)$:
1. **Kvadratni članovi:**
   - Uz $x_1^2$ stoji koeficijent $1$, što u formi $\frac{1}{2} Q_{11} x_1^2$ daje $Q_{11} = 2$.
   - Uz $x_2^2$ stoji koeficijent $2$, što u formi $\frac{1}{2} Q_{22} x_2^2$ daje $Q_{22} = 4$.
   - Mješoviti član je $-0.3 x_1 x_2$. U kvadratnoj formi simetrične matrice on se dijeli simetrično: $\frac{1}{2}(Q_{12} + Q_{21}) = -0.3 \implies Q_{12} = Q_{21} = -0.3$.
   Dakle, Hesseova matrica je:
   $$Q = \begin{bmatrix} 2 & -0.3 \\ -0.3 & 4 \end{bmatrix} \in \mathbb{S}^2.$$
2. **Linearni članovi:**
   - Uz $x_1$ stoji koeficijent $+2$, a uz $x_2$ koeficijent $-3$:
   $$c = \begin{bmatrix} 2 \\ -3 \end{bmatrix} \in \mathbb{R}^2.$$
3. **Ograničenja u formatu $Gx - h \leq 0$ (notacija prof. Jokića na Vježbama 3):**
   - Prvo ograničenje: $-x_1 - x_2 \leq -10 \iff -x_1 - x_2 + 10 \leq 0 \implies g_1(x) = -x_1 - x_2 + 10$.
   - Drugo ograničenje: $x_1 - x_2 \leq 3 \iff x_1 - x_2 - 3 \leq 0 \implies g_2(x) = x_1 - x_2 - 3$.
   Zapisano u matričnom obliku:
   $$G = \begin{bmatrix} -1 & -1 \\ 1 & -1 \end{bmatrix}, \qquad h = \begin{bmatrix} -10 \\ 3 \end{bmatrix}.$$

---

## 1.5 Dokaz stroge konveksnosti, egzistencije i jedinstvenosti optimuma

Da bismo odgovorili na podzadatak (a) s maksimalnom ocjenom na usmenom ispitu, provodimo egzaktni matematički dokaz u tri koraka:

### Korak 1: Ispitivanje definitnosti Hesseove matrice $Q$
Hesseova matrica funkcije cilja je konstantna i jednaka matrici $Q$:
$$\nabla^2 f(x) = Q = \begin{bmatrix} 2 & -0.3 \\ -0.3 & 4 \end{bmatrix}.$$
Karakteristična jednadžba glasi:
$$\det(\lambda I - Q) = \det \begin{bmatrix} \lambda - 2 & 0.3 \\ 0.3 & \lambda - 4 \end{bmatrix} = (\lambda - 2)(\lambda - 4) - (-0.3)^2 = 0,$$
$$\lambda^2 - 6\lambda + 8 - 0.09 = \lambda^2 - 6\lambda + 7.91 = 0.$$
Korijeni karakterističnog polinoma su:
$$\lambda_{1,2} = \frac{6 \pm \sqrt{36 - 4 \cdot 1 \cdot 7.91}}{2} = \frac{6 \pm \sqrt{36 - 31.64}}{2} = \frac{6 \pm \sqrt{4.36}}{2}.$$
Budući da je $\sqrt{4.36} \approx 2.088061$, dobivamo egzaktne svojstvene vrijednosti:
$$\lambda_1 = \frac{6 - 2.088061}{2} = 1.955969 > 0,$$
$$\lambda_2 = \frac{6 + 2.088061}{2} = 4.044031 > 0.$$
Budući da su obje svojstvene vrijednosti strogo pozitivne ($\lambda_1 > 0, \lambda_2 > 0$), matrica $Q$ je **strogo pozitivno definitna** ($Q \succ 0$).

> **Zaključak o funkciji cilja:** Funkcija cilja $f(x)$ je **strogo konveksna** na cijelom prostoru $\mathbb{R}^2$.

### Korak 2: Ispitivanje konveksnosti dopustivog skupa $\mathcal{F}$
Funkcije ograničenja su afine:
$$g_1(x) = -x_1 - x_2 + 10, \qquad g_2(x) = x_1 - x_2 - 3.$$
Budući da je svaka afina funkcija ujedno i konveksna (vrijedi $\nabla^2 g_i(x) = 0 \succeq 0$), nivo-podskupovi $\{x \mid g_i(x) \leq 0\}$ predstavljaju zatvorene poluprostore u $\mathbb{R}^2$.
Dopustivi skup je njihov presjek:
$$\mathcal{F} = \{x \in \mathbb{R}^2 \mid g_1(x) \leq 0\} \cap \{x \in \mathbb{R}^2 \mid g_2(x) \leq 0\}.$$
Presjek dvaju zatvorenih konveksnih skupova je **zatvoren i konveksan skup**.

### Korak 3: Egzistencija i jedinstvenost minimuma (Weierstrassov teorem i koercivnost)
Kako dopustivi skup $\mathcal{F}$ nije omeđen (proteže se u beskonačnost u smjeru pozitivnih osi $x_1, x_2$), standardni Weierstrassov teorem na kompaktnom skupu ne može se primijeniti izravno. Međutim:
1. Budući da je $Q \succ 0$, minimalna svojstvena vrijednost je $\lambda_{\min} = 1.9560 > 0$.
2. Vrijedi Rayleigh-Ritzova nejednakost za kvadratnu formu: $x^{\mathsf{T}} Q x \geq \lambda_{\min} \|x\|_2^2$.
3. Prema Cauchy-Schwarzovoj nejednakosti je $|c^{\mathsf{T}} x| \leq \|c\|_2 \|x\|_2$.
4. Stoga je funkcija odozdo ograničena paraboloidom:
   $$f(x) \geq \frac{1}{2} \lambda_{\min} \|x\|_2^2 - \|c\|_2 \|x\|_2.$$
   Kada $\|x\|_2 \to \infty$, desna strana teži u $+\infty$. Funkcija $f$ je dakle **koercivna** (*radially unbounded*).
5. Za bilo koju točku $x_0 \in \mathcal{F}$, podnivo-skup $S = \{x \in \mathcal{F} \mid f(x) \leq f(x_0)\}$ je zatvoren i omeđen, dakle **kompaktan**.
6. Prema Weierstrassovom teoremu, neprekidna funkcija na nepraznom kompaktnom skupu nužno poprima svoj minimum.
7. Zbog **stroge konveksnosti** funkcije cilja, ta točka minimuma $x^*$ je **jedinstvena**.

---

## 1.6 Slaterov uvjet kvalifikacije ograničenja

Na usmenom ispitu prof. Jokić redovito postavlja pitanje: *"Kako znate da KKT uvjeti nisu samo nužni, nego i dovoljni za globalni optimum, te da ne postoji relaksacijski procjep (duality gap)?"*

Odgovor leži u **Slaterovom uvjetu kvalifikacije ograničenja** (*Slater's constraint qualification*):

> **Teorem 1.2 (Slaterov teorem):**  
> Za konveksan optimizacijski problem oblika (1.1), ako postoji točka $x \in \mathrm{relint}(\mathcal{F})$ koja strogo zadovoljava sva nelinearna ograničenja nejednakosti, tada:
> 1. Vrijedi **jaka dualnost** ($d^* = p^*$, dualni procjep je nula).
> 2. Ako je $p^*$ konačan, dualni optimum $\mu^*$ je dosegnut (postoji optimalni vektor Lagrangeovih množitelja).
> 3. KKT uvjeti postaju **nužni i dovoljni** uvjeti optimalnosti.
> 
> *Specijalni slučaj (Afina ograničenja):* Ako su sva ograničenja nejednakosti afina ($Gx \leq h$), Slaterov uvjet se reducira na običnu dopustivost: dovoljno je da postoji točka $x$ u kojoj su sva ograničenja strogo zadovoljena ($Gx < h$).

### Provjera Slaterovog uvjeta za Zadatak 1
Odaberimo točku unutar dopustivog skupa, npr. $x_{\mathrm{test}} = \begin{bmatrix} 7 \\ 6 \end{bmatrix}$:
$$\begin{aligned}
g_1(x_{\mathrm{test}}) &= -7 - 6 + 10 = -3 < 0, \\
g_2(x_{\mathrm{test}}) &= 7 - 6 - 3 = -2 < 0.
\end{aligned}$$
Budući da točka $x_{\mathrm{test}} = [7, 6]^{\mathsf{T}}$ strogo zadovoljava oba ograničenja ($g_1 < 0$ i $g_2 < 0$), ona leži u unutrašnjosti skupa $\mathcal{F}$. **Slaterov uvjet je zadovoljen**.

---

## 1.7 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori

### ❓ Tipična ispitna pitanja profesora na obrani

#### Pitanje 1.1: Zašto je u inženjerskoj praksi konveksnost znatno važnija od linearnosti?
*Kontekst:* Pitanje provjerava razumijevanje računalne složenosti i naravi optimizacije.
> **Modelski odgovor studenta:**  
> "Linearnost je tek uski podskup konveksnosti. U prošlosti se smatralo da je granica između lakih i teških problema bila linearnost naspram nelinearnosti. Međutim, moderni proboj u optimizaciji (Boyd, Nesterov, Nemirovski) pokazao je da je stvarna vododijelnica **konveksnost**.  
> Kod konveksnih problema svaki lokalni minimum je nužno globalni, nema zapinjanja u lokalnim 'zamkama', a metode unutrašnje točke (*interior-point*) rješavaju ih u polinomijalnom vremenu sa zajamčenom konvergencijom. Nekonveksni problemi, čak i s malo varijabli, u općem su slučaju NP-teški."

#### Pitanje 1.2: Što bi se geometrijski i fizikalno dogodilo da je determinanta matrice $Q$ bila jednaka nuli ($\det Q = 0$)?
*Kontekst:* Pitanje testira razumijevanje pozitivne semidefinitnosti i jedinstvenosti optimuma.
> **Modelski odgovor studenta:**  
> "Ako je $\det Q = 0$, a matrica je pozitivno semidefinitna ($Q \succeq 0$), to znači da je najmanja svojstvena vrijednost jednaka nuli ($\lambda_{\min} = 0$).  
> Geometrijski, nivo-krivulje funkcije cilja više nisu elipse, već postaju **eliptički cilindri** (parabolički žlijeb) ispruženi duž svojstvenog vektora koji pripada nultoj svojstvenoj vrijednosti.  
> Fizikalno, to znači da u smjeru tog svojstvenog vektora nema 'zakrivljenosti' funkcije (energija se ne mijenja). Ako dopustivi skup dopušta gibanje duž tog žlijeba u smjeru pada linearnog člana, problem može postati neograničen odozdo ($p^* = -\infty$). Ako je ograničen, rješenje više ne mora biti jedinstveno, već optimum čini čitava dužina ili pravac točaka."

#### Pitanje 1.3: Zašto matrica $Q$ u definiciji kvadratne forme mora biti simetrična? Što ako zadana matrica nije simetrična?
*Kontekst:* Matematička preciznost u formulaciji QP-a.
> **Modelski odgovor studenta:**  
> "Za bilo koju kvadratnu matricu $M$ vrijedi da je kvadratna forma $x^{\mathsf{T}} M x$ identički jednaka kvadratnoj formi njezina simetričnog dijela:
> $$x^{\mathsf{T}} M x = x^{\mathsf{T}} \left( \frac{M + M^{\mathsf{T}}}{2} \right) x,$$
> jer je antisimetrični dio $x^{\mathsf{T}} (M - M^{\mathsf{T}}) x \equiv 0$ za svaki vektor $x$.  
> Međutim, ako bismo uzeli nesimetričnu matricu $M$, njezine svojstvene vrijednosti mogle bi biti kompleksne ili pogrešno indicirati definitnost. Hesseova matrica funkcije iz klase $C^2$ po Schwarzovom teoremu o mješovitim derivacijama **uvijek je simetrična**. Zato se kvadratni program uvijek standardizira sa simetričnom matricom $Q = \frac{1}{2}(M + M^{\mathsf{T}})$."

---

### ⚠️ Fatalne zablude i zamke u izvođenju

1. **Zamka nesimetrične matrice:** Student zapiše kvadratni oblik $x_1^2 + 2x_2^2 - 0.3 x_1 x_2$ i u matricu stavi $-0.3$ na poziciju $(1,2)$, a $0$ na poziciju $(2,1)$.  
   *Posljedica:* Računanje svojstvenih vrijednosti takve matrice daje pogrešne rezultate koji ne odgovaraju pravoj Hesseovoj matrici.
2. **Brkanje strogog i nestrogog minimuma:** Tvrdnja da $Q \succeq 0$ jamči jedinstveni minimum.  
   *Ispravak:* $Q \succeq 0$ jamči da je svaki lokalni minimum globalni, ali jedinstvenost jamči **isključivo stroga konveksnost** ($Q \succ 0$) ili geometrija ograničenja koja siječe prostor u jednoj točki.
3. **Zanemarivanje omeđenosti:** Pretpostavka da Weierstrassov teorem automatski vrijedi na $\mathcal{F}$. Dopustivi skup $\mathcal{F}$ u Zadatku 1 je **neomeđen**. Postojanje minimuma mora se argumentirati **koercivnošću** funkcije cilja ($f(x) \to \infty$ kada $\|x\| \to \infty$).
