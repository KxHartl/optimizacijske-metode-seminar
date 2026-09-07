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
