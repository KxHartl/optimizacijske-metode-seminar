# VALIDACIJSKO IZVJEŠĆE — Seminarski rad OMRiUS

**Student:** Krešimir Hartl
**Predmet:** Optimizacijske metode u razvoju i upravljanju sustava
**Mentor:** Prof. dr. sc. Andrej Jokić
**Datum recenzije:** 17. kolovoza 2026.
**Recenzent:** Nezavisni akademsko-tehnički validator (uloga: strogi recenzent)

---

## 1. SAŽETAK OCJENE (SCORECARD)

| Kriterij | Ocjena | Status |
|---|---|---|
| Usklađenost sa zadatkom | 92% | Zadovoljava |
| Matematička i inženjerska točnost | 78% | Djelomično |
| Vizualizacije i podaci (grafovi/tablice) | 85% | Djelomično |
| Jezik, pravopis i akademski stil | 70% | Djelomično |
| **KONAČNI STATUS** | — | **POTREBNA ZNAČAJNA REVIZIJA** |

**Sažeti komentar:** Rad pokriva sve četiri zadataka s vidljivim inženjerskim razumijevanjem i struktura je logički dosljedna. Zadaci 1, 2 i 3 matematički su egzaktni i numerički verificirani. Međutim, Zadatak 4 sadrži **blokirajuću numeričku grešku** u jednadžbama (5.10)–(5.11) koja ruši vjerodostojnost cijelog poglavlja, a kroz rad su raspršene brojne "AI floskule", napuhani pridjevi i suvišni pasusi koji radu oduzimaju autentičan inženjerski ton. Jezik je općenito dobar, ali nije dosljedno bezličan/passivan, a nekoliko terminoloških i pravopisnih propusta zahtijeva ispravak.

---

## 2. KRITIČNI NEDOSTACI I BLOKIRAJUĆE GREŠKE

### BLOCKER 1 — Netočni elementi matrica prijelaza stanja (Zadatak 4, jednadžbe 5.10 i 5.11)

- **Lokacija:** Poglavlje 5.2, jednadžbe (5.10) i (5.11), stranica 31.
- **Uočeni problem:** Seminar navodi:
  $$
  \Phi_{\text{parno}} \approx \begin{bmatrix} 0.0000 & -0.2122 \\ 1.9099 & 0.0000 \end{bmatrix}, \quad \Phi_{\text{neparno}} \approx \begin{bmatrix} 0.0000 & -1.9099 \\ 0.2122 & 0.0000 \end{bmatrix}
  $$
  $$
  \Phi_{\text{cycle}} \approx \begin{bmatrix} -3.6476 & 0.0000 \\ 0.0000 & -0.0450 \end{bmatrix}
  $$
- **Zašto je pogrešno:** Matrica $A_{\text{parno}}$ ima svojstvene vrijednosti $-1 \pm j\pi/2$. Za $t=1$ s, analitička formula glasi:
  $$
  e^{A_{\text{parno}} \cdot 1} = e^{-1}\left[\cos\!\left(\tfrac{\pi}{2}\right)I + \frac{\sin(\pi/2)}{\pi/2}(A_{\text{parno}}+I)\right] = e^{-1}\cdot\frac{2}{\pi}(A_{\text{parno}}+I)
  $$
  Uvrštavanjem:
  - $(A_{\text{parno}}+I)_{12} = -\pi/6 \;\Rightarrow\; e^{-1}\cdot\frac{2}{\pi}\cdot\frac{\pi}{6} = \frac{e^{-1}}{3} \approx 0.1226$
  - $(A_{\text{parno}}+I)_{21} = 3\pi/2 \;\Rightarrow\; e^{-1}\cdot\frac{2}{\pi}\cdot\frac{3\pi}{2} = 3e^{-1} \approx 1.1036$

  Numerička verifikacija (`scipy.linalg.expm`) daje:
  $$
  \Phi_{\text{parno}} = \begin{bmatrix} 0 & -0.1226 \\ 1.1036 & 0 \end{bmatrix}, \quad \Phi_{\text{neparno}} = \begin{bmatrix} 0 & -1.1036 \\ 0.1226 & 0 \end{bmatrix}
  $$
  Seminarske vrijednosti su za faktor $\sqrt{3}\approx 1.732$ veće od točnih. Posljedično, elementi $\Phi_{\text{cycle}}$ su za faktor $3$ veći ($-3.6476$ umjesto $-1.2180$, $-0.0450$ umjesto $-0.0150$).
