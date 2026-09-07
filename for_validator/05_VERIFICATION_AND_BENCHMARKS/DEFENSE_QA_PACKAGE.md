# Pitanja za obranu i odgovori

> **Kolegij:** Optimizacijske metode u razvoju i upravljanju sustava (OMRiUS)
> **Student:** Krešimir Hartl
> **Mentor:** Prof. dr. sc. Andrej Jokić
> **Verzija rada:** v1.2

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
komplementarnosti $\mu_2^* = 0$, a iz teorema o osjetljivosti
$\partial p^*/\partial v_2 = -\mu_2^* = 0$. To vrijedi lokalno: dok je pomak
granice manji od rezerve $1.484848$, aktivni skup se ne mijenja i optimum ostaje
isti. Pri većem pomaku $g_2$ bi postalo aktivno i derivacija više ne bi bila nula.

### 3. Zašto je robusni ekvivalent s 8 nejednakosti egzaktan, a ne konzervativan?

Zato što je svaki skup nesigurnosti pravokutnik, dakle konveksna ljuska svoja
četiri vrha, a lijeva strana ograničenja je **linearna** u nesigurnom vektoru
$a_i$. Za $a = \sum_k \gamma_k v^{(k)}$ uz $\gamma_k \geq 0$, $\sum_k \gamma_k = 1$
iz $\big(v^{(k)}\big)^{\mathsf{T}} x \leq h_i$ za sve $k$ slijedi
$a^{\mathsf{T}} x = \sum_k \gamma_k \big(v^{(k)}\big)^{\mathsf{T}} x \leq h_i$.
Obrat je trivijalan jer su vrhovi elementi skupa. Dakle vrijedi ekvivalencija, a
ne samo implikacija — nema relaksacijskog procjepa.

### 4. Kako znate da su u robusnom optimumu aktivna oba najgora ograničenja?

Provjerom. Ako se pretpostavi da je aktivno samo najgore prvo ograničenje,
rješenje je $x = (6.9073,\ 4.8574)$, a tada je
$1.15 (6.9073) - 0.85 (4.8574) - 3 = +0.8146 > 0$, dakle točka nije dopustiva.
Prema tome oba moraju biti aktivna, što daje $x_{\mathrm{rob}}^* = (6.5,\ 179/34)$.
Pripadajući množitelji $(17.607439,\ 1.344118)$ strogo su pozitivni, a preostalih
šest nejednakosti ima rezervu barem $1.5794$ — svi KKT uvjeti su zadovoljeni.

### 5. Zašto $J^*$ **raste** kada se mreža profini s $N = 20$ na $N = 100$?

Zato što je diskretni kriterij $J_{\mathrm{disc}} = \Delta x \sum_i |y_i - h_i|$
pravokutna kvadratura po čvorovima. Na rijetkoj mreži odstupanje je uzorkovano u
malo točaka i dio površine između čvorova izmiče sumi, pa je integral podcijenjen.
Pogreška je reda $O(\Delta x)$, pa s pet puta gušćom mrežom vrijednost raste prema
pravom integralu (+2.60 % za slučaj A, +2.13 % za B). Nije riječ o tome da je
rješenje pri $N = 20$ bolje, nego da je kriterij tamo lošije aproksimiran.

### 6. Zašto u tablici nema stupaca „iskop” i „nasip”?

Jer ta podjela nije jedinstvena. Linearni program je degeneriran: postoji više
optimalnih $y$ s istom vrijednošću $J^*$, ali različitom raspodjelom na iskop i
nasip. Različiti rješavači daju različite parove koji zbrajanjem uvijek daju isti
$J^*$. Navoditi te brojke značilo bi tvrditi nešto što rezultat ne određuje.

### 7. Zašto sklopni sustav nije stabilan kada su obje matrice Hurwitzove?

Hurwitzovost jamči konvergenciju samo ako sustav trajno ostane u jednom modu.
Ovdje se dinamika mijenja svake sekunde, pa je mjerodavna matrica prijelaza preko
punog perioda. Ona iznosi
$\Phi_{\mathrm{cikl}} = e^{A_{\mathrm{neparno}}} e^{A_{\mathrm{parno}}} = e^{-2}\,\mathrm{diag}(-9,\ -1/9)$,
sa spektralnim radijusom $\rho = 9e^{-2} = 1.218018 > 1$. Kako je
$x(2(k+1)) = \Phi_{\mathrm{cikl}} x(2k)$, norma stanja u stroboskopskim točkama
raste geometrijski, faktorom $1.218$ po ciklusu. Umnožak dviju matrica sa
spektralnim radijusom manjim od jedan općenito ne mora imati spektralni radijus
manji od jedan.

### 8. Zašto Hurwitzovost zatvorenih modova nije dovoljna, nego treba LMI?

Iz istog razloga zbog kojeg otvoreni krug nije stabilan: svojstvene vrijednosti
pojedinih matrica ne govore ništa o prespajanju. Dokaz daje **zajednička**
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
a među dopustivim parovima izabran je onaj s najmanjom normom $\lVert Y \rVert$,
dakle regulator najmanjeg pojačanja. Drugi izbor normalizacije daje drugi
stabilizirajući $K$; svi rezultati i sve slike u radu odgovaraju navedenom.

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
