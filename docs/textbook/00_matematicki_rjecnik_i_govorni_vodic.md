# POGLAVLJE 0: Matematički rječnik, leksikon oznaka i govorni vodič za usmeni ispit

> **Svrha ovog poglavlja:**  
> Ovo poglavlje je **polazna točka za svakoga tko prvi put ulazi u svijet matematičke optimizacije**.  
> Ovdje se ne pretpostavlja apsolutno nikakvo predznanje: svaki matematički simbol, znak jednakosti, kuka, indeks, slovo grčkog alfabeta i prostorni koncept detaljno su objašnjeni na jednostavnom inženjerskom jeziku.  
> Uz svaku oznaku naveden je **doslovan govorni izgovor** kako biste na usmenom ispitu pred profesorom Jokićem govorili s punim matematičkim i stručnim autoritetom.

---

## 0.1 Logički i temeljni matematički simboli

| Simbol / Znak | Naziv simbola | Kako se izgovara na ispitu | Što točno znači (Intuicija za početnika) | Primjer u našem seminaru |
| :---: | :--- | :--- | :--- | :--- |
| $:=$ | Jednakost po definiciji | *"jednako po definiciji"* ili *"definiramo kao"* | Za razliku od obične jednakosti $=$ koja tvrdi da su dvije već postojeće stvari jednake (npr. $2+2=4$), znak $:=$ **uvodi novu kraticu ili novu oznaku** za neki izraz. Lijeva strana do tog trenutka nije postojala, već je upravo definiramo desnom stranom. | $\mathcal{Q} := P^{-1}$ (Novu matricu $\mathcal{Q}$ definiramo kao inverz postojeće matrice $P$). |
| $\in$ | Znak pripadnosti skupu | *"je element od"* ili *"pripada skupu"* | Označava da se neki objekt (broj, vektor, matrica) nalazi unutar određene skupine ili prostora. | $x \in \mathbb{R}^2$ (Vektor $x$ ima dvije realne komponente, dakle točka je u ravnini). |
| $\notin$ | Znak nepripadnosti | *"nije element od"* ili *"ne pripada"* | Objekt se ne nalazi u tom skupu. | $x \notin \mathcal{F}$ (Točka $x$ leži izvan dopustivog skupa, tj. krši neko ograničenje). |
| $\forall$ | Univerzalni kvantifikator | *"za svaki"* ili *"za bilo koji"* | Tvrdnja koja slijedi mora vrijediti za apsolutno svaki element bez ijedne iznimke. | $\forall x \in \mathbb{R}^n$ (Tvrdnja vrijedi za bilo koji vektor u prostoru). |
| $\exists$ | Egzistencijalni kvantifikator | *"postoji"* ili *"možemo naći barem jedan"* | Tvrdi da postoji barem jedan element koji ima traženo svojstvo. | $\exists x \in \mathcal{F}$ takav da je $Gx < h$ (Postoji barem jedna točka u unutrašnjosti). |
| $\implies$ | Implikacija | *"povlači"* ili *"iz toga slijedi"* | Ako je istinita lijeva tvrdnja, onda je nužno istinita i desna tvrdnja. | $Q \succ 0 \implies f(x)$ je strogo konveksna. |
| $\iff$ | Ekvivalencija | *"ako i samo ako"* ili *"ekvivalentno je"* | Dvije tvrdnje znače potpuno istu stvar: lijeva povlači desnu, a desna povlači lijevu. | $a^{\mathsf{T}} x \leq h, \forall a \in \mathcal{P} \iff (v^{(k)})^{\mathsf{T}} x \leq h, \forall k$. |
| $\subset, \subseteq$ | Podskup | *"je podskup od"* | Svi elementi prvog skupa nalaze se i u drugom skupu. | $\mathcal{F} \subset \mathbb{R}^n$ (Dopustivo područje je dio prostora). |
| $\cap$ | Presjek skupova | *"presjek"* | Područje koje pripada i prvom i drugom skupu istovremeno (logički "I"). | $\mathcal{F} = \{x \mid g_1(x) \leq 0\} \cap \{x \mid g_2(x) \leq 0\}$. |
| $\cup$ | Unija skupova | *"unija"* | Područje koje pripada prvom, drugom ili obama skupovima (logički "ILI"). | $t \in [0, 1) \cup [2, 3)$ (Vremenski intervali u kojima je aktivan parni mod). |
| $\setminus$ | Skupovna razlika | *"manje"* ili *"bez"* | Prvi skup iz kojeg su izbačeni svi elementi drugog skupa. | $\mathbb{R}^n \setminus \{0\}$ (Čitav prostor osim samog ishodišta, tj. svi vektori osim nul-vektora). |
| $\min, \max$ | Minimum i Maksimum | *"minimum"*, *"maksimum"* | **Najmanja odnosno najveća vrijednost** koju funkcija poprima na zadanom skupu, uz uvjet da se ta vrijednost stvarno dostiže u nekoj točki skupa. | $\min_x f(x)$ uz $Gx \leq h$. |
| $\inf, \sup$ | Infimum i Supremum | *"infimum"*, *"supremum"* | **Najveća donja međa** (infimum) odnosno **najmanja gornja međa** (supremum). Koristi se kada nismo sigurni dostiže li funkcija minimum (npr. funkcija $e^{-x}$ za $x \geq 0$ nema minimum jer se nula dostiže tek u beskonačnosti, ali njezin infimum je točno 0). | $\theta(\mu) = \inf_x \mathcal{L}(x, \mu)$ (Tražimo donju među Lagrangiana po cijelom prostoru). |

