Rad je matematički i programski vrlo dobro odrađen, u skladu sa zadanim zadacima; glavne dorade koje su potrebne odnose se na jezik, stil (smanjiti “paperski/AI” ton) i nekoliko manjih tehničkih nedosljednosti između teksta i koda.

---

## 1. SAŽETAK OCJENE (SCORECARD)

**Usklađenost sa zadatkom: 95% — Zadovoljava**

Sva četiri zadatka iz originalnog teksta su pokrivena, s jasnim mapiranjem: poglavlje 2 ≙ Zadatak 1 (QP, KKT, dualnost, osjetljivost), poglavlje 3 ≙ Zadatak 2 (robusni QP s intervalnom nesigurnošću), poglavlje 4 ≙ Zadatak 3 (nivelacija ceste, LP formulacija, četiri slučaja), poglavlje 5 ≙ Zadatak 4 (sklopni sustav, monodromijska matrica, LMI, regulator).

Nedostaju jedino vrlo kratke, eksplicitne rečenice koje bi vezale pojedine matematičke rezultate direktno uz svaku podtočku zadatka (npr. (1a)–(1f)).

**Matematička i inženjerska točnost: 92% — Zadovoljava**

Dokaz stroge konveksnosti (Hesseova matrica, svojstvene vrijednosti), KKT analiza po slučajevima, dualni problem i osjetljivost u Zadatku 1 konzistentni su s kodom u MATLAB-u i Pythonu. Formulacija robusnog QP-a preko 8 vrhova poliedra nesigurnosti, LP formulacija nivelacije ceste (epigraf, ograničenja nagiba i zakrivljenosti) te LMI postavka za sklopni sustav, uz numeričnu sintezu regulatora, također su korektni i dosljedno implementirani.

Uočen je manji, ali stvarni bug u MATLAB kodu za Zadatak 4 pri ispisu svojstvenih vrijednosti zatvorenog kruga.

**Vizualizacije i podaci (grafovi/tablice): 90% — Zadovoljava**

Struktura slika i tablica u popisu (2.1–5.3, 2.1–4.1) logično prati tekst; grafovi su generirani s jasnim naslovima i legendama, osi su većinom označene, a interpretacije u tekstu su tehničke (npr. geometrija QP, cijena robusnosti, fleksibilnost/krutost ceste, divergencija i stabilizacija sklopnog sustava).

Potrebno je dosljedno dodati mjerne jedinice gdje se radi o fizikalnim veličinama (npr. profil ceste, vrijeme, “volumen zemljanih radova”).

**Jezik, pravopis i akademski stil: 70% — Djelomično**

Tekst je gramatički dobar i terminološki precizan, ali uvod i zaključak sadrže dosta “paperskih” i pomalo generičkih fraza koje ostavljaju “AI” dojam. Ton je više nalik časopisnom preglednom radu nego klasičnom seminarskom izvješću; stil je moguće zadržati stručnim, ali kondenzirati i učiniti neposrednijim.

**KONAČNI STATUS: POTREBNE MANJE KOREKCIJE**

Nema blokirajućih matematičkih grešaka koje bi rušile rezultate; potrebno je ispraviti jedan programski bug, dosljedno označiti jedinice na grafovima gdje je primjenjivo te reducirati i naturalizirati uvodne/zaključne dijelove da zvuče kao human-written tehnički tekst.

---

## 2. KRITIČNI NEDOSTACI I BLOKIRAJUĆE GREŠKE

### 2.1. MATLAB – Zadatak 4: pogrešno računanje svojstvenih vrijednosti zatvorenog kruga

U kodu se svojstvene vrijednosti zatvorenog kruga računaju pozivom `eig(Acl_even(1))` i `eig(Acl_odd(1))` umjesto `eig(Acl_even)` i `eig(Acl_odd)`, tj. funkcija `eig` se primjenjuje na skalarni element matrice, a ne na matricu sustava.

**Zašto je pogrešno:** Analiza stabilnosti zatvorenog kruga u tekstu (hurwitzovost modova) pretpostavlja korektnu spektralnu analizu; ako se netko osloni isključivo na MATLAB ispis, mogao bi zaključke o stabilnosti temeljiti na pogrešnim brojevima.

**Ispravak:**

Zamijeniti linije za ispis zatvorenih eigenvrijednosti s:

```matlab
eig_cl_even = eig(Acl_even);
eig_cl_odd = eig(Acl_odd);
fprintf('Closed-loop Mode 1 Eigenvalues: %.4f +/- %.4fj\n', real(eig_cl_even(1)), imag(eig_cl_even(1)));
fprintf('Closed-loop Mode 2 Eigenvalues: %.4f +/- %.4fj\n', real(eig_cl_odd(1)), imag(eig_cl_odd(1)));
```

### 2.2. Tekst – opis ciljne funkcije u Zadatku 3

Tekst govori o “trošku proporcionalnom količini materijala (zemlje) kojeg treba oduzeti ili dodati”, dok je u kodu ciljna funkcija definirana kao integral ukupne apsolutne devijacije \( |y(x)-h(x)| \), tj. ukupni volumen zemljanih radova bez eksplicitnog razdvajanja iskopa i nasipa u funkciji cilja (oni se naknadno analiziraju, ali nisu zasebni ciljevi).

**Zašto je potencijalno zbunjujuće:** Čitatelju može izgledati kao da je definiran složeniji troškovni funkcional (npr. različiti koeficijenti za iskop i nasip), dok se zapravo minimizira ukupna apsolutna devijacija (iskop + nasip) jednako.

**Ispravak:**

