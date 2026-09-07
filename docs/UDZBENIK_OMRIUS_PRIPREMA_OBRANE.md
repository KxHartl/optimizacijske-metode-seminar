# OPTIMIZACIJSKE METODE U RAZVOJU I UPRAVLJANJU SUSTAVA
## Sveučilišni udžbenik, teorijski vodič i priručnik za pripremu usmene obrane i ispita
### Kroz prizmu rješavanja i dubinske analize projektnih zadataka seminara v1.2

> **Institucija:** Sveučilište u Zagrebu, Fakultet strojarstva i brodogradnje (FSB)  
> **Katedra:** Katedra za strojarsku automatiku, Zavod za robotiku i automatizaciju proizvodnih sustava  
> **Kolegij:** Optimizacijske metode u razvoju i upravljanju sustava (OMRiUS)  
> **Predmetni nastavnik:** Prof. dr. sc. Andrej Jokić  
> **Student:** Krešimir Hartl  
> **Baza rada:** Seminarski rad v1.2, službena predavanja (1–8), auditorne vježbe (1–5), MATLAB R2025b / YALMIP / SDPT3  

---

## 1. O ovom udžbeniku

Ovaj dokument zamišljen je i napisan kao **samostalan, matematički rigorozan i pedagoški cjelovit sveučilišni udžbenik** namijenjen studentima diplomskog i poslijediplomskog studija strojarstva, mehatronike i robotike. Nastao je s dvostrukim ciljem:
1. **Potpuno teorijsko svladavanje gradiva kolegija (100% pokrivenost usmenog ispita):** Svaki koncept izvodi se od nultih pretpostavki (*First Principles*), što znači da se čitatelju ne nameću gotovi rezultati bez jasne geometrijske, algebarske i fizikalne podloge. Svaki matematički simbol, indeks, koordinatni sustav i inženjerska pretpostavka eksplicitno se definiraju pri prvom spominjanju.
2. **Beskompromisna priprema za usmenu obranu seminara v1.2:** Zadaci seminara pokrivaju oko 80% gradiva usmenog ispita. Ovaj udžbenik koristi ta 4 projektna zadatka kao okosnicu kroz koju se secira cjelokupna teorija:
   - **Zadatak 1:** Kvadratni program (QP), konveksnost, Karush-Kuhn-Tucker (KKT) uvjeti, Lagrangeova dualnost i analiza osjetljivosti (teorija perturbacija i cijene u sjeni).
   - **Zadatak 2:** Robusna optimizacija pod poliedarskom nesigurnošću parametara, egzaktna ekvivalencija konveksne ljuske vrhova, Monte Carlo simulacija i inženjerska "cijena robusnosti" (*Price of Robustness*).
   - **Zadatak 3:** Kontinuirano modeliranje nivelacije terena (cestogradnja), diskretizacija konačnim razlikama, $\ell_1$-aproksimacija, svođenje nelinearnih normi na Linearni Program (LP), degeneracija rješenja i utjecaj numeričke kvadrature ($N=20$ vs. $N=100$).
   - **Zadatak 4:** Dinamički sklopni sustavi (*switching systems*), Hurwitzovost modova, paradoks divergencije otvorenog kruga (monodromijska matrica ciklusa), Ljapunovljeva teorija, zajednička kvadratna Ljapunovljeva funkcija (CQLF), transformacija kongruencije, eliminacija bilinearnosti (BMI $\to$ LMI), semidefinitno programiranje (SDP/YALMIP) i poopćeni problem svojstvenih vrijednosti (GEVP) za stopu prigušenja $\alpha$.
   - **Širi ispitni kontekst (Preostalih 20%):** Schurov komplement, konično programiranje drugog reda (SOCP), elipsoidne nesigurnosti i regularizacija ($\ell_1$ vs. $\ell_2$, LASSO).

---

## 2. Struktura i kazalo udžbenika

Udžbenik je podijeljen u **5 tematskih cjelina** i **10 specijaliziranih poglavlja**:

### DIO I: TEMELJI KONVEKSNE OPTIMIZACIJE I ANALIZA STATIČKIH PROBLEMA
- [Poglavlje 1: Matematički aparat, klasifikacija i konveksnost](01_temelji_i_konveksnost.md)
  - First Principles matematički rječnik ($\mathbb{R}^n, \mathbb{S}^n, \succeq, \succ$).
  - Definicije optimizacijskih problema, lokalni i globalni optimum.
  - Konveksni skupovi, konveksne funkcije, Hesseova matrica i Slaterov uvjet kvalifikacije ograničenja.
  - Zadatak 1a seminara: analitički izvod i dokaz stroge konveksnosti.
  - *Ispitni modul: pitanja, zamke i modelski odgovori.*
- [Poglavlje 2: Karush-Kuhn-Tucker (KKT) uvjeti optimalnosti i geometrija problema](02_uvjeti_optimalnosti_i_kkt.md)
  - Geometrija dozvoljenih smjerova i stožac normala.
  - Četiri stupa KKT sustava (stacionarnost, primarna/dualna dopustivost, komplementarnost).
  - Zadatak 1b seminara: rješavanje svih $2^2 = 4$ kombinacija aktivnosti ograničenja.
  - Fatalna ispitna zamka: Zašto se točka na sjecištu oba ograničenja odbacuje ($\mu_2 < 0$)?
  - Geometrijski prikaz i kolinearnost gradijenata ($\nabla f(x^*) = -\mu_1^* \nabla g_1$).
  - *Ispitni modul: pitanja, zamke i modelski odgovori.*
- [Poglavlje 3: Lagrangeova dualnost i analiza osjetljivosti (Shadow Prices)](03_dualnost_i_osjetljivost.md)
  - Lagrangeova dualna funkcija $\theta(\mu)$, teorem slabe i jake dualnosti.
  - Zadatak 1e seminara: analitički izvod dualnog problema za QP i solversko rješavanje u MATLAB-u (`quadprog`).
  - Teorija perturbacija i izvod $\nabla_v p^*(0) = -\mu^*$.
  - Zadatak 1f seminara: inženjersko značenje "cijena u sjeni" i granica rezerve (slack).
  - *Ispitni modul: pitanja, zamke i modelski odgovori.*

### DIO II: OPTIMIZACIJA U UVJETIMA NESIGURNOSTI
- [Poglavlje 4: Robusno programiranje pod poliedarskom nesigurnošću](04_robusna_optimizacija.md)
  - Filozofija worst-case optimizacije naspram stohastičkog pristupa.
  - Zadatak 2 seminara: intervalna nesigurnost od $\pm 15\%$ na koeficijentima $a_{ij}$.
  - Egzaktna ekvivalencija konveksne ljuske vrhova (dokaz zašto nema konzervatizma).
  - Deterministički robusni QP s 8 nejednakosti i rješavanje robusnog optimuma $x_{\mathrm{rob}}^* = (6.5, 179/34)$.
  - Monte Carlo verifikacija (54/100 kršenja nominalnog vs. 0/100 robusnog rješenja).
  - Inženjerska i ekonomska interpretacija "cijene robusnosti" (+39.63% porasta troška).
  - *Ispitni modul: pitanja, zamke i modelski odgovori.*

### DIO III: LINEARNO PROGRAMIRANJE I OPTIMIZACIJSKA APROKSIMACIJA
- [Poglavlje 5: Modeliranje kontinuiranih sustava i numerička diskretizacija](05_modeliranje_ceste_i_diskretizacija.md)
  - Kontinuirani problem nivelacije trase: kriterij zemljanih radova i fizikalna ograničenja.
  - Inženjersko značenje nagiba $y'$ (vučna sila) i promjene nagiba $y''$ (dinamička udobnost vožnje $a_z \approx v^2 y''$).
  - Diskretizacija konačnim razlikama i konstrukcija matrica $D_1$ i $D_2$.
  - *Ispitni modul: pitanja, zamke i modelski odgovori.*
- [Poglavlje 6: Egzaktna transformacija u Linearni Program (LP) i analiza degeneracije](06_lp_i_l1_aproksimacija.md)
  - Teorija normi ($\ell_1, \ell_2, \ell_\infty$) i robusna aproksimacija.
  - Tehnika eliminacije apsolutne vrijednosti pomoću pomoćnih varijabli $t_i$.
  - Standardni LP oblik za `linprog` i komparativna analiza 4 scenarija (Slučaj A i B za $N=20$ i $N=100$).
  - Zašto kriterij $J^*$ RASTE pri zgušnjavanju mreže (pravokutna kvadratura i podcjenjivanje integrala).
  - Fenomen degeneracije LP-a: Zašto su uklonjeni zasebni stupci za "iskop" i "nasip".
  - *Ispitni modul: pitanja, zamke i modelski odgovori.*

### DIO IV: DINAMIČKI SUSTAVI, TEORIJA STABILNOSTI I LMI KONTROLA
- [Poglavlje 7: Stabilnost dinamičkih sustava i paradoks sklopnih sustava](07_stabilnost_i_sklopni_sustavi.md)
  - LTI sustavi, Hurwitzov kriterij i Ljapunovljeva matrična jednadžba $A^T P + PA \prec 0$.
  - Zadatak 4a seminara: Hurwitzovost pojedinačnih modova ($\lambda_{1,2} = -1 \pm j \pi/2$).
  - Zadatak 4b seminara: Paradoks divergencije otvorenog kruga pri periodičkom prespajanju.
  - Egzaktno izvođenje monodromijske matrice ciklusa $\Phi_{\mathrm{cikl}} = e^{-2} \mathrm{diag}(-9, -1/9)$.
  - Spektralni radijus $\rho(\Phi_{\mathrm{cikl}}) = 9e^{-2} \approx 1.218 > 1$ i fizikalna interpretacija "pumpanja energije".
  - *Ispitni modul: pitanja, zamke i modelski odgovori.*
- [Poglavlje 8: Linearne matrične nejednakosti (LMI) i sinteza robusnog upravljanja](08_lmi_robusna_stabilizacija.md)
  - Semidefinitno programiranje (SDP) i zajednička kvadratna Ljapunovljeva funkcija (CQLF).
  - Problem bilinearnosti (BMI) $PBK$ i transformacija kongruencije s $P^{-1}$.
  - Supstitucija $\mathcal{Q} = P^{-1}, Y = KP^{-1}$ i izvod afine LMI formulacije.
  - Solverska implementacija u YALMIP-u uz normalizaciju i minimizaciju norme pojačanja $\min \|Y\|_2$.
  - Optimalni regulator $K = [-3.424629, -0.104650]$ i matrica $P$.
  - Poopćeni problem svojstvenih vrijednosti (GEVP) i izvod stope eksponencijalnog prigušenja $\alpha = 0.2884\,\mathrm{s}^{-1}$.
  - *Ispitni modul: pitanja, zamke i modelski odgovori.*

### DIO V: INTEGRALNI ISPITNI VODIČ I ŠIRI KONTEKST KOLEGIJA
- [Poglavlje 9: Schurov komplement, konična hijerarhija i napredno modeliranje](09_konicno_programiranje_i_schur.md)
  - Schurov komplement za blok-matrice i primjena u eliminaciji nelinearnosti.
  - Konična hijerarhija: $\mathrm{LP} \subset \mathrm{QP} \subset \mathrm{QCQP} \subset \mathrm{SOCP} \subset \mathrm{SDP}$.
  - SOCP programiranje i elipsoidne nesigurnosti parametara.
  - Regularizacija u optimizaciji: $\ell_2$ (Tikhonov) vs. $\ell_1$ (LASSO / rijetka rješenja).
  - *Ispitna pitanja za 100% pokrivenost usmenog ispita.*
- [Poglavlje 10: Vodič za usmenu obranu — "Face-to-Face s ispitivačem"](10_vodic_za_usmenu_obranu.md)
  - Matrica brzih odgovora: 25 zlatnih ispitnih pitanja s odgovorima u 3 inženjerske rečenice.
  - Top 15 studentskih fatalnih zabluda i zamki na usmenom ispitu.
  - Protokol obrane seminara v1.2: Vodič za prezentaciju i interpretaciju svih 7 ključnih slika rada.

---

## 3. Metodološki savjeti za pripremu obrane i usmenog ispita

Kako bi priprema bila maksimalno efikasna, preporučuje se sljedeći radni postupak:
1. **Svladavanje teorije (First Principles):** Pročitajte teorijski dio svakog poglavlja i samostalno na papiru ponovite matematičke izvode bez gledanja u tekst.
2. **Provjera numeričkih rezultata:** Povežite svaki analitički izraz s brojkama koje daje MATLAB ispis (sve brojke u udžbeniku su u decimalu usklađene s datotekama u `docs/code/task*_output.txt`).
3. **Trening ispitnih pitanja (Simulacija obrane):** Za svako pitanje u ispitnom modulu pokušajte naglas odgovoriti unutar 60 sekundi, prateći strukturu *modelskog odgovora*.
4. **Analiza grafova:** Za svaku sliku u seminaru budite spremni objasniti što prikazuje svaka os, svaka krivulja, gdje se nalazi optimum i zašto sustav reagira upravo na taj način.


---

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

Kako bismo optimizacijske metode proučavali na sveučilišnoj inženjerskoj razini, moramo krenuti od nultih pretpostavki (*First Principles*). To znači da svaki simbol, operaciju i geometrijski objekt definiramo precizno prije njegove primjene.

### Vektori i koordinatni sustav
Promatramo realni $n$-dimenzionalni euklidski prostor označen sa $\mathbb{R}^n$. Element tog prostora je vektor-stupac $x \in \mathbb{R}^n$:
$$x = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}, \qquad x_i \in \mathbb{R}, \quad i \in \{1, 2, \dots, n\}.$$
U kontekstu inženjerske optimizacije, komponente $x_i$ nazivamo **projektnim varijablama** (*decision variables* ili *design variables*). To su parametri sustava koje inženjer ima slobodu birati (npr. debljina stijenke, upravljački napon, visina nivelete ceste, raspodjela mase).

### Skalarni (unutrašnji) produkt i norma
Za dva vektora $x, y \in \mathbb{R}^n$, standardni euklidski skalarni produkt definiran je kao:
$$\langle x, y \rangle := x^{\mathsf{T}} y = \sum_{i=1}^n x_i y_i,$$
gdje je $(\cdot)^{\mathsf{T}}$ operacija transponiranja (pretvaranje stupca u redak). Skalarni produkt inducira **euklidsku normu** ($\ell_2$-normu) koja predstavlja fizikalnu duljinu vektora u prostoru:
$$\|x\|_2 := \sqrt{x^{\mathsf{T}} x} = \sqrt{\sum_{i=1}^n x_i^2}.$$
Uz euklidsku normu, u inženjerstvu i kolegiju OMRiUS ključne su još dvije p-norme:
1. **$\ell_1$-norma (Manhattan ili taksi norma):** $\|x\|_1 := \sum_{i=1}^n |x_i|$. U Zadacima 3 i 4 vidjet ćemo da $\ell_1$-norma mjeri volumen iskopa/nasipa ili služi za poticanje rijetkosti (*sparsity*).
2. **$\ell_\infty$-norma (Chebyshevjeva norma):** $\|x\|_\infty := \max_{1 \leq i \leq n} |x_i|$, koja mjeri maksimalno vršno odstupanje u sustavu.

### Simetrične matrice i parcijalni poredak definitnosti
Skup svih realnih simetričnih matrica dimenzija $n \times n$ označavamo sa $\mathbb{S}^n$:
$$\mathbb{S}^n := \{A \in \mathbb{R}^{n \times n} \mid A = A^{\mathsf{T}}\}.$$
Za simetričnu matricu $A \in \mathbb{S}^n$ promatramo **kvadratnu formu** $q(x) = x^{\mathsf{T}} A x$. 

> **Definicija 1.1 (Pozitivna semidefinitnost i definitnost):**
> Neka je $A \in \mathbb{S}^n$. Kažemo da je matrica $A$:
> 1. **Pozitivno semidefinitna**, u oznaci $A \succeq 0$, ako vrijedi:
>    $$x^{\mathsf{T}} A x \geq 0, \quad \forall x \in \mathbb{R}^n.$$
>    Ekvivalentno: sve svojstvene vrijednosti matrice $A$ su nenegativne ($\lambda_i(A) \geq 0, \, \forall i$).
> 2. **Pozitivno definitna**, u oznaci $A \succ 0$, ako vrijedi:
>    $$x^{\mathsf{T}} A x > 0, \quad \forall x \in \mathbb{R}^n \setminus \{0\}.$$
>    Ekvivalentno: sve svojstvene vrijednosti matrice $A$ su strogo pozitivne ($\lambda_i(A) > 0, \, \forall i$).

Relacija $A \succeq B$ (odnosno $A - B \succeq 0$) naziva se **Loewnerov parcijalni poredak**. To nije obična skalarna nejednakost, već **linearna matrična nejednakost (LMI)**, koja predstavlja temelj koničnog i semidefinitnog programiranja (Predavanje 6 i Zadatak 4).

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


---

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


---

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


---

# POGLAVLJE 4: Robusno programiranje pod poliedarskom nesigurnošću

> **Sadržaj poglavlja:**  
> 4.1 Filozofija robusnosti: Deterministička vs. Worst-Case optimizacija  
> 4.2 Skup nesigurnosti u Zadatku 2: Poliedarska geometrija i intervalne varijacije  
> 4.3 Egzaktna ekvivalencija konveksne ljuske: Dokaz nepostojanja konzervatizma  
> 4.4 Rješavanje determinističkog robusnog QP-a s 8 nejednakosti  
> 4.5 Monte Carlo verifikacija (54/100 kršenja) i "Cijena robusnosti" (+39.63%)  
> 4.6 Povezivanje sa Slikom 3.1 seminara (`fig2_1_robust_envelope_monte_carlo.pdf`)  
> 4.7 Širi ispitni kontekst: Dualni pristup robusnosti i elipsoidne nesigurnosti (SOCP)  
> 4.8 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori  

---

## 4.1 Filozofija robusnosti: Deterministička vs. Worst-Case optimizacija

U klasičnom inženjerskom projektiranju često se pretpostavlja da su svi parametri modela poznati s apsolutnom točnošću (nominalni model). Međutim, u stvarnom inženjerskom svijetu nominalni model je fikcija (prof. Jokić, Predavanje 8):
- Mehaničke tolerancije pri izradi dijelova uzrokuju geometrijska odstupanja.
- Fizikalna svojstva materijala (modul elastičnosti, koeficijenti trenja, toplinska vodljivost) variraju s temperaturom i starenjem.
- Mjerenja senzora opterećena su šumom i nesigurnošću.

### Katastrofa nominalnog optimuma
Ako optimizaciju provedemo na nominalnom modelu, rješenje $x_{\mathrm{nom}}^*$ u pravilu završava **točno na samoj granici dopustivog skupa** (jer funkcija cilja "gura" točku dokle god može, tj. aktivira ograničenja).  
Kada takav projekt pustimo u stvarni rad, **i najmanja nepovoljna varijacija parametara pomaknut će granicu ograničenja preko točke $x_{\mathrm{nom}}^*$**, čime sustav postaje nedopustiv, što u inženjerstvu znači lom konstrukcije, termički preopterećen aktuator ili nestabilnost!

### Stohastički vs. Robusni pristup
Kako se boriti protiv nesigurnosti? Postoje dva glavna pristupa:
1. **Stohastičko programiranje:** Pretpostavlja se da su parametri slučajne varijable s *poznatom razdiobom vjerojatnosti* (npr. Gaussova razdioba). Minimizira se očekivani trošak ili se dopušta malo kršenje s malom vjerojatnošću (tzv. *chance constraints*).  
   *Ograničenje:* U inženjerskoj praksi točnu razdiobu vjerojatnosti gotovo nikada ne poznajemo, a optimizacija za "prosječni slučaj" može biti kobna za kritične sustave.
2. **Robusno optimiranje (Worst-Case pristup):** Ne pretpostavlja se nikakva razdioba vjerojatnosti. Jedino što znamo jest da se stvarni parametri nalaze unutar zadanog, kompaktnog **skupa nesigurnosti** $\mathcal{U}$.  
   Traži se rješenje koje mora biti dopustivo za **svaku moguću realizaciju** parametara unutar $\mathcal{U}$, uzimajući u obzir *najgori mogući scenarij* (*worst-case*).

---

## 4.2 Skup nesigurnosti u Zadatku 2: Poliedarska geometrija i intervalne varijacije

U Zadatku 2 seminara promatramo isti optimizacijski problem kao u Zadatku 1, ali s nesigurnim koeficijentima matrice ograničenja:
$$\min_{x \in \mathbb{R}^2} \quad f(x) = x_1^2 + 2x_2^2 - 0.3 x_1 x_2 + 2x_1 - 3x_2 \tag{4.1}$$
uz ograničenja:
$$a_1^{\mathsf{T}} x \leq h_1, \qquad a_2^{\mathsf{T}} x \leq h_2, \tag{4.2}$$
gdje su nominalne vrijednosti vektora bile:
$$a_1^0 = \begin{bmatrix} a_{11}^0 \\ a_{12}^0 \end{bmatrix} = \begin{bmatrix} -1 \\ -1 \end{bmatrix}, \quad h_1 = -10; \qquad a_2^0 = \begin{bmatrix} a_{21}^0 \\ a_{22}^0 \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}, \quad h_2 = 3.$$

### Definicija intervala nesigurnosti ($\pm 15\%$)
Zadano je da se stvarna vrijednost svakog koeficijenta $a_{ij}$ nalazi u intervalu od $\pm 15\%$ oko nominalne vrijednosti:
$$a_{ij} \in [0.85 a_{ij}^0, \; 1.15 a_{ij}^0], \quad i \in \{1, 2\}, \; j \in \{1, 2\}. \tag{4.3}$$

Pažljivo izračunajmo intervale za svaki parametar:
- Za $a_{11}^0 = -1$: interval je $[-1.15, -0.85]$.
- Za $a_{12}^0 = -1$: interval je $[-1.15, -0.85]$.
- Za $a_{21}^0 = +1$: interval je $[+0.85, +1.15]$.
- Za $a_{22}^0 = -1$: interval je $[-1.15, -0.85]$.

Vektori redaka $a_1$ i $a_2$ stoga se nalaze u Kartezijevim produktima intervala, što geometrijski predstavlja **pravokutnike nesigurnosti** u prostoru parametara $\mathbb{R}^2$:
$$\mathcal{P}_1 = [-1.15, -0.85] \times [-1.15, -0.85] \subset \mathbb{R}^2, \tag{4.4a}$$
$$\mathcal{P}_2 = [0.85, 1.15] \times [-1.15, -0.85] \subset \mathbb{R}^2. \tag{4.4b}$$

### Formulacija robusnog pandana (Robust Counterpart)
Robusni problem zahtijeva da rješenje $x$ zadovoljava ograničenja za **sve** točke unutar pravokutnika nesigurnosti:
$$\begin{aligned}
\min_{x \in \mathbb{R}^2} \quad & \frac{1}{2} x^{\mathsf{T}} Q x + c^{\mathsf{T}} x \\
\text{uz} \quad & a_1^{\mathsf{T}} x \leq -10, \quad \forall a_1 \in \mathcal{P}_1, \\
& a_2^{\mathsf{T}} x \leq 3, \quad \forall a_2 \in \mathcal{P}_2.
\end{aligned} \tag{4.5}$$

Budući da skupovi $\mathcal{P}_1$ i $\mathcal{P}_2$ sadrže beskonačno mnogo točaka, relacije (4.5) predstavljaju problem s **beskonačno mnogo ograničenja** (tzv. *semi-infinite program*). Može se zapisati preko supremuma:
$$\sup_{a_1 \in \mathcal{P}_1} a_1^{\mathsf{T}} x \leq -10, \qquad \sup_{a_2 \in \mathcal{P}_2} a_2^{\mathsf{T}} x \leq 3. \tag{4.6}$$

---

## 4.3 Egzaktna ekvivalencija konveksne ljuske: Dokaz nepostojanja konzervatizma

Kako beskonačno mnogo ograničenja svesti na konačan broj jednadžbi s kojima računalo može raditi? Odgovor daje teorija konveksnih poliedara.