---

## 0.2 Vektori, prostori i euklidska geometrija

Što zapravo znače pojmovi poput *vektor*, *dimenzija* i *Euklidski prostor*? Razjasnimo ih od nule:

### 1. Što je skup $\mathbb{R}$?
Slovo $\mathbb{R}$ označava **skup svih realnih brojeva**. To su svi mogući brojevi koje možete zamisliti na neprekidnom brojevnom pravcu: pozitivni, negativni, nula, razlomci (npr. $140/33$), korijeni ($\sqrt{4.36}$) i brojevi poput $\pi$. U inženjerstvu realnim brojevima mjerimo fizikalne veličine: duljinu u metrima, napon u voltima, masu u kilogramima.

### 2. Što je $\mathbb{R}^n$ i zašto se zove "Euklidski prostor"?
- $\mathbb{R}^1 = \mathbb{R}$ je **jednodimenzionalni prostor** (jedna os, običan pravac). Točka je definirana jednim brojem $x_1$.
- $\mathbb{R}^2$ je **dvodimenzionalni prostor** (ravnina, poput lista papira). Točka ili vektor ima dvije koordinate: $x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$. Primjer: naš Zadatak 1 i Zadatak 2 odvijaju se u $\mathbb{R}^2$.
- $\mathbb{R}^3$ je **trodimenzionalni prostor** (fizički prostor sobe). Točka ima tri koordinate: širinu, dužinu i visinu.
- $\mathbb{R}^n$ je **$n$-dimenzionalni prostor**. Iako ga ljudsko oko ne može vizualizirati za $n \geq 4$, matematički je to jednostavno popis od $n$ brojeva: $x = [x_1, x_2, \dots, x_n]^{\mathsf{T}}$. U Zadatku 3 naša cesta ima $N=100$ podintervala, pa imamo $n = 101$ visinsku točku nivelete — naš vektor $y$ živi u prostoru $\mathbb{R}^{101}$!
- **Zašto se zove "Euklidski prostor"?** Ime je dobio po starogrčkom matematičaru Euklidu iz Aleksandrije (oko 300. pr. Kr.) koji je postavio aksiome geometrije u kojoj vrijedi **Pitagorin teorem**. Prostor $\mathbb{R}^n$ nazivamo euklidskim jer je udaljenost između dvije točke definirana generaliziranim Pitagorinim teoremom:
  $$d(x, y) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + \dots + (x_n - y_n)^2}.$$

---

