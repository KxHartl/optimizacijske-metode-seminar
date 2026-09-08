# Pitanja za obranu i odgovori

> **Kolegij:** Optimizacijske metode u razvoju i upravljanju sustava (OMRiUS)
> **Student:** Krešimir Hartl
> **Mentor:** Prof. dr. sc. Andrej Jokić
> **Verzija rada:** v1.6

---

### 1. Zašto ste odbacili slučaj 4, iako su tamo oba ograničenja aktivna?

Zato što u toj točki množitelj $\mu_2$ ispada negativan. Sjecište pravaca
$x_1 + x_2 = 10$ i $x_1 - x_2 = 3$ je $x = (6.5,\ 3.5)$, a uvrštavanjem u uvjet
stacionarnosti dobiva se $\mu_1 = 11.50$ i $\mu_2 = -2.45$. Uvjet dualne
dopustivosti $\mu \geq 0$ time je narušen, pa ta točka ne može biti optimum.
Geometrijski: da bi $g_2$ bilo aktivno s $\mu_2 > 0$, gradijent funkcije cilja
morao bi imati komponentu koja gura točku preko granice $g_2$; ovdje je nema, pa
je optimum na granici samo prvog ograničenja.

### 2. Zašto je perturbacija $b_2$ bez utjecaja na $p^*$?

Jer je $g_2$ u optimumu neaktivno, $g_2(x^*) = -1.484848 < 0$, pa je iz uvjeta
komplementarnosti $\mu_2^* = 0$. Za ovaj problem lokalno, dok se aktivni skup ne
promijeni, vrijedi $\partial p^*/\partial v_2 = -\mu_2^* = 0$. To nije globalna
tvrdnja: dovoljno jako stezanje drugog ograničenja može aktivirati $g_2$, nakon
čega ova lokalna derivacija više ne opisuje promjenu optimalne vrijednosti.

### 3. Zašto je robusni ekvivalent s 8 nejednakosti egzaktan, a ne konzervativan?

Zato što je svaki skup nesigurnosti pravokutnik, dakle konveksna ljuska svoja
četiri vrha, a lijeva strana ograničenja je **linearna** u nesigurnom vektoru
$a_i$. Za $a = \sum_k \gamma_k v^{(k)}$ uz $\gamma_k \geq 0$, $\sum_k \gamma_k = 1$
iz $\big(v^{(k)}\big)^{\mathsf{T}} x \leq h_i$ za sve $k$ slijedi
$a^{\mathsf{T}} x = \sum_k \gamma_k \big(v^{(k)}\big)^{\mathsf{T}} x \leq h_i$.
Obrat je trivijalan jer su vrhovi elementi skupa. Dakle vrijedi ekvivalencija, a
ne samo implikacija — nema relaksacijskog procjepa.

### 4. Kako znate da su u robusnom optimumu aktivna oba najgora ograničenja?

KKT certifikatom za kandidat $x_{\mathrm{rob}}^* = (6.5,\ 179/34)$. Vršna
ograničenja $k=1$ i $k=7$ aktivna su, preostalih šest ima rezervu barem $1.5794$,
a množitelji aktivnih ograničenja $(17.607439,\ 1.344118)$ strogo su pozitivni i
zadovoljavaju stacionarnost. Funkcija cilja strogo je konveksna, pa taj primarno i
dualno dopustiv KKT kandidat jest jedinstveni globalni optimum. Dodatna provjera
kandidata s aktivnim samo prvim najgorim ograničenjem daje kršenje drugoga od
$+0.8146$; to objašnjava zašto taj aktivni skup otpada, ali samo po sebi nije dokaz
da oba ograničenja moraju biti aktivna.

### 5. Što zaključujete iz usporedbe mreža $N = 20$ i $N = 100$?

Samo opažanje za riješene diskretne probleme: $J^*$ raste za $2.60\%$ u slučaju A
i za $2.13\%$ u slučaju B. Promjenom $N$ mijenjaju se i diskretizirana funkcija
cilja i diskretizirana ograničenja, pa dvije mreže nisu dovoljne za određivanje
uzroka promjene, reda konvergencije ni predznaka pogreške prema kontinuiranom
problemu. Za jači zaključak bila bi potrebna zasebna studija konvergencije.

### 6. Zašto u tablici nema stupaca „iskop” i „nasip”?

Zadatak traži ukupni kriterij $J$, odnosno ukupnu površinu između nivelete i
terena, a za širinu $w$ pripadni je volumen $V=wJ$. Razdvajanje rezultata na iskop
i nasip nije traženo niti je u ovoj implementaciji posebno analizirano, pa se o
njegovoj jednoznačnosti ne donosi zaključak.