- **Konkretan ispravak:**
  $$
  \Phi_{\text{parno}} \approx \begin{bmatrix} 0.0000 & -0.1226 \\ 1.1036 & 0.0000 \end{bmatrix}, \quad \Phi_{\text{neparno}} \approx \begin{bmatrix} 0.0000 & -1.1036 \\ 0.1226 & 0.0000 \end{bmatrix}
  $$
  $$
  \Phi_{\text{cycle}} = \Phi_{\text{neparno}}\Phi_{\text{parno}} \approx \begin{bmatrix} -1.2180 & 0.0000 \\ 0.0000 & -0.0150 \end{bmatrix}
  $$
- **Napomena:** Svojstvene vrijednosti monodromijske matrice ($\lambda_1 \approx -1.2180$, $\lambda_2 \approx -0.0150$) i spektarni radijus $\rho \approx 1.2180 > 1$ su **slučajno točni** jer greška u elementima ne utječe na dijagonalnost matrice $\Phi_{\text{cycle}}$ (ostaje dijagonalna). Ipak, netočni elementi ruše vjerodostojnost izvođenja i moraju se ispraviti jer recenzent to nužno primjećuje.

### BLOCKER 2 — Nekonzistentnost između dva sintetizirana regulatora (Zadatak 4, jednadžba 5.24 i 5.25–5.27)

- **Lokacija:** Poglavlje 5.5, jednadžba (5.24) i Poglavlje 5.5.1, jednadžbe (5.25)–(5.27).
- **Uočeni problem:** U jednadžbi (5.24) navode se dva različita regulatora:
  - CVXPY rješenje: $K = [-2.7120,\; 0.0926]$
  - YALMIP "referentno": $K = [-3.7097,\; 0.0000]$
  Zatim jednadžbe (5.25)–(5.27) koriste **samo CVXPY K** za izračun zatvorenog kruga ($A_{\text{cl,parno}} = A_{\text{parno}} + BK$ s $K_{11}=-3.7120$), ali tekst eksplicitno kaže "Referentno YALMIP pojaanje iznosi $K = [-3.7097, 0.0000]$, koje također u potpunosti zadovoljava LMI sustav" — bez da se za njega izračunaju i prikažu svojstvene vrijednosti zatvorenog kruga.
- **Zašto je pogrešno:** Numerička verifikacija pokazuje da YALMIP $K=[-3.7097, 0]$ daje **realne** svojstvene vrijednosti zatvorenog kruga $\lambda \approx -3.841,\; -1.868$ (oba realna, negativna), dok CVXPY $K=[-2.712, 0.0926]$ daje kompleksni par $\lambda \approx -2.356 \pm 0.439j$ (parni) odnosno $-2.356 \pm 0.762j$ (neparni). Seminar u (5.27) navodi kompleksne vrijednosti $-2.356 \pm 0.4387j$ i $-2.356 \pm 0.7617j$, što odgovara CVXPY K, ali to nije eksplicitno jasno označeno. Čitatelj ne zna kojem K pripadaju navedeni rezultati.
- **Konkretan ispravak:** U jednadžbi (5.25) eksplicitno napisati "za $K = [-2.7120,\; 0.0926]$ (CVXPY rješenje)" i dodati zasebnu tablicu ili pasus s rezultatima za YALMIP $K = [-3.7097,\; 0.0000]$:
  - $A_{\text{cl,parno}}^{\text{YALMIP}} = \begin{bmatrix} -4.7097 & -0.5236 \\ 4.7124 & -1.0000 \end{bmatrix}$, $\lambda \approx -3.841,\; -1.868$
  - $A_{\text{cl,neparno}}^{\text{YALMIP}} = \begin{bmatrix} -4.7097 & -4.7124 \\ 0.5236 & -1.0000 \end{bmatrix}$, $\lambda \approx -3.841,\; -1.868$
  - $\rho(\Phi_{\text{cl,cycle}}^{\text{YALMIP}}) \approx 0.0551$

### NEDOSTATAK 3 — Mjerne jedinice u tablici 4.1 nisu dosljedne