### 3. Anatomija vektora: Stupac vs. Redak i Transponiranje $(\cdot)^{\mathsf{T}}$
U matematičkoj optimizaciji i matričnom računu postoji strogi standard: **svaki vektor po defaultu je stupac**:
$$x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \in \mathbb{R}^{2 \times 1}.$$
Oznaka $(\cdot)^{\mathsf{T}}$ (ili $(\cdot)'$ u MATLAB-u) označava **transponiranje** — operaciju kojom se reci i stupci zamjenjuju. Dakle, transponiranjem vektor-stupac postaje vektor-redak:
$$x^{\mathsf{T}} = \begin{bmatrix} x_1 & x_2 \end{bmatrix} \in \mathbb{R}^{1 \times 2}.$$
- *Kako se izgovara na ispitu:* *"iks transponirano"*.

---

### 4. Skalarni (unutrašnji) produkt: Simboli $\langle x, y \rangle$ i $x^{\mathsf{T}} y$
- **Što je simbol $\langle x, y \rangle$?** To je standardna matematička oznaka za **skalarni produkt** (unutrašnji umnožak) dvaju vektora $x$ i $y$.
- **Što je $x^{\mathsf{T}} y$?** To je matrični zapis istog tog skalarnog produkta (množenje retka dimenzija $1 \times n$ sa stupcem dimenzija $n \times 1$, što kao rezultat daje običan broj — skalar dimenzija $1 \times 1$):
  $$\langle x, y \rangle := x^{\mathsf{T}} y = x_1 y_1 + x_2 y_2 + \dots + x_n y_n = \sum_{i=1}^n x_i y_i.$$
- *Kako se izgovara na ispitu:* *"skalarni umnožak vektora x i y"* ili *"iks transponirano puta y"*.
- **Geometrijska intuicija:** Skalarni produkt mjeri **kut i međusobno preklapanje** dvaju vektora:
  $$x^{\mathsf{T}} y = \|x\|_2 \|y\|_2 \cos \angle(x, y).$$
  - Ako dva vektora pokazuju u istom smjeru, skalarni produkt je maksimalno pozitivan.
  - Ako su dva vektora **međusobno okomita (ortogonalna)**, kut je $90^\circ$, pa je $\cos(90^\circ) = 0 \implies x^{\mathsf{T}} y = 0$.
  - Ako pokazuju u suprotnim smjerovima, skalarni produkt je negativan.

---

### 5. Norme vektora: Što znače oznake $\|x\|_2$, $\|x\|_1$ i $\|x\|_\infty$?
Norma je funkcija koja svakom vektoru pridružuje nenegativan realan broj koji predstavlja njegovu **fizikalnu veličinu ili duljinu**. Oznaka su dvostruke okomite crte $\|\cdot\|$.

| Oznaka norme | Naziv | Matematička formula | Govorni izgovor na ispitu | Fizikalna intuicija i primjena |
| :---: | :--- | :--- | :--- | :--- |
| $\|x\|_2$ | Euklidska norma ($\ell_2$-norma) | $\|x\|_2 := \sqrt{x_1^2 + \dots + x_n^2} = \sqrt{x^{\mathsf{T}} x}$ | *"euklidska norma od iks"* ili *"dva-norma od iks"* | Prava geometrijska udaljenost izmjerena ravnalom ("zračna linija"). U Zadacima 1 i 2 funkcija cilja sadrži euklidske kvadrate, a u Zadatku 4 minimiziramo pojačanje $\min \|Y\|_2$. |
| $\|x\|_1$ | Manhattan / taksi norma ($\ell_1$-norma) | $\|x\|_1 := \sum_{i=1}^n \|x_i\| = \|x_1\| + \dots + \|x_n\|$ | *"jedan-norma od iks"* ili *"el-jedan norma"* | Udaljenost u gradu s pravilnim blokovima ulica gdje se ne može ići dijagonalno nego samo po koordinatnim osima (kao taksi na Manhattanu). U Zadatku 3 mjeri **ukupni volumen zemljanih radova** (površinu između ceste i terena). U Poglavlju 9 služi za **LASSO** regularizaciju. |
| $\|x\|_\infty$ | Maksimalna / Chebyshevjeva norma | $\|x\|_\infty := \max_{1 \leq i \leq n} \|x_i\|$ | *"beskonačno-norma od iks"* ili *"maks-norma"* | Mjeri najveće vršno odstupanje jedne pojedinačne komponente. Koristi se u tolerancijama strojne obrade gdje je bitan najgori komad. |

---

## 0.3 Matrice, definitnost i parcijalni poredak (LMI)

| Oznaka | Naziv | Kako se izgovara na ispitu | Značenje za početnika |
| :---: | :--- | :--- | :--- |
| $\mathbb{R}^{m \times n}$ | Prostor matrica | *"er em puta en"* | Tablica realnih brojeva koja ima $m$ vodoravnih redaka i $n$ okomitih stupaca. |
| $\mathbb{S}^n$ | Prostor simetričnih matrica | *"es en"* | Kvadratne matrice dimenzija $n \times n$ koje su jednake vlastitom transponiranom obliku ($A = A^{\mathsf{T}}$). Elementi zrcaljeni preko glavne dijagonale su identični ($A_{ij} = A_{ji}$). Hesseove matrice funkcija drugog reda uvijek leže u $\mathbb{S}^n$. |
| $x^{\mathsf{T}} A x$ | Kvadratna forma | *"kvadratna forma iks transponirano A iks"* | Skalarni izraz u kojem matrica $A$ "težinski množi" vektor $x$ sam sa sobom. Rezultat je običan broj (skalar). U Zadatku 1 imamo $\frac{1}{2} x^{\mathsf{T}} Q x = x_1^2 + 2x_2^2 - 0.3x_1 x_2$. |
| $A \succ 0$ | Strogo pozitivno definitna matrica | *"matrica A je strogo pozitivno definitna"* ili *"A je veće od nula u smislu Loewnera"* | Za svaki vektor $x \neq 0$ vrijedi $x^{\mathsf{T}} A x > 0$. Geometrijski, graf funkcije $x^{\mathsf{T}} A x$ izgleda kao **savršena trodimenzionalna zdjela (paraboloid) okrenuta prema gore**. Sve svojstvene vrijednosti matrice $A$ su strogo pozitivne ($\lambda_i > 0$). |
| $A \succeq 0$ | Pozitivno semidefitna matrica | *"matrica A je pozitivno semidefitna"* | Za svaki vektor vrijedi $x^{\mathsf{T}} A x \geq 0$. Zdjela može na dnu imati ravni žlijeb duž kojeg funkcija miruje. Najmanja svojstvena vrijednost može biti nula ($\lambda_{\min} \geq 0$). |
| $A \succ B$ | Loewnerov poredak | *"A je veće od B u smislu pozitivne definitnosti"* | Skraćeni zapis za nejednakost: $A - B \succ 0$. To **nije** usporedba element-po-element, već znači da je matrica razlike $(A - B)$ pozitivno definitna! |
| $\lambda_i(A)$ | Svojstvena (vlastita) vrijednost | *"lambda i od A"* ili *"svojstvena vrijednost matrice A"* | Skalari $\lambda$ za koje postoji vektor $v \neq 0$ takav da je $A v = \lambda v$. U optimizaciji predstavljaju **glavne zakrivljenosti nivo-elipsi**. U dinamičkim sustavima (Zadatak 4) predstavljaju **polove sustava** (brzinu i prigušenje titranja). |
| $\det(A)$ | Determinanta matrice | *"determinanta od A"* | Broj pridružen kvadratnoj matrici koji mjeri koliko matrica rasteže ili stišće volumen prostora. Ako je $\det(A) \neq 0$, matrica je regularna i posjeduje inverz $A^{-1}$. |
| $\mathrm{Tr}(A)$ | Trag matrice (*Trace*) | *"trag od A"* | Zbroj elemenata na glavnoj dijagonali: $\mathrm{Tr}(A) = \sum A_{ii}$. Zanimljivo inženjersko svojstvo: trag je uvijek točno jednak zbroju svih svojstvenih vrijednosti! |
| $\kappa(P)$ | Uvjetovanost matrice (*Condition number*) | *"kapa od P"* ili *"broj uvjetovanosti"* | Omjer najveće i najmanje svojstvene vrijednosti: $\kappa(P) = \lambda_{\max}/\lambda_{\min}$. Mjeri izduženost elipsoida. Ako je $\kappa = 1$, elipsoid je savršena kugla. U Zadatku 4 imamo $\kappa(P) = 1.7743$, pa je $\sqrt{\kappa} = 1.3320$. |

---

## 0.4 Funkcije, derivacije i analiza

| Oznaka | Naziv | Govorni izgovor na ispitu | Što fizikalno znači |
| :---: | :--- | :--- | :--- |
| $\nabla f(x)$ | Gradijent funkcije | *"nabla f od iks"* ili *"gradijent od f"* | Vektor prvih parcijalnih derivacija: $\nabla f(x) = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}$. **Fizikalno:** strelica koja pokazuje u smjeru **najbržeg uspona (najvećeg rasta)** funkcije. Njegov iznos $\|\nabla f\|$ govori koliko je brijeg strm. |
| $-\nabla f(x)$ | Vektor najbržeg pada | *"minus gradijent od f"* | Strelica koja pokazuje točno u smjeru **najbržeg spuštanja niz brijeg**. Prema njemu bi se kotrljala kuglica puštena na plohu funkcije. |
| $\nabla^2 f(x)$ | Hesseova matrica (Hessian) | *"nabla kvadrat f od iks"* ili *"Hesseova matrica"* | Matrica drugih parcijalnih derivacija: $[\nabla^2 f(x)]_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}$. Mjeri **zakrivljenost plohe**. Ako ubrzanje promjene nagiba raste u svim smjerovima, Hessian je $\succ 0$ i funkcija je konveksna zdjela. |
| $d \in \mathbb{R}^n$ | Dozvoljeni smjer (*Feasible direction*) | *"vektor dozvoljenog smjera d"* | Vektor duž kojeg se možemo malo pomaknuti iz trenutne točke $x$, a da pritom ostanemo unutar dopuštenog područja (ne probijemo nijedan zid ograničenja). |
| $\mathrm{epi}(f)$ | Epigraf funkcije | *"epigraf funkcije f"* | Skup svih točaka koje leže **na grafu funkcije ili iznad njega**. Funkcija je konveksna ako i samo ako je njezin epigraf konveksan skup u prostoru $\mathbb{R}^{n+1}$. |
| $\mathrm{co}(\mathcal{S})$ | Konveksna ljuska (*Convex Hull*) | *"konveksna ljuska skupa S"* | Najmanji konveksni skup koji obuhvaća sve točke skupa $\mathcal{S}$. Zamislite točke kao čavle zabijene u dasku: ako oko njih rastegnete gumicu i pustite je da se stisne, oblik koji gumica zauzme je konveksna ljuska! U Zadatku 2 konveksna ljuska 4 vrha tvori pravokutnik nesigurnosti. |