### 7. Zašto sklopni sustav nije stabilan kada su obje matrice Hurwitzove?

Hurwitzovost svake matrice jamči asimptotsku stabilnost odgovarajućeg zasebnog
LTI moda, ali ne jamči stabilnost pri prespajanju. Za zadani periodički zakon
mjerodavna je matrica prijelaza preko punog perioda:
$\Phi_{\mathrm{cikl}} = e^{A_{\mathrm{neparno}}} e^{A_{\mathrm{parno}}} = e^{-2}\,\mathrm{diag}(-9,\ -1/9)$,
sa spektralnim radijusom $\rho = 9e^{-2} = 1.218018 > 1$, što dokazuje
nestabilnost. Za zadani početni uvjet $x(0)=e_1=[1,0]^{\mathsf T}$ vrijedi
$x(2k)=(-9e^{-2})^k e_1$, pa upravo ta trajektorija u stroboskopskim točkama raste
geometrijski faktorom $1.218018$ po ciklusu. Ne tvrdi se da raste svaka
trajektorija.

### 8. Zašto Hurwitzovost zatvorenih modova nije dovoljna, nego treba LMI?

Iz istog razloga zbog kojeg otvoreni krug nije stabilan: Hurwitzovost pojedinih
matrica potvrđuje stabilnost svakoga fiksnog moda, ali ne rješava pitanje
stabilnosti pri prespajanju. Dokaz daje **zajednička**
kvadratna Ljapunovljeva funkcija $V(x) = x^{\mathsf{T}} P x$ s istim $P$ za oba
moda. Ako postoji $P \succ 0$ takav da je
$(A_i + BK)^{\mathsf{T}} P + P (A_i + BK) \prec 0$ za oba $i$, tada $V$ pada duž
trajektorija bez obzira na to koji je mod trenutno aktivan, pa je sustav
eksponencijalno stabilan za **svaki** po dijelovima kontinuiran izbor moda.
Za dobiveni $K$ vrijedi $\lambda_{\max} = -0.910478$ odnosno $-0.329090$.

### 9. Zašto uvodite supstituciju $\mathcal{Q} = P^{-1}$, $Y = KP^{-1}$?

Zato što uvjet $(A_i + BK)^{\mathsf{T}} P + P (A_i + BK) \prec 0$ sadrži umnožak
dviju nepoznanica, $PBK$, pa nije linearan — riječ je o bilinearnoj matričnoj
nejednakosti, koja nije konveksna. Množenjem s lijeva i s desna matricom
$P^{-1} \succ 0$ (transformacija kongruencije) predznak definitnosti se ne mijenja,
a uz $\mathcal{Q} = P^{-1}$ i $Y = K P^{-1}$ dobiva se
$A_i \mathcal{Q} + \mathcal{Q} A_i^{\mathsf{T}} + BY + Y^{\mathsf{T}} B^{\mathsf{T}} \prec 0$,
što je afino u $(\mathcal{Q}, Y)$, dakle LMI. Iz rješenja se vraća
$P = \mathcal{Q}^{-1}$, $K = YP$.

### 10. Rješenje LMI-ja nije jedinstveno — kako ste odabrali baš taj $K$?

Točno, riječ je o problemu dopustivosti. Sustav je uz to homogen: ako je
$(\mathcal{Q}, Y)$ dopustiv, dopustiv je i $(t\mathcal{Q}, tY)$ za $t \geq 1$, uz
isti $K$. Zato su stroge nejednakosti realizirane usklađenim parom normalizacija
$\mathcal{Q} \succeq I$ i
$A_i \mathcal{Q} + \mathcal{Q} A_i^{\mathsf{T}} + BY + Y^{\mathsf{T}} B^{\mathsf{T}} \preceq -I$,
a minimizacijom $\lVert Y \rVert$ izabrano je jedno dopustivo rješenje. Budući da
je $K=Y\mathcal{Q}^{-1}$ i da je $\mathcal{Q}$ također optimizacijska varijabla,
ovaj kriterij ne minimizira niti jamči najmanju normu $K$. Drugi izbor
normalizacije ili rješavača može dati drugi stabilizirajući $K$; svi rezultati i
sve slike u radu odgovaraju navedenom regulatoru.

### 11. Odakle stopa $\alpha = 0.288374\ \mathrm{s}^{-1}$?