- **Lokacija:** Tablica 4.1, stranica 21.
- **Uočeni problem:** Stupac "Ukupni trošak $J^*$ [$\text{m}^2$]" je dimenzijski točan ($\int |y-h|\,dx$ ima jedinicu $[\text{m}\cdot\text{m}] = [\text{m}^2]$). Međutim, stupci "Iskop [$\text{m}^2$]" i "Nasip [$\text{m}^2$]" predstavljaju površine iskopa i nasipa, ali u formulaciji (4.1) kriterij je $\int |y-h|\,dx$ — to je površina (2D), ne volumen (3D). U građevinskoj praksi "količina materijala" je volumen $[\text{m}^3]$, a ne površina. Seminar u uvodu Poglavlja 4.1 kaže "Trošak izrade ceste proporcionalan je količini materijala (zemlje) kojeg treba oduzeti (otkopati) ili dodati" — količina = volumen. No funkcija cilja (4.1) daje površinu. Nedostaje eksplicitna napomena da je pretpostavka jedinične širine ceste ($w=1$ m), pa je volumen $= w \cdot J^*$.
- **Konkretan ispravak:** Dodati u Poglavlje 4.1 rečenicu: "Pretpostavlja se jedinična širina ceste ($w = 1$ m), čime se ukupni volumen zemljanih radova svodi na površinu poprečnog presjeka $J = \int_0^L |y(x)-h(x)|\,dx$ izraženu u $[\text{m}^2]$."

### NEDOSTATAK 4 — Zaključak ne odgovara izravno na sva pitanja iz uvoda

- **Lokacija:** Poglavlje 6.1, stranice 30–31.
- **Uočeni problem:** Zaključak daje sažetak po zadacima, ali ne sadrži eksplicitan odgovor na pitanje iz Zadatka 1f (osjetljivost na perturbacije $b_1$ i $b_2$) u sintetičkom obliku, niti na pitanje iz Zadatka 3 o klasi optimizacijskog problema (LP). Također, Zadatak 4 pita "Je li ovaj sustav stabilan?" (b) — odgovor u zaključku je implicitan kroz $\rho > 1$, ali nije eksplicitno formuliran kao "Sustav nije stabilan".
- **Konkretan ispravak:** U zaključku dodati eksplicitne jednostavne odgovore: "Zadatak 1f: $p^*$ je osjetljiva na perturbacije $b_1$ s gradijentom $-\mu_1^* = -12.242$, a neosjetljiva na perturbacije $b_2$ ($\mu_2^*=0$)." i "Zadatak 3: Problem pripada klasi linearnog programiranja (LP)."

---

## 3. ANALIZA GRAFOVA, SLIKA I TABLICA

### Slika 2.1 — Geometrija QP problema, nivo-krivulje i KKT ravnoteža gradijenata
- **Opravdanost:** Opravdano — vizualizira dopustivi skup, nivo-krivulje i gradijente u KKT točki.
- **Tehnička ispravnost:** Osi su označene samo s $x_1$, $x_2$ — **bez mjernih jedinica**. Budući da su $x_1, x_2$ bezdimenzionalne projektne varijable, to je prihvatljivo, ali bi trebalo eksplicitno naglasiti da su varijable bezdimenzionalne. Legenda je prisutna i čitljiva.
- **Kvaliteta interpretacije u tekstu:** Dobra — pasus ispod slike eksplicitno komentira kolinearnost $\nabla f$ i $\nabla g_1$ i daje fizikalnu interpretaciju "ravnoteže sila".
- **Potrebna dorada:** Dodati napomenu o bezdimenzionalnosti varijabli; razmotriti prikaz $\nabla g_2$ iako je neaktivno (radi potpunosti).

### Slika 2.2 — Nivo-krivulje dualne funkcije $g(\mu_1, \mu_2)$
- **Opravdanost:** Opravdano — vizualizira konkavnost dualne funkcije i lokaciju $\mu^*$.
- **Tehnička ispravnost:** Osi $\mu_1, \mu_2$ bez jedinica (Lagrangeovi množitelji su bezdimenzionalni — prihvatljivo). Legenda prisutna.
- **Kvaliteta interpretacije:** Dobra — tekst ispod slike opisuje metodu rješavanja (`fmincon`) i rezultat.
- **Potrebna dorada:** Minimalna — eventualno označiti nivo-krivulje vrijednostima funkcije cilja.