---

## 0.5 Optimizacija, KKT i dualnost

| Oznaka | Naziv | Govorni izgovor na ispitu | Što točno znači |
| :---: | :--- | :--- | :--- |
| $p^*$ | Optimalna vrijednost primara | *"pe sa zvjezdicom"* ili *"optimalna vrijednost funkcije cilja"* | Najmanji trošak koji se može postići uz poštivanje svih zadanih ograničenja. U Zadatku 1 imamo $p^* = 60.606061$. |
| $x^*$ | Optimalno rješenje (točka optimuma) | *"iks sa zvjezdicom"* ili *"optimalna točka"* | Koordinate u kojima se postiže minimalni trošak $p^*$. U Zadatku 1 to je točka $x^* = (190/33, 140/33)$. |
| $\mathcal{F}$ | Dopustivi skup (*Feasible set*) | *"kaligrafsko ef"* ili *"dopustivi skup"* | Skup svih točaka $x$ koje zadovoljavaju sva ograničenja istovremeno: $\mathcal{F} = \{x \mid Gx \leq h\}$. |
| $\mathcal{A}(x)$ | Aktivni skup ograničenja | *"aktivni skup ograničenja"* | Indeksi onih ograničenja koja su u promatranoj točki zadovoljena točno na granici (kao jednakost, $g_i(x) = 0$). U Zadatku 1 je $\mathcal{A}(x^*) = \{1\}$. |
| $\mathcal{L}(x, \mu)$ | Lagrangeova funkcija (Lagrangian) | *"Lagrangian"* ili *"Lagrangeova funkcija od iks i mi"* | Funkcija koja spaja funkciju cilja i sva ograničenja pomnožena s njihovim množiteljima: $\mathcal{L} = f(x) + \sum \mu_i g_i(x)$. Predstavlja ravnotežu potencijalne energije i rada reakcija veza. |
| $\mu_i$ | Lagrangeov množitelj (multiplikator) | *"mi i"* ili *"Lagrangeov množitelj i-tog ograničenja"* | Mjera napetosti ili intenziteta sile kojom se $i$-to ograničenje odupire proboju. Naziva se i **cijena u sjeni** (*shadow price*). U Zadatku 1 imamo $\mu_1^* = 404/33 \approx 12.2424$. |
| $\theta(\mu)$ | Lagrangeova dualna funkcija | *"teta od mi"* ili *"dualna funkcija"* | Funkcija dobivena pronalaženjem najniže točke Lagrangiana po varijabli $x$: $\theta(\mu) = \inf_x \mathcal{L}(x, \mu)$. Uvijek je konkavna i daje zajamčenu donju granicu primarnog optimuma. |
| $d^*$ | Optimalna vrijednost duala | *"de sa zvjezdicom"* | Najveća moguća donja međa primarnog troška: $d^* = \max_{\mu \geq 0} \theta(\mu)$. |
| $p^* - d^*$ | Dualni procjep (*Duality Gap*) | *"dualni procjep"* | Razlika između najboljeg primarnog troška i najbolje dualne procjene. Ako je problem konveksan i vrijedi Slaterov uvjet, procjep je točno nula ($p^* - d^* = 0$, jaka dualnost). |
| $v$ | Perturbacijski vektor | *"vektor perturbacije ve"* | Mala promjena desne strane ograničenja: $g_i(x) \leq v_i$. Prema teoremu o osjetljivosti je $\partial p^*/\partial v_i = -\mu_i^*$. |