Iz same Ljapunovljeve nejednakosti, a ne iz grafa. Uz
$M_i = (A_i + BK)^{\mathsf{T}} P + P (A_i + BK)$ vrijedi $\dot V = x^{\mathsf{T}} M_i x$
i $V = x^{\mathsf{T}} P x$, pa je $\dot V \leq \lambda_{\max}(M_i, P)\, V$, gdje je
$\lambda_{\max}(M_i, P)$ najveća poopćena svojstvena vrijednost para $(M_i, P)$.
Uzimanjem najgoreg od dva moda i pisanjem $\dot V \leq -2\alpha V$ slijedi
$\alpha = 0.288374\ \mathrm{s}^{-1}$ i ocjena
$\lVert x(t) \rVert \leq \sqrt{\kappa(P)}\, e^{-\alpha t} \lVert x(0) \rVert$ s
$\sqrt{\kappa(P)} = 1.3320$. Ta se ocjena odnosi na proizvoljno prespajanje, pa je
znatno konzervativnija od stvarne kontrakcije pri zadanom periodičkom
prespajanju, gdje je $\rho(\Phi_{\mathrm{cikl}}^{\mathrm{zk}}) = 0.069720$.

### 12. Zašto ste dualni problem riješili funkcijom `quadprog`, a ne `fmincon`?

Jer je dual kvadratnog programa opet kvadratni program. Dualna funkcija je
$\theta(\mu) = -\tfrac12 \mu^{\mathsf{T}} G Q^{-1} G^{\mathsf{T}} \mu + (-c^{\mathsf{T}} Q^{-1} G^{\mathsf{T}} - h^{\mathsf{T}})\mu - \tfrac12 c^{\mathsf{T}} Q^{-1} c$,
a $\max_{\mu \geq 0} \theta(\mu)$ je minimizacija konveksne kvadratne funkcije uz
donju granicu $\mu \geq 0$. `quadprog` je za to namijenjen i vraća `exitflag = 1`;
`fmincon` daje isto rješenje, ali završava na kriteriju duljine koraka
(`exitflag = 2`).

---

## Promjene v1.6 za obranu

| Nalaz | Što je promijenjeno | Zašto je sada točno | Kako se provjerava |
|---|---|---|---|
| F01 | $\min\lVert Y\rVert$ opisuje se kao odabir jednog dopustivog LMI rješenja, bez tvrdnje o najmanjoj normi $K$. | Vrijedi $K=Y\mathcal{Q}^{-1}$, a i $\mathcal{Q}$ je varijabla. | Usporediti kriterij i formulu za rekonstrukciju $K$; LMI reziduali ostaju negativni. |
| F02 | Usporedba $N=20$ i $N=100$ ostaje brojčano opažanje. | Dvije mreže ne određuju uzrok, red konvergencije ni predznak pogreške kontinuiranog problema. | Reproducirati četiri vrijednosti $J^*$; za jači zaključak trebala bi dodatna mrežna studija. |
| F03 | Interval koeficijenta zapisuje se s apsolutnom vrijednošću nominalnog koeficijenta. | Zapis $[a^0-0.15|a^0|,\ a^0+0.15|a^0|]$ ima ispravan poredak i kada je $a^0<0$. | Za $a^0=-1$ dobiva se $[-1.15,-0.85]$. |
| F04 | Razdvojeni su stvarni izvandijagonalni umnožak $-\pi^2/4$ i pozitivni član $+\pi^2/4$ u polinomu. | U determinanti $\lambda I-A_i$ izvandijagonalni se umnožak oduzima. | Izravno izračunati $A_{12}A_{21}$ i $\det(\lambda I-A_i)$. |
| F05 | Geometrijski rast vezan je uz zadani $x(0)=e_1$. | $\rho(\Phi_{\mathrm{cikl}})>1$ dokazuje nestabilnost, ali ne rast svake trajektorije. | Primijeniti dijagonalnu $\Phi_{\mathrm{cikl}}$ na $e_1$ i dobiti $\|x(2k)\|=(9e^{-2})^k$. |
| F06 | Formula osjetljivosti izričito je lokalna i vrijedi bez promjene aktivnog skupa. | Dovoljno jako stezanje $g_2$ može promijeniti aktivni skup. | Za mali korak $10^{-4}$ numerička derivacija za $v_2$ ostaje nula; tvrdnja se ne ekstrapolira globalno. |
| F07 | Graf razlikuje dopustive poluravnine i njihov robusni presjek bez sjenčanja svih 100 realizacija. | Čitatelj može očitati dopustivu stranu i robusno područje bez zatrpavanja. | Vizualno provjeriti strelice/oznake poluravnina, presjek i položaj oba optimuma. |
| F11 | Usklađene su jedinice $J$ i $V=wJ$, dodana je $\mathrm{m}^{-1}$ uz drugu podijeljenu razliku te su popravljeni prijelomi stranica. | Površina i volumen više se ne poistovjećuju, a izvedena veličina ima navedenu jedinicu. | Provjeriti tablicu zadatka 3 i render svih stranica v1.6. |
