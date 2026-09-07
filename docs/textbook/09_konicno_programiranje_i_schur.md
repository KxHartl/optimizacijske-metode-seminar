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
