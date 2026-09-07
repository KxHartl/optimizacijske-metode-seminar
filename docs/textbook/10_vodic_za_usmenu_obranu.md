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