### Slika 2.3 — Analiza osjetljivosti $p^*(b_1 + \Delta b_1)$
- **Opravdanost:** Opravdano — vizualno verificira teorem osjetljivosti.
- **Tehnička ispravnost:** Osi: "Perturbacija desne strane $\Delta b_1$" (bez jedinice — $b_1$ je bezdimenzionalan, prihvatljivo) i "Optimalna vrijednost $p^*$" (bez jedinice — $f(x)$ je bezdimenzionalna, prihvatljivo). Legenda prisutna.
- **Kvaliteta interpretacije:** Dobra — tekst daje numeričku verifikaciju s $\Delta b_1 = 10^{-4}$ i odstupanje $6.75\times 10^{-5}$.
- **Potrebna dorada:** Minimalna.

### Slika 3.1 — Robusni dopustivi skup i Monte Carlo ovojnica
- **Opravdanost:** Opravdano — ključna vizualizacija robusnog pristupa.
- **Tehnička ispravnost:** Osi $x_1, x_2$ bez jedinica (prihvatljivo). Legenda detaljna i čitljiva. Prikazano 100 realizacija, nominalne i robusne granice, te obje optimalne točke.
- **Kvaliteta interpretacije:** Vrlo dobra — tekst ispod detaljno opisuje sve elemente slike i tablicu 3.1.
- **Potrebna dorada:** Minimalna — eventualno povećati oznake točaka $x_{\text{nom}}^*$ i $x_{\text{rob}}^*$.

### Slika 3.2 — Pomak točke optimuma i cijena robusnosti
- **Uočeni problem:** U PDF-u slika 3.2 prikazuje se kao tekstualni opis "[Graph: Contour plot showing the shift from nominal optimum to robust optimum...]" umjesto stvarnog grafa. Ovo ukazuje na to da graf nije pravilno renderiran ili je ubačen kao placeholder.
- **Potrebna dorada:** Osigurati da slika 3.2 bude stvarni contour plot s nivo-krivuljama $f(x)$, nominalnim i robusnim ograničenjima, te obje optimalne točke s označenim $\Delta f^*$.

### Slike 4.1 i 4.2 — Optimalni uzdužni profil ceste
- **Opravdanost:** Opravdano — ključni rezultati Zadatka 3.
- **Tehnička ispravnost:** Osi: "Udaljenost $x$ [m]" i visina $y(x)$ [m] (iz naslova). Legenda prisutna s oznakama terena, nivelacije za $N=20$ i $N=100$, te zonama iskopa/nasipa.
- **Kvaliteta interpretacije:** Dobra — tekst u 4.5 analizira utjecaj $N$ i $b_2$.
- **Potrebna dorada:** Provjeriti je li os y-koordinate eksplicitno označena s "Visina $y(x)$ [m]" (u PDF ekstraktu nije jasno vidljivo).

### Slika 4.3 — Provjera ograničenja prvog reda (nagib)
- **Opravdanost:** Opravdano — verificira zadovoljenje ograničenja $|y'|\le b_1$.
- **Tehnička ispravnost:** Osi: "Udaljenost $x$ [m]" i "Nagib ceste $y'(x)$ [m/m]". Jedinica [m/m] je tehnički točna (nagib je bezdimenzionalan, ali se često piše [m/m] ili [%]). Legenda prisutna s granicom $\pm b_1$.
- **Kvaliteta interpretacije:** Nedovoljna — tekst ne komentira ovu sliku eksplicitno (samo u 4.5 općenito).
- **Potrebna dorada:** Dodati 1-2 rečenice ispod slike: "Na slici 4.3 vidi se da nagib $y'(x)$ u oba slučaja ostaje unutar granica $\pm 0.5$, uz povremeno zasićenje na gornjoj granici $+0.5$ u zoni uspona."

### Slika 4.4 — Provjera ograničenja drugog reda (zakrivljenost)
- **Opravdanost:** Opravdano — ključno za provjeru aktivnosti ograničenja $b_2$.
- **Tehnička ispravnost:** Osi: "Udaljenost $x$ [m]" i "Zakrivljenost $y''(x)$" — **bez eksplicitne jedinice** u osi. Treba biti [m$^{-1}$] (kako je navedeno u tekstu i tablici 4.1). Legenda prisutna s granicama $\pm b_2$.
- **Kvaliteta interpretacije:** Dobra — tekst ispod slike komentira zasićenje u Slučaju B na $\pm 0.2$.
- **Potrebna dorada:** Dodati jedinicu [m$^{-1}$] na os y-koordinate.