> **Teorem 4.1 (Ekvivalencija konveksne ljuske vrhova):**  
> Neka je $\mathcal{P} \subset \mathbb{R}^n$ konveksan politop definiran kao konveksna ljuska svojih $K$ vrhova:
> $$\mathcal{P} = \mathrm{co}\big(v^{(1)}, v^{(2)}, \dots, v^{(K)}\big) = \left\{ \sum_{k=1}^K \gamma_k v^{(k)} \;\middle|\; \gamma_k \geq 0, \; \sum_{k=1}^K \gamma_k = 1 \right\}.$$
> Tada je robusno ograničenje $\sup_{a \in \mathcal{P}} a^{\mathsf{T}} x \leq h$ **egzaktno ekvivalentno** sustavu od $K$ determinističkih linearnih nejednakosti:
> $$\sup_{a \in \mathcal{P}} a^{\mathsf{T}} x \leq h \iff (v^{(k)})^{\mathsf{T}} x \leq h, \quad \forall k \in \{1, \dots, K\}. \tag{4.7}$$

### Egzaktni matematički dokaz (u dva smjera):
Dokazujemo ekvivalenciju $\iff$, što jamči da nema nikakvog gubitka točnosti (nema relaksacijskog procjepa!):

1. **Smjer $(\implies)$ [Trivijalan]:**  
   Budući da je svaki vrh $v^{(k)}$ element skupa $\mathcal{P}$ (dobije se odabirom $\gamma_k = 1$ i $\gamma_j = 0$ za $j \neq k$), ako nejednakost vrijedi za sve elemente skupa $\mathcal{P}$, ona nužno mora vrijediti i za svaki vrh $v^{(k)}$.
2. **Smjer $(\impliedby)$ [Ključan]:**  
   Pretpostavimo da nejednakost vrijedi za svih $K$ vrhova:
   $$(v^{(k)})^{\mathsf{T}} x \leq h, \quad \forall k \in \{1, \dots, K\}.$$
   Uzmimo proizvoljnu točku $a \in \mathcal{P}$. Po definiciji konveksne ljuske, ona se može prikazati kao $a = \sum_{k=1}^K \gamma_k v^{(k)}$ uz $\gamma_k \geq 0$ i $\sum_{k=1}^K \gamma_k = 1$.  
   Izračunajmo skalarni produkt $a^{\mathsf{T}} x$:
   $$a^{\mathsf{T}} x = \left( \sum_{k=1}^K \gamma_k v^{(k)} \right)^{\mathsf{T}} x = \sum_{k=1}^K \gamma_k \big( (v^{(k)})^{\mathsf{T}} x \big).$$
   Kako je svaki $(v^{(k)})^{\mathsf{T}} x \leq h$, a svi $\gamma_k \geq 0$, možemo ocijeniti sumu odozgo:
   $$a^{\mathsf{T}} x \leq \sum_{k=1}^K \gamma_k h = h \left( \sum_{k=1}^K \gamma_k \right) = h \cdot 1 = h.$$
   Budući da ovo vrijedi za **svaku** točku $a \in \mathcal{P}$, uzimanjem supremuma slijedi:
   $$\sup_{a \in \mathcal{P}} a^{\mathsf{T}} x \leq h. \quad \blacksquare$$

> 💡 **Inženjerski zaključak:** Zato što je funkcija $a \mapsto a^{\mathsf{T}} x$ **linearna** po parametru $a$, njezin maksimum na konveksnom skupu uvijek se postiže u nekom od ekstremnih točaka (vrhova).  
> **Formulacija preko vrhova nije aproksimacija niti konzervativna ocjena, već egzaktan identitet!**

---

## 4.4 Rješavanje determinističkog robusnog QP-a s 8 nejednakosti

Svaki pravokutnik u ravnini ima $2^2 = 4$ vrha. Za dva ograničenja imamo ukupno $2 \times 4 = 8$ linearnih nejednakosti:

$$\begin{aligned}
\text{Vrhovi za } \mathcal{P}_1: \quad
&v_1^{(1)} = [-0.85, -0.85]^{\mathsf{T}}, \quad &&v_1^{(2)} = [-0.85, -1.15]^{\mathsf{T}}, \\
&v_1^{(3)} = [-1.15, -0.85]^{\mathsf{T}}, \quad &&v_1^{(4)} = [-1.15, -1.15]^{\mathsf{T}}. \\[6pt]
\text{Vrhovi za } \mathcal{P}_2: \quad
&v_2^{(1)} = [0.85, -0.85]^{\mathsf{T}}, \quad &&v_2^{(2)} = [0.85, -1.15]^{\mathsf{T}}, \\
&v_2^{(3)} = [1.15, -0.85]^{\mathsf{T}}, \quad &&v_2^{(4)} = [1.15, -1.15]^{\mathsf{T}}.
\end{aligned}$$

Sustav od 8 determinističkih ograničenja $G_{\mathrm{rob}} x \leq h_{\mathrm{rob}}$ glasi:
$$\begin{aligned}
1) \quad -0.85 x_1 - 0.85 x_2 &\leq -10 \\
2) \quad -0.85 x_1 - 1.15 x_2 &\leq -10 \\
3) \quad -1.15 x_1 - 0.85 x_2 &\leq -10 \\
4) \quad -1.15 x_1 - 1.15 x_2 &\leq -10 \\
5) \quad \phantom{-}0.85 x_1 - 0.85 x_2 &\leq 3 \\
6) \quad \phantom{-}0.85 x_1 - 1.15 x_2 &\leq 3 \\
7) \quad \phantom{-}1.15 x_1 - 0.85 x_2 &\leq 3 \\
8) \quad \phantom{-}1.15 x_1 - 1.15 x_2 &\leq 3
\end{aligned} \tag{4.8}$$

### Analitičko prepoznavanje "najgorih" ograničenja (Worst-Case)
Budući da varijable $x_1$ i $x_2$ u radnom području poprimaju pozitivne vrijednosti ($x_1 > 0, x_2 > 0$):
1. U prvom ograničenju tražimo najveću (najmanje negativnu) lijevu stranu. Za $x_1, x_2 > 0$, izraz $-a_{11} x_1 - a_{12} x_2$ je najmanje negativan kada su koeficijenti po apsolutnoj vrijednosti **najmanji** ($0.85$):
   $$-0.85 x_1 - 0.85 x_2 \leq -10 \iff x_1 + x_2 \geq \frac{10}{0.85} \approx 11.7647.$$
   To je vrh $k = 1$ (najstrože ograničenje koje gura točku najdalje od ishodišta).
2. U drugom ograničenju tražimo najveću lijevu stranu $a_{21} x_1 + a_{22} x_2 \leq 3$. Kako bismo maksimizirali izraz, $x_1$ mora biti pomnožen s najvećim koeficijentom ($+1.15$), a $x_2$ s najmanjim negativnim koeficijentom po apsolutnoj vrijednosti ($-0.85$, što manje oduzima):
   $$1.15 x_1 - 0.85 x_2 \leq 3.$$
   To je vrh $k = 7$.

### Dokaz aktivnosti oba najgora ograničenja u optimumu
Postavimo pitanje: *"Može li u robusnom optimumu biti aktivno samo prvo najgore ograničenje ($k=1$), a drugo neaktivno?"*  
Pretpostavimo da je aktivno samo ograničenje $k=1$. Analogno Zadatku 1, rješavanje stacionarnosti daje točku:
$$x_{\mathrm{test}} = [6.9073, 4.8574]^{\mathsf{T}}.$$
Uvrstimo ovu točku u najgore drugo ograničenje ($k=7$):
$$g_{2,\mathrm{wc}}(x_{\mathrm{test}}) = 1.15(6.9073) - 0.85(4.8574) - 3 = 7.9434 - 4.1288 - 3 = +0.8146 > 0!$$
Točka je **nedopustiva** jer krši drugo robusno ograničenje!  
Prema tome, u robusnom optimumu **moraju biti aktivna oba najgora ograničenja ($k=1$ i $k=7$)**!

### Egzaktni izračun robusne točke optimuma $x_{\mathrm{rob}}^*$
Sjecište aktivnih pravaca $k=1$ i $k=7$:
$$\begin{aligned}
-0.85 x_1 - 0.85 x_2 &= -10 \iff x_1 + x_2 = \frac{10}{0.85} = \frac{200}{17} \quad &(I) \\
1.15 x_1 - 0.85 x_2 &= 3 \quad &(II)
\end{aligned}$$
Zbrojimo jednadžbu $(II)$ s $0.85 \times (I)$, odnosno izrazimo $0.85 x_2 = 10 - 0.85 x_1$ i uvrstimo u $(II)$:
$$1.15 x_1 - (10 - 0.85 x_1) = 3 \implies 2.00 x_1 - 10 = 3 \implies 2.00 x_1 = 13 \implies x_1^* = 6.5 = \frac{13}{2}.$$
Sada izračunajmo $x_2^*$:
$$x_2^* = \frac{200}{17} - 6.5 = \frac{200}{17} - \frac{110.5}{17} = \frac{89.5}{17} = \frac{179}{34} \approx 5.264706.$$

Dakle, egzaktna robusna optimalna točka je:
$$x_{\mathrm{rob}}^* = \begin{bmatrix} 6.500000 \\ 5.264706 \end{bmatrix} = \begin{bmatrix} \frac{13}{2} \\[4pt] \frac{179}{34} \end{bmatrix}.$$

### Izračun robusnih Lagrangeovih množitelja:
Iz uvjeta stacionarnosti:
$$\nabla f(x_{\mathrm{rob}}^*) = \begin{bmatrix} 2(6.5) - 0.3(5.2647) + 2 \\ -0.3(6.5) + 4(5.2647) - 3 \end{bmatrix} = \begin{bmatrix} 13.420588 \\ 16.108824 \end{bmatrix}.$$
Kako su aktivni samo vrhovi $1$ i $7$:
$$\mu_1 \begin{bmatrix} -0.85 \\ -0.85 \end{bmatrix} + \mu_7 \begin{bmatrix} 1.15 \\ -0.85 \end{bmatrix} = -\begin{bmatrix} 13.420588 \\ 16.108824 \end{bmatrix}.$$
Rješavanjem ovog regularnog sustava $2 \times 2$ dobivamo:
$$\mu_1^* = 17.607439 > 0, \qquad \mu_7^* = 1.344118 > 0.$$
Oba množitelja su **strogo pozitivna**, što dokazuje dualnu dopustivost.

### Provjera rezerve (Slack) za preostalih 6 nejednakosti:
Uvrštavanjem točke $x_{\mathrm{rob}}^*$ u svih 8 nejednakosti (izravno iz `task2_output.txt`):
- $k=1$: $-0.85 x_1 - 0.85 x_2 = -10.0000 \implies \text{slack} = 0.0000$ (aktivno)
- $k=2$: $-0.85 x_1 - 1.15 x_2 = -11.5794 \implies \text{slack} = 1.5794$
- $k=3$: $-1.15 x_1 - 0.85 x_2 = -11.9500 \implies \text{slack} = 1.9500$
- $k=4$: $-1.15 x_1 - 1.15 x_2 = -13.5294 \implies \text{slack} = 3.5294$
- $k=5$: $\phantom{-}0.85 x_1 - 0.85 x_2 = \phantom{-}1.0500 \implies \text{slack} = 1.9500$
- $k=6$: $\phantom{-}0.85 x_1 - 1.15 x_2 = -0.5294 \implies \text{slack} = 3.5294$
- $k=7$: $\phantom{-}1.15 x_1 - 0.85 x_2 = \phantom{-}3.0000 \implies \text{slack} = 0.0000$ (aktivno)
- $k=8$: $\phantom{-}1.15 x_1 - 1.15 x_2 = \phantom{-}1.4206 \implies \text{slack} = 1.5794$

Svi uvjeti KKT teorema su rigorozno i potpuno zadovoljeni!

---

## 4.5 Monte Carlo verifikacija (54/100 kršenja) i "Cijena robusnosti" (+39.63%)

Kako bismo eksperimentalno potvrdili teorijski model, provedena je Monte Carlo simulacija sa $N_{\mathrm{MC}} = 100$ slučajnih realizacija koeficijenata matrice ograničenja uz uniformnu razdiobu unutar zadanih intervala pod MATLAB-ovim generatorom `rng(42)`.

### Rezultati Monte Carlo ispitivanja:
1. **Nominalno rješenje $x_{\mathrm{nom}}^* = [5.7576, 4.2424]^{\mathsf{T}}$:**
   - Prekršilo je ograničenja u **54 od 100 realizacija** (stopa otkaza od čak 54%)!
   - Čim stvarni koeficijenti $a_{11}$ ili $a_{12}$ postanu po apsolutnoj vrijednosti manji od nominalnih (npr. $-0.90$ umjesto $-1.00$), suma $-x_1 - x_2$ postaje veća od $-10$, što automatski izbacuje sustav iz dopustivog područja.
2. **Robusno rješenje $x_{\mathrm{rob}}^* = [6.5000, 5.2647]^{\mathsf{T}}$:**
   - Prekršilo je ograničenja u **točno 0 od 100 realizacija** (100% pouzdanost i imunost na nesigurnost).

### Kvantifikacija "Cijene robusnosti" (*Price of Robustness*):
Optimalna vrijednost funkcije cilja iznosi:
- Za nominalno rješenje: $f(x_{\mathrm{nom}}^*) = \frac{2000}{33} \approx 60.606061$.
- Za robusno rješenje: $f(x_{\mathrm{rob}}^*) = \frac{978253}{11560} \approx 84.623962$.

Apsolutni porast troška:
$$\Delta f = f(x_{\mathrm{rob}}^*) - f(x_{\mathrm{nom}}^*) = 84.623962 - 60.606061 = 24.017901.$$
Relativni porast troška:
$$\frac{\Delta f}{f(x_{\mathrm{nom}}^*)} \times 100\% = \frac{24.017901}{60.606061} \times 100\% = \mathbf{+39.63\%}.$$

> **Inženjerska interpretacija cijene robusnosti:**  
> Porast troška od $39.63\%$ predstavlja **premiju osiguranja** koju inženjer plaća kako bi sustav zajamčeno funkcionirao bez otkaza u 100% mogućih radnih uvjeta. Pomakom točke s $(5.76, 4.24)$ na $(6.50, 5.26)$ sustav se povukao dublje u dopustivo područje, stvarajući dovoljnu sigurnosnu marginu prema svim rubnim varijacijama parametara.

---

## 4.6 Povezivanje sa Slikom 3.1 seminara (`fig2_1_robust_envelope_monte_carlo.pdf`)

Na slici 3.1 seminara Krešimira Hartla prikazana je geometrija robusnog rješenja:
1. **Snop sivih pravaca:** Prikazuje 100 slučajnih realizacija granica ograničenja iz Monte Carlo eksperimenta. Pravci tvore gustu "anvelopu" ili pojas nesigurnosti.
2. **Položaj točke $x_{\mathrm{nom}}^*$:** Nominalna točka leži točno po sredini sivog pojasa prvog ograničenja. Zato polovina realizacija prolazi "ispod" nje (dopustivo), a polovina "iznad" nje (kršenje ograničenja).
3. **Položaj točke $x_{\mathrm{rob}}^*$:** Robusna točka leži točno na sjecištu **najudaljenijih rubnih pravaca** anvelope (vrhovi $k=1$ i $k=7$). Čitav sivi snop realizacija leži s jedne strane robusne točke, što vizualno demonstrira zašto je stopa kršenja točno 0%.

---

## 4.7 Širi ispitni kontekst: Dualni pristup robusnosti i elipsoidne nesigurnosti (SOCP)

Profesor Jokić na Predavanju 8 obrađuje i naprednije formulacije robusne optimizacije koje se često pojavljuju kao podpitanja:

### 1. Dualni pristup rješavanju robusnog ograničenja
Što ako skup nesigurnosti $\mathcal{U}$ nije zadan vrhovima, već kao poliedar u obliku nejednakosti $\mathcal{U} = \{a \mid D a \leq d\}$?  
Tada unutrašnji problem najgoreg slučaja $\max_{a \in \mathcal{U}} a^{\mathsf{T}} x$ rješavamo **Lagrangeovom dualnošću**:
- Primar unutrašnjeg problema je linearni program po varijabli $a$.
- Prema teoremu jake dualnosti za LP, njegov maksimum jednak je minimumu njegova dualnog problema:
  $$\max_{a: Da \leq d} a^{\mathsf{T}} x = \min_{p \geq 0: D^{\mathsf{T}} p = x} d^{\mathsf{T}} p.$$
- Zamjenom unutrašnjeg problema njegovim dualom, robusno ograničenje $\max a^{\mathsf{T}} x \leq h$ svodi se na:
  $$\exists p \geq 0 \quad \text{takav da je} \quad D^{\mathsf{T}} p = x \quad \text{i} \quad d^{\mathsf{T}} p \leq h.$$
  Time ponovno dobivamo deterministička linearna ograničenja bez eksplicitnog nabrajanja vrhova!

### 2. Elipsoidna nesigurnost i prijelaz na SOCP
Ako parametri variraju unutar elipsoida $\mathcal{U} = \{a^0 + P u \mid \|u\|_2 \leq 1\}$:
- Najgori slučaj linearne funkcije na euklidskoj kugli je:
  $$\sup_{\|u\|_2 \leq 1} (a^0 + Pu)^{\mathsf{T}} x = (a^0)^{\mathsf{T}} x + \sup_{\|u\|_2 \leq 1} u^{\mathsf{T}} (P^{\mathsf{T}} x) = (a^0)^{\mathsf{T}} x + \|P^{\mathsf{T}} x\|_2.$$
- Robusni pandan glasi:
  $$(a^0)^{\mathsf{T}} x + \|P^{\mathsf{T}} x\|_2 \leq h.$$
- Član $\|P^{\mathsf{T}} x\|_2$ predstavlja euklidsku normu afine funkcije. Ograničenje ovog oblika naziva se **ograničenje stošca drugog reda** (*Second-Order Cone constraint*), a optimizacijski problem pripada klasi **SOCP (Second-Order Cone Programming)**.

---

## 4.8 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori

### ❓ Tipična ispitna pitanja profesora na obrani

#### Pitanje 4.1: Zašto je formulacija robusnog problema s 8 nejednakosti egzaktna, a ne konzervativna aproksimacija?
*Kontekst:* Pitanje provjerava razumijevanje konveksne geometrije i prijelaza s beskonačnog na konačan skup nejednakosti.
> **Modelski odgovor studenta:**  
> "Zato što je skup nesigurnosti parametara konveksan poliedar (pravokutnik), dakle konveksna ljuska svoja četiri vrha, a funkcija u ograničenju je **linearna** u nesigurnom vektoru parametara $a_i$.  
> Linearna funkcija poprima svoj globalni supremum na konveksnom politopu točno u jednom od ekstremnih točaka (vrhova). Budući da se svaka točka poliedra može prikazati kao konveksna kombinacija vrhova $a = \sum \gamma_k v^{(k)}$, iz zadovoljenja nejednakosti u svim vrhovima $(v^{(k)})^{\mathsf{T}} x \leq h$ direktno slijedi zadovoljenje nejednakosti za čitav skup: $a^{\mathsf{T}} x = \sum \gamma_k (v^{(k)})^{\mathsf{T}} x \leq h \sum \gamma_k = h$.  
> Obrat je trivijalan jer su vrhovi elementi skupa. Vrijedi puna ekvivalencija $(\iff)$, pa nema relaksacijskog procjepa niti konzervatizma."

#### Pitanje 4.2: Kako analitički dokazujete da su u robusnom optimumu aktivna oba najgora ograničenja, a ne samo jedno?
*Kontekst:* Analitička provjera KKT strukture robusnog rješenja.
> **Modelski odgovor studenta:**  
> "Dokaz provodimo metodom eliminacije.  
> Ako pretpostavimo da je aktivno samo najgore prvo ograničenje (vrh $k=1$: $-0.85 x_1 - 0.85 x_2 = -10$), dobivamo točku $x = (6.9073, 4.8574)$. Uvrštavanjem te točke u najgore drugo ograničenje (vrh $k=7$) dobiva se $1.15(6.9073) - 0.85(4.8574) - 3 = +0.8146 > 0$, što znači da ta točka krši drugo ograničenje i nije dopustiva.  
> Prema tome, optimum mora ležati na sjecištu oba najgora ograničenja ($k=1$ i $k=7$), što daje točku $x_{\mathrm{rob}}^* = (6.5, 179/34)$. Pripadajući Lagrangeovi množitelji $\mu_1^* = 17.6074$ i $\mu_7^* = 1.3441$ strogo su pozitivni, a preostalih šest nejednakosti ima rezervu od najmanje $1.5794$, čime je dokaz potpun."

#### Pitanje 4.3: Što inženjerski predstavlja "cijena robusnosti" i kako biste taj porast od 39.63% opravdali voditelju projekta?
*Kontekst:* Inženjerska i ekonomska interpretacija optimizacije.
> **Modelski odgovor studenta:**  
> "Cijena robusnosti predstavlja mjerljivi gubitak nominalnih performansi (porast funkcije troška s $60.61$ na $84.62$) koji nastaje kao nužna posljedica pomicanja radne točke dublje u dopustivo područje radi stvaranja sigurnosne margine.  
> Voditelju projekta bih to opravdao rezultatima Monte Carlo analize: nominalno rješenje ima stopu otkaza od čak **54%** pri realnim fizikalnim tolerancijama od $\pm 15\%$. Porast troška od $39.63\%$ zapravo je **premija osiguranja** kojom se eliminira rizik od katastrofalnog kvara sustava, osigurava 100% pouzdanost i sprječavaju višestruko veći troškovi zastoja i popravaka u eksploataciji."

---

### ⚠️ Fatalne zablude i zamke u izvođenju

1. **Odabir najgoreg vrha na temelju predznaka bez varijabli:** Student zaključi da je najgori slučaj onaj s najvećim koeficijentima $a_{ij}$. To je točno samo ako je optimizacijska varijabla $x_j$ pozitivna! Da je $x_j < 0$, veći koeficijent $a_{ij}$ zapravo bi smanjivao lijevu stranu. Uvijek se mora promatrati predznak umnoška $a_{ij} x_j$!
2. **Tvrdnja da je robusni problem konzervativan:** Studenti često robusnu optimizaciju poistovjećuju s inženjerskim "faktorima sigurnosti" koji su često proizvoljni i konzervativni. Kao što smo dokazali u Teoremu 4.1, worst-case optimizacija nad poliedrom vrhova je **egzaktna**, a ne konzervativna.
3. **Miješanje broja realizacija s brojem ograničenja:** Prilikom postavljanja Monte Carlo simulacije studenti ponekad misle da se simulacijom rješava problem. Monte Carlo služi **isključivo za naknadnu statističku verifikaciju** ponašanja sustava, dok se samo robusno rješenje dobiva analitički ili determinističkim QP solverom.


---

# POGLAVLJE 5: Modeliranje kontinuiranih sustava i numerička diskretizacija

> **Sadržaj poglavlja:**  
> 5.1 Kontinuirani inženjerski problem: Nivelacija trase i zemljani radovi  
> 5.2 Fizikalna i kinematička ograničenja ceste: Nagib ($b_1$) i dinamička udobnost ($b_2$)  
> 5.3 Diskretizacija metodom konačnih razlika: Mreža čvorova i korak $\Delta x$  
> 5.4 Konstrukcija diferencijskih matrica $D_1$ i $D_2$ (Analiza dimenzija)  
> 5.5 Numerička kvadratura i aproksimacija funkcionala troška  
> 5.6 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori  

---

## 5.1 Kontinuirani inženjerski problem: Nivelacija trase i zemljani radovi

U Zadatku 3 seminara suočavamo se s klasičnim problemom građevinskog i prometnog inženjerstva: **optimalnom nivelacijom uzdužnog profila ceste** na neravnom prirodnom terenu (prof. Jokić, Predavanje 5 i Vježbe 4).