---

## 0.6 Dinamički sustavi, stabilnost i LMI sinteza

| Oznaka | Naziv | Govorni izgovor na ispitu | Što točno znači |
| :---: | :--- | :--- | :--- |
| $\dot{x}(t)$ | Vremenska derivacija stanja | *"iks točka od t"* | Brzina promjene varijabli stanja u vremenu: $\dot{x}(t) := \frac{\mathrm{d}x(t)}{\mathrm{d}t}$. Sustav $\dot{x} = Ax$ opisuje kako brzine ovise o trenutnom položaju u prostoru stanja. |
| $\lfloor t \rfloor$ | Funkcija najvećeg cijelog broja (*Floor*) | *"najveće cijelo od t"* ili *"floor od t"* | Zaokruživanje realnog vremena $t$ na prvi manji ili jednaki cijeli broj (npr. $\lfloor 0.7 \rfloor = 0$, $\lfloor 1.4 \rfloor = 1$, $\lfloor 2.99 \rfloor = 2$). U Zadatku 4 određuje kada sustav mijenja mod. |
| Hurwitzova matrica | Hurwitzova matrica dinamike | *"matrica A je Hurwitzova"* | Kvadratna matrica čije sve svojstvene vrijednosti leže strogo u lijevoj poluravnini kompleksne ravnine ($\mathrm{Re}(\lambda_i) < 0$). Jamči da LTI sustav bez prespajanja asimptotski konvergira u nulu. |
| $e^{At}$ | Matrični eksponent | *"e na A puta t"* ili *"matrični eksponent"* | Matrica prijelaza stanja LTI sustava. Množenjem s početnim stanjem $x(0)$ daje točan položaj stanja u trenutku $t$: $x(t) = e^{At} x(0)$. |
| $\Phi_{\mathrm{cikl}}$ | Monodromijska matrica ciklusa | *"monodromijska matrica ciklusa"* ili *"fi ciklusa"* | Diskretna matrica prijelaza preko jednog punog perioda prespajanja ($T=2\,\mathrm{s}$): $\Phi_{\mathrm{cikl}} = e^{A_{\mathrm{nep}}} e^{A_{\mathrm{par}}}$. Povezuje stanje na kraju ciklusa s početkom ciklusa: $x(2k) = (\Phi_{\mathrm{cikl}})^k x(0)$. |
| $\rho(M)$ | Spektralni radijus matrice | *"ro od M"* ili *"spektralni radijus"* | Maksimalna apsolutna vrijednost (modul) svojstvenih vrijednosti matrice: $\rho(M) := \max_i \|\lambda_i(M)\|$. Ako je $\rho > 1$, diskretni sustav divergira u beskonačnost! U Zadatku 4b imamo $\rho = 1.218 > 1$. |
| CQLF | Zajednička kvadratna Ljapunovljeva funkcija | *"zajednička kvadratna Ljapunovljeva funkcija"* (kratica CQLF) | Skalarna funkcija energije $V(x) = x^{\mathsf{T}} P x$ ($P \succ 0$) s istom matricom $P$ za sve modove, koja monotono opada duž trajektorija bez obzira na prespajanje. |
| BMI | Bilinearna matrična nejednakost | *"be-em-i"* ili *"bilinearna matrična nejednakost"* | Matrična nejednakost u kojoj se dvije optimizacijske nepoznanice množe (član $PBK$). Problem je nekonveksan i NP-težak. |
| LMI | Linearna matrična nejednakost | *"el-em-i"* ili *"linearna matrična nejednakost"* | Matrična nejednakost u kojoj sve nepoznanice ulaze afino (linearno). Problem je konveksan i rješava se u polinomijalnom vremenu. |
| Kongruencija | Transformacija kongruencije | *"transformacija kongruencije"* | Množenje simetrične matrice s lijeva s $T$ i s desna s $T^{\mathsf{T}}$ uz regularnu $T$. Prema Sylvesterovom teoremu, kongruencija čuva predznake svojstvenih vrijednosti (očuvava negativnu definitnost!). |
| GEVP | Poopćeni problem svojstvenih vrijednosti | *"ge-ve-pe"* ili *"poopćeni problem svojstvenih vrijednosti"* | Problem oblika $\det(M - \lambda P) = 0$. Koristi se za izračun stope eksponencijalnog prigušenja $\alpha = 0.2884\,\mathrm{s}^{-1}$. |
| $\alpha$ | Stopa eksponencijalnog prigušenja | *"alfa"* | Brzina kojom se stanja guše prema ishodištu: $\|x(t)\| \leq \sqrt{\kappa(P)} e^{-\alpha t} \|x(0)\|$. |