### Slika 5.1 — Simulacija otvorenog kruga (divergencija)
- **Opravdanost:** Opravdano — vizualno dokazuje nestabilnost.
- **Tehnička ispravnost:** Osi: "Vrijeme $t$ [s]" i "Varijabla stanja $x_1(t), x_2(t)$" (bez jedinice — $x$ je bezdimenzionalno, prihvatljivo). Fazni portret s osima $x_1, x_2$.
- **Kvaliteta interpretacije:** Dobra — tekst komentira "ekspandirajuću spiralu" i mehanizam ubacivanja energije.
- **Potrebna dorada:** Minimalna.

### Slika 5.2 — Simulacija zatvorenog kruga (stabilizacija)
- **Opravdanost:** Opravdano — ključni rezultat Zadatka 4.
- **Tehnička ispravnost:** Osi s jedinicama [s] i bezdimenzionalnim $x$. Nivo-elipse Ljapunova prikazane.
- **Kvaliteta interpretacije:** Dobra — tekst opisuje konvergenciju unutar 3 s i sijecanje nivo-elipsa.
- **Potrebna dorada:** Razjasniti kojem K odgovara prikaz (CVXPY ili YALMIP).

### Slika 5.3 — Disipacija energije Ljapunova
- **Opravdanost:** Opravdano — dokazuje eksponencijalnu stabilnost.
- **Tehnička ispravnost:** Logaritamska os y, jedinica $V(x(t))$ (bezdimenzionalno). Eksponencijalna ovojnica $V_0 e^{-\alpha t}$ s $\alpha = 0.85$.
- **Kvaliteta interpretacije:** Dobra — tekst komentira strogo monoton pad bez skokova.
- **Potrebna dorada:** Navesti kako je $\alpha = 0.85$ određeno (teorijski iz LMI-ja ili empirijski).

### Tablica 2.1 — Usporedba analitičkih i numeričkih rezultata
- **Opravdanost:** Opravdano — ključna verifikacija Zadatka 1.
- **Tehnička ispravnost:** Sve vrijednosti su numerički verificirane i točne ($x^* = 190/33$, $\mu_1^* = 404/33$, $p^* = 2000/33$).
- **Potrebna dorada:** Minimalna — eventualno dodati stupac s relativnom pogreškom.

### Tablica 3.1 — Monte Carlo provjera dopustivosti
- **Opravdanost:** Opravdano — empirijska verifikacija robusnosti.
- **Tehnička ispravnost:** Rezultati konzistentni (57% nedopustivosti nominalnog, 0% robusnog).
- **Potrebna dorada:** Navesti seed za generator slučajnih brojeva (u MATLAB kodu je `rng(42)`) radi reproducibilnosti.

### Tablica 4.1 — Numerički rezultati nivelacije ceste
- **Opravdanost:** Opravdano — sažeti prikaz svih 4 slučaja.
- **Tehnička ispravnost:** Zbrojevi iskop+nasip podudaraju se s $J^*$ u svim redcima (verificirano). Jedinica [m$^2$] za $J^*$ je točna uz pretpostavku jedinične širine.
- **Potrebna dorada:** Dodati napomenu o pretpostavci jedinične širine ceste (vidi Nedostatak 3).

---

## 4. JEZIČNE, STILSKE I "HUMAN-WRITTEN" KOREKCIJE