### Fizikalna postavka problema
Promatramo horizontalnu dionicu duljine $L = 10\,\mathrm{m}$. Neka je koordinata $x \in [0, L]$ horizontalna udaljenost duž trase. Prirodni reljef terena opisan je poznatom visinskom funkcijom $h(x)$:
$$h(x) = 0.0053 x^4 - 0.095 x^3 + 0.48 x^2 - 0.3 x + 1, \quad x \in [0, 10]. \tag{5.1}$$

Provjerimo visine terena na rubovima dionice:
- Na početku ($x = 0$): $h(0) = 1.0000\,\mathrm{m}$.
- Na kraju ($x = 10$):
  $$h(10) = 0.0053(10000) - 0.095(1000) + 0.48(100) - 0.3(10) + 1 = 53 - 95 + 48 - 3 + 1 = 4.0000\,\mathrm{m}.$$

Cilj je odrediti funkciju visine nivelete ceste $y(x)$ za $x \in [0, L]$.

### Ekonomski funkcional zemljanih radova
Trošak izgradnje trase primarno je određen volumenom zemljanih radova:
1. **Iskop (usjek):** Tamo gdje je niveleta ceste ispod prirodnog terena ($y(x) < h(x)$), materijal (zemlju i stijenu) potrebno je otkopati i odvesti.
2. **Nasip:** Tamo gdje je niveleta ceste iznad prirodnog terena ($y(x) > h(x)$), materijal je potrebno dovesti i nasipati.

Uz inženjersku pretpostavku **jedinične širine prometnog traka** ($w = 1\,\mathrm{m}$), elementarni diferencijalni volumen na odsječku $\mathrm{d}x$ iznosi:
$$\mathrm{d}V = w \cdot |y(x) - h(x)| \, \mathrm{d}x = 1 \cdot |y(x) - h(x)| \, \mathrm{d}x.$$
Volumen zemljanih radova (u $\mathrm{m}^3$) time je brojčano identičan **površini između krivulje nivelete i reljefa terena** (u $\mathrm{m}^2$).

Ako pretpostavimo da su jedinični troškovi iskopa i nasipa jednaki (jednakovrijedno ponderiranje), ukupni trošak izgradnje proporcionalan je integralu apsolutnog odstupanja:
$$J[y] = \int_0^L \big| y(x) - h(x) \big| \, \mathrm{d}x. \tag{5.2}$$

---

## 5.2 Fizikalna i kinematička ograničenja ceste: Nagib ($b_1$) i dinamička udobnost ($b_2$)

Kada ne bi bilo nikakvih ograničenja, očito optimalno rješenje bilo bi $y(x) \equiv h(x)$, što daje $J = 0$. Međutim, cesta koja točno prati reljef terena bila bi neprohodna, opasna i neupotrebljiva za promet! Zato se uvode tri ključna skupa inženjerskih ograničenja:

### 1. Ograničenje nagiba nivelete ($b_1$)
Nagib trase predstavlja prvu derivaciju visine po horizontalnoj koordinati:
$$|y'(x)| \leq b_1, \quad \forall x \in [0, L]. \tag{5.3}$$
- **Fizikalno i prometno značenje:**  
  Nagib $y'(x) = \frac{\mathrm{d}y}{\mathrm{d}x} = \tan \theta$ (bezdimenzionalna veličina, m/m) ograničava uspon i pad ceste.  
  Ograničenje je određeno vučnom silom motora vozila, silom trenja između guma i kolnika radi sprječavanja proklizavanja na usponima i pri kočenju nizbrdo, te minimalnim nagibom potrebnim za prirodnu odvodnju oborinskih voda s kolnika.
- U zadatku je za oba slučaja zadano:
  $$b_1 = 0.5 \quad (50\% \text{ nagiba}).$$