---

## 0.7 Vodič za usmeni ispit: "Kako točno izgovoriti pred ispitivačem"

Kada na usmenom ispitu izvodite formule na ploči ili odgovarate na pitanja profesora Jokića, **ključno je koristiti besprijekoran akademski rječnik**. 

Evo tablice 10 najčešćih rečenica na ispitu i kako ih izgovoriti poput pravog inženjerskog eksperta:

| Što pišete na ploči | Kako to NE BI smjeli reći (Laicistički / Zbunjeno) | Kako to TREBATE reći (Profesionalni inženjerski govor) |
| :--- | :--- | :--- |
| $\nabla f(x^*) = -\mu_1^* \nabla g_1$ | *"Ovdje se strelice poništavaju pa je to nula."* | *"U točki optimuma gradijent funkcije cilja leži u stožcu vanjskih normala aktivnih ograničenja; gradijent cilja i gradijent aktivnog ograničenja su strogo kolinearni i suprotnog smjera uz pozitivan Lagrangeov multiplikator."* |
| $\mu_2 = -2.45 < 0$ u sjecištu | *"Ovdje je broj negativan pa točka otpada."* | *"U točki sjecišta narušen je uvjet dualne dopustivosti. Negativan multiplikator znači da bi veza morala djelovati kao privlačna sila, dok nejednakost dopušta samo odbojne reakcije. Funkcija cilja opada kretanjem prema unutrašnjosti dopustivog skupa."* |
| $Q \succ 0 \implies \lambda_i > 0$ | *"Matrica je pozitivna pa je sve konveksno."* | *"Hesseova matrica funkcije cilja je strogo pozitivno definitna jer su obje njezine svojstvene vrijednosti strogo veće od nule. Iz toga slijedi da je funkcija cilja strogo konveksna i koercivna, što jamči egzistenciju i jedinstvenost globalnog minimuma."* |
| $\rho(\Phi_{\mathrm{cikl}}) = 1.218 > 1$ | *"Umnožak matrica je veći od jedan pa to raste."* | *"Iako su pojedinačne matrice modova Hurwitzove, spektralni radijus monodromijske matrice ciklusa strogo je veći od jedan. Stanje u stroboskopskim trenucima geometrijski raste faktorom 1.218 po ciklusu uslijed parametarske rezonancije i neusklađenosti energetskih elipsoida."* |
| $A_i \mathcal{Q} + \mathcal{Q} A_i^{\mathsf{T}} + B Y + Y^{\mathsf{T}} B^{\mathsf{T}} \prec 0$ | *"Pomnožili smo s P minus jedan da maknemo P puta K."* | *"Izvorni nelinearni problem bilinearne matrične nejednakosti (BMI) linearizirali smo primjenom transformacije kongruencije s inverzom Ljapunovljeve matrice $P^{-1} \succ 0$. Uvođenjem supstitucije varijabli $\mathcal{Q} = P^{-1}$ i $Y = K P^{-1}$, dobili smo afinu formulaciju koju egzaktno rješavamo u YALMIP-u kao linearnu matričnu nejednakost."* |
| $\partial p^* / \partial v_1 = -\mu_1^*$ | *"Derivacija je množitelj samo s minusom."* | *"Prema teoremu o lokalnoj osjetljivosti, parcijalna derivacija optimalne vrijednosti po perturbaciji desne strane ograničenja jednaka je negativnom Lagrangeovom multiplikatoru. Multiplikator predstavlja granični trošak ili cijenu u sjeni aktivnog ograničenja."* |
| $J^*$ raste pri $N = 20 \to 100$ | *"Prije je bilo manje jer je bilo manje točaka."* | *"Diskretni kriterij je pravokutna kvadraturna aproksimacija kontinuiranog integrala zemljanih radova. Na rijetkoj mreži integral je podcijenjen za red veličine $O(\Delta x)$ jer valoviti reljef izmiče čvorovima; zgušnjavanjem mreže numerička suma konvergira odozdo prema stvarnoj vrijednosti integrala."* |
| Nema stupaca "iskop" i "nasip" | *"Nisam ih stavio jer se to ne može znati."* | *"Linearni program nivelacije trase je matematički degeneriran. Postoji beskonačno mnogo profila nivelete s identičnom optimalnom vrijednošću funkcije cilja, ali različitom preraspodjelom između iskopa i nasipa. Navođenje pojedinačnih kubatura bilo bi numerički proizvoljno."* |
| $\sup_{a \in \mathcal{P}} a^{\mathsf{T}} x \leq h$ | *"Uzeli smo kutove pa je to to."* | *"Budući da je skup nesigurnosti konveksan poliedar, a funkcija u ograničenju linearna po nesigurnim parametrima, supremum se egzaktno dostiže u nekom od vrhova. Ekvivalencija je egzaktna, pa formulacija s 8 nejednakosti nema relaksacijskog procjepa."* |
| $\begin{bmatrix} A & B \\ B^{\mathsf{T}} & C \end{bmatrix} \succ 0$ | *"Rastavili smo matricu na komade."* | *"Primjenom teorema o Schurovom komplementu, blok-matrica je strogo pozitivno definitna ako i samo ako je blok $A \succ 0$ i njegov Schurov komplement $C - B^{\mathsf{T}} A^{-1} B \succ 0$. Dokaz se temelji na blok-kongruenciji koja matricu svodi na blok-dijagonalni oblik."* |
