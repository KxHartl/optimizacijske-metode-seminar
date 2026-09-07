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