### 2. Ograničenje brzine promjene nagiba / vertikalne zakrivljenosti ($b_2$)
Brzina promjene nagiba duž trase predstavlja drugu derivaciju visine:
$$|y''(x)| \leq b_2, \quad \forall x \in [0, L]. \tag{5.4}$$
- **Dinamičko značenje i udobnost putnika (Fizika vozila):**  
  Za funkciju $y(x)$ s malim nagibima ($y' \ll 1$), vertikalna zakrivljenost krivulje $\kappa(x)$ aproksimira se drugom derivacijom:
  $$\kappa(x) = \frac{y''(x)}{\left(1 + [y'(x)]^2\right)^{3/2}} \approx y''(x).$$
  Kada se vozilo giba horizontalnom brzinom $v_0 = \frac{\mathrm{d}x}{\mathrm{d}t} = \mathrm{const}$, vertikalno ubrzanje koje djeluje na putnike i ovjes vozila iznosi:
  $$a_z(t) = \frac{\mathrm{d}^2 y}{\mathrm{d}t^2} = \frac{\mathrm{d}}{\mathrm{d}t}\left( y'(x) \frac{\mathrm{d}x}{\mathrm{d}t} \right) = y''(x) \left(\frac{\mathrm{d}x}{\mathrm{d}t}\right)^2 + y'(x) \frac{\mathrm{d}^2 x}{\mathrm{d}t^2} = v_0^2 y''(x).$$
  Dakle, ograničenje $|y''(x)| \leq b_2$ izravno ograničava **maksimalno vertikalno centrifugalno ubrzanje**:
  $$|a_z| \leq v_0^2 b_2.$$
  Ako je $b_2$ prevelik (oštri prijelomi nivelete):
  - Na grebenu (konveksni prijelom, $y'' < 0$) vozilo gubi kontakt s podlogom, a putnici doživljavaju bestežinsko stanje ili "odvajanje od sjedala".
  - U udolini (konkavni prijelom, $y'' > 0$) putnici osjećaju snažno preopterećenje ("propadanje želuca"), a ovjes vozila može probiti graničnike.
- Zadani parametri:
  - **Slučaj A:** $b_2 = 0.5\,\mathrm{m}^{-1}$ (dopuštena veća zakrivljenost).
  - **Slučaj B:** $b_2 = 0.2\,\mathrm{m}^{-1}$ (visoki standard udobnosti, blaža zakrivljenost).

### 3. Rubni uvjeti (Dirichletova ograničenja)
Cesta se na krajevima dionice mora glatko spojiti na postojeću prometnu infrastrukturu čije su kote fiksirane:
$$y(0) = a = 1.0\,\mathrm{m}, \qquad y(L) = b = 4.0\,\mathrm{m}. \tag{5.5}$$

---

## 5.3 Diskretizacija metodom konačnih razlika: Mreža čvorova i korak $\Delta x$

Problem (5.2)–(5.5) je problem varijacijskog računa u beskonačnodimenzionalnom prostoru funkcija. Kako bismo ga riješili na računalu, provodimo **prostornu diskretizaciju metodom konačnih razlika**.

### Mreža čvorova
Interval $[0, L]$ podijelimo na $N$ jednakih podintervala duljine:
$$\Delta x = \frac{L}{N}.$$
Time nastaje diskretna mreža od $N + 1$ čvorova:
$$x_i = i \cdot \Delta x, \quad i \in \{0, 1, 2, \dots, N\},$$
pri čemu je početni čvor $x_0 = 0$, a završni čvor $x_N = L$.

Diskretne visine prirodnog reljefa u čvorovima su poznate konstante:
$$h_i = h(x_i), \quad i = 0, \dots, N.$$
Optimizacijske varijable su nepoznate visine nivelete ceste u čvorovima:
$$y_i = y(x_i), \quad i = 0, \dots, N \implies y = \begin{bmatrix} y_0 \\ y_1 \\ \vdots \\ y_N \end{bmatrix} \in \mathbb{R}^{N+1}.$$

---

## 5.4 Konstrukcija diferencijskih matrica $D_1$ i $D_2$ (Analiza dimenzija)

Prema uputama zadatka i materijalima s Vježbi 4, derivacije u kontinuiranom prostoru aproksimiraju se jednostranim podijeljenim razlikama unazad (*backward finite differences*).

### Aproksimacija prve derivacije (Nagib):
U svakom intervalu između susjednih čvorova nagib se aproksimira prvom podijeljenom razlikom:
$$\nabla y_i := \frac{y_i - y_{i-1}}{\Delta x}, \quad i \in \{1, 2, \dots, N\}. \tag{5.6}$$

Uočimo dimenzije:
- Imamo $N+1$ čvorova visine ($y_0, \dots, y_N$).
- Između njih postoji točno $N$ odsječaka, dakle definirano je $N$ nagiba $\nabla y_1, \dots, \nabla y_N$.
- Zato matrica prve diferencije $D_1$ ima dimenziju **$N \times (N+1)$**:

$$D_1 y = \begin{bmatrix} \nabla y_1 \\ \nabla y_2 \\ \vdots \\ \nabla y_N \end{bmatrix} = \frac{1}{\Delta x} \begin{bmatrix}
-1 & 1 & 0 & \dots & 0 & 0 \\
0 & -1 & 1 & \dots & 0 & 0 \\
\vdots & \vdots & \ddots & \ddots & \vdots & \vdots \\
0 & 0 & 0 & \dots & -1 & 1
\end{bmatrix} \begin{bmatrix} y_0 \\ y_1 \\ \vdots \\ y_N \end{bmatrix}. \tag{5.7}$$

Ograničenje na nagib u vektorskom obliku glasi:
$$-b_1 \cdot \mathbf{1}_N \leq D_1 y \leq b_1 \cdot \mathbf{1}_N \iff \begin{bmatrix} D_1 \\ -D_1 \end{bmatrix} y \leq \begin{bmatrix} b_1 \cdot \mathbf{1}_N \\ b_1 \cdot \mathbf{1}_N \end{bmatrix}. \tag{5.8}$$
To čini sustav od $2N$ linearnih nejednakosti.

### Aproksimacija druge derivacije (Zakrivljenost):
Brzina promjene nagiba (druga derivacija) aproksimira se drugom podijeljenom razlikom:
$$\nabla^2 y_i := \frac{\nabla y_i - \nabla y_{i-1}}{\Delta x} = \frac{\frac{y_i - y_{i-1}}{\Delta x} - \frac{y_{i-1} - y_{i-2}}{\Delta x}}{\Delta x} = \frac{y_i - 2y_{i-1} + y_{i-2}}{\Delta x^2}, \quad i \in \{2, 3, \dots, N\}. \tag{5.9}$$

Uočimo dimenzije:
- Za izračun druge diferencije potrebna su tri uzastopna čvora ($y_{i-2}, y_{i-1}, y_i$).
- Indeks $i$ teče od $2$ do $N$, što daje ukupno $N - 1$ točaka zakrivljenosti.
- Zato matrica druge diferencije $D_2$ ima dimenziju **$(N-1) \times (N+1)$**:

$$D_2 y = \begin{bmatrix} \nabla^2 y_2 \\ \nabla^2 y_3 \\ \vdots \\ \nabla^2 y_N \end{bmatrix} = \frac{1}{\Delta x^2} \begin{bmatrix}
1 & -2 & 1 & 0 & \dots & 0 \\
0 & 1 & -2 & 1 & \dots & 0 \\
\vdots & \vdots & \ddots & \ddots & \ddots & \vdots \\
0 & 0 & \dots & 1 & -2 & 1
\end{bmatrix} \begin{bmatrix} y_0 \\ y_1 \\ \vdots \\ y_N \end{bmatrix}. \tag{5.10}$$

Ograničenje na drugu derivaciju u vektorskom obliku glasi:
$$-b_2 \cdot \mathbf{1}_{N-1} \leq D_2 y \leq b_2 \cdot \mathbf{1}_{N-1} \iff \begin{bmatrix} D_2 \\ -D_2 \end{bmatrix} y \leq \begin{bmatrix} b_2 \cdot \mathbf{1}_{N-1} \\ b_2 \cdot \mathbf{1}_{N-1} \end{bmatrix}. \tag{5.11}$$
To čini sustav od $2(N-1)$ linearnih nejednakosti.

---

## 5.5 Numerička kvadratura i aproksimacija funkcionala troška

Kontinuirani integral troška (5.2) diskretizira se pomoću **pravokutne numeričke kvadrature** po čvorovima mreže:
$$J[y] = \int_0^L |y(x) - h(x)| \, \mathrm{d}x \approx J_{\mathrm{disc}} = \sum_{i=0}^N |y_i - h_i| \cdot \Delta x = \Delta x \sum_{i=0}^N |y_i - h_i|. \tag{5.12}$$

> ⚠️ **KRITIČNA NAPOMENA O KORAKU $\Delta x$:**  
> Multiplikator $\Delta x$ u funkciji cilja (5.12) je **obavezan** jer pretvara sumu diskretnih odstupanja (m) u stvarnu površinu profila ceste ($\mathrm{m}^2$).  
> Ako student izostavi $\Delta x$ i minimizira samo $\sum |y_i - h_i|$, vrijednost kriterija bi rasla proporcionalno broju točaka $N$ (bila bi 5 puta veća za $N=100$ nego za $N=20$), što bi bio teški numerički i inženjerski apsurd!

---

## 5.6 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori

### ❓ Tipična ispitna pitanja profesora na obrani

#### Pitanje 5.1: Koje je točno dinamičko i fizikalno značenje ograničenja na drugu derivaciju nivelete ceste ($b_2$)?
*Kontekst:* Povezivanje mehanike vozila i optimizacijskog modela.
> **Modelski odgovor studenta:**  
> "Druga derivacija nivelete $y''(x)$ pri malim nagibima predstavlja vertikalnu zakrivljenost ceste $\kappa(x) \approx y''(x)$.  
> Kada se vozilo kreće horizontalnom brzinom $v_0$, na njega i putnike djeluje vertikalno centrifugalno ubrzanje $a_z = v_0^2 y''(x)$. Ograničenjem $|y''| \leq b_2$ izravno ograničavamo maksimalno vertikalno ubrzanje $|a_z| \leq v_0^2 b_2$.  
> Time se sprječavaju dinamička preopterećenja putnika i ovjesa u udolinama te gubitak kontakta guma s kolnikom ili odvajanje putnika od sjedala na prijevojima (sljemenskim krivinama), čime se jamči zakonom propisana dinamička udobnost i sigurnost vožnje."

#### Pitanje 5.2: Zašto matrica $D_1$ ima dimenziju $N \times (N+1)$, a matrica $D_2$ dimenziju $(N-1) \times (N+1)$?
*Kontekst:* Provjera razumijevanja diskretizacije konačnim razlikama.
> **Modelski odgovor studenta:**  
> "Zato što na mreži od $N+1$ čvorova postoji točno $N$ susjednih intervala duljine $\Delta x$. Budući da se nagib $\nabla y_i = \frac{y_i - y_{i-1}}{\Delta x}$ računa između dva susjedna čvora, imamo točno $N$ vrijednosti nagiba, pa matrica $D_1$ mora imati $N$ redaka i $N+1$ stupaca.  
> Za drugu derivaciju $\nabla^2 y_i = \frac{y_i - 2y_{i-1} + y_{i-2}}{\Delta x^2}$ potrebna su tri uzastopna čvora. Ona se može izračunati tek u unutrašnjim točkama počevši od indeksa $i=2$ pa sve do $i=N$. Tih točaka ima točno $(N - 2 + 1) = N - 1$, pa matrica $D_2$ nužno ima $N - 1$ redaka i $N+1$ stupaca."

#### Pitanje 5.3: Zašto u rubnim točkama nismo koristili simetrične centralne diferencije drugog reda točnosti $O(\Delta x^2)$?
*Kontekst:* Numerička matematika i robusnost formulacije (Vježbe 4).
> **Modelski odgovor studenta:**  
> "Centralne diferencije $y'(x_i) \approx \frac{y_{i+1} - y_{i-1}}{2\Delta x}$ imaju viši red točnosti $O(\Delta x^2)$, ali na rubovima domene ($x_0$ i $x_N$) zahtijevaju uvođenje fiktivnih čvorova izvan intervala ($y_{-1}$ i $y_{N+1}$).  
> Korištenjem podijeljenih razlika unazad prema uputama zadatka, diferencijski operatori $D_1$ i $D_2$ ostaju strogo definirani unutar zadanog skupa čvorova bez uvođenja nefizikalnih pretpostavki o ponašanju terena izvan dionice $[0, L]$. Uz to, jednostrane razlike daju konzervativniju ocjenu nagiba unutar svakog odsječka, što je povoljnije sa stajališta sigurnosti trase."

---

### ⚠️ Fatalne zablude i zamke u izvođenju

1. **Izostavljanje koraka $\Delta x$ u funkciji cilja:** Najčešća studentska greška. Minimiziranje čiste sume $\sum |y_i - h_i|$ umjesto $\Delta x \sum |y_i - h_i|$ dovodi do toga da funkcija cilja ovisi o broju čvorova, umjesto da konvergira prema fizikalnoj površini zemljanih radova ($\mathrm{m}^2$).
2. **Pogrešno dimenzioniranje vektora jedinica $\mathbf{1}$ u ograničenjima:** Zadavanje $D_1 y \leq b_1 \cdot \mathbf{1}_{N+1}$ umjesto $\mathbf{1}_N$. MATLAB će javiti grešku neusklađenih matričnih dimenzija (`Matrix dimensions must agree`).
3. **Zaboravljanje faktora $\Delta x^2$ u nazivniku matrice $D_2$:** Druga derivacija ima mjernu jedinicu $\mathrm{m}^{-1}$. Ako se u nazivnik stavi $\Delta x$ umjesto $\Delta x^2$, ograničenje zakrivljenosti postaje drastično preblago ili prestrogo ovisno o koraku mreže.


---

# POGLAVLJE 6: Egzaktna transformacija u Linearni Program (LP) i analiza degeneracije

> **Sadržaj poglavlja:**  
> 6.1 Teorija aproksimacija u normama ($\ell_1, \ell_2, \ell_\infty$)  
> 6.2 Egzaktna transformacija nelinearne $\ell_1$-norme u standardni LP  
> 6.3 Dimenzije proširenog problema i implementacija u MATLAB-u (`linprog`)  
> 6.4 Komparativna analiza rezultata za 4 zadana scenarija  
> 6.5 Zagonetka 1: Zašto vrijednost kriterija $J^*$ RASTE sa zgušnjavanjem mreže?  
> 6.6 Zagonetka 2: Zašto u tablici nema zasebnih stupaca za "iskop" i "nasip" (Degeneracija LP-a)?  
> 6.7 Povezivanje sa Slikama 4.1, 4.2 i 4.3 seminara  
> 6.8 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori  

---

## 6.1 Teorija aproksimacija u normama ($\ell_1, \ell_2, \ell_\infty$)

Prilikom formuliranja inženjerskih optimizacijskih problema, ključan korak je izbor prikladne **funkcije gubitka** (*loss function*) ili **norme** za mjerenje pogreške (prof. Jokić, Predavanje 5 i Vježbe 4).

Promotrimo aproksimaciju vektora odstupanja $e = y - h \in \mathbb{R}^{N+1}$:
1. **$\ell_2$-norma (Najmanji kvadrati):** $\min \|e\|_2^2 = \sum e_i^2$.  
   Daje glatka analitička rješenja (kvadratni program), ali je **izrazito osjetljiva na velike pogreške** (kvadrira odstupanje). U cestogradnji bi to značilo da jedno veliko brdo stvara nerazmjerno ogroman trošak, dok se mala odstupanja ignoriraju.
2. **$\ell_\infty$-norma (Chebyshevjeva / Minimax norma):** $\min \|e\|_\infty = \max_i |e_i|$.  
   Minimizira vršnu maksimalnu pogrešku na cijeloj trasi. Koristi se u instrumentaciji i kalibraciji senzora, ali je u zemljanim radovima neupotrebljiva jer potpuno ignorira ukupni volumen materijala.
3. **$\ell_1$-norma (Suma apsolutnih odstupanja):** $\min \|e\|_1 = \sum |e_i|$.  
   Linearno penalizira svako odstupanje. U građevinarstvu, svaki kubični metar iskopanog ili nasipanog materijala ima jediničnu cijenu (rad bagera, prijevoz kamionom, zbijanje valjkom). Zato je **$\ell_1$-norma jedini fizikalno i ekonomski ispravan izbor za modeliranje zemljanih radova**.

---

## 6.2 Egzaktna transformacija nelinearne $\ell_1$-norme u standardni LP

Diskretizirani problem iz Poglavlja 5 glasi:
$$\min_{y \in \mathbb{R}^{N+1}} \quad J_{\mathrm{disc}} = \Delta x \sum_{i=0}^N |y_i - h_i| \tag{6.1}$$
uz ograničenja:
$$-b_1 \cdot \mathbf{1}_N \leq D_1 y \leq b_1 \cdot \mathbf{1}_N, \tag{6.2}$$
$$-b_2 \cdot \mathbf{1}_{N-1} \leq D_2 y \leq b_2 \cdot \mathbf{1}_{N-1}, \tag{6.3}$$
$$y_0 = a = 1.0, \qquad y_N = b = 4.0. \tag{6.4}$$

Funkcija cilja (6.1) sadrži operaciju apsolutne vrijednosti $|y_i - h_i|$ koja **nije diferencijabilna** u točkama gdje niveleta siječe teren ($y_i = h_i$). Kako ovaj nelinearni problem prevesti u glatki Linearni Program?

### Tehnika pomoćnih varijabli (Slack variables)
Uvodimo pomoćni vektor $t = [t_0, t_1, \dots, t_N]^{\mathsf{T}} \in \mathbb{R}^{N+1}$ koji predstavlja gornju među apsolutnog odstupanja u svakom čvoru:
$$|y_i - h_i| \leq t_i, \quad i = 0, \dots, N. \tag{6.5}$$

Nejednakost s apsolutnom vrijednošću $|u| \leq t$ ekvivalentna je paru linearnih nejednakosti:
$$-t \leq u \leq t \iff \begin{cases} u \leq t \\ -u \leq t \end{cases} \iff \begin{cases} u - t \leq 0 \\ -u - t \leq 0 \end{cases}$$

Primijenjeno na naša odstupanja $u_i = y_i - h_i$:
$$\begin{aligned}
y_i - t_i &\leq h_i \\
-y_i - t_i &\leq -h_i
\end{aligned} \quad \forall i \in \{0, 1, \dots, N\}. \tag{6.6}$$

U vektorskom matričnom obliku za sve čvorove:
$$\begin{bmatrix} I_{N+1} & -I_{N+1} \\ -I_{N+1} & -I_{N+1} \end{bmatrix} \begin{bmatrix} y \\ t \end{bmatrix} \leq \begin{bmatrix} h \\ -h \end{bmatrix}. \tag{6.7}$$

### Ekvivalentni optimizacijski problem:
Umjesto nelinearne funkcije $|y_i - h_i|$, sada minimiziramo linearnu funkciju pomoćnih varijabli:
$$\min_{y, t} \quad \Delta x \sum_{i=0}^N t_i = \Delta x \cdot \mathbf{1}_{N+1}^{\mathsf{T}} t. \tag{6.8}$$

> **Zašto je ova transformacija egzaktna?**  
> Budući da u funkciji cilja minimiziramo $t_i$ uz pozitivne koeficijente $\Delta x > 0$, rješavač će pritisnuti svaku varijablu $t_i$ prema dolje dokle god joj to dopuštaju ograničenja (6.6).  
> U optimumu će svaka pomoćna varijabla poprimiti točnu vrijednost $t_i^* = |y_i^* - h_i|$.  
> Nema nikakve relaksacije niti gubitka točnosti — problem je **egzaktno transformiran u Linearni Program (LP)**!

---

## 6.3 Dimenzije proširenog problema i implementacija u MATLAB-u (`linprog`)

Definirajmo prošireni vektor optimizacijskih varijabli $z \in \mathbb{R}^{2N+2}$:
$$z = \begin{bmatrix} y \\ t \end{bmatrix} = \begin{bmatrix} y_0 \\ \vdots \\ y_N \\ t_0 \\ \vdots \\ t_N \end{bmatrix}.$$

### Analiza dimenzija:
1. **Broj varijabli:** $(N+1) + (N+1) = 2N + 2$.
   - Za $N = 20$: $2(20) + 2 = \mathbf{42}$ varijable.
   - Za $N = 100$: $2(100) + 2 = \mathbf{202}$ varijable.
2. **Vektor funkcije cilja $c_z \in \mathbb{R}^{2N+2}$:**
   $$c_z = \begin{bmatrix} \mathbf{0}_{N+1} \\ \Delta x \cdot \mathbf{1}_{N+1} \end{bmatrix}.$$
3. **Matrica ograničenja nejednakosti $A_{\mathrm{in}} z \leq b_{\mathrm{in}}$:**
   Sastoji se od tri bloka ograničenja:
   - $\ell_1$-dio (odstupanja nivelete od terena): $2(N+1) = 2N + 2$ nejednakosti.
   - Nagib nivelete ($|D_1 y| \leq b_1$): $2N$ nejednakosti.
   - Zakrivljenost nivelete ($|D_2 y| \leq b_2$): $2(N-1) = 2N - 2$ nejednakosti.
   Ukupan broj redaka matrice $A_{\mathrm{in}}$ iznosi:
   $$m_{\mathrm{in}} = (2N + 2) + 2N + (2N - 2) = \mathbf{6N} \text{ nejednakosti}!$$
   - Za $N = 20$: $6 \times 20 = \mathbf{120}$ nejednakosti.
   - Za $N = 100$: $6 \times 100 = \mathbf{600}$ nejednakosti.
4. **Ograničenja jednakosti $A_{\mathrm{eq}} z = b_{\mathrm{eq}}$:**
   Fiksiraju rubne točke $y_0 = a = 1.0$ i $y_N = b = 4.0$:
   $$A_{\mathrm{eq}} = \begin{bmatrix} 1 & 0 & \dots & 0 & 0 & \dots & 0 \\ 0 & \dots & 0 & 1 & 0 & \dots & 0 \end{bmatrix} \in \mathbb{R}^{2 \times (2N+2)}, \quad b_{\mathrm{eq}} = \begin{bmatrix} 1.0 \\ 4.0 \end{bmatrix}.$$

### MATLAB poziv:
```matlab
options = optimoptions('linprog', 'Algorithm', 'dual-simplex', 'Display', 'none');
[z_opt, fval, exitflag] = linprog(c_z, A_in, b_in, A_eq, b_eq, [], [], options);
y_opt = z_opt(1:N+1);
```
Solver završava sa statusom `exitflag = 1`, što označava uspješno postignut globalni optimum.

---

## 6.4 Komparativna analiza rezultata za 4 zadana scenarija

U tablici 6.1 prikazani su numerički rezultati rješavanja za sva 4 zadana slučaja (izravno iz referentnog ispisa `task3_output.txt`):

| Slučaj | Ograničenja | Broj intervala $N$ | Korak $\Delta x$ | Broj varijabli | Broj nejednakosti | Optimalni trošak $J^*$ [$\mathrm{m}^2$] | $\max |\nabla y|$ | $\max |\nabla^2 y|$ | Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **A (i)** | $b_1=0.5, b_2=0.5$ | $N = 20$ | $0.50\,\mathrm{m}$ | 42 | 120 | **1.916180** | 0.5000 | 0.5000 | `exitflag = 1` |
| **A (ii)** | $b_1=0.5, b_2=0.5$ | $N = 100$ | $0.10\,\mathrm{m}$ | 202 | 600 | **1.965940** | 0.5000 | 0.5000 | `exitflag = 1` |
| **B (iii)** | $b_1=0.5, b_2=0.2$ | $N = 20$ | $0.50\,\mathrm{m}$ | 42 | 120 | **2.453727** | 0.5000 | 0.2000 | `exitflag = 1` |
| **B (iv)** | $b_1=0.5, b_2=0.2$ | $N = 100$ | $0.10\,\mathrm{m}$ | 202 | 600 | **2.506047** | 0.5000 | 0.2000 | `exitflag = 1` |

### Utjecaj inženjerskih parametara:
1. **Utjecaj zahtjeva za udobnošću vožnje ($b_2$):**  
   Pri rezoluciji $N = 100$, pooštravanje dopuštene zakrivljenosti s $b_2 = 0.5\,\mathrm{m}^{-1}$ na $b_2 = 0.2\,\mathrm{m}^{-1}$ dovodi do skoka troška s $1.9659\,\mathrm{m}^2$ na $2.5060\,\mathrm{m}^2$, što je porast od čak **+27.47%**!  
   *Inženjersko objašnjenje:* Blaža zakrivljenost ($b_2 = 0.2$) prisiljava cestu na znatno veće radijuse vertikalnih zaobljenja. Cesta ne smije "preroniti" u udolinu niti se oštro prelomiti preko grebena prirodnog reljefa, pa projektant mora napraviti golem nasip u udolini i dubok usjek na uzvišenju. Udobnost i brzina vožnje izravno se plaćaju većom kubaturom zemljanih radova.
2. **Zasićenje ograničenja (Aktivni skup):**  
   U sva 4 slučaja i nagib i zakrivljenost dostižu svoje maksimalne dozvoljene vrijednosti ($\max |\nabla y| = b_1$, $\max |\nabla^2 y| = b_2$), što dokazuje da su kinematička ograničenja aktivna i diktiraju oblik trase.

---

## 6.5 Zagonetka 1: Zašto vrijednost kriterija $J^*$ RASTE sa zgušnjavanjem mreže?

Pogledajmo pažljivo retke tablice 6.1 pri prijelazu s $N = 20$ na $N = 100$:
- Za slučaj A: $J^*$ raste s $1.916180$ na $1.965940$ (**+2.60%**).
- Za slučaj B: $J^*$ raste s $2.453727$ na $2.506047$ (**+2.13%**).

Ovo je jedno od najopasnijih pitanja prof. Jokića na usmenom ispitu!  
*Naivna studentska intuicija:* "Gušća mreža ($N=100$) ima 202 varijable u odnosu na 42 varijable pri $N=20$. Više optimizacijskih varijabli znači veći stupanj slobode za minimizaciju, pa bi vrijednost kriterija trebala pasti ili ostati ista. Zašto kriterij raste?!"

### Egzaktno inženjersko i numeričko objašnjenje:
Kriterij $J_{\mathrm{disc}} = \Delta x \sum_{i=0}^N |y_i - h_i|$ nije ništa drugo nego **pravokutna numerička integracija (kvadratura)** kontinuiranog integrala $J_{\mathrm{kont}} = \int_0^L |y(x) - h(x)| \mathrm{d}x$.

1. **Podcjenjivanje integrala na rijetkoj mreži:**  
   Na rijetkoj mreži ($N = 20$, $\Delta x = 0.5\,\mathrm{m}$), funkcija odstupanja $|y(x) - h(x)|$ uzorkovana je u svega 21 točki. Prirodni reljef $h(x)$ je polinom 4. stupnja s izraženim valovitim profilom. Između dva čvora udaljena pola metra reljef ima "trbuh" koji rijetka mreža jednostavno preskače i ne registrira. Zato suma na rijetkoj mreži **podcjenjuje** stvarni volumen zemljanih radova!
2. **Red integracijske pogreške:**  
   Pravokutna kvadratura ima red točnosti $O(\Delta x)$. Za $N = 20$ korak je $\Delta x = 0.5\,\mathrm{m}$, dok je za $N = 100$ korak $\Delta x = 0.1\,\mathrm{m}$ (pet puta manji). Kako zgušnjavamo mrežu, numerička kvadratura točnije zahvaća cjelokupnu površinu između krivulja, pa vrijednost numeričkog integrala **konvergira odozdo prema pravoj kontinuiranoj vrijednosti**.
3. **Zaključak:** Nije rješenje pri $N = 20$ "bolje" od onoga pri $N = 100$, nego je mjerenje troška pri $N = 20$ bilo numerički neprecizno i optimistično podcijenjeno!

---

## 6.6 Zagonetka 2: Zašto u tablici nema zasebnih stupaca za "iskop" i "nasip" (Degeneracija LP-a)?

U verziji v1.0 seminara postojali su stupci s kubaturama iskopa i nasipa. U pročišćenoj verziji v1.2 ti su stupci **namjerno uklonjeni**. Zašto?

### Fenomen degeneracije u Linearnom Programiranju:
Optimizacijski problem minimizira isključivo ukupnu površinu:
$$J = \int |y - h| \, \mathrm{d}x = V_{\mathrm{iskop}} + V_{\mathrm{nasip}}.$$
Na ravnim dionicama trase ili tamo gdje je prirodni teren blag, postoji **čitava familija različitih profila nivelete $y(x)$** koji imaju identičan zbroj odstupanja $J^*$, ali potpuno različitu raspodjelu između iskopa ($y < h$) i nasipa ($y > h$).

To znači da je problem linearnog programiranja **degeneriran** (optimalna vrijednost cilja $J^*$ je jedinstvena, ali točka optimuma $y^*$ u prostoru stanja **nije jedinstvena**!).
- Ako problem riješite pomoću algoritma *Dual Simplex*, solver će odabrati jedan ekstremni vrh simpleksnog politopa.
- Ako isti problem riješite algoritmom *Interior Point*, solver će konvergirati u analitičko središte skupa optimalnih rješenja.
- Oba rješavača dat će identičnu vrijednost $J^* = 1.965940\,\mathrm{m}^2$, ali će jedan dati npr. $V_{\mathrm{iskop}} = 1.10, V_{\mathrm{nasip}} = 0.86$, a drugi $V_{\mathrm{iskop}} = 0.95, V_{\mathrm{nasip}} = 1.01$!

> 💡 **Ispitni zaključak:** Prikazivanje zasebnih brojki za iskop i nasip u inženjerskom izvještaju značilo bi tvrditi nešto što optimizacijski problem matematički ne određuje jedinstveno. Uklanjanjem tih stupaca u verziji v1.2 zadržana je maksimalna inženjerska preciznost i integritet rezultata.

---

## 6.7 Povezivanje sa Slikama 4.1, 4.2 i 4.3 seminara

1. **Slika 4.1 (`fig3_1_road_case_A.pdf`):**  
   Prikazuje profil nivelete za slučaj A ($b_2 = 0.5$). Vidljivo je da niveleta vrlo vjerno prati prirodni teren jer joj dopuštena zakrivljenost omogućuje brže prilagođavanje brežuljcima i udolinama.
2. **Slika 4.2 (`fig3_2_road_case_B.pdf`):**  
   Prikazuje profil nivelete za slučaj B ($b_2 = 0.2$). Krivulja nivelete je znatno "ispeglana", s blagim vertikalnim radijusima. Vidljiva su velika odstupanja od prirodnog reljefa, posebice na stacionaži oko $x \approx 6\,\mathrm{m}$ gdje nastaje veliki nasip.
3. **Slika 4.3 (`fig3_3_road_constraint_check.pdf`):**  
   Dijagram verifikacije ograničenja. Prikazuje vrijednosti nagiba $|\nabla y_i|$ i druge derivacije $|\nabla^2 y_i|$ duž trase. Vidljivo je da druga derivacija za slučaj B točno udara u gornju granicu $0.2\,\mathrm{m}^{-1}$ duž većeg dijela trase, što grafički potvrđuje aktivnost ograničenja.

---

## 6.8 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori

### ❓ Tipična ispitna pitanja profesora na obrani

#### Pitanje 6.1: Zašto vrijednost kriterija $J^*$ raste kada se mreža profini s $N = 20$ na $N = 100$, ako gušća mreža ima više optimizacijskih varijabli?
*Kontekst:* Razumijevanje odnosa kontinuiranog integrala i diskretne sume.
> **Modelski odgovor studenta:**  
> "Zato što je diskretna funkcija cilja $J_{\mathrm{disc}} = \Delta x \sum |y_i - h_i|$ pravokutna kvadraturna aproksimacija kontinuiranog integrala $\int |y - h| \mathrm{d}x$.  
> Na rijetkoj mreži od $N = 20$ točaka ($\Delta x = 0.5\,\mathrm{m}$), funkcija odstupanja je rijetko uzorkovana i valoviti dijelovi terena između čvorova izmiču sumi, pa rijetka mreža **podcjenjuje** stvarni integral za red veličine $O(\Delta x)$.  
> Zgušnjavanjem mreže na $N = 100$ ($\Delta x = 0.1\,\mathrm{m}$), numerička integracija postaje pet puta finija i točnije registrira površinu zemljanih radova, pa vrijednost sume raste konvergirajući odozdo prema pravoj kontinuiranoj vrijednosti (+2.60% za slučaj A, +2.13% za B). Nije rješenje pri $N = 20$ fizikalno bolje, nego je izračun troška tamo bio grublji."

#### Pitanje 6.2: Zašto u službenoj tablici seminara nema zasebnih stupaca za kubature iskopa i nasipa?
*Kontekst:* Razumijevanje degeneracije i nejedinstvenosti optimalnog skupa u LP-u.
> **Modelski odgovor studenta:**  
> "Zato što raspodjela na iskop i nasip **matematički nije jedinstvena**.  
> Linearni program je degeneriran: funkcija cilja penalizira samo ukupnu sumu $|y_i - h_i|$, pa na ravnim dionicama postoji beskonačno mnogo profila nivelete koji postižu identičnu minimalnu vrijednost $J^*$, ali s različitim omjerima iskopa i nasipa.  
> Različiti algoritmi (npr. Dual Simplex vs. Interior-Point) daju različite podjele na iskop i nasip unutar istog globalnog optimuma. Navoditi fiksne brojke u tablici značilo bi tvrditi svojstvo koje model ne određuje jedinstveno."

#### Pitanje 6.3: Kako je uklonjena apsolutna vrijednost iz funkcije cilja i zašto ta transformacija ne unosi konzervatizam?
*Kontekst:* Poznavanje tehnike uvođenja pomoćnih varijabli (Vježbe 4).
> **Modelski odgovor studenta:**  
> "Uvođenjem vektora pomoćnih varijabli $t_i \geq 0$ i zamjenom nelinearnog uvjeta $|y_i - h_i| \leq t_i$ parom linearnih nejednakosti $y_i - t_i \leq h_i$ i $-y_i - t_i \leq -h_i$.  
> U funkciji cilja minimiziramo linearnu sumu $\Delta x \sum t_i$. Budući da su koeficijenti uz $t_i$ strogo pozitivni, minimizacija će potisnuti svaku varijablu $t_i$ do njezine donje granice određene nejednakostima, pa će u optimumu vrijediti točan identitet $t_i^* = |y_i^* - h_i|$. Transformacija je egzaktna i ne unosi nikakav relaksacijski procjep."

---

### ⚠️ Fatalne zablude i zamke u izvođenju

1. **Zaboravljanje množenja s korakom $\Delta x$ u funkciji cilja:** Pisanje $c_z = [0, \mathbf{1}]^{\mathsf{T}}$ umjesto $[0, \Delta x \cdot \mathbf{1}]^{\mathsf{T}}$. Ako se korak izostavi, trošak za $N=100$ ispada pet puta veći nego za $N=20$, što diskreditira inženjersku valjanost rada.
2. **Pogrešan broj redaka u matrici ograničenja nejednakosti:** Student napiše da matrica ima $4N$ nejednakosti umjesto $6N$. Uvijek provjeriti zbroj: $2(N+1)$ za $\ell_1$ + $2N$ za nagib + $2(N-1)$ za zakrivljenost $= 6N$ redaka!
3. **Tvrdnja da se na rijetkoj mreži dobiva točniji profil:** Ne razlikovati vrijednost funkcije cilja od kvalitete modela. Manji $J^*$ na rijetkoj mreži je numerički artefakt podcjenjivanja integrala pravokutnom formulom, a ne superiornost rješenja.


---

# POGLAVLJE 7: Stabilnost dinamičkih sustava i paradoks sklopnih sustava

> **Sadržaj poglavlja:**  
> 7.1 First Principles stabilnosti kontinuiranih sustava: Hurwitzov kriterij i Ljapunovljeva teorija  
> 7.2 Model hibridnog / sklopnog sustava sa skokovitom promjenom dinamike (Switching Systems)  
> 7.3 Zadatak 4a seminara: Egzaktna provjera Hurwitzovosti pojedinačnih modova  
> 7.4 Paradoks sklopnih sustava: Zašto sustav stabilnih podsustava divergira?  
> 7.5 Analitičko izvođenje monodromijske matrice ciklusa ($\Phi_{\mathrm{cikl}}$) i dokaz nestabilnosti  
> 7.6 Fizikalna interpretacija "pumpanja energije" i geometrija faznog portreta  
> 7.7 Simulacija otvorenog kruga u MATLAB-u (Slika 5.1 seminara)  
> 7.8 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori  

---

## 7.1 First Principles stabilnosti kontinuiranih sustava: Hurwitzov kriterij i Ljapunovljeva teorija

U teoriji automatskog upravljanja i dinamike sustava, stabilnost je temeljni preduvjet rada bilo kojeg inženjerskog uređaja (prof. Jokić, Predavanje 7).

### Linearni vremenski invarijantni (LTI) sustavi
Promatramo kontinuirani autonomni LTI sustav u prostoru stanja:
$$\dot{x}(t) = A x(t), \qquad x(0) = x_0, \tag{7.1}$$
gdje je $x(t) \in \mathbb{R}^n$ vektor stanja, a $A \in \mathbb{R}^{n \times n}$ matrica sustava (matrica dinamike).

Egzaktno analitičko rješenje diferencijalne jednadžbe (7.1) dano je preko **matričnog eksponenta**:
$$x(t) = e^{At} x_0, \qquad e^{At} := \sum_{k=0}^\infty \frac{(At)^k}{k!} = I + At + \frac{A^2 t^2}{2!} + \dots \tag{7.2}$$

### Definicije stabilnosti u smislu Ljapunova
1. **Stabilnost po Ljapunovu:** Sustav je stabilan ako za svaki $\epsilon > 0$ postoji $\delta > 0$ takav da iz $\|x(0)\| < \delta$ slijedi $\|x(t)\| < \epsilon$ za sve $t \geq 0$ (trajektorije ostaju omeđene).
2. **Asimptotska stabilnost:** Sustav je stabilan po Ljapunovu i dodatno vrijedi da sva stanja konvergiraju u ravnotežnu točku: $\lim_{t \to \infty} x(t) = 0$.
3. **Eksponencijalna stabilnost:** Postoje konstante $M \geq 1$ i $\alpha > 0$ takve da za sve trajektorije vrijedi:
   $$\|x(t)\| \leq M e^{-\alpha t} \|x(0)\|, \quad \forall t \geq 0. \tag{7.3}$$
   Veličina $\alpha$ naziva se **stopa eksponencijalnog prigušenja** (*decay rate*).

> **Teorem 7.1 (Hurwitzov kriterij za LTI sustave):**  
> Za LTI sustav $\dot{x} = Ax$ sljedeće tvrdnje su međusobno ekvivalentne:
> 1. Sustav je asimptotski (i eksponencijalno) stabilan.
> 2. Sve svojstvene vrijednosti matrice $A$ leže u otvorenoj lijevoj poluravnini kompleksne ravnine:
>    $$\mathrm{Re}(\lambda_i(A)) < 0, \quad \forall i \in \{1, \dots, n\}.$$
>    Takva matrica naziva se **Hurwitzova matrica**.
> 3. Za bilo koju simetričnu pozitivno definitnu matricu $Q \succ 0$, postoji jedinstvena simetrična pozitivno definitna matrica $P \succ 0$ koja zadovoljava **Ljapunovljevu matričnu jednadžbu**:
>    $$A^{\mathsf{T}} P + P A = -Q \prec 0. \tag{7.4}$$
>    Funkcija $V(x) = x^{\mathsf{T}} P x$ tada je striktna Ljapunovljeva funkcija sustava čija je derivacija duž trajektorija strogo negativna:
>    $$\dot{V}(x) = \dot{x}^{\mathsf{T}} P x + x^{\mathsf{T}} P \dot{x} = x^{\mathsf{T}} (A^{\mathsf{T}} P + P A) x = -x^{\mathsf{T}} Q x < 0, \quad \forall x \neq 0.$$

---

## 7.2 Model hibridnog / sklopnog sustava sa skokovitom promjenom dinamike (Switching Systems)

U Zadatku 4 seminara promatramo vremenski promjenjiv dinamički sustav:
$$\dot{x}(t) = A(t) x(t) + B u(t), \qquad x(t) \in \mathbb{R}^2, \quad u(t) \in \mathbb{R}, \tag{7.5}$$
s matricom ulaza:
$$B = \begin{bmatrix} 1 \\ 0 \end{bmatrix}.$$

Matrica dinamike $A(t)$ nije konstantna, već skokovito mijenja vrijednost na svakoj cjelobrojnoj sekundi prema pravilu:
$$A(t) = \begin{cases} A_{\mathrm{parno}}, & \text{kad je } \lfloor t \rfloor \text{ paran broj} \\ A_{\mathrm{neparno}}, & \text{kad je } \lfloor t \rfloor \text{ neparan broj} \end{cases} \tag{7.6}$$
gdje $\lfloor t \rfloor$ označava funkciju najvećeg cijelog broja manjeg ili jednakog $t$ (*floor function*).

Zadane matrice dinamike modova glase:
$$A_{\mathrm{parno}} = \begin{bmatrix} -1 & -\frac{\pi}{6} \\[4pt] \frac{3\pi}{2} & -1 \end{bmatrix}, \qquad A_{\mathrm{neparno}} = \begin{bmatrix} -1 & -\frac{3\pi}{2} \\[4pt] \frac{\pi}{6} & -1 \end{bmatrix}. \tag{7.7}$$

### Klasifikacija sustava
Ovdje je riječ o **sklopnom sustavu** (*switched linear system*), koji pripada široj klasi **hibridnih sustava**.  
- Između svaka dva trenutka prespajanja (unutar intervala $t \in [k, k+1)$) sustav se ponaša kao običan LTI sustav.
- Sustav ima dva diskretna stanja (dva dinamička moda): **parni mod** za $t \in [0,1) \cup [2,3) \cup \dots$ i **neparni mod** za $t \in [1,2) \cup [3,4) \cup \dots$
- Period ciklusa prespajanja iznosi točno:
  $$T_{\mathrm{cikl}} = 1\,\mathrm{s} + 1\,\mathrm{s} = 2.0\,\mathrm{s}.$$

---

## 7.3 Zadatak 4a seminara: Egzaktna provjera Hurwitzovosti pojedinačnih modova

Prvo pitanje glasi: *"Jesu li matrice $A_{\mathrm{parno}}$ i $A_{\mathrm{neparno}}$ stabilne (Hurwitzove) matrice?"*

### Analiza parnog moda ($A_{\mathrm{parno}}$):
Karakteristična jednadžba glasi:
$$\det(\lambda I - A_{\mathrm{parno}}) = \det \begin{bmatrix} \lambda + 1 & \frac{\pi}{6} \\[4pt] -\frac{3\pi}{2} & \lambda + 1 \end{bmatrix} = (\lambda + 1)^2 - \left( -\frac{3\pi}{2} \right) \left( \frac{\pi}{6} \right) = 0,$$
$$(\lambda + 1)^2 + \frac{3\pi^2}{12} = (\lambda + 1)^2 + \frac{\pi^2}{4} = 0.$$
Odavde slijedi:
$$(\lambda + 1)^2 = -\frac{\pi^2}{4} \implies \lambda + 1 = \pm j \frac{\pi}{2}.$$
Svojstvene vrijednosti parnog moda su konjugirano-kompleksni par:
$$\lambda_{1,2}(A_{\mathrm{parno}}) = -1 \pm j \frac{\pi}{2} \approx -1.000000 \pm 1.570796 j. \tag{7.8}$$

### Analiza neparnog moda ($A_{\mathrm{neparno}}$):
Karakteristična jednadžba glasi:
$$\det(\lambda I - A_{\mathrm{neparno}}) = \det \begin{bmatrix} \lambda + 1 & \frac{3\pi}{2} \\[4pt] -\frac{\pi}{6} & \lambda + 1 \end{bmatrix} = (\lambda + 1)^2 - \left( -\frac{\pi}{6} \right) \left( \frac{3\pi}{2} \right) = (\lambda + 1)^2 + \frac{\pi^2}{4} = 0.$$
Karakteristični polinom je **potpuno identičan** kao za parni mod! Svojstvene vrijednosti neparnog moda su:
$$\lambda_{1,2}(A_{\mathrm{neparno}}) = -1 \pm j \frac{\pi}{2} \approx -1.000000 \pm 1.570796 j. \tag{7.9}$$

> **Zaključak za Zadatak 4a:**  
> Realni dijelovi svih svojstvenih vrijednosti oba moda iznose:
> $$\mathrm{Re}(\lambda) = -1.000000 < 0.$$
> **Obje matrice su Hurwitzove.** Kada bi sustav trajno ostao u parnom modu ili trajno u neparnom modu, bio bi asimptotski stabilan s prigušenim oscilacijama frekvencije $\omega = \frac{\pi}{2}\,\mathrm{rad/s}$ i vremenskom konstantom smirivanja $\tau = 1\,\mathrm{s}$.

---

## 7.4 Paradoks sklopnih sustava: Zašto sustav stabilnih podsustava divergira?

U podzadatku 4b provodimo simulaciju otvorenog kruga ($u(t) \equiv 0$) s početnim uvjetom $x(0) = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ kroz vrijeme $t \in [0, 20]\,\mathrm{s}$.

Rezultat simulacije (prikazan na Slici 5.1 seminara i u datoteci `task4_output.txt`) je šokantan za svakog studenta koji se prvi put susreće s hibridnim sustavima:
$$\|x(0)\| = 1.0000 \implies \|x(20)\| = \mathbf{7.1868}!$$
**Sustav ne samo da ne konvergira u nulu, nego divlje oscilira i eksponencijalno divergira u beskonačnost!**

Kako je moguće da sustav sastavljen od dva dokazano stabilna, Hurwitzova moda postane nestabilan jednostavnim prespajanjem svake sekunde?

---

## 7.5 Analitičko izvođenje monodromijske matrice ciklusa ($\Phi_{\mathrm{cikl}}$) i dokaz nestabilnosti

Kako bismo na usmenom ispitu briljirali, nećemo samo pokazati simulacijski graf, već ćemo izvesti **egzaktni analitički dokaz nestabilnosti** pomoću Floquetove teorije i monodromijske matrice prijelaza (prof. Jokić, Predavanje 7).

### Korak 1: Izračun matrice prijelaza za pojedinačni mod
Unutar segmenta duljine $\Delta t = 1\,\mathrm{s}$, matrica dinamike je konstantna. Matrica prijelaza stanja parnog moda glasi $\Phi_{\mathrm{parno}} = e^{A_{\mathrm{parno}} \cdot 1}$.  
Rastavimo matricu $A_{\mathrm{parno}}$ na dijagonalni dio i matricu rotacije:
$$A_{\mathrm{parno}} = -I + \Omega_{\mathrm{par}}, \qquad \Omega_{\mathrm{par}} = \begin{bmatrix} 0 & -\frac{\pi}{6} \\[4pt] \frac{3\pi}{2} & 0 \end{bmatrix}.$$
Budući da skalarna matrica $-I$ komutira sa svakom matricom ($-I \cdot \Omega = \Omega \cdot (-I)$), matrični eksponent se egzaktno rastavlja:
$$e^{A_{\mathrm{parno}} \cdot 1} = e^{-I \cdot 1} \cdot e^{\Omega_{\mathrm{par}} \cdot 1} = e^{-1} e^{\Omega_{\mathrm{par}}}.$$

Izračunajmo potencije matrice $\Omega_{\mathrm{par}}$:
$$\Omega_{\mathrm{par}}^2 = \begin{bmatrix} 0 & -\frac{\pi}{6} \\[4pt] \frac{3\pi}{2} & 0 \end{bmatrix} \begin{bmatrix} 0 & -\frac{\pi}{6} \\[4pt] \frac{3\pi}{2} & 0 \end{bmatrix} = \begin{bmatrix} -\frac{3\pi^2}{12} & 0 \\[4pt] 0 & -\frac{3\pi^2}{12} \end{bmatrix} = -\frac{\pi^2}{4} I = -\omega^2 I, \quad \text{uz } \omega = \frac{\pi}{2}.$$
Budući da je $\Omega_{\mathrm{par}}^2 = -\omega^2 I$, Taylorov red matrice $e^{\Omega_{\mathrm{par}}}$ svodi se na trigonometrijske funkcije:
$$e^{\Omega_{\mathrm{par}} \cdot 1} = \cos(\omega) I + \frac{\sin(\omega)}{\omega} \Omega_{\mathrm{par}} = \cos\left(\frac{\pi}{2}\right) I + \frac{\sin(\pi/2)}{\pi/2} \begin{bmatrix} 0 & -\frac{\pi}{6} \\[4pt] \frac{3\pi}{2} & 0 \end{bmatrix}.$$
Kako je $\cos(\pi/2) = 0$ i $\sin(\pi/2) = 1$:
$$e^{\Omega_{\mathrm{par}}} = \frac{1}{\pi/2} \begin{bmatrix} 0 & -\frac{\pi}{6} \\[4pt] \frac{3\pi}{2} & 0 \end{bmatrix} = \begin{bmatrix} 0 & -\frac{\pi/6}{\pi/2} \\[4pt] \frac{3\pi/2}{\pi/2} & 0 \end{bmatrix} = \begin{bmatrix} 0 & -\frac{1}{3} \\[4pt] 3 & 0 \end{bmatrix}!$$

Uvrštavanjem faktora $e^{-1}$ dobivamo **egzaktnu matricu prijelaza parnog moda**:
$$\Phi_{\mathrm{parno}} = e^{-1} \begin{bmatrix} 0 & -\frac{1}{3} \\[4pt] 3 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -\frac{1}{3} e^{-1} \\[4pt] 3 e^{-1} & 0 \end{bmatrix} \approx \begin{bmatrix} 0.000000 & -0.122626 \\[4pt] 1.103638 & 0.000000 \end{bmatrix}. \tag{7.10}$$

### Korak 2: Matrica prijelaza neparnog moda
Potpuno analognim postupkom za neparni mod $\Omega_{\mathrm{nep}} = \begin{bmatrix} 0 & -\frac{3\pi}{2} \\ \frac{\pi}{6} & 0 \end{bmatrix}$ dobivamo:
$$\Phi_{\mathrm{neparno}} = e^{-1} \begin{bmatrix} 0 & -3 \\[4pt] \frac{1}{3} & 0 \end{bmatrix} = \begin{bmatrix} 0 & -3 e^{-1} \\[4pt] \frac{1}{3} e^{-1} & 0 \end{bmatrix} \approx \begin{bmatrix} 0.000000 & -1.103638 \\[4pt] 0.122626 & 0.000000 \end{bmatrix}. \tag{7.11}$$

### Korak 3: Monodromijska matrica ciklusa ($\Phi_{\mathrm{cikl}}$)
Jedan puni ciklus sustava traje $T_{\mathrm{cikl}} = 2\,\mathrm{s}$ (prvo 1 s parnog moda, zatim 1 s neparnog moda).  
Stanje sustava nakon jednog punog ciklusa povezano je s početnim stanjem preko **monodromijske matrice prijelaza**:
$$x(2) = \Phi_{\mathrm{neparno}} \cdot x(1) = \Phi_{\mathrm{neparno}} \cdot \Phi_{\mathrm{parno}} \cdot x(0) = \Phi_{\mathrm{cikl}} \cdot x(0).$$

Izmnožimo matrice (7.11) i (7.10):
$$\Phi_{\mathrm{cikl}} = \Phi_{\mathrm{neparno}} \Phi_{\mathrm{parno}} = \left( e^{-1} \begin{bmatrix} 0 & -3 \\[4pt] \frac{1}{3} & 0 \end{bmatrix} \right) \left( e^{-1} \begin{bmatrix} 0 & -\frac{1}{3} \\[4pt] 3 & 0 \end{bmatrix} \right) = e^{-2} \begin{bmatrix} (-3)(3) & 0 \\[4pt] 0 & \left(\frac{1}{3}\right)\left(-\frac{1}{3}\right) \end{bmatrix} = e^{-2} \begin{bmatrix} -9 & 0 \\[4pt] 0 & -\frac{1}{9} \end{bmatrix}! \tag{7.12}$$

Uvrstimo numeričku vrijednost baze $e^{-2} = \frac{1}{e^2} \approx \frac{1}{7.389056} \approx 0.135335$:
$$\Phi_{\mathrm{cikl}} = \begin{bmatrix} -9 e^{-2} & 0 \\[4pt] 0 & -\frac{1}{9} e^{-2} \end{bmatrix} \approx \begin{bmatrix} -1.218018 & 0.000000 \\[4pt] 0.000000 & -0.015037 \end{bmatrix}. \tag{7.13}$$

### Korak 4: Spektralni radijus i dokaz nestabilnosti
Budući da je matrica $\Phi_{\mathrm{cikl}}$ dijagonalna, njezine svojstvene vrijednosti su njezini dijagonalni elementi:
$$\mu_1 = -9 e^{-2} \approx -1.218018, \qquad \mu_2 = -\frac{1}{9} e^{-2} \approx -0.015037.$$

**Spektralni radijus** monodromijske matrice definira se kao maksimalni modul svojstvenih vrijednosti:
$$\rho(\Phi_{\mathrm{cikl}}) := \max_i |\mu_i| = 9 e^{-2} \approx \mathbf{1.218018} > 1! \tag{7.14}$$

> 🔴 **MATEMATIČKI DOKAZ DIVERGENCIJE:**  
> Stanje sustava u stroboskopskim trenucima na krajevima ciklusa ($t = 2k$, $k = 0, 1, 2, \dots$) ponaša se kao diskretni sustav:
> $$x(2k) = (\Phi_{\mathrm{cikl}})^k x(0).$$
> Za zadani početni uvjet $x(0) = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$, prva komponenta stanja iznosi:
> $$x_1(2k) = (-1.218018)^k \cdot 1.$$
> Nakon svakog ciklusa od 2 sekunde, stanje mijenja predznak i **amplituda mu naraste za 21.8%**!  
> Nakon $T = 20\,\mathrm{s}$ (što je $k = 10$ ciklusa), amplituda iznosi:
> $$|x_1(20)| = (1.218018)^{10} \approx 7.1868.$$
> Budući da je $\rho(\Phi_{\mathrm{cikl}}) > 1$, sustav je **eksponencijalno nestabilan**! $\blacksquare$

---

## 7.6 Fizikalna interpretacija "pumpanja energije" i geometrija faznog portreta

Zašto se ovo događa? Kako periodičko prespajanje unosi energiju u sustav?

1. **Geometrija elipsoida nivoa energije:**  
   Za parni mod, nivo-krivulje energije (Ljapunovljeve funkcije $V_{\mathrm{par}}(x)$) su izdužene elipse čija je glavna poluos u smjeru osi $x_1$ tri puta dulja nego u smjeru $x_2$ (omjer osi $3 : 1$).  
   Za neparni mod, elipse su zarotirane za $90^\circ$ — glavna os je izdužena u smjeru $x_2$ (omjer osi $1 : 3$).
2. **Mehanizam pumpanja energije:**  
   - Kroz prvu sekundu (parni mod), trajektorija se giba duž svoje elipse i skuplja se prema ishodištu faktorom $e^{-1}$, ali rotira za kut $\pi/2$ tako da završava točno na osi $x_2$.
   - U sekundi $t = 1.0\,\mathrm{s}$, sustav skokovito prespaja na neparni mod. No, točka na osi $x_2$ za neparni mod leži na **vrlo visokoj energetskoj razini**!
   - Kroz drugu sekundu trajektorija rotira natrag na os $x_1$, gdje u trenutku $t = 2.0\,\mathrm{s}$ prespajanje ponovno pronalazi točku na još višoj energetskoj razini parnog moda.
   - Iako unutar svakog moda sustav disipira energiju, **skokovita promjena koordinatnih osi elipsoida djeluje kao parametarska rezonancija** koja ubacuje više energije nego što je podsustavi stignu disipirati!

---

## 7.7 Simulacija otvorenog kruga u MATLAB-u (Slika 5.1 seminara)

### Segmentna simulacija s `ode45`:
Budući da je matrica dinamike po dijelovima konstantna, numerička simulacija provodi se po segmentima duljine $1\,\mathrm{s}$:
```matlab
A_par = [-1, -pi/6;   3*pi/2, -1];
A_nep = [-1, -3*pi/2; pi/6,   -1];
x0 = [1; 0];  T = 20;

xc = x0;
for kseg = 0:T-1
    if mod(kseg, 2) == 0, Aa = A_par; else, Aa = A_nep; end
    o = odeset('RelTol', 1e-9, 'AbsTol', 1e-11);
    [ts, xs] = ode45(@(t, x) Aa*x, [kseg, kseg+1], xc, o);
    xc = xs(end, :)'; % Završno stanje segmenta postaje početno stanje sljedećeg
end
```

### Karakteristike odziva na Slici 5.1 (`fig4_1_open_loop_divergence.pdf`):
- **Vremenski odziv:** Stanja $x_1(t)$ i $x_2(t)$ pokazuju oscilacije čija amplituda progresivno buja. Na $t = 20\,\mathrm{s}$ vršna vrijednost prelazi $7.0$.
- **Fazni portret ($x_1$ vs. $x_2$):** Trajektorija tvori spiralu koja se **odmotava prema van**, demonstrirajući divergenciju otvorenog kruga.

---

## 7.8 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori

### ❓ Tipična ispitna pitanja profesora na obrani

#### Pitanje 7.1: Kako je moguće da je sklopni sustav nestabilan ako su oba njegova dinamička moda Hurwitzova?
*Kontekst:* Glavno konceptualno pitanje iz teorije sklopnih sustava.
> **Modelski odgovor studenta:**  
> "Hurwitzovost pojedinačnih matrica jamči stabilnost samo ako sustav trajno ostane u jednom modu. Čim postoji prespajanje, svojstvene vrijednosti pojedinih matrica više ne određuju stabilnost.  
> Za periodičko prespajanje mjerodavna je **monodromijska matrica ciklusa** $\Phi_{\mathrm{cikl}} = e^{A_{\mathrm{neparno}}} e^{A_{\mathrm{parno}}}$.  
> Umnožak dviju matrica koje zasebno imaju spektralni radijus manji od jedan općenito ne mora imati spektralni radijus manji od jedan. U našem slučaju je $\Phi_{\mathrm{cikl}} = e^{-2} \mathrm{diag}(-9, -1/9)$, pa je spektralni radijus $\rho(\Phi_{\mathrm{cikl}}) = 9 e^{-2} \approx 1.218 > 1$. Geometrijski, elipsoidi nivoa energije dvaju modova nisu usklađeni, pa prespajanje djeluje kao parametarska rezonancija koja pumpa energiju u sustav brže nego što je disipacija može odvesti."

#### Pitanje 7.2: Što je monodromijska matrica i kako se ona analitički računa?
*Kontekst:* Provjera matematičkog izvođenja matrice prijelaza.
> **Modelski odgovor studenta:**  
> "Monodromijska matrica $\Phi_{\mathrm{cikl}}$ je stroboskopska matrica prijelaza stanja preko jednog punog perioda prespajanja $T_{\mathrm{cikl}}$, takva da vrijedi $x(t + T_{\mathrm{cikl}}) = \Phi_{\mathrm{cikl}} x(t)$.  
> Računa se analitičkim množenjem matričnih eksponenata pojedinih modova: $\Phi_{\mathrm{cikl}} = e^{A_2 \Delta t_2} e^{A_1 \Delta t_1}$.  
> Koristeći dekompoziciju matrica $A_i = -I + \Omega_i$ i činjenicu da je $\Omega_i^2 = -(\pi/2)^2 I$, matrični eksponenti se svode na trigonometrijske funkcije, što daje egzaktne matrice prijelaza $\Phi_{\mathrm{parno}} = e^{-1} \begin{bmatrix} 0 & -1/3 \\ 3 & 0 \end{bmatrix}$ i $\Phi_{\mathrm{neparno}} = e^{-1} \begin{bmatrix} 0 & -3 \\ 1/3 & 0 \end{bmatrix}$. Njihov umnožak daje dijagonalnu matricu $\Phi_{\mathrm{cikl}} = e^{-2} \mathrm{diag}(-9, -1/9)$."

#### Pitanje 7.3: Može li sklopni sustav sastavljen od dva NESTABILNA moda prespajanjem postati stabilan?
*Kontekst:* Povezivanje dualnog fenomena sklopnih sustava (Predavanje 7).
> **Modelski odgovor studenta:**  
> "Da, apsolutno! Fenomen funkcionira i u suprotnom smjeru.  
> Kao što nepovoljno prespajanje stabilnih podsustava može destabilizirati sustav, tako i pažljivo projektirano prespajanje između dva nestabilna podsustava može rezultirati stabilnim sustavom.  
> Ključ je u tome da se prespajanje tempira u trenucima kada trajektorija prvog nestabilnog moda prolazi kroz regiju prostora stanja gdje drugi mod ima kontrakciju. Ako monodromijska matrica umnoška ima spektralni radijus $\rho(\Phi_{\mathrm{cikl}}) < 1$, zatvoreni sklopni sustav bit će eksponencijalno stabilan."

---

### ⚠️ Fatalne zablude i zamke u izvođenju

1. **Pokušaj dokazivanja stabilnosti preko zbira ili prosjeka svojstvenih vrijednosti:** Student tvrdi da je sustav stabilan jer je prosječna matrica $\frac{1}{2}(A_{\mathrm{par}} + A_{\mathrm{nep}})$ Hurwitzova. To je potpuno pogrešno: dinamika sklopnog sustava određena je umnoškom matričnih eksponenata, a ne prosjekom matrica!
2. **Pogrešan redoslijed množenja matrica prijelaza:** Pisanje $\Phi_{\mathrm{cikl}} = \Phi_{\mathrm{parno}} \Phi_{\mathrm{neparno}}$ umjesto $\Phi_{\mathrm{neparno}} \Phi_{\mathrm{parno}}$. Budući da sustav u prvom intervalu $t \in [0, 1)$ evoluira pod parnim modom, stanje na kraju ciklusa je $x(2) = \Phi_{\mathrm{neparno}} x(1) = \Phi_{\mathrm{neparno}} \Phi_{\mathrm{parno}} x(0)$. Matrice se primjenjuju s desna na lijevo!
3. **Miješanje determinirane nestabilnosti s kaosom:** Nestabilnost u Zadatku 4b nije kaos niti slučajni šum, već determinirana eksponencijalna divergencija linearne strukture po dijelovima sa strogom stopom rasta od $1.218$ po ciklusu.


---

# POGLAVLJE 8: Linearne matrične nejednakosti (LMI) i sinteza robusnog upravljanja

> **Sadržaj poglavlja:**  
> 8.1 First Principles Semidefinitnog programiranja (SDP) i Linearne Matrične Nejednakosti (LMI)  
> 8.2 Koncept zajedničke kvadratne Ljapunovljeve funkcije (CQLF)  
> 8.3 Problem bilinearne matrične nejednakosti (BMI) kod sinteze upravljanja  
> 8.4 Linearizacija: Transformacija kongruencije i supstitucija varijabli ($\mathcal{Q} = P^{-1}, Y = KP^{-1}$)  
> 8.5 Solverska implementacija u YALMIP-u: Eliminacija homogenosti i minimalno pojačanje ($\min \|Y\|_2$)  
> 8.6 Poopćeni problem svojstvenih vrijednosti (GEVP) i egzaktna stopa prigušenja $\alpha = 0.2884\,\mathrm{s}^{-1}$  
> 8.7 Simulacija zatvorenog kruga i elipsoidna kontrakcija (Slika 5.2 seminara)  
> 8.8 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori  

---

## 8.1 First Principles Semidefinitnog programiranja (SDP) i Linearne Matrične Nejednakosti (LMI)

U modernoj teoriji robusnog upravljanja, linearne matrične nejednakosti predstavljaju najmoćniji računski alat jer omogućuju rješavanje niza složenih inženjerskih problema (stabilizacija, $H_\infty$ vođenje, disipativnost, estimacija stanja) kroz standardne konveksne optimizacijske rješavače (prof. Jokić, Predavanje 6 i Predavanje 7).

### Što je linearna matrična nejednakost (LMI)?
> **Definicija 8.1 (LMI):**  
> Linearna matrična nejednakost je relacija oblika:
> $$F(x) := F_0 + \sum_{i=1}^m x_i F_i \succ 0 \quad (\text{ili } \succeq 0), \tag{8.1}$$
> gdje je $x = [x_1, \dots, x_m]^{\mathsf{T}} \in \mathbb{R}^m$ vektor skalarnih optimizacijskih varijabli, a $F_0, F_1, \dots, F_m \in \mathbb{S}^n$ su zadane konstantne simetrične matrice.

Ključno svojstvo:
Dozvoljeni skup varijabli definiran LMI-jem $\mathcal{F}_{\mathrm{LMI}} = \{x \in \mathbb{R}^m \mid F(x) \succ 0\}$ naziva se **spektroedar** i **uvijek je konveksan skup**.  
Problem minimizacije linearne funkcije nad spektroedrom naziva se **Semidefinitni Program (SDP)** i rješava se metodama unutrašnje točke u polinomijalnom vremenu.

---

## 8.2 Koncept zajedničke kvadratne Ljapunovljeve funkcije (CQLF)

U Poglavlju 7 vidjeli smo da sklopni sustav $\dot{x}(t) = A(t) x(t)$ sastavljen od dva stabilna moda divergira jer pojedinačne Ljapunovljeve funkcije $V_1(x) = x^{\mathsf{T}} P_1 x$ i $V_2(x) = x^{\mathsf{T}} P_2 x$ nisu međusobno usklađene.

Kako osigurati da sustav bude stabilan za **bilo koji** zakon prespajanja?

> **Teorem 8.1 (Zajednička kvadratna Ljapunovljeva funkcija - CQLF):**  
> Ako postoji **jedinstvena** simetrična pozitivno definitna matrica $P \succ 0$ takva da za sve dinamičke modove $i \in \{1, \dots, M\}$ vrijedi:
> $$A_i^{\mathsf{T}} P + P A_i \prec 0, \quad \forall i \in \{1, \dots, M\}, \tag{8.2}$$
> tada je skalarna funkcija:
> $$V(x) = x^{\mathsf{T}} P x \tag{8.3}$$
> **zajednička Ljapunovljeva funkcija** sustava.  
> Derivacija funkcije $V(x)$ duž trajektorija sustava strogo je negativna u svakom trenutku vremena $t$:
> $$\dot{V}(x(t)) = x^{\mathsf{T}}(t) \left[ A_i^{\mathsf{T}} P + P A_i \right] x(t) < 0, \quad \forall x(t) \neq 0,$$
> neovisno o tome koji je mod $i$ trenutno aktivan.  
> Sustav je tada **eksponencijalno stabilan za proizvoljno, po dijelovima neprekidno prespajanje** (*arbitrary switching*).

Za naš otvoreni sustav takva matrica $P$ nije postojala (zato je sustav i divergirao). Naš cilj u Zadatku 4c je **projektirati upravljanje koje će stvoriti zajedničku Ljapunovljevu funkciju**.

---

## 8.3 Problem bilinearne matrične nejednakosti (BMI) kod sinteze upravljanja

Uvodimo statičku povratnu vezu po stanju:
$$u(t) = K x(t), \qquad K = [k_1, k_2] \in \mathbb{R}^{1 \times 2}. \tag{8.4}$$
Uvrštavanjem upravljanja (8.4) u sustav $\dot{x} = A(t)x + Bu(t)$ dobivamo zatvoreni krug:
$$\dot{x}(t) = (A(t) + BK) x(t). \tag{8.5}$$

Matrice dinamike zatvorenog kruga za parni i neparni mod glase:
$$A_{\mathrm{cl}, \mathrm{par}} = A_{\mathrm{parno}} + BK, \qquad A_{\mathrm{cl}, \mathrm{nep}} = A_{\mathrm{neparno}} + BK. \tag{8.6}$$

Prema Teoremu 8.1, zatvoreni sustav bit će stabilan ako pronađemo matricu $P \succ 0$ i vektor pojačanja $K$ takve da vrijedi:
$$(A_i + BK)^{\mathsf{T}} P + P (A_i + BK) \prec 0, \quad i \in \{\mathrm{parno}, \mathrm{neparno}\}. \tag{8.7}$$

Rastavimo nejednakost (8.7):
$$A_i^{\mathsf{T}} P + P A_i + K^{\mathsf{T}} B^{\mathsf{T}} P + P B K \prec 0. \tag{8.8}$$

> 🔴 **FUNDAMENTALNI PROBLEM (BMI):**  
> Pogledajmo član $P B K$. U njemu se **optimizacijska matrica $P$ množi s optimizacijskim vektorom $K$**!  
> Nejednakost (8.8) sadrži umnožak dviju nepoznanica, što znači da je ona **bilinearna matrična nejednakost (BMI - Bilinear Matrix Inequality)**.  
> Skup točaka koji zadovoljava BMI općenito **nije konveksan**. Rješavanje općih BMI problema je NP-težak problem u kojem standardni LMI solveri ne mogu raditi!

---

## 8.4 Linearizacija: Transformacija kongruencije i supstitucija varijabli ($\mathcal{Q} = P^{-1}, Y = KP^{-1}$)

Kako riješiti ovaj problem? Koristimo matematički trik koji je temelj moderne teorije robusnog upravljanja: **transformaciju kongruencije** (prof. Jokić, Predavanje 7).

### Teorem o očuvanju definitnosti kongruencijom:
Za bilo koju simetričnu matricu $M \in \mathbb{S}^n$ i bilo koju regularnu matricu $T \in \mathbb{R}^{n \times n}$ ($\det T \neq 0$), matrica $T M T^{\mathsf{T}}$ ima identičan broj pozitivnih, negativnih i nultih svojstvenih vrijednosti kao matrica $M$ (Sylvesterov zakon inercije).  
Posebno vrijedi:
$$M \prec 0 \iff T M T^{\mathsf{T}} \prec 0. \tag{8.9}$$

Budući da tražimo matricu $P \succ 0$, njezin inverz $P^{-1}$ postoji, simetričan je i strogo pozitivno definitan ($P^{-1} \succ 0$).  
Odaberimo $T = P^{-1}$ i **pomnožimo nejednakost (8.8) s lijeva i s desna s $P^{-1}$**:
$$P^{-1} \left[ A_i^{\mathsf{T}} P + P A_i + K^{\mathsf{T}} B^{\mathsf{T}} P + P B K \right] P^{-1} \prec 0. \tag{8.10}$$

Raspisujemo član po član:
- $P^{-1} (A_i^{\mathsf{T}} P) P^{-1} = P^{-1} A_i^{\mathsf{T}} (P P^{-1}) = P^{-1} A_i^{\mathsf{T}}$.
- $P^{-1} (P A_i) P^{-1} = (P^{-1} P) A_i P^{-1} = A_i P^{-1}$.
- $P^{-1} (K^{\mathsf{T}} B^{\mathsf{T}} P) P^{-1} = P^{-1} K^{\mathsf{T}} B^{\mathsf{T}} (P P^{-1}) = P^{-1} K^{\mathsf{T}} B^{\mathsf{T}} = (K P^{-1})^{\mathsf{T}} B^{\mathsf{T}}$.
- $P^{-1} (P B K) P^{-1} = (P^{-1} P) B K P^{-1} = B (K P^{-1})$.

Uvrštavanjem natrag u (8.10) dobivamo:
$$A_i P^{-1} + P^{-1} A_i^{\mathsf{T}} + B (K P^{-1}) + (K P^{-1})^{\mathsf{T}} B^{\mathsf{T}} \prec 0. \tag{8.11}$$

### Supstitucija optimizacijskih varijabli:
Definirajmo nove optimizacijske varijable:
$$\mathcal{Q} := P^{-1} \in \mathbb{S}^2, \qquad \mathcal{Q} \succ 0, \tag{8.12a}$$
$$Y := K P^{-1} \in \mathbb{R}^{1 \times 2}. \tag{8.12b}$$

Uvrštavanjem (8.12) u relaciju (8.11) dobivamo:
$$A_i \mathcal{Q} + \mathcal{Q} A_i^{\mathsf{T}} + B Y + Y^{\mathsf{T}} B^{\mathsf{T}} \prec 0, \quad i \in \{\mathrm{parno}, \mathrm{neparno}\}. \tag{8.13}$$

>  **ČUDO LINEARIZACIJE:**  
> Pogledajmo izraz (8.13): nepoznanice su simetrična matrica $\mathcal{Q} \in \mathbb{S}^2$ i redak-vektor $Y \in \mathbb{R}^{1 \times 2}$.  
> U izrazu (8.13) **nigdje nema umnoška nepoznanica**! Nepoznanice $\mathcal{Q}$ i $Y$ ulaze potpuno **linearno (afino)**!  
> Nejednakost (8.13) je **čista Linearna Matrična Nejednakost (LMI)**!

Nakon što numerički odredimo rješenje $(\mathcal{Q}, Y)$, izvorni parametri sustava se **egzaktno rekonstruiraju**:
$$P = \mathcal{Q}^{-1}, \qquad K = Y P = Y \mathcal{Q}^{-1}. \tag{8.14}$$

---

## 8.5 Solverska implementacija u YALMIP-u: Eliminacija homogenosti i minimalno pojačanje ($\min \|Y\|_2$)

Postavljanje LMI problema u numerički solver (YALMIP + SDPT3) zahtijeva rješavanje dva inženjerska izazova:

### 1. Problem homogenosti i striktnih nejednakosti:
Nejednakost (8.13) je **homogena**: ako je par $(\mathcal{Q}, Y)$ dopustivo rješenje, tada je i skalirani par $(t\mathcal{Q}, tY)$ rješenje za bilo koji skalarni faktor $t > 0$, jer skaliranje s $t$ daje isti regulator:
$$K = (tY)(t\mathcal{Q})^{-1} = Y \mathcal{Q}^{-1}.$$
Također, numerički solveri ne mogu raditi sa strogim nejednakostima ($\prec 0, \succ 0$) jer dopustivi skup mora biti zatvoren.  
Zato uvodimo **usklađeni par normalizacija**:
$$\mathcal{Q} \succeq I, \tag{8.15a}$$
$$A_i \mathcal{Q} + \mathcal{Q} A_i^{\mathsf{T}} + B Y + Y^{\mathsf{T}} B^{\mathsf{T}} \preceq -I, \quad i \in \{\mathrm{parno}, \mathrm{neparno}\}. \tag{8.15b}$$

### 2. Kriterij minimalnog upravljačkog pojačanja ($\min \|Y\|_2$):
Problem dopustivosti ima beskonačno mnogo rješenja. Koje rješenje odabrati?  
U inženjerskoj praksi želimo regulator koji troši najmanje energije upravljanja i ne dovodi aktuatore u zasićenje. Zato minimiziramo normu vektora $Y$:
$$\min_{\mathcal{Q}, Y} \quad \|Y\|_2. \tag{8.16}$$

### YALMIP kod za sintezu:
```matlab
% Definiranje optimizacijskih varijabli
Q = sdpvar(2, 2); % Simetricna matrica 2x2
Y = sdpvar(1, 2); % Vektor pojacanja 1x2

% Postavljanje LMI ogranicenja
F = [Q >= eye(2)];
F = [F, A_par * Q + Q * A_par' + B * Y + Y' * B' <= -eye(2)];
F = [F, A_nep * Q + Q * A_nep' + B * Y + Y' * B' <= -eye(2)];

% Optimizacija minimalne norme pojacanja
options = sdpsettings('solver', 'sdpt3', 'verbose', 0);
optimize(F, norm(Y), options);

% Rekonstrukcija matrice P i regulatora K
Q_opt = value(Q);
Y_opt = value(Y);
P_opt = inv(Q_opt);
K_opt = Y_opt * P_opt;
```

### Numerički rezultati (izravno iz `task4_output.txt`):
Solver SDPT3 uspješno rješava problem (`Successfully solved (SDPT3)`):
- Matrica $\mathcal{Q}$:
  $$\mathcal{Q} = \begin{bmatrix} 1.354304 & -0.385757 \\ -0.385757 & 1.420003 \end{bmatrix}.$$
- Vektor $Y$:
  $$Y = \begin{bmatrix} -4.597618 & 1.172472 \end{bmatrix}.$$
- Rekonstruirana Ljapunovljeva matrica $P = \mathcal{Q}^{-1}$:
  $$P = \begin{bmatrix} 0.800314 & 0.217413 \\ 0.217413 & 0.763286 \end{bmatrix}, \qquad \lambda(P) = \{0.563600, 1.000000\}.$$
- **Optimalni vektor pojačanja regulatora $K$:**
  $$K = Y \mathcal{Q}^{-1} = \begin{bmatrix} -3.424629 & -0.104650 \end{bmatrix}. \tag{8.17}$$

---

## 8.6 Poopćeni problem svojstvenih vrijednosti (GEVP) i egzaktna stopa prigušenja $\alpha = 0.2884\,\mathrm{s}^{-1}$

Kako rigorozno odrediti brzinu smirivanja zatvorenog sustava?

Definirajmo Ljapunovljeve derivacijske matrice zatvorenog kruga:
$$M_i := (A_i + BK)^{\mathsf{T}} P + P (A_i + BK) \prec 0, \quad i \in \{\mathrm{par}, \mathrm{nep}\}.$$
Numerički proračun u MATLAB-u daje maksimalne svojstvene vrijednosti:
$$\lambda_{\max}(M_{\mathrm{par}}) = -0.910478 < 0, \qquad \lambda_{\max}(M_{\mathrm{nep}}) = -0.329090 < 0.$$

Derivacija zajedničke Ljapunovljeve funkcije glasi:
$$\dot{V}(x) = x^{\mathsf{T}} M_i x.$$
Tražimo maksimalnu stopu eksponencijalnog smirivanja $\alpha > 0$ takvu da vrijedi:
$$\dot{V}(x) \leq -2\alpha V(x) \iff x^{\mathsf{T}} M_i x \leq -2\alpha x^{\mathsf{T}} P x, \quad \forall x \neq 0. \tag{8.18}$$

Dijeljenjem s $x^{\mathsf{T}} P x > 0$ dobivamo Rayleigh-Ritzov kvocijent:
$$\frac{x^{\mathsf{T}} M_i x}{x^{\mathsf{T}} P x} \leq -2\alpha \iff \lambda_{\max}(M_i, P) \leq -2\alpha, \tag{8.19}$$
gdje je $\lambda(M_i, P)$ **poopćeni problem svojstvenih vrijednosti (GEVP)** definiran jednadžbom:
$$\det(M_i - \lambda P) = 0 \iff P^{-1} M_i v = \lambda v.$$

Uvrštavanjem u MATLAB dobivamo da je najnepovoljnija (najveća negativna) poopćena svojstvena vrijednost određena neparnim modom:
$$\max_i \lambda_{\max}(M_i, P) = -0.576748.$$
Izjednačavanjem s $-2\alpha$ dobivamo **egzaktnu stopu eksponencijalnog prigušenja**:
$$-2\alpha = -0.576748 \implies \mathbf{\alpha = 0.288374\,\mathrm{s}^{-1}}. \tag{8.20}$$

Integriranjem diferencijalne nejednakosti $\dot{V} \leq -2\alpha V$ slijedi:
$$V(x(t)) \leq V(x(0)) \cdot e^{-2\alpha t}. \tag{8.21}$$

### Ocjena euklidske norme stanja $\|x(t)\|_2$:
Kako je $\lambda_{\min}(P) \|x\|^2 \leq x^{\mathsf{T}} P x \leq \lambda_{\max}(P) \|x\|^2$, imamo:
$$\lambda_{\min}(P) \|x(t)\|^2 \leq V(x(t)) \leq e^{-2\alpha t} V(x(0)) \leq e^{-2\alpha t} \lambda_{\max}(P) \|x(0)\|^2.$$
Dijeljenjem s $\lambda_{\min}(P)$ i korjenovanjem dobivamo gornju među trajektorije:
$$\|x(t)\|_2 \leq \sqrt{\frac{\lambda_{\max}(P)}{\lambda_{\min}(P)}} e^{-\alpha t} \|x(0)\|_2 = \sqrt{\kappa(P)} \cdot e^{-\alpha t} \|x(0)\|_2, \tag{8.22}$$
gdje je uvjetovanost matrice $P$:
$$\kappa(P) = \frac{\lambda_{\max}(P)}{\lambda_{\min}(P)} = \frac{1.000000}{0.563600} = 1.774308 \implies \sqrt{\kappa(P)} = \mathbf{1.332031}.$$

Konačna inženjerska analitička ocjena glasi:
$$\|x(t)\|_2 \leq 1.3320 \cdot e^{-0.2884 t} \|x(0)\|_2. \tag{8.23}$$

> **Zašto je ova ocjena konzervativna?**  
> Ocjena sa stopom $\alpha = 0.2884\,\mathrm{s}^{-1}$ izvedena je za **proizvoljno, najgore moguće prespajanje** (*arbitrary switching*).  
> Kada sustav prespaja točno periodički svake sekunde, stvarna kontrakcija je dramatično brža!  
> Monodromijska matrica zatvorenog kruga iznosi $\Phi_{\mathrm{cl,cikl}} = e^{A_{\mathrm{cl,nep}}} e^{A_{\mathrm{cl,par}}}$, a njezin spektralni radijus iznosi:
> $$\rho(\Phi_{\mathrm{cl,cikl}}) = \mathbf{0.069720} \ll 1!$$
> To znači da se u stvarnoj periodičkoj simulaciji amplituda stanja smanjuje za više od **93% po svakom ciklusu**!

---

## 8.7 Simulacija zatvorenog kruga i elipsoidna kontrakcija (Slika 5.2 seminara)

Usporedba ponašanja otvorenog i zatvorenog kruga (iz `task4_output.txt`):
- **Otvoreni krug ($u = 0$):** $\|x(0)\| = 1.0 \implies \|x(20)\| = \mathbf{7.1868}$ (DIVERGENCIJA).
- **Zatvoreni krug ($u = Kx$):**  
  - $\|x(0)\| = 1.0000$
  - $\|x(5)\| = 1.5176 \times 10^{-3}$
  - $\|x(20)\| = \mathbf{4.7232 \times 10^{-12}}$ (POTPUNO SMIRIVANJE U ISHODIŠTE).

### Analiza Slike 5.2 (`fig4_2_closed_loop_stabilization.pdf`):
1. **Vremenski odziv:** Stanja $x_1(t)$ i $x_2(t)$ te upravljački signal $u(t) = Kx(t)$ eksponencijalno trnu i unutar prvih nekoliko sekundi postaju praktički nula.
2. **Fazni portret ($x_1$ vs. $x_2$):** Trajektorija zatvorenog kruga tvori spiralu koja se **munjevito uvija u ishodište**.
3. **Elipsoidi Ljapunovljeve funkcije:** Prikazani su koncentrični elipsoidi $x^{\mathsf{T}} P x = c$. Trajektorija u svakom trenutku siječe elipsoide izvana prema unutra, što grafički dokazuje da je $\dot{V} < 0$ u svakoj točki prostora stanja.

---

## 8.8 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori

### ❓ Tipična ispitna pitanja profesora na obrani

#### Pitanje 8.1: Zašto činjenica da su obje matrice zatvorenog kruga $(A_i + BK)$ Hurwitzove NIJE dovoljna za stabilnost, nego smo morali postavljati LMI?
*Kontekst:* Temeljno razumijevanje stabilnosti sklopnih sustava i uloge LMI-ja.
> **Modelski odgovor studenta:**  
> "Zato što Hurwitzovost matrica jamči asimptotsku stabilnost samo ako se sustav ne prespaja. Kao što smo dokazali u Zadatku 4b, otvoreni krug je divergirao iako su obje matrice bile Hurwitzove!  
> Zato puko traženje regulatora koji bi zasebno smjestio polove matrica u lijevu poluravninu ne jamči stabilnost pri prespajanju.  
> Jedino postojanje **zajedničke kvadratne Ljapunovljeve funkcije (CQLF)** $V(x) = x^{\mathsf{T}} P x$ s istom matricom $P \succ 0$ za oba moda jamči da energija sustava monotono opada duž trajektorija bez obzira na trenutak i frekvenciju prespajanja. To postojanje dokazuje se i rješava isključivo kroz sustav LMI-ja."

#### Pitanje 8.2: Zašto uvodite supstituciju $\mathcal{Q} = P^{-1}$ i $Y = K P^{-1}$ i kako se naziva ta matematička transformacija?
*Kontekst:* Matematički postupak linearizacije bilinearnosti.
> **Modelski odgovor studenta:**  
> "Izvorni Ljapunovljev uvjet $(A_i + BK)^{\mathsf{T}} P + P(A_i + BK) \prec 0$ sadrži nelinearni član $P B K$ u kojem se množe dvije optimizacijske nepoznanice ($P$ i $K$). Riječ je o bilinearnoj matričnoj nejednakosti (BMI), koja nije konveksna.  
> Kako bismo je linearizirali, provodimo **transformaciju kongruencije**: množimo nejednakost s lijeva i s desna regularnom simetričnom matricom $P^{-1} \succ 0$. Prema Sylvesterovom zakonu inercije, kongruencija čuva negativnu definitnost.  
> Uvođenjem supstitucije $\mathcal{Q} = P^{-1} \succ 0$ i $Y = K P^{-1}$, nelinearni član $P B K$ prelazi u $B Y$, čime nejednakost postaje afina (linearna) po novim varijablama $(\mathcal{Q}, Y)$. Riječ je o egzaktnoj konveksnoj reparametrizaciji bez gubitka točnosti."

#### Pitanje 8.3: Rješenje LMI-ja nije jedinstveno. Na temelju kojeg kriterija ste odabrali baš vektor pojačanja $K$?
*Kontekst:* Povezivanje matematičke optimizacije i inženjerskog projektiranja.
> **Modelski odgovor studenta:**  
> "LMI problem stabilizacije je problem dopustivosti i uz to je homogen.  
> Kako bismo uklonili numeričku neodređenost, prvo smo fiksirali skalu usklađenim parom normalizacija $\mathcal{Q} \succeq I$ i Ljapunovljeve nejednakosti $\preceq -I$.  
> Među svim dopustivim regulatorima odabrali smo onaj s **minimalnom euklidskom normom $\min \|Y\|_2$**, što odgovara regulatoru najmanjeg pojačanja (*low-gain feedback*). Inženjerski razlog je sprječavanje zasićenja aktuatora i minimalni utrošak upravljačke energije, što je dalo optimalni vektor $K = [-3.424629, -0.104650]$."

#### Pitanje 8.4: Odakle potječe stopa eksponencijalnog prigušenja $\alpha = 0.2884\,\mathrm{s}^{-1}$ i zašto je ona konzervativna u odnosu na simulirani odziv?
*Kontekst:* Analitički izvod stope prigušenja iz Ljapunovljeve funkcije.
> **Modelski odgovor studenta:**  
> "Stopa $\alpha$ potječe iz rješavanja poopćenog problema svojstvenih vrijednosti (GEVP) para $(M_i, P)$, gdje je $M_i = (A_i + BK)^{\mathsf{T}} P + P(A_i + BK) \prec 0$.  
> Iz odnosa $\dot{V} \leq -2\alpha V$ slijedi $-2\alpha = \max_i \lambda_{\max}(M_i, P)$, što daje $\alpha = 0.288374\,\mathrm{s}^{-1}$ i gornju među trajektorije $\|x(t)\| \leq \sqrt{\kappa(P)} e^{-\alpha t} \|x(0)\|$.  
> Ta ocjena je konzervativna jer vrijedi za **proizvoljno, najgore moguće prespajanje**. U našem sustavu prespajanje je točno periodičko sa sekundnim intervalima, gdje monodromijska matrica zatvorenog ciklusa ima spektralni radijus $\rho = 0.069720 \ll 1$, pa je stvarna kontrakcija stanja u simulaciji preko 93% po ciklusu, dakle znatno brža od teorijske gornje međe za najgori slučaj."

---

### ⚠️ Fatalne zablude i zamke u izvođenju

1. **Pogrešna rekonstrukcija pojačanja $K$:** Nakon rješavanja LMI-ja student izračuna $K = P Y$ umjesto $K = Y P = Y \mathcal{Q}^{-1}$. Budući da je $Y = K P^{-1}$, množenjem s $P$ s desne strane slijedi $K = Y P$. Zamjena redoslijeda množenja matrica daje potpuno pogrešan regulator koji destabilizira sustav!
2. **Postavljanje LMI-ja bez normalizacije:** Pokušaj rješavanja homogenog problema dopustivosti u YALMIP-u bez uvjeta $\mathcal{Q} \succeq I$. Solver može odlutati u numerički beskonačno velika ili beskonačno mala rješenja, što rezultira numeričkom nestabilnošću solvera (`Solver failed: ill-conditioned`).
3. **Miješanje svojstvenih vrijednosti zatvorenih matrica s Ljapunovljevom stopom:** Tvrdnja da je stopa prigušenja jednaka $\min |\mathrm{Re}(\lambda(A_{\mathrm{cl}}))|$. Kao što je više puta naglašeno, svojstvene vrijednosti matrica ne govore ništa o brzini smirivanja sklopnog sustava — mjerodavna je isključivo poopćena svojstvena vrijednost para $(M_i, P)$ ili spektralni radijus monodromijske matrice!


---

# POGLAVLJE 9: Schurov komplement, konična hijerarhija i napredno modeliranje

> **Sadržaj poglavlja:**  
> 9.1 Schurov komplement: Definicija, dokaz preko kongruencije i primjena  
> 9.2 Svođenje nelinearnih matričnih uvjeta na Linearne Matrične Nejednakosti (LMI)  
> 9.3 Hijerarhija konveksne optimizacije: $\mathrm{LP} \subset \mathrm{QP} \subset \mathrm{QCQP} \subset \mathrm{SOCP} \subset \mathrm{SDP}$  
> 9.4 Stožac drugog reda (SOCP) i robusna optimizacija pod elipsoidnim nesigurnostima  
> 9.5 Regularizacija u optimizaciji: $\ell_2$ (Tikhonov) vs. $\ell_1$ (LASSO i svojstvo rijetkosti)  
> 9.6 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori  

---

## 9.1 Schurov komplement: Definicija, dokaz preko kongruencije i primjena

Uz transformaciju kongruencije koju smo koristili u Zadatku 4, **Schurov komplement** je najčešće korišteni matematički alat na usmenom ispitu iz OMRiUS-a (prof. Jokić, Predavanje 6). On omogućuje da nelinearne matrične nejednakosti (npr. nejednakosti s inverzima ili kvadratnim članovima) egzaktno transformiramo u linearne matrične nejednakosti (LMI).

### Definicija Schurovog komplementa
Promotrimo simetričnu blok-matricu $M \in \mathbb{S}^{n+m}$ razdijeljenu na četiri bloka:
$$M = \begin{bmatrix} A & B \\ B^{\mathsf{T}} & C \end{bmatrix}, \tag{9.1}$$
gdje su $A \in \mathbb{S}^n$, $C \in \mathbb{S}^m$, a $B \in \mathbb{R}^{n \times m}$.

1. Ako je matrica $A$ regularna, matrica:
   $$S_A := C - B^{\mathsf{T}} A^{-1} B \in \mathbb{S}^m \tag{9.2}$$
   naziva se **Schurov komplement bloka $A$ u matrici $M$**.
2. Ako je matrica $C$ regularna, matrica:
   $$S_C := A - B C^{-1} B^{\mathsf{T}} \in \mathbb{S}^n \tag{9.3}$$
   naziva se **Schurov komplement bloka $C$ u matrici $M$**.

> **Teorem 9.1 (Teorem o Schurovom komplementu):**  
> Neka je matrica $M = \begin{bmatrix} A & B \\ B^{\mathsf{T}} & C \end{bmatrix}$ simetrična.  
> 1. Uz pretpostavku $A \succ 0$, vrijedi:
>    $$M \succ 0 \iff C - B^{\mathsf{T}} A^{-1} B \succ 0. \tag{9.4}$$
> 2. Uz pretpostavku $C \succ 0$, vrijedi:
>    $$M \succ 0 \iff A - B C^{-1} B^{\mathsf{T}} \succ 0. \tag{9.5}$$
> 3. Za semidefinitnost ($\succeq 0$): ako je $A \succ 0$, tada je:
>    $$M \succeq 0 \iff C - B^{\mathsf{T}} A^{-1} B \succeq 0. \tag{9.6}$$

### Elegantni dokaz preko transformacije kongruencije:
Zašto ovaj teorem vrijedi? Dokaz se temelji na blok-Gaussovoj eliminaciji:
Definirajmo donje-trokutastu blok-matricu:
$$T = \begin{bmatrix} I & 0 \\ -B^{\mathsf{T}} A^{-1} & I \end{bmatrix}.$$
Budući da je determinanta matrice $T$ jednaka $1$ ($\det T = \det(I)\det(I) = 1$), matrica $T$ je regularna za bilo koje matrice $A$ i $B$.

Provedimo transformaciju kongruencije matrice $M$ pomoću matrice $T$:
$$T M T^{\mathsf{T}} = \begin{bmatrix} I & 0 \\ -B^{\mathsf{T}} A^{-1} & I \end{bmatrix} \begin{bmatrix} A & B \\ B^{\mathsf{T}} & C \end{bmatrix} \begin{bmatrix} I & -A^{-1} B \\ 0 & I \end{bmatrix}.$$
Izmnožimo prve dvije matrice:
$$\begin{bmatrix} I & 0 \\ -B^{\mathsf{T}} A^{-1} & I \end{bmatrix} \begin{bmatrix} A & B \\ B^{\mathsf{T}} & C \end{bmatrix} = \begin{bmatrix} A & B \\ -B^{\mathsf{T}} + B^{\mathsf{T}} & -B^{\mathsf{T}} A^{-1} B + C \end{bmatrix} = \begin{bmatrix} A & B \\ 0 & C - B^{\mathsf{T}} A^{-1} B \end{bmatrix}.$$
Sada pomnožimo s $T^{\mathsf{T}}$ s desne strane:
$$\begin{bmatrix} A & B \\ 0 & C - B^{\mathsf{T}} A^{-1} B \end{bmatrix} \begin{bmatrix} I & -A^{-1} B \\ 0 & I \end{bmatrix} = \begin{bmatrix} A & -A A^{-1} B + B \\ 0 & C - B^{\mathsf{T}} A^{-1} B \end{bmatrix} = \begin{bmatrix} A & 0 \\ 0 & C - B^{\mathsf{T}} A^{-1} B \end{bmatrix}! \tag{9.7}$$

Matrica $T M T^{\mathsf{T}}$ je **blok-dijagonalna**!  
Prema Sylvesterovom zakonu inercije, kongruencija čuva definitnost:
$$M \succ 0 \iff T M T^{\mathsf{T}} \succ 0 \iff \begin{bmatrix} A & 0 \\ 0 & C - B^{\mathsf{T}} A^{-1} B \end{bmatrix} \succ 0.$$
Blok-dijagonalna matrica je strogo pozitivno definitna ako i samo ako je svaki njezin dijagonalni blok strogo pozitivno definitan:
$$A \succ 0 \quad \text{i} \quad C - B^{\mathsf{T}} A^{-1} B \succ 0. \quad \blacksquare$$

---

## 9.2 Svođenje nelinearnih matričnih uvjeta na Linearne Matrične Nejednakosti (LMI)

Schurov komplement je inženjerski "čarobni štapić" za pretvaranje nelinearnih uvjeta u LMI:

### 1. Kvadratna nejednakost po vektoru $x$:
Promotrimo konveksnu kvadratnu nejednakost:
$$x^{\mathsf{T}} P x + q^{\mathsf{T}} x + r \leq 0, \qquad P \succ 0.$$
Preuredimo:
$$-(q^{\mathsf{T}} x + r) - x^{\mathsf{T}} P x \geq 0 \iff -(q^{\mathsf{T}} x + r) - x^{\mathsf{T}} (P^{-1})^{-1} x \geq 0.$$
Prema Schurovom komplementu uz $A = P^{-1} \succ 0$, $B = x$, $C = -(q^{\mathsf{T}} x + r)$:
$$\begin{bmatrix} P^{-1} & x \\ x^{\mathsf{T}} & -(q^{\mathsf{T}} x + r) \end{bmatrix} \succeq 0. \tag{9.8}$$
Ova matrica je afina (linearna) po optimizacijskoj varijabli $x$!

### 2. Ograničenje matrične norme (Matrix Norm Constraint):
U robusnom upravljanju često želimo osigurati da je inducirana norma matrice sustava manja od zadanog broja $\gamma$:
$$\|A(x)\|_2 \leq \gamma \iff \lambda_{\max}(A(x)^{\mathsf{T}} A(x)) \leq \gamma^2 \iff \gamma I - \frac{1}{\gamma} A(x)^{\mathsf{T}} A(x) \succeq 0.$$
Primjenom Schurovog komplementa dobivamo ekvivalentni LMI:
$$\begin{bmatrix} \gamma I & A(x) \\ A(x)^{\mathsf{T}} & \gamma I \end{bmatrix} \succeq 0. \tag{9.9}$$
Upravo smo ovu relaciju iskoristili u Zadatku 4 za minimizaciju norme pojačanja $\min \|Y\|_2$!

---

## 9.3 Hijerarhija konveksne optimizacije: $\mathrm{LP} \subset \mathrm{QP} \subset \mathrm{QCQP} \subset \mathrm{SOCP} \subset \mathrm{SDP}$

Jedno od temeljnih teorijskih pitanja kolegija OMRiUS je **konična hijerarhija optimizacijskih problema** (prof. Jokić, Predavanje 6). Konveksni problemi organizirani su u ugniježđeni niz klasa, gdje svaka viša klasa strogo uključuje sve prethodne:

$$\boxed{\mathrm{LP}} \;\subset\; \boxed{\mathrm{QP}} \;\subset\; \boxed{\mathrm{QCQP}} \;\subset\; \boxed{\mathrm{SOCP}} \;\subset\; \boxed{\mathrm{SDP}}$$

```
+-------------------------------------------------------------------+
|               Semidefinite Programming (SDP)                      |
|  +-------------------------------------------------------------+  |
|  |       Second-Order Cone Programming (SOCP)                  |  |
|  |  +-------------------------------------------------------+  |  |
|  |  | Quadratically Constrained Quadratic Prog. (QCQP)      |  |  |
|  |  |  +-------------------------------------------------+  |  |  |
|  |  |  |          Quadratic Programming (QP)             |  |  |  |
|  |  |  |  +-------------------------------------------+  |  |  |  |
|  |  |  |  |       Linear Programming (LP)             |  |  |  |  |
|  |  |  |  +-------------------------------------------+  |  |  |  |
|  |  |  +-------------------------------------------------+  |  |  |
|  |  +-------------------------------------------------------+  |  |
|  +-------------------------------------------------------------+  |
+-------------------------------------------------------------------+
```

### Karakteristike pojedinih klasa:
1. **Linearno programiranje (LP):**  
   - Kriterij: linearan ($c^{\mathsf{T}} x$). Ograničenja: poliedarska ($Ax \leq b$).  
   - Primjer: Nivelacija ceste u Zadatku 3.
2. **Kvadratno programiranje (QP):**  
   - Kriterij: konveksan kvadratni ($\frac{1}{2} x^{\mathsf{T}} Q x + c^{\mathsf{T}} x$). Ograničenja: linearna ($Ax \leq b$).  
   - Primjer: Deterministički i robusni problem u Zadacima 1 i 2.
3. **Kvadratno ograničeno kvadratno programiranje (QCQP):**  
   - Kriterij: kvadratan. Ograničenja: konveksne kvadratne nejednakosti ($x^{\mathsf{T}} P_i x + q_i^{\mathsf{T}} x + r_i \leq 0$).
4. **Programiranje stošca drugog reda (SOCP - Second-Order Cone Programming):**  
   - Kriterij: linearan. Ograničenja: afine funkcije unutar Lorentzovog stožca: $\|A_i x + b_i\|_2 \leq c_i^{\mathsf{T}} x + d_i$.
5. **Semidefinitno programiranje (SDP):**  
   - Kriterij: linearan. Ograničenja: Linearne Matrične Nejednakosti ($F_0 + \sum x_i F_i \succeq 0$).  
   - Primjer: LMI sinteza robusnog upravljanja u Zadatku 4.

> 👑 **Zašto je SDP "kralj konveksne optimizacije"?**  
> Zato što se svaki LP, QP, QCQP i SOCP problem pomoću Schurovog komplementa može **egzaktno zapisati kao SDP**!  
> SDP je najopćenitija klasa konveksnih problema koja se još uvijek može rješavati u polinomijalnom vremenu pomoću algoritama unutrašnje točke.

---

## 9.4 Stožac drugog reda (SOCP) i robusna optimizacija pod elipsoidnim nesigurnostima

### Lorentzov stožac (Ice-cream cone)
Stožac drugog reda u $\mathbb{R}^{n+1}$ definira se kao:
$$\mathcal{K}_2^{n+1} := \left\{ (x, t) \in \mathbb{R}^n \times \mathbb{R} \;\middle|\; \|x\|_2 \leq t \right\}. \tag{9.10}$$
Geometrijski u $\mathbb{R}^3$, to je kružni stožac s vrhom u ishodištu nagnut pod $45^\circ$ u smjeru osi $t$.

### Veza s robusnim linearnim programiranjem (Predavanje 8)
U Poglavlju 4 vidjeli smo da poliedarska nesigurnost vodi na sustav determinističkih linearnih nejednakosti u vrhovima. Što ako je nesigurnost **elipsoidna**?

Neka je ograničenje $a^{\mathsf{T}} x \leq b$, gdje vektor parametara $a$ leži u elipsoidu nesigurnosti:
$$\mathcal{E} = \{a^0 + P u \mid \|u\|_2 \leq 1\}, \qquad P \succ 0.$$
Robusni pandan zahtijeva:
$$\sup_{a \in \mathcal{E}} a^{\mathsf{T}} x \leq b \iff (a^0)^{\mathsf{T}} x + \sup_{\|u\|_2 \leq 1} u^{\mathsf{T}} (P^{\mathsf{T}} x) \leq b.$$
Prema Cauchy-Schwarzovoj nejednakosti, maksimum linearne funkcije $u^{\mathsf{T}} v$ na jediničnoj euklidskoj kugli je točno euklidska norma $\|v\|_2$:
$$\sup_{\|u\|_2 \leq 1} u^{\mathsf{T}} (P^{\mathsf{T}} x) = \|P^{\mathsf{T}} x\|_2.$$
Prema tome, robusno ograničenje poprima oblik:
$$(a^0)^{\mathsf{T}} x + \|P^{\mathsf{T}} x\|_2 \leq b \iff \|P^{\mathsf{T}} x\|_2 \leq b - (a^0)^{\mathsf{T}} x. \tag{9.11}$$
Ovo je **točno ograničenje stošca drugog reda (SOCP)**!

> **Ispitni zaključak:**  
> - Robusni LP s **poliedarskom nesigurnošću** svodi se na **LP** (Zadatak 2).  
> - Robusni LP s **elipsoidnom nesigurnošću** svodi se na **SOCP**.

---

## 9.5 Regularizacija u optimizaciji: $\ell_2$ (Tikhonov) vs. $\ell_1$ (LASSO i svojstvo rijetkosti)

U inženjerskoj identifikaciji sustava i strojnom učenju često imamo preodređeni ili loše uvjetovani problem najmanjih kvadrata $\min \|Ax - b\|_2^2$. Kako bismo spriječili preprilagođavanje (*overfitting*) i nestabilnost inverza, uvodimo **funkciju regularizacije** $R(x)$:
$$\min_{x} \quad \|Ax - b\|_2^2 + \lambda R(x), \qquad \lambda > 0. \tag{9.12}$$

### 1. $\ell_2$-regularizacija (Tikhonov / Ridge regresija):
Odabir $R(x) = \|x\|_2^2 = \sum x_i^2$.
- Problem ostaje gladak kvadratni program:
  $$\min_x \quad x^{\mathsf{T}} (A^{\mathsf{T}} A + \lambda I) x - 2 b^{\mathsf{T}} A x + b^{\mathsf{T}} b.$$
- Analitičko rješenje:
  $$x^* = (A^{\mathsf{T}} A + \lambda I)^{-1} A^{\mathsf{T}} b. \tag{9.13}$$
- **Svojstvo:** Član $\lambda I$ dodaje se na dijagonalu matrice $A^{\mathsf{T}} A$, čime matrica zajamčeno postaje strogo pozitivno definitna ($A^{\mathsf{T}} A + \lambda I \succ 0$) i uklanja se loša uvjetovanost. Sve komponente vektora $x$ se ravnomjerno smanjuju prema nuli (*shrinkage*), ali **nijedna komponenta ne postaje točno nula**.

### 2. $\ell_1$-regularizacija (LASSO - Least Absolute Shrinkage and Selection Operator):
Odabir $R(x) = \|x\|_1 = \sum |x_i|$.
- Problem se svodi na konveksni program (ili QP uvođenjem pomoćnih varijabli).
- **Fundamentalno svojstvo rijetkosti (*Sparsity*):** Za razliku od $\ell_2$, $\ell_1$-regularizacija **prisiljava mnoge komponente vektora $x$ da postanu točno jednake nuli**!

### Geometrijski dokaz zašto $\ell_1$ generira rijetka rješenja:
Zamislimo problem u ravnini $(x_1, x_2)$:
- Nivo-krivulje funkcije najmanjih kvadrata $\|Ax - b\|_2^2$ su **elipse** sa središtem u točki najmanjih kvadrata $x_{\mathrm{LS}}$.
- Dopustivi skup $\ell_2$-norme $\{\|x\|_2 \leq t\}$ je **glatka kružnica**.
- Dopustivi skup $\ell_1$-norme $\{\|x\|_1 \leq t\}$ je **kockasti dijamant (rotirani kvadrat)** čiji se oštri vrhovi nalaze točno na koordinatnim osima ($x_1 = 0$ ili $x_2 = 0$).

Kada elipsa najmanjih kvadrata ekspandira iz svog središta prema van:
- Kružnicu ($\ell_2$) će gotovo sigurno dodirnuti u nekoj općenitoj točki gdje su obje komponente $x_1 \neq 0$ i $x_2 \neq 0$.
- Dijamant ($\ell_1$) ima izražene "šiljke" na koordinatnim osima. Elipsa će s ogromnom vjerojatnošću **prvo dotaknuti jedan od šiljaka dijamanta**!  
U toj točki dodira jedna od koordinata je **točno jednaka nuli** ($x_1^* = 0$ ili $x_2^* = 0$).

> 💡 **Inženjerska primjena:** LASSO automatski provodi **odabir parametara** (*feature selection*). U mehatronici i robotici, ako imamo 50 mogućih dinamičkih parametara modela, $\ell_1$-regularizacija će odabrati npr. 5 dominantnih koji stvarno utječu na dinamiku, a ostalih 45 postaviti točno na nulu!

---

## 9.6 Modul za pripremu usmene obrane: Ispitna pitanja, zamke i modelski odgovori

### ❓ Tipična ispitna pitanja profesora na obrani

#### Pitanje 9.1: Kako pomoću Schurovog komplementa dokazujete da je matrica $\begin{bmatrix} A & B \\ B^{\mathsf{T}} & C \end{bmatrix}$ pozitivno definitna?
*Kontekst:* Provjera poznavanja teorema o Schurovom komplementu.
> **Modelski odgovor studenta:**  
> "Matrica $M = \begin{bmatrix} A & B \\ B^{\mathsf{T}} & C \end{bmatrix}$ je strogo pozitivno definitna ($M \succ 0$) ako i samo ako je vodeći blok $A$ strogo pozitivno definitan ($A \succ 0$) i njegov Schurov komplement $S_A = C - B^{\mathsf{T}} A^{-1} B$ strogo pozitivno definitan ($S_A \succ 0$).  
> Ekvivalentno, ako krenemo od bloka $C$, $M \succ 0$ ako i samo ako je $C \succ 0$ i $S_C = A - B C^{-1} B^{\mathsf{T}} \succ 0$.  
> Dokaz se provodi transformacijom kongruencije pomoću donje-trokutaste matrice $T = \begin{bmatrix} I & 0 \\ -B^{\mathsf{T}} A^{-1} & I \end{bmatrix}$, koja matricu $M$ svodi na blok-dijagonalni oblik $\mathrm{diag}(A, C - B^{\mathsf{T}} A^{-1} B)$, čime se definitnost izravno prenosi."

#### Pitanje 9.2: Kako glasi hijerarhija konveksnih optimizacijskih problema i zašto je SDP najopćenitiji?
*Kontekst:* Poznavanje klasifikacije konveksne optimizacije.
> **Modelski odgovor studenta:**  
> "Hijerarhija ugniježđenih klasa glasi: $\mathrm{LP} \subset \mathrm{QP} \subset \mathrm{QCQP} \subset \mathrm{SOCP} \subset \mathrm{SDP}$.  
> Svaka prethodna klasa je strogi podskup sljedeće:  
> - LP ima linearni kriterij i poliedarska ograničenja.  
> - QP uvodi konveksni kvadratni kriterij.  
> - QCQP dopušta i konveksna kvadratna ograničenja.  
> - SOCP dopušta ograničenja euklidske norme afinih funkcija (stožac drugog reda).  
> - SDP postavlja matrične nejednakosti (LMI) nad stošcem pozitivno semidefinitnih matrica $\mathbb{S}_+^n$.  
> SDP je najopćenitiji jer se svako skalarno i vektorsko ograničenje iz prethodnih klasa može preko Schurovog komplementa zapisati kao blok-dijagonalni LMI."

#### Pitanje 9.3: Zašto $\ell_1$-regularizacija (LASSO) generira rijetka rješenja (sparsity), a $\ell_2$-regularizacija (Tikhonov) ne?
*Kontekst:* Geometrijska i inženjerska interpretacija regularizacije.
> **Modelski odgovor studenta:**  
> "Razlika leži u geometriji nivo-ploha funkcija regularizacije.  
> Nivo-plohe $\ell_2$-norme su glatke euklidske sfere (kružnice). Prilikom dodira s elipsoidima funkcije pogreške, točka dodira se gotovo sigurno nalazi na glatkom dijelu sfere gdje su sve komponente različite od nule.  
> Nivo-plohe $\ell_1$-norme su poliedri (dijamanti / unakrsni politopi) koji posjeduju **oštre vrhove smještene točno na koordinatnim osima**. Zbog te geometrije, elipsoid pogreške pri ekspanziji prvo dodiruje jedan od vrhova politopa. U vrhu se jedna ili više optimizacijskih varijabli poništava, što rezultira egzaktnim nulama u vektoru rješenja."

---

### ⚠️ Fatalne zablude i zamke u izvođenju

1. **Zaboravljanje uvjeta $A \succ 0$ u Schurovom komplementu:** Student napiše da je $M \succ 0 \iff C - B^{\mathsf{T}} A^{-1} B \succ 0$, bez provjere je li $A \succ 0$. Ako je $A$ negativno definitna, Schurov komplement može biti pozitivan, ali matrica $M$ je indefinitna!
2. **Pogrešan redoslijed faktora u Schurovom komplementu:** Pisanje $B A^{-1} B^{\mathsf{T}}$ umjesto $B^{\mathsf{T}} A^{-1} B$. Ako je $A \in \mathbb{S}^n$ i $B \in \mathbb{R}^{n \times m}$, matrica $A^{-1}$ ima dimenziju $n \times n$. Kako bi umnožak bio dimenzija $m \times m$ (kao matrica $C$), mora se množiti $B^{\mathsf{T}} (m \times n)$ s $A^{-1} (n \times n)$ i $B (n \times m)$!
3. **Miješanje LASSO i Ridge regresije:** Tvrdnja da Tikhonovljeva regularizacija izbacuje nepotrebne varijable. Tikhonovljeva regularizacija samo smanjuje njihove iznose (nikada ih ne postavlja na egzaktne nule). Isključivo $\ell_1$-norma (LASSO) provodi selekciju varijabli.


---

# POGLAVLJE 10: Vodič za usmenu obranu — "Face-to-Face s ispitivačem"

> **Sadržaj poglavlja:**  
> 10.1 Matrica brzih odgovora: 25 zlatnih ispitnih pitanja u 3 inženjerske rečenice  
> 10.2 Katalog fatalnih studentskih zabluda (Top 15 Pitfalls na usmenom ispitu)  
> 10.3 Protokol obrane seminara v1.2: Vodič kroz interpretaciju svih 7 slika rada  
> 10.4 Strategija i psihologija usmene obrane pred profesorom Jokićem  

---

## 10.1 Matrica brzih odgovora: 25 zlatnih ispitnih pitanja u 3 inženjerske rečenice

Ova matrica služi za završno ponavljanje neposredno prije ulaska u kabinet. Svaki odgovor formuliran je po pravilu **"Zlatne tri rečenice"**:
1. *Definicija / Izravan odgovor na pitanje.*
2. *Matematički dokaz ili mehanizam.*
3. *Fizikalno / inženjersko značenje.*

---

### CJELINA 1: KONVEKSNOST I FORMULACIJA PROBLEMA
1. **Zašto je konveksnost ključna u inženjerskoj optimizaciji?**  
   - Kod konveksnih problema svaki lokalni minimum je nužno i globalni minimum, pa algoritmi ne mogu zapeti u subverzivnim lokalnim ekstremima.  
   - Matematički se dokazuje preko uvjeta prvog reda $f(y) \geq f(x) + \nabla f(x)^{\mathsf{T}}(y-x)$ i konveksnosti dopustivog skupa.  
   - Inženjerski, to jamči pouzdanost i ponovljivost rješenja u polinomijalnom vremenu primjenom metoda unutrašnje točke.

2. **Koji je nužan i dovoljan uvjet da funkcija iz klase $C^2$ bude strogo konveksna?**  
   - Uvjet je da njezina Hesseova matrica drugih parcijalnih derivacija bude strogo pozitivno definitna ($\nabla^2 f(x) \succ 0$) u svakoj točki domene.  
   - To je ekvivalentno zahtjevu da su sve svojstvene vrijednosti Hesseove matrice strogo veće od nule ($\lambda_i > 0$).  
   - Za kvadratnu funkciju $f(x) = \frac{1}{2}x^{\mathsf{T}} Q x + c^{\mathsf{T}} x$ to znači $Q \succ 0$, što jamči postojanje jedinstvene točke minimuma.

3. **Kako glasi Slaterov uvjet kvalifikacije ograničenja?**  
   - Za konveksan problem, Slaterov uvjet zahtijeva postojanje barem jedne točke u relativnoj unutrašnjosti koja strogo zadovoljava sva nelinearna ograničenja nejednakosti ($g_i(x) < 0$).  
   - Ako su sva ograničenja afina ($Gx \leq h$), Slaterov uvjet se reducira na običnu dopustivost postojanja točke $Gx < h$.  
   - Njegovo ispunjenje jamči jaku dualnost ($d^* = p^*$, nulti dualni procjep) i nužnost i dovoljnost KKT uvjeta.

4. **Što znači ako je Hesseova matrica $Q$ samo pozitivno semidefinitna ($Q \succeq 0$), a $\det Q = 0$?**  
   - To znači da je najmanja svojstvena vrijednost jednaka nuli ($\lambda_{\min} = 0$), pa funkcija u tom smjeru nema zakrivljenost.  
   - Nivo-krivulje prestaju biti elipse i postaju parabolički žlijebovi (cilindri).  
   - Minimum više ne mora biti jedinstven (može biti čitav pravac točaka), a ako dopustivi skup dopušta gibanje duž žlijeba, problem može biti neograničen odozdo ($p^* = -\infty$).

5. **Zašto se Hesseova matrica kvadratne forme uvijek mora simetrizirati?**  
   - Kvadratna forma $x^{\mathsf{T}} M x$ identički je jednaka formi njezina simetričnog dijela jer antisimetrični dio uvijek daje nulu.  
   - Međutim, samo simetrična matrica $Q = \frac{1}{2}(M + M^{\mathsf{T}})$ ima realne svojstvene vrijednosti koje točno opisuju zakrivljenost prostora.  
   - Schwarzov teorem o jednakosti mješovitih parcijalnih derivacija nalaže da je pravi Hessian uvijek simetrična matrica.

---

### CJELINA 2: KKT UVJETI I OPTIMALNOST
6. **Koja su četiri temeljna stupa KKT uvjeta?**  
   - To su: stacionarnost ($\nabla f + \sum \mu_i \nabla g_i = 0$), primarna dopustivost ($g_i(x) \leq 0$), dualna dopustivost ($\mu_i \geq 0$) i komplementarno popuštanje ($\mu_i g_i(x) = 0$).  
   - Za konveksne probleme uz Slaterov uvjet, oni su nužni i dovoljni za globalnu optimalnost.  
   - Fizikalno predstavljaju ravnotežu sila potencijalnog polja i reakcija jednostranih krutih veza.

7. **Što fizikalno predstavlja uvjet komplementarnog popuštanja ($\mu_i g_i(x) = 0$)?**  
   - Predstavlja princip da veza ne može proizvoditi silu reakcije ako sustav fizički ne dodiruje granicu.  
   - Ako je ograničenje neaktivno ($g_i(x) < 0$), sustav je u unutrašnjosti pa je reakcija nužno nula ($\mu_i = 0$).  
   - Sila reakcije ($\mu_i > 0$) može postojati isključivo na samom rubu ($g_i(x) = 0$), čime se eliminira "djelovanje sile na daljinu".

8. **Zašto Lagrangeovi množitelji nejednakosti moraju biti nenegativni ($\mu_i \geq 0$)?**  
   - Zato što ograničenja nejednakosti $g_i(x) \leq 0$ predstavljaju jednostrane veze (zidove) koje sustav smiju samo gurati natrag u dopustivo područje.  
   - Budući da vektor $\nabla g_i$ pokazuje prema van, vektor reakcije $-\mu_i \nabla g_i$ mora pokazivati prema unutra, što zahtijeva $\mu_i \geq 0$.  
   - Negativan množitelj značio bi da zid privlači sustav (ponaša se kao ljepljiva traka), što je fizikalno nedopustivo.

9. **Zašto ste u Zadatku 1 odbacili Slučaj 4 (sjecište oba ograničenja) iako su oba zadovoljena?**  
   - U sjecištu $x = (6.5, 3.5)$ uvjet stacionarnosti daje množitelje $\mu_1 = 11.50$ i $\mu_2 = -2.45$.  
   - Multiplikator $\mu_2 < 0$ grubo narušava uvjet dualne dopustivosti.  
   - Geometrijski, gradijent funkcije cilja ima negativan skalarni produkt s unutarnjom normalom $-\nabla g_2$, što dokazuje da funkcija cilja strogo opada kretanjem duž pravca $g_1 = 0$ prema unutrašnjosti skupa $g_2 < 0$.

10. **Što geometrijski predstavlja optimalna točka Zadatka 1 na Slici 2.1?**  
    - Točka $x^* = (190/33, 140/33)$ predstavlja točku u kojoj nivo-elipsa funkcije cilja $f(x) = 60.606$ tangira pravac $x_1 + x_2 = 10$.  
    - Gradijent funkcije cilja $\nabla f(x^*)$ i gradijent ograničenja $\nabla g_1$ su strogo kolinearni i suprotnog smjera: $\nabla f(x^*) = -\mu_1^* \nabla g_1$.  
    - Drugo ograničenje leži na udaljenosti od $1.4848\,\mathrm{m}$ i ne utječe na ravnotežu.

---

### CJELINA 3: DUALNOST I OSJETLJIVOST
11. **Što je Lagrangeova dualna funkcija i koje je njezino ključno svojstvo?**  
    - Dualna funkcija je $\theta(\mu) = \inf_x \mathcal{L}(x, \mu)$, odnosno infimum Lagrangiana po primarnim varijablama.  
    - Njezino ključno svojstvo je da je **uvijek konkavna**, bez obzira na konveksnost primarnog problema, jer je definirana kao infimum familije afinih funkcija.  
    - Ona daje zajamčenu donju granicu optimalne vrijednosti primarnog problema ($\theta(\mu) \leq p^*$).

12. **Kako glasi teorem slabe dualnosti i što je dualni procjep?**  
    - Teorem slabe dualnosti tvrdi da je optimalna vrijednost dualnog problema uvijek manja ili jednaka primarnoj: $d^* \leq p^*$.  
    - Razlika $p^* - d^* \geq 0$ naziva se dualni procjep (*duality gap*).  
    - Za konveksne probleme uz Slaterov uvjet procjep je točno nula ($d^* = p^*$), što nazivamo jakom dualnošću.

13. **Zašto je dualni problem kvadratnog programa ponovno kvadratni program?**  
    - Zato što analitičkim izjednačavanjem $\nabla_x \mathcal{L} = 0$ dobivamo stacionarnu točku $x(\mu) = -Q^{-1}(c + G^{\mathsf{T}}\mu)$ koja je linearna u $\mu$.  
    - Uvrštavanjem tog izraza u Lagrangian, funkcija $\theta(\mu)$ poprima kvadratni oblik s negativno semidefitnom matricom $-G Q^{-1} G^{\mathsf{T}}$.  
    - Maksimizacija takve konkavne funkcije uz $\mu \geq 0$ identična je standardnom QP problemu minimizacije.

14. **Kako se matematički i inženjerski tumači "cijena u sjeni" (Shadow Price)?**  
    - Cijena u sjeni je parcijalna derivacija optimalne vrijednosti po perturbaciji ograničenja: $\frac{\partial p^*}{\partial v_i} = -\mu_i^*$.  
    - Predznak minus znači da popuštanje ograničenja ($v_i > 0$) smanjuje trošak sustava.  
    - Inženjerski predstavlja granični trošak resursa ili intenzitet naprezanja veze u radnoj točki.

15. **Zašto perturbacija $v_2$ u Zadatku 1 ima nultu osjetljivost?**  
    - Zato što je ograničenje $g_2$ neaktivno ($g_2(x^*) = -1.4848 < 0$), pa je njegov množitelj $\mu_2^* = 0$.  
    - To je **strogo lokalno svojstvo** koje vrijedi sve dok je pomak granice manji od rezerve od $1.4848\,\mathrm{m}$.  
    - Ako perturbacija prijeđe rezervu, ograničenje postaje aktivno i derivacija prestaje biti nula.

---

### CJELINA 4: ROBUSNOST I NESIGURNOST
16. **Zašto formulacija robusnog QP-a preko 8 vrhova nije konzervativna, već egzaktna?**  
    - Zato što je skup nesigurnosti konveksan poliedar (pravokutnik), a funkcija ograničenja je strogo linearna po nesigurnim parametrima $a_i$.  
    - Maksimum linearne funkcije na konveksnoj ljusci uvijek se postiže u nekom od njezinih vrhova.  
    - Zadovoljenje nejednakosti u svim vrhovima nužno i dovoljno povlači zadovoljenje za čitav skup, pa nema relaksacijskog procjepa.

17. **Zašto je nominalno rješenje Zadatka 1 u Monte Carlo simulaciji palo u čak 54% slučajeva?**  
    - Nominalni optimum nalazi se na samom rubu nominalnog dopustivog skupa bez ikakve sigurnosne margine.  
    - Pod utjecajem uniformnih varijacija od $\pm 15\%$, u 54% slučajeva stvarni koeficijenti pomiču granicu preko nominalne točke.  
    - To demonstrira inženjersku krhkost determinističke optimizacije i nužnost robusnog pristupa.

18. **Što predstavlja "cijena robusnosti" i kolika je u Zadatku 2?**  
    - Cijena robusnosti je relativni porast funkcije troška pri prelasku s nominalnog na robusno rješenje.  
    - U Zadatku 2 ona iznosi točno $+39.63\%$ (porast troška s $60.61$ na $84.62$).  
    - Inženjerski, to je premija osiguranja kojom kupujemo 100% pouzdanost i nultu stopu otkaza sustava.

---

### CJELINA 5: LINEARNO PROGRAMIRANJE I DISKRETIZACIJA
19. **Zašto diskretizirani kriterij $J^*$ RASTE pri zgušnjavanju mreže sa $N=20$ na $N=100$?**  
    - Diskretna suma je pravokutna numerička kvadratura kontinuiranog integrala zemljanih radova.  
    - Na rijetkoj mreži ($N=20$) valoviti dijelovi terena između čvorova izmiču uzorkovanju, pa rijetka mreža podcjenjuje stvarni integral za red $O(\Delta x)$.  
    - Gušća mreža finije integrira površinu i konvergira odozdo prema pravoj kontinuiranoj vrijednosti (+2.60% za slučaj A).

20. **Zašto u tablici Zadatka 3 nema zasebnih stupaca za kubature iskopa i nasipa?**  
    - Linearni program nivelacije je matematički degeneriran jer funkcija cilja penalizira samo ukupnu sumu odstupanja.  
    - Postoji čitava familija različitih optimalnih profila nivelete s identičnim ukupnim troškom $J^*$, ali različitom podjelom na iskop i nasip.  
    - Različiti solverski algoritmi daju različite podjele, pa bi navođenje pojedinačnih kubatura bilo proizvoljno i numerički neopravdano.

21. **Koje je dinamičko značenje ograničenja na drugu derivaciju nivelete ceste ($b_2$)?**  
    - Druga derivacija predstavlja vertikalnu zakrivljenost nivelete $\kappa(x) \approx y''(x)$.  
    - Pri vožnji brzinom $v_0$ na putnike djeluje vertikalno centrifugalno ubrzanje $a_z = v_0^2 y''(x)$.  
    - Ograničenje $|y''| \leq b_2$ osigurava dinamičku udobnost i sprječava opasno "odvajanje od sjedala" na grebenima ili preopterećenje ovjesa u udolinama.

---

### CJELINA 6: SKLOPNI SUSTAVI I LMI SINTEZA
22. **Zašto sklopni sustav divergira u otvorenom krugu iako su oba moda Hurwitzova?**  
    - Hurwitzovost jamči stabilnost samo ako sustav ne prespaja; kod periodičkog prespajanja stabilnost određuje monodromijska matrica ciklusa $\Phi_{\mathrm{cikl}} = e^{A_{\mathrm{nep}}} e^{A_{\mathrm{par}}}$.  
    - U našem slučaju je $\Phi_{\mathrm{cikl}} = e^{-2} \mathrm{diag}(-9, -1/9)$, pa je spektralni radijus $\rho = 9 e^{-2} \approx 1.218 > 1$.  
    - Neusklađenost elipsoida energije dvaju modova djeluje kao parametarska rezonancija koja na svakom skoku ubacuje energiju u sustav.

23. **Zašto je za stabilizaciju sklopnog sustava nužno tražiti zajedničku Ljapunovljevu funkciju (CQLF)?**  
    - Postojanje zasebnih funkcija $V_1$ i $V_2$ ne jamči pad energije pri preskoku s jednog moda na drugi.  
    - Jedino postojanje jedinstvene matrice $P \succ 0$ osigurava da skalarna energija $V(x) = x^{\mathsf{T}} P x$ monotono opada duž trajektorija oba moda.  
    - To jamči stabilnost za proizvoljno, pa i najgore moguće prespajanje.

24. **Kako je bilinearna matrična nejednakost (BMI) prevedena u linearnu (LMI)?**  
    - Izvorni uvjet $(A_i + BK)^{\mathsf{T}} P + P(A_i + BK) \prec 0$ sadrži nelinearni umnožak nepoznanica $P B K$.  
    - Provedena je transformacija kongruencije množenjem s $P^{-1} \succ 0$ s lijeva i desna, što čuva definitnost.  
    - Uvođenjem supstitucije $\mathcal{Q} = P^{-1}$ i $Y = K P^{-1}$, član prelazi u linearni oblik $B Y$, čime problem postaje egzaktni konveksni LMI.

25. **Kako glasi teorem o Schurovom komplementu i zašto je važan?**  
    - Za blok-matricu $M = \begin{bmatrix} A & B \\ B^{\mathsf{T}} & C \end{bmatrix}$ uz $A \succ 0$ vrijedi $M \succ 0 \iff C - B^{\mathsf{T}} A^{-1} B \succ 0$.  
    - Dokazuje se transformacijom kongruencije pomoću donje-trokutaste matrice eliminacije.  
    - Omogućuje svođenje nelinearnih matričnih uvjeta, normi i kvadratnih nejednakosti na linearne matrične nejednakosti (LMI).

---

## 10.2 Katalog fatalnih studentskih zabluda (Top 15 Pitfalls na usmenom ispitu)

| # | Fatalna zabluda studenta | Egzaktna inženjerska i matematička istina |
| :---: | :--- | :--- |
| **1** | *"Točka na sjecištu oba ograničenja u Zadatku 1 je optimum jer zadovoljava $g_1=0$ i $g_2=0$."* | **NETOČNO.** U sjecištu je multiplikator $\mu_2 = -2.45 < 0$, što krši dualnu dopustivost. Funkcija cilja opada kretanjem prema unutrašnjosti $g_2 < 0$. |
| **2** | *"Ako su sve svojstvene vrijednosti pojedinih podsustava u lijevoj poluravnini, sklopni sustav je stabilan."* | **NETOČNO.** Spektralni radijus umnoška matrica $\rho(AB)$ općenito nije jednak $\rho(A)\rho(B)$. Monodromijska matrica može imati $\rho > 1$ i divergirati. |
| **3** | *"Manji $J^*$ na rijetkoj mreži ($N=20$) dokazuje da je rijetka mreža dala bolje rješenje od $N=100$."* | **NETOČNO.** Rijetka mreža je pravokutnom kvadraturom grubo podcijenila integral za red $O(\Delta x)$. Zgušnjavanjem mreže računamo stvarni integral. |
| **4** | *"Robusna optimizacija nad 8 vrhova je konzervativna procjena stvarnog stanja."* | **NETOČNO.** Budući da je ograničenje linearno u parametrima, maksimum na poliedru se egzaktno dostiže u vrhu. Nema nikakvog konzervatizma. |
| **5** | *"Derivacija osjetljivosti je $\frac{\partial p^*}{\partial v} = +\mu^*$."* | **NETOČNO.** Derivacija ima predznak minus ($-\mu^*$) jer popuštanje ograničenja ($v > 0$) širi dopustivi skup i smanjuje optimalni trošak. |
| **6** | *"Kvadratna forma $x^{\mathsf{T}} M x$ s nesimetričnom matricom $M$ ispituje se preko svojstvenih vrijednosti matrice $M$."* | **NETOČNO.** Kvadratna forma ovisi samo o simetričnom dijelu $Q = \frac{1}{2}(M + M^{\mathsf{T}})$. Svojstvene vrijednosti nesimetrične matrice daju krive zaključke o konveksnosti. |
| **7** | *"U Zadatku 3 možemo jednoznačno očitati kubature iskopa i nasipa."* | **NETOČNO.** Linearni program nivelacije je degeneriran. Postoji čitava familija profila s istim $J^*$ i različitim omjerima iskopa i nasipa. |
| **8** | *"Nakon LMI sinteze pojačanje regulatora računa se kao $K = P Y$."* | **NETOČNO.** Supstitucija je bila $Y = K P^{-1}$, pa množenjem s $P$ s desne strane slijedi $K = Y P = Y \mathcal{Q}^{-1}$. |
| **9** | *"Lagrangeova dualna funkcija $\theta(\mu)$ je konveksna ako je primar konveksan."* | **NETOČNO.** Dualna funkcija $\theta(\mu)$ je **uvijek konkavna**, bez obzira na konveksnost primara, jer je infimum familije afinih funkcija. |
| **10** | *"Slaterov uvjet služi za dokazivanje lokalne optimalnosti."* | **NETOČNO.** Slaterov uvjet služi za kvalifikaciju ograničenja, jamči nestanak dualnog procjepa ($d^* = p^*$, jaka dualnost) i dovoljnost KKT uvjeta. |
| **11** | *"Stopa prigušenja sklopnog sustava $\alpha$ jednaka je najmanjoj realnoj svojstvenoj vrijednosti zatvorenih matrica."* | **NETOČNO.** Svojstvene vrijednosti pojedinih matrica ne određuju brzinu smirivanja; $\alpha = 0.2884$ računa se iz poopćenog svojstvenog problema para $(M_i, P)$. |
| **12** | *"Tikhonovljeva regularizacija izbacuje parametre koji nisu važni za model."* | **NETOČNO.** $\ell_2$-regularizacija samo ravnomjerno smanjuje parametre. Isključivo $\ell_1$-regularizacija (LASSO) postavlja parametre na egzaktne nule. |
| **13** | *"Ograničenje $g_2$ u Zadatku 1 možemo trajno izbrisati iz modela jer je njegova osjetljivost nula."* | **NETOČNO.** Nulta osjetljivost vrijedi samo lokalno dok je perturbacija manja od rezerve $1.4848$. Veća promjena aktivira ograničenje. |
| **14** | *"Schurov komplement glasi $S = C - B A^{-1} B^{\mathsf{T}}$."* | **NETOČNO.** Blok $B$ je dimenzija $n \times m$, pa mora biti $B^{\mathsf{T}} (m \times n) \cdot A^{-1} (n \times n) \cdot B (n \times m) = S (m \times m)$. |
| **15** | *"Monte Carlo simulacija rješava robusni problem optimizacije."* | **NETOČNO.** Monte Carlo služi isključivo za naknadnu statističku verifikaciju rješenja. Robusno rješenje dobiva se determinističkim rješavanjem 8 nejednakosti. |

---

## 10.3 Protokol obrane seminara v1.2: Vodič kroz interpretaciju svih 7 slika rada

Kada profesor na obrani otvori seminar i pokaže prstom na sliku, student mora unutar 5 sekundi započeti strukturirano izlaganje:

### Slika 1: `fig1_1_qp_primal_geometry.pdf` (Zadatak 1c)
- **Što prikazuje:** Geometriju primarnog problema u ravnini $(x_1, x_2)$.
- **Ključni elementi:**
  - Nagnute elipse predstavljaju nivo-krivulje funkcije cilja $f(x) = \mathrm{const}$.
  - Plavi šrafirani poliedar je dopustivi skup $\mathcal{F}$ definiran presjekom poluprostora $g_1 \leq 0$ i $g_2 \leq 0$.
  - Crvena točka je optimum $x^* = (5.7576, 4.2424)$.
  - Vektor $\nabla f(x^*)$ (crveni) i vektor $-\mu_1 \nabla g_1$ (zeleni) leže na istom pravcu i savršeno se poništavaju.
- **Poanta za profesora:** *"Slika dokazuje da je aktivno samo prvo ograničenje te da nivo-elipsa glatko tangira granicu $g_1 = 0$, dok je granica $g_2 = 0$ udaljena za iznos rezerve od $1.4848$."*

### Slika 2: `fig2_1_robust_envelope_monte_carlo.pdf` (Zadatak 2)
- **Što prikazuje:** Anvelopu nesigurnosti i položaj nominalnog naspram robusnog optimuma.
- **Ključni elementi:**
  - Gusti sivi snop pravaca prikazuje 100 slučajnih realizacija granica iz Monte Carlo simulacije ($\pm 15\%$).
  - Crna točka je nominalni optimum $x_{\mathrm{nom}}^*$, a crvena točka je robusni optimum $x_{\mathrm{rob}}^* = (6.5, 5.2647)$.
- **Poanta za profesora:** *"Vidljivo je da nominalna točka leži unutar sivog pojasa nesigurnosti, pa je sivi pravci presijecaju u 54% slučajeva. Robusna točka potisnuta je na vanjski rub anvelope (sjecište najnepovoljnijih vrhova 1 i 7), čime je postignuta nulta stopa kršenja uz cijenu robusnosti od +39.63%."*

### Slike 3 i 4: `fig3_1_road_case_A.pdf` i `fig3_2_road_case_B.pdf` (Zadatak 3)
- **Što prikazuje:** Uzdužni profil ceste $y(x)$ naspram prirodnog terena $h(x)$ na dionici od 10 metara.
- **Usporedba A vs. B:**
  - Na Slici 3 (slučaj A, $b_2 = 0.5$) cesta vrlo agilno prati zavoje terena jer joj je dopuštena veća zakrivljenost.
  - Na Slici 4 (slučaj B, $b_2 = 0.2$) niveleta je znatno "ispeglana" s blagim radijusima, što stvara veliki nasip na sredini dionice i povećava trošak za +27.47%.
- **Poanta za profesora:** *"Restriktivniji zahtjev za udobnošću vožnje ($b_2 = 0.2$) izravno se plaća većim volumenom zemljanih radova."*

### Slika 5: `fig3_3_road_constraint_check.pdf` (Zadatak 3)
- **Što prikazuje:** Provjeru zasićenja ograničenja nagiba $|\nabla y_i|$ i zakrivljenosti $|\nabla^2 y_i|$ duž trase.
- **Ključni elementi:** Crvene isprekidane linije označavaju gornje granice $b_1$ i $b_2$.
- **Poanta za profesora:** *"Grafikon potvrđuje da rješenje nigdje ne prelazi dopuštene granice, a platoi gdje krivulje dotiču crvene linije dokazuju da su ograničenja aktivna i diktiraju optimalnu geometriju trase."*

### Slika 6: `fig4_1_open_loop_divergence.pdf` (Zadatak 4b)
- **Što prikazuje:** Divergenciju otvorenog kruga sklopnog sustava bez upravljanja.
- **Ključni elementi:**
  - Vremenski odziv pokazuje oscilacije koje progresivno rastu do amplitude preko 7.0 na $t=20\,\mathrm{s}$.
  - Fazni portret pokazuje spiralu koja se odmotava prema van.
- **Poanta za profesora:** *"Grafička potvrda paradoksa sklopnih sustava: iako su oba moda Hurwitzova, spektralni radijus ciklusa $\rho = 1.218 > 1$ uzrokuje eksponencijalnu nestabilnost."*

### Slika 7: `fig4_2_closed_loop_stabilization.pdf` (Zadatak 4c)
- **Što prikazuje:** Eksponencijalnu stabilizaciju zatvorenog kruga s LMI regulatorom $u = Kx$.
- **Ključni elementi:**
  - Vremenski odziv stanja i upravljanja trne u nulu unutar 5 sekundi (na $t=20$ norma stanja je $10^{-12}$).
  - Fazni portret prikazuje spiralu koja se munjevito uvija u ishodište, presijecajući elipsoide zajedničke Ljapunovljeve funkcije izvana prema unutra.
- **Poanta za profesora:** *"Dokaz uspješne sinteze: zajednička Ljapunovljeva funkcija osigurava eksponencijalnu kontrakciju elipsoida uz stopu $\alpha = 0.2884\,\mathrm{s}^{-1}$ i minimalno pojačanje regulatora $K = [-3.4246, -0.1047]$."*

---

## 10.4 Strategija i psihologija usmene obrane pred profesorom Jokićem

1. **Govorite inženjerskim rječnikom:** Izbjegavajte laičke izraze poput *"točka se miče"* ili *"funkcija ide dolje"*. Koristite precizne termine: *"vektor stanja konvergira duž invarijantnog potprostora"*, *"gradijent cilja leži u stožcu vanjskih normala"*, *"narušena je dualna dopustivost"*.
2. **Uvijek povežite formulu s fizikom:** Čim napišete Ljapunovljevu jednadžbu ili KKT uvjet, odmah dodajte fizikalno značenje: *"Ovo predstavlja ravnotežu reakcija veza"* ili *"Ovo dokazuje disipaciju energije duž trajektorija"*. Profesor Jokić izrazito cijeni inženjersku intuiciju iza matematičkog aparata.
3. **Priznajte degeneraciju i konzervatizam kada postoje:** Ako vas profesor pita zašto nema iskopa i nasipa ili zašto je stopa $\alpha$ konzervativna, nemojte braniti neobranjivo! Odmah recite: *"LP je degeneriran i rješenje nije jedinstveno"* i *"Ocjena $\alpha$ vrijedi za proizvoljno prespajanje pa je prirodno konzervativnija od periodičkog ciklusa"*. To dokazuje najvišu razinu akademske zrelosti.


---