| Lokacija / Izvorni tekst | Vrsta problema | Predloženi ispravak |
|---|---|---|
| §1, "Matematičko optimiranje i teorija sustava čine temelj suvremenog inženjerskog projektiranja..." | AI floskula — napuhani, generički uvod | Skratiti na: "Optimizacijske metode su temelj suvremenog inženjerskog projektiranja i analize dinamičkih sustava [1,2]." |
| §1, "razvoj optimizacijskih metoda doživio je ključnu promjenu paradigme" | Suvišni pridjev "ključnu" + metafora | "razvoj optimizacijskih metoda prolazi kroz promjenu paradigme" |
| §1, "iznimno efikasnih, polinomijalno složenih algoritama" | Suvišni pridjev "iznimno" | "efikasnih, polinomijalno složenih algoritama" |
| §1.2, "matematički i numerički rigorozno obrađene inženjerske cjeline" | AI samohvala — "rigorozno" | "obrađene inženjerske cjeline" |
| §2.1.1, "Uvrštavanjem se potvrđuje identitet" | Suvišna metakomentarska fraza | Izbrisati rečenicu — identitet je očigledan iz jednadžbe (2.9) |
| §2.1.2, "Stoga je dopustivo područje $\mathcal{F}$ konveksan poliedar." | Terminologija: "poliedar" vs "poliedar" | Prihvatljivo, ali dosljedno koristiti "poliedar" (ili "polieder") kroz cijeli rad |
| §2.4, "Uočava se savršena kolinearnost suprotnog smjera" | Suvišni pridjev "savršena" | "Uočava se kolinearnost suprotnog smjera" |
| §2.4, "Fizička interpretacija ovog uvjeta odgovara ravnoteži sila" | Dobra analogija, ali "Fizička" je neformalna | "Mehanička interpretacija ovog uvjeta odgovara ravnoteži sila" ili ostaviti bez "Fizička" |
| §2.7.1, "Množitelj $\mu_1^* = 12.2424$ ima ulogu cijene u sjeni (shadow price)" | Anglizam u zagradi nepotreban ako je hrvatski termin jasan | Ostaviti "cijene u sjeni" bez engleskog u zagradi, ili obrnuto |
| §3.1, "U stvarnim inženjerskim primjenama parametri optimizacijskog modela... rijetko su egzaktno poznati." | AI floskula — generički uvod u poglavlje | Skratiti: "Parametri optimizacijskog modela često nisu egzaktno poznati zbog mjernih pogrešaka i tolerancija [3,4]." |
| §3.1, "Oni podliježu mjernim pogreškama, tolerancijama izrade i promjenama radnih uvjeta." | Ponavljanje iste ideje drugim riječima | Spojiti s prethodnom rečenicom |
| §3.5, "Uvođenje zahtjeva za robusnošću neumitno povlači određenu konzervativnost" | Suvišni pridjev "neumitno" + književni ton | "Uvođenje zahtjeva za robusnošću povlači konzervativnost" |
| §3.5, "predstavlja inženjersku premiju osiguranja koja jamči apsolutnu operativnu sigurnost i izostanak kršenja ograničenja pod svim mogućim varijacijama" | AI napuhavanje — "apsolutnu", "svim mogućim" | "predstavlja premiju koja jamči dopustivost pod svim varijacijama parametara unutar zadanog skupa nesigurnosti" |
| §4.1, "U građevinarstvu i prometnom inženjerstvu projektiranje uzdužnog profila prometnice predstavlja temeljni optimizacijski zadatak." | AI floskula — generički uvod | Skratiti ili izbrisati; izravno prijeći na formulaciju |
| §4.1, "uz istovremeno strogo zadovoljavanje prometno-tehničkih standarda" | Suvišno "strogo" | "uz zadovoljavanje prometno-tehničkih standarda" |
| §4.5, "Fina mreža omogućuje vjernije praćenje lokalnih promjena bez numeričkog 'peglanja' na gruboj skali." | Kolokvijalizam "peglanja" | "Fina mreža omogućuje vjernije praćenje lokalnih promjena bez numeričkog zaglađivanja na gruboj skali." |
| §5.2, "Jedan od najintrigantnijih fenomena u teoriji hibridnih sustava jest da..." | AI floskula — "najintrigantnijih" | "Poznati fenomen u teoriji hibridnih sustava je da..." |
| §5.2, "Slika 5.1 zorno prikazuje nestabilnost otvorenog kruga" | Suvišni pridjev "zorno" | "Slika 5.1 prikazuje nestabilnost otvorenog kruga" |
| §5.2, "promjena smjera vektorskog polja u trenucima $t = 1, 2, 3, \dots$ ubacuje energiju u sustav" | Neprecizno — "ubacuje energiju" je metafora | "promjena smjera vektorskog polja u trenucima $t = 1, 2, 3, \dots$ povećava normu stanja" |
| §5.6, "Kao što je prikazano na slici 5.2, stanja $x_1(t)$ i $x_2(t)$ brzo i glatko konvergiraju" | Suvišni pridjevi "brzo i glatko" | "Stanja $x_1(t)$ i $x_2(t)$ konvergiraju prema ishodištu unutar prvih 3 s." |
| §5.6, "strogo monoton pad krivulje bez skokova na prijelazima modova potvrđuje postojanje jedinstvene zajedničke funkcije Ljapunova" | Dobra rečenica, ali "jedinstvene" je suvišno | "strogo monoton pad krivulje potvrđuje postojanje zajedničke funkcije Ljapunova" |
| §6.2, "Rad demonstrira snagu i fleksibilnost konveksne optimizacije u inženjerskom modeliranju" | AI samohvala | "Rad pokazuje primjenjivost konveksne optimizacije u inženjerskom modeliranju" |
| §6.2, "Kao logičan nastavak ovog rada u inženjerskoj praksi predlaže se" | AI floskula | "Mogući nastavak rada je" |
| §1, naslov "Taksonomija konveksnih optimizacijskih problema" | Pretenciozan naslov za kratki popis | "Klase optimizacijskih problema" |
| Kroz cijeli rad | Miješanje "dopustivi skup" i "dopustivo područje" | Dosljedno koristiti "dopustivi skup" |
| §2.3, naslov "Analitičko rješavanje KKT sustava (4 kombinacije aktivnih skupova)" | "aktivnih skupova" je anglicizam od "active sets" | "Analitičko rješavanje KKT sustava (4 kombinacije aktivnih ograničenja)" |
| §4.3, "epigrafske pomoćne varijable (engl. slack variables)" | "slack variables" nije epigrafske već pomoćne/izravnavajuće | "pomoćne varijable (engl. slack variables)" — "epigrafske" je ovdje netočan termin; epigraf je koncept iz konveksne analize, ne LP |
| §5.4, "kongruentnu transformaciju" | Točan termin, ali provjeriti je li "kongruentna" standardna u hrvatskoj literaturi | Prihvatljivo; alternativa "kongruencijska transformacija" |
| §2.3.2, "Slučaj 1 odbacuje kao primarno nedopustiv" | Gramatika: treba "odbacuje se" | "Slučaj 1 se odbacuje kao primarno nedopustiv" |
| §3.4, "Uočava se da nominalno rješenje... krši ograničenja u čak 57% slučajnih realizacija jer leži točno na nominalnoj granici." | "čak" je suvišni emfatični pridjev | "Uočava se da nominalno rješenje krši ograničenja u 57% slučajnih realizacija jer leži na nominalnoj granici." |
| §4.5, "asimptotski konvergira" | Pravopis: "asimptotski" → "asimptotski" je netočno | "asimptotski" treba biti "asimptotski" (provjeriti; standardni oblik je "asimptotski") — zapravo je "asimptotski" točan oblik, ali čest je i "asimptotski"; provjeriti u Rječniku |
| §4.5, "Fina mreža omogućuje" | "omogućuje" vs "omogućava" — oba prihvatljiva, ali dosljednost | Dosljedno koristiti jedan oblik kroz cijeli rad |