U poglavlju 4 eksplicitno napisati da se kao trošak uzima integral \( \int_0^L |y(x)-h(x)|\,dx \), tj. ukupna količina materijala koja se premješta (iskop + nasip), i naglasiti da se eventualna različita cijena iskopa/nasipa ovdje ne modelira nego se pretpostavlja jednaki ponder.

### 2.3. Tekst – preambule i zaključak

Uvod i zaključak sadrže višak meta-komentara i “paperskih” fraza tipa “promjena paradigme”, “snaga i fleksibilnost konveksne optimizacije”, “moćan matematički aparat”, “matematički i numerički rigorozno obrađene inženjerske cjeline”. To daje blagi “AI generički” dojam.

**Ispravak:**

Skraćivanje uvoda na kraći, konkretan opis konveksne vs. nekonveksne optimizacije i jasnu mapu poglavlja bez pridjeva “rigorozno”, “snaga”, “ključna paradigma”; zaključak usmjeriti na rezime ključnih numeričkih nalaza po zadacima i jednu-dvije konkretne smjernice za praksu, bez generičkih sugestija tipa “Tube MPC”, “adaptivni LMI regulator” ako nisu direktno povezane s dobivenim rezultatima.

---

## 3. ANALIZA GRAFOVA, SLIKA I TABLICA

### 3.1. QP geometrija, dualna površina, osjetljivost

Geometrijski graf QP problema (dopustivi skup, granice \(g_1, g_2\), nesputani minimum i KKT točka \(x^*\)) je dobro postavljen i izravno povezan s analitičkim izrazima u tekstu. Dualna površina i graf osjetljivosti potvrđuju rezultate o jakoj dualnosti i cijenama u sjeni.

Preporuka: uz Sliku 2.1 eksplicitno navesti da su nivo-krivulje \(f(x)=\text{const}\) elipse proizašle iz pozitivno definitne matrice \(Q\), čime se naglašava jedinstvenost optimuma.

### 3.2. Robusni QP i Monte Carlo ovojnica

Graf robusnog dopustivog skupa s Monte Carlo ovojnicom korektno prikazuje nominalne i robusne granice te 100 realizacija parametara nesigurnosti, što vizualno potvrđuje da robusni optimum ostaje dopustiv za sve realizacije, dok nominalni povremeno krši ograničenja.

Graf “price of robustness” dobro prikazuje pomak između nominalnog i robusnog optimuma, zajedno s promjenom vrijednosti funkcije cilja \(\Delta f^*\).

### 3.3. Nivelacija ceste

Grafovi uzdužnog profila ceste za slučajeve A i B prikazuju prirodni profil \(h(x)\) i optimirani profil \(y(x)\), a grafovi nagiba i zakrivljenosti pokazuju zasićenje na granicama \(\pm b_1\) i \(\pm b_2\). Numerički ispisi maksimalnog nagiba i zakrivljenosti u kodu se slažu s grafičkim prikazima.

Preporuka: dosljedno označiti jedinice na osi visine (npr. [m]) i troška (npr. [m²]).

### 3.4. Sklopni sustav, otvoreni/zatvoreni krug, Ljapunov

Grafovi vremenskog odziva i faznog portreta otvorenog kruga jasno pokazuju divergenciju usprkos hurwitzovosti pojedinačnih modova, što je u skladu s analizom monodromijske matrice. Grafovi zatvorenog kruga, Ljapunovljeve funkcije i energije potvrđuju eksponencijalnu stabilnost sintetiziranog regulatora.

---

## 4. JEZIČNE, STILSKE I "HUMAN-WRITTEN" KOREKCIJE

Primjeri konkretnih stilskih poboljšanja:

- Uvod: umjesto “razvoj optimizacijskih metoda doživio je ključnu promjenu paradigme” jednostavno napisati da se moderni pristup temelji na razlici između konveksnih i nekonveksnih problema.
- Uvod 1.2: umjesto “matematički i numerički rigorozno obrađene inženjerske cjeline” reći da su poglavlja organizirana prema zadacima iz kolegija.
- Zaključak: umjesto “rad demonstrira snagu i fleksibilnost konveksne optimizacije” sažeto navesti da su zadani problemi uspješno formulirani kao LP/QP/LMI i riješeni standardnim rješavačima.

Cilj je zadržati stručni ton, ali ukloniti samohvalu i generičke fraze koje ne donose dodatnu informaciju.

---

## 5. KORAK-PO-KORAK AKCIJSKI PLAN ZA POPRAVAK

1. **Tehničke korekcije koda i teksta**  
   - Ispraviti MATLAB kod za Zadatak 4 tako da se svojstvene vrijednosti zatvorenog kruga računaju nad cijelim matricama \(A_{\text{even}}+BK\) i \(A_{\text{odd}}+BK\).  
   - U poglavlju 4 jasno definirati da se trošak nivelacije računa kao integral apsolutne razlike \( |y(x)-h(x)| \), što odgovara LP formulaciji u implementaciji.

2. **Stilska kondenzacija uvoda i zaključka**  
   - Skratiti uvod na 2–3 odlomka s fokusom na konveksnu optimizaciju i strukturu rada, bez retoričkih fraza.  
   - U zaključku se fokusirati na sažetak numeričkih rezultata po zadacima i jedna–dvije realne smjernice za primjenu u praksi.

3. **Lektura i dosljednost vizualizacija**  
   - Ukloniti podebljanja i pridjeve koji nisu nužni (“rigorozno”, “moćan”, “snaga”).  
   - Provjeriti da su svi grafovi i tablice eksplicitno referencirani u tekstu te da osi fizikalnih veličina imaju jasno naznačene SI jedinice.  
   - Provesti završnu lekturu radi uklanjanja predugačkih rečenica i eventualnih ostataka “AI” stila.