---

## 5. KORAK-PO-KORAK AKCIJSKI PLAN ZA POPRAVAK

### Prioritet 1: Blokirajuće greške (mora se ispraviti prije predaje)

1. **Ispraviti jednadžbe (5.10) i (5.11):** Zamijeniti netočne elemente matrica $\Phi_{\text{parno}}$, $\Phi_{\text{neparno}}$ i $\Phi_{\text{cycle}}$ točnim vrijednostima:
   - $\Phi_{\text{parno}} = \begin{bmatrix} 0 & -0.1226 \\ 1.1036 & 0 \end{bmatrix}$
   - $\Phi_{\text{neparno}} = \begin{bmatrix} 0 & -1.1036 \\ 0.1226 & 0 \end{bmatrix}$
   - $\Phi_{\text{cycle}} = \begin{bmatrix} -1.2180 & 0 \\ 0 & -0.0150 \end{bmatrix}$
   Svojstvene vrijednosti i $\rho$ ostaju kako su napisani (točni su).

2. **Razjasniti koji K se koristi u (5.25)–(5.30):** Eksplicitno označiti da se zatvoreni krug računa s CVXPY $K = [-2.7120, 0.0926]$. Dodati zasebnu tablicu ili pasus s rezultatima za YALMIP $K = [-3.7097, 0]$ (svojstvene vrijednosti i $\rho_{\text{cl}}$).

3. **Ispraviti sliku 3.2:** Osigurati da slika 3.2 bude stvarni contour plot, a ne tekstualni placeholder.

### Prioritet 2: Sadržajne dorade

4. **Dodati pretpostavku jedinične širine ceste** u Poglavlje 4.1 (vidi Nedostatak 3).

5. **Dodati eksplicitne odgovore** na pitanja iz zadatka u zaključku (vidi Nedostatak 4): osjetljivost na $b_1, b_2$; klasa problema (LP); stabilnost otvorenog kruga ("nije stabilan").

6. **Dodati jedinicu [m$^{-1}$]** na os y-koordinate slike 4.4.

7. **Dodati komentar ispod slike 4.3** (1-2 rečenice o zasićenju nagiba).

8. **Navesti seed `rng(42)`** u tablici 3.1 ili tekstu ispod nje.

### Prioritet 3: Jezično poliranje i uklanjanje AI stila

9. **Ukloniti sve AI floskule i napuhnute pridjeve** navedene u tablici iz Odjeljka 4 (sistematno pretražiti kroz cijeli rad: "iznimno", "savršena", "zorno", "neumitno", "apsolutnu", "najintrigantnijih", "čak", "strogo" gdje nije nužno).

10. **Skratiti generičke uvodne pasuse** u Poglavlju 1, Poglavlju 3.1 i Poglavlju 4.1 — ukloniti ponavljanje iste ideje drugim riječima.

11. **Postići dosljednost terminologije:** "dopustivi skup" (ne "dopustivo područje"), "aktivnih ograničenja" (ne "aktivnih skupova"), "asimptotski" (dosljedno).

12. **Ispraviti "epigrafske pomoćne varijable"** u "pomoćne varijable" — "epigrafske" je ovdje netočan termin za LP slack varijable.

13. **Provjeriti pasivni/bezlični stil:** Zamijeniti oblike poput "Uočava se", "Provjeravamo" s bezličnim "Uočeno je", "Provjereno je" gdje je prikladno (iako je "Uočava se" prihvatljivo kao bezlična konstrukcija).

14. **Konačna lektura:** Pročitati cijeli rad naglas i ukloniti preostale kolokvijalizme ("peglanja", "ubacuje energiju") i emfatične konstrukcije.

---

## DODATAK: Sažeti komentar o kvaliteti rada

Rad je tehnički ambiciozan i pokriva sve zadatke s vidljivim razumijevanjem optimizacijskih metoda. Zadaci 1, 2 i 3 su izvedeni s visokom matematičkom preciznošću — svi analitički izvodi su egzaktni, numerička verifikacija je provedena u dva neovisna okruženja (MATLAB i Python), a rezultati se podudaraju do na $10^{-8}$. LP formulacija Zadatka 3 je elegantna i ispravno izvedena.

Slabost je koncentrirana u Zadatku 4, gdje su elementi matrica prijelaza netočni (faktor $\sqrt{3}$ i $3$), iako su svojstvene vrijednosti slučajno točne. Ovo ukazuje na to da je autor vjerojatno ručno prepisao/računao elemente matrica s pogrešnim skaliranjem, ali je spektarnu analizu proveo ispravno (možda izravno preko `eig(expm(A))` u MATLAB-u). Greška je lako ispravljiva, ali recenzent je nužno primjećuje.

Stilski, rad pati od tipičnih "AI" obrazaca: napuhanih uvoda, suvišnih pridjeva, metafora ("ravnoteža sila", "ubacuje energiju") i ponavljanja. Uklanjanje ovih elemenata i skraćivanje za ~15-20% teksta značajno bi poboljšalo autentičnost i čitljivost. Preporuka je da autor prođe kroz rad s fokusom na konciznost i bezlični tehnički ton.

**Nakon ispravka Prioriteta 1 i 2 te jezičnog poliranja (Prioritet 3), rad bi bio spreman za ocjenu "potreban manje korekcije" ili "odobreno".**
