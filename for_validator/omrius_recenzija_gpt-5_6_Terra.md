# Neovisna ultra-striktna recenzija seminara OMRiUS

**Predmet pregleda:** tekst zadatka, PDF seminara i priložene MATLAB datoteke.  
**Granica provjere:** numeričke tvrdnje provjerene su gdje ih je moguće izvesti iz dostavljenog materijala. Priložene datoteke nisu potpuni reproducibilni paket: nedostaju `config_plot`, dijelovi koda za simulacije i grafove te bilo kakav Python izvorni kod. Zato se sve tvrdnje o Pythonu i dijelu MATLAB vizualizacija ne mogu neovisno reproducirati iz priloga.

---

## 1. SAŽETAK OCJENE (SCORECARD)

- **Usklađenost sa zadatkom: 78% — Djelomično.** Sva četiri zadatka obrađena su sadržajno, ali dijelovi traženih MATLAB simulacija i grafova nisu dokazivo pokriveni dostavljenim kodom. Zadatak 4 sadržava i unutarnju numeričku proturječnost.
- **Matematička i inženjerska točnost: 73% — Djelomično.** Zadatci 1–3 većinom su točni, uz nekoliko pogrešnih ili nedovoljno preciznih formulacija. U zadatku 4 matrice prijelaza stanja i monodromijska matrica navedene u jednadžbama (5.10)–(5.11) nisu konzistentne s vlastitim svojstvenim vrijednostima; to je kritična pogreška.
- **Vizualizacije i podaci (grafovi/tablice): 70% — Djelomično.** Skup slika je dobro odabran, ali dio oznaka je suvišno dug, nedostaje jasna provjera izvora podataka, a priloženi MATLAB kod ne generira većinu slika za koje tekst tvrdi da su generirane.
- **Jezik, pravopis i akademski stil: 58% — Djelomično.** Hrvatski je uglavnom razumljiv i terminološki dobar, no tekst je izrazito preopširan, pun promocijskih formulacija, anglizama u zagradama i tvrdnji koje zvuče generički ili strojno. Ton treba svesti na mjerljive tvrdnje i rezultate.
- **KONAČNI STATUS: POTREBNA ZNAČAJNA REVIZIJA.** Rad nije za odbacivanje: jezgra rješenja je dobra. Međutim, prije predaje treba otkloniti pogrešku u zadatku 4, uskladiti rad s kodom i znatno skratiti/tehnički izoštriti prozu.

---

## 2. KRITIČNI NEDOSTACI I BLOKIRAJUĆE GREŠKE (CRITICAL BLOCKERS)

- **[Lokacija: 5.2, jednadžbe (5.10)–(5.13)]**
  - **Uočeni problem:** Navedene pojedinačne matrice prijelaza i monodromijska matrica međusobno su pogrešne/internosno nekonzistentne. U radu stoji
    \[
    \Phi_{\mathrm{parno}}=\begin{bmatrix}0&-0.2122\\1.9099&0\end{bmatrix},\qquad
    \Phi_{\mathrm{neparno}}=\begin{bmatrix}0&-1.9099\\0.2122&0\end{bmatrix},
    \]
    te \(\Phi_{\mathrm{cycle}}=\operatorname{diag}(-3.6476,-0.0450)\), a zatim svojstvene vrijednosti \(-1.2180\) i \(-0.0150\).
  - **Zašto je pogrešno:** Umnožak upravo navedenih matrica daje \(\operatorname{diag}(-3.6476,-0.0450)\), čije su svojstvene vrijednosti upravo \(-3.6476\) i \(-0.0450\), a ne \(-1.2180\) i \(-0.0150\). Za zadane matrice sustava točan izračun eksponencijala daje druge pojedinačne matrice, dok su u radu navedene svojstvene vrijednosti ciklusa slučajno točne.
  - **Konkretan ispravak:** Za trajanje moda \(1\,\mathrm{s}\) treba uvrstiti
    \[
    \Phi_{\mathrm{parno}}=e^{A_{\mathrm{parno}}}=
    \begin{bmatrix}0&-0.122626\\1.103638&0\end{bmatrix},\qquad
    \Phi_{\mathrm{neparno}}=e^{A_{\mathrm{neparno}}}=
    \begin{bmatrix}0&-1.103638\\0.122626&0\end{bmatrix},
    \]
    
    \[
    \Phi_{\mathrm{cycle}}=\Phi_{\mathrm{neparno}}\Phi_{\mathrm{parno}}=
    \begin{bmatrix}-1.218018&0\\0&-0.015037\end{bmatrix}.
    \]
    Tada su svojstvene vrijednosti i spektralni radijus \(\rho(\Phi_{\mathrm{cycle}})=1.218018>1\), pa zaključak o nestabilnosti ostaje valjan. Obavezno regenerirati sliku 5.1 i svaku brojku koja se oslanja na (5.10)–(5.13).

- **[Lokacija: 5.5 i dostavljena datoteka `task4_lmi_switched_stabilization.m`]**
  - **Uočeni problem:** Tekst tvrdi da su izvedene simulacije otvorenog i zatvorenog kruga, izračun energije Ljapunova te grafovi 5.1–5.3. Dostavljeni kod završava nakon ispisa svojstvenih vrijednosti zatvorenog kruga; nema `ode45`, vremenske mreže, preklopne dinamike, faznog portreta, izračuna \(V(x)=x^TPx\) ni izvoza slika.
  - **Zašto je pogrešno:** Rezultati nisu reproducibilni iz priloženog izvornog koda. To nije samo dokumentacijski nedostatak: bez simulacije nije moguće provjeriti da su grafovi doista nastali s matricom \(K\) i matricom \(P\) navedenima u radu.
  - **Konkretan ispravak:** Priložiti stvarni kod za simulaciju kao zasebnu datoteku ili dopuniti skriptu. Funkcija dinamike mora preklapati `A_even` i `A_odd` prema `floor(t)`, imati oblik \(\dot x=(A(t)+BK)x\), te posebno izračunati \(V(t)=x(t)^TPx(t)\). U rad dodati: solver, relativnu/apsolutnu toleranciju, interval simulacije, način obrade diskontinuiteta u trenucima \(t=k\), korišteni \(K\) i korišteni \(P\).

- **[Lokacija: odjeljak 2.5, 3.3, 5.5; prilozi koda]**
  - **Uočeni problem:** Rad navodi verifikaciju u YALMIP-u i Pythonu (`scipy.optimize`, `cvxpy`, `CLARABEL`), ali u prilogu nema Python datoteka. MATLAB skripta za zadatak 1 nema YALMIP dio, a skripta za zadatak 2 nema kod za prikazane slike. `run_all.m` poziva i nedefiniranu funkciju `config_plot()`.
  - **Zašto je pogrešno:** Riječ „verificirano” podrazumijeva da čitatelj može slijediti podatke i reprodukcijski postupak. Trenutačni prilog ne može se pokrenuti kao samostalan paket.
  - **Konkretan ispravak:** Ili (a) priložiti potpuni, pokretljiv repozitorij sa svim `.m` i `.py` datotekama, popisom verzija MATLAB-a/toolboxa/YALMIP-a/rješavača i uputom za pokretanje, ili (b) iz rada ukloniti tvrdnje o alatima za koje kôd nije priložen. `run_all.m` smije prijaviti uspjeh samo ako su provjereni `exitflag` i dostupnost svih ovisnosti.

- **[Lokacija: 4.3, jednadžbe (4.13), (4.17), tablica 4.1]**
  - **Uočeni problem:** Diskretni kriterij (4.13) zapisan je kao \(J_{\mathrm{disc}}=\sum_{i=0}^{N}|y_i-h_i|\), a u kôdu je cilj \(\Delta x\sum_i z_i\). Tablica daje vrijednosti s jedinicom \(\mathrm{m^2}\), što odgovara drugom zapisu, ne prvome.
  - **Zašto je pogrešno:** Bez faktora \(\Delta x\), kriterij ima jedinicu metra i ovisi o gustoći mreže na pogrešan način; s faktorom \(\Delta x\) aproksimira integral i ima jedinicu \(\mathrm{m^2}\). Tekst i implementacija nisu potpuno usklađeni.
  - **Konkretan ispravak:** Jednadžbu napisati kao
    \[
    J_{\mathrm{disc}}(y)=\Delta x\sum_{i=0}^{N}z_i,\qquad z_i\ge |y_i-h_i|.
    \]
    Ako se želi bolja kvadraturna aproksimacija, na krajevima koristiti trapezne težine \(w_0=w_N=1/2\), \(w_i=1\) za unutarnje čvorove. Tada i kôd mora upotrijebiti `f(ny+1:end)=dx*[0.5;ones(N-1,1);0.5]`.

- **[Lokacija: 3.4, tablica 3.1 i tekst nakon nje]**
  - **Uočeni problem:** Iz 0 povreda u 100 Monte Carlo uzoraka izvodi se „100 % pouzdanost” i „zajamčeno”.
  - **Zašto je pogrešno:** Konačan slučajni uzorak ne dokazuje robusnu dopustivost. Jamstvo slijedi iz analitički točno postavljenog robusnog ekvivalenta preko svih vrhova skupa nesigurnosti, ne iz Monte Carlo pokusa.
  - **Konkretan ispravak:** Zamijeniti s: „U svih 100 generiranih uzoraka nije utvrđena povreda. Robusna dopustivost za cijeli intervalni skup slijedi iz zadovoljenja osam vršnih nejednakosti.” U tablici stupac „Robusni status” preimenovati u „Ishod Monte Carlo provjere”; ne pisati „zajamčeno” uz empirijski rezultat.

- **[Lokacija: 3.3, prijelaz na jednadžbe (3.20)–(3.24)]**
  - **Uočeni problem:** Najgori vrhovi reduciraju se uz pretpostavku \(x_1,x_2\ge0\), no obrazloženje da je optimum u tom kvadrantu nije dano prije te redukcije.
  - **Zašto je pogrešno:** Izbor vrha intervalnog skupa ovisi o predznaku svake komponente \(x\). Zaključak je za dobiveno rješenje točan, ali logički redoslijed nije zatvoren.
  - **Konkretan ispravak:** Prvo navesti da kandidirana točka \((6.5,179/34)\) ima pozitivne komponente, potom za taj ortant izvesti (3.20) i (3.21), te na kraju provjeriti svih osam nejednakosti i KKT uvjete aktivnih robusnih ograničenja. Alternativno, zadržati svih osam ograničenja u analitičkoj provjeri i time izbjeći ortantnu pretpostavku.

- **[Lokacija: 4.1–4.2, terminologija i jedinice]**
  - **Uočeni problem:** \(|y''|\) se bez rezerve naziva „zakrivljenost”. Za uzdužnu krivulju \(y(x)\) geometrijska zakrivljenost je \(\kappa=y''/(1+(y')^2)^{3/2}\). U zadatku se zapravo ograničava druga derivacija, odnosno brzina promjene nagiba.
  - **Zašto je pogrešno:** Pri većim nagibima \(y''\) i geometrijska zakrivljenost nisu ista veličina. U radu se uz to metrička jedinica \(\mathrm{m^{-1}}\) prikazuje kao da je riječ o punoj geometrijskoj zakrivljenosti.
  - **Konkretan ispravak:** Dosljedno koristiti „druga derivacija nivelete” ili „brzina promjene nagiba”; po želji dodati: „U ovom diskretnom modelu \(y''\) se koristi kao aproksimacija vertikalne zakrivljenosti pri malim nagibima.”

- **[Lokacija: 2.1.2 i 2.2]**
  - **Uočeni problem:** Formulacija da stroga konveksnost i neprazan konveksan skup „jamče postojanje” optimuma nije općenito dovoljna bez dodatnog uvjeta zatvorenosti/koercivnosti ili izravne provjere ograničenog ponašanja funkcije.
  - **Zašto je pogrešno:** Strogo konveksna funkcija na nepraznom konveksnom, ali otvorenom skupu može imati infimum koji se ne postiže.
  - **Konkretan ispravak:** Napisati: „Skup \(F\) je neprazan i zatvoren, a \(f\) je strogo konveksna i koercivna jer je \(Q\succ0\). Stoga optimum postoji i jedinstven je.” KKT uvjeti su dovoljni zbog konveksnosti, a nužni uz zadovoljen Slaterov uvjet, koji se kasnije eksplicitno verificira.

---

## 3. ANALIZA GRAFOVA, SLIKA I TABLICA

### Zadatak 1

- **[Element: Slika 2.1 — geometrija QP-a]**
  - **Opravdanost:** Opravdano; izravno odgovara točki (c) zadatka.
  - **Tehnička ispravnost:** U PDF-u su vidljive oznake \(x_1\), \(x_2\), granice i optimum. Kako su varijable bez fizikalne dimenzije, jedinice nisu potrebne. Međutim, dopustivi skup treba biti grafički nedvosmisleno zasjenjen, a vektori gradijenata trebaju imati skalu ili jasnu napomenu da je duljina samo grafički skalirana.
  - **Kvaliteta interpretacije u tekstu:** Dobra u matematičkom dijelu, ali izraz „ravnoteža sila” je nepotrebna metafora. Dovoljna je KKT relacija \(\nabla f(x^*)=-\mu_1\nabla g_1(x^*)\).
  - **Potrebna dorada:** U opisu dodati da je \(g_2(x^*)=-1.484848<0\), pa njegov gradijent ne ulazi u aktivnu KKT ravnotežu. Ukloniti riječ „savršena”.

- **[Element: Tablica 2.1 — usporedba rješenja]**
  - **Opravdanost:** Opravdano.
  - **Tehnička ispravnost:** Tablica treba sadržavati identičan broj decimala za analitičke i numeričke rezultate te jasno razlikovati apsolutnu od relativne pogreške. Stupac „Status” je nepotreban za retke \(x_1,x_2\); važnija je rezidualna provjera KKT uvjeta.
  - **Kvaliteta interpretacije u tekstu:** Dovoljna, ali prenaglašeno se tvrdi „Egzaktno” uz numeričke vrijednosti.
  - **Potrebna dorada:** Zamijeniti „Egzaktno” s „podudaranje do prikazane tolerancije”. Dodati maksimum primarnog reziduala, stacionarnosti i komplementarnosti.

- **[Element: Slika 2.2 — dualna funkcija]**
  - **Opravdanost:** Opravdano, ali nije nužna ako prostor treba skratiti.
  - **Tehnička ispravnost:** Obje osi moraju biti \(\mu_1\) i \(\mu_2\), s označenim ograničenjem \(\mu\ge0\). U natpisu optimalne točke treba navesti punu vrijednost ili dosljedno zaokružiti sve vrijednosti.
  - **Kvaliteta interpretacije u tekstu:** Prekratka: tekst samo kaže što slika prikazuje.
  - **Potrebna dorada:** Jedna precizna rečenica: „Maksimum konkavne dualne funkcije na kvadrantu postiže se na rubu \(\mu_2=0\), što odgovara neaktivnosti drugog primarnog ograničenja.”

- **[Element: Slika 2.3 — osjetljivost]**
  - **Opravdanost:** Opravdano, ali samo ako su osi, raspon perturbacije i metoda izračuna jasni.
  - **Tehnička ispravnost:** Osi trebaju biti \(b_1\) i \(p^*(b_1)\); linearna aproksimacija mora biti eksplicitno definirana kao \(p^*(-10)-\mu_1^*(b_1+10)\).
  - **Kvaliteta interpretacije u tekstu:** Dobra ideja, ali „u potpunosti verificiran” je prejako za jednostranu numeričku razliku.
  - **Potrebna dorada:** Prikazati raspon perturbacije unutar kojega ostaje isti aktivni skup. Za \(b_2\) dovoljna je jedna rečenica, ne treba zaseban graf.

### Zadatak 2

- **[Element: Slika 3.1 — robusni skup i Monte Carlo ovojnica]**
  - **Opravdanost:** Opravdano; izravno odgovara zahtjevu zadatka.
  - **Tehnička ispravnost:** Legenda je sadržajno preopterećena. Sive realizacije, nominalne granice, robusne granice i dvije točke moraju ostati čitljivi pri ispisu u sivim tonovima. Označiti da je slučajni generator inicijaliziran s `rng(42)`.
  - **Kvaliteta interpretacije u tekstu:** Dobra, ali treba razlikovati „empirijska ovojnica 100 realizacija” od točne robusne granice.
  - **Potrebna dorada:** Promijeniti opis „100 % pouzdanost” u formulaciju iz prethodnog odjeljka. Dodati napomenu da crvena granica nastaje iz vršnih realizacija, a ne iz Monte Carlo uzoraka.

- **[Element: Tablica 3.1 — Monte Carlo provjera]**
  - **Opravdanost:** Opravdano.
  - **Tehnička ispravnost:** „57/100” treba biti zapisan u jednom stupcu ili razdvojeno na „povrede” i „broj uzoraka”. Riječ „rizično” je interpretativna i nepotrebna.
  - **Kvaliteta interpretacije u tekstu:** Korektna nakon uklanjanja tvrdnje o dokazivanju jamstva.
  - **Potrebna dorada:** Dodati da se uzorak odnosi na realizacije matrice, a broj ne broji pojedinačne povrede svakog retka nego uzorke s barem jednom povredom.

- **[Element: Slika 3.2 — cijena robusnosti]**
  - **Opravdanost:** Potrebno spojiti sa slikom 3.1 ako rad treba skratiti; obje slike prikazuju isti pomak optimuma.
  - **Tehnička ispravnost:** U dostupnom PDF izvatku dio grafičkog sadržaja prikazan je kao generički tekst „Graph Contour plot...”, što nije prihvatljivo za konačni PDF.
  - **Kvaliteta interpretacije u tekstu:** Sadržaj je ponovljen iz odjeljka 3.5.
  - **Potrebna dorada:** Ili izvesti stvarni graf visoke rezolucije i zadržati samo njega, ili ukloniti sliku te razliku \(24.017901\) i relativni porast \(39.63\%\) prikazati u jednoj tablici/rečenici.

### Zadatak 3

- **[Element: Tablica 4.1 — četiri slučaja nivelacije]**
  - **Opravdanost:** Opravdano i potrebno.
  - **Tehnička ispravnost:** Najveće odstupanje treba označiti kao \(\max_i |(D_1y)_i|\) ili \(\max_i |(D_2y)_i|\), a ne samo nejasnim simbolom. Za retke A i B tablica trenutačno prikazuje samo jedno ograničenje; mora sadržavati oba maksimuma, inače ne dokazuje da su oba skupa ograničenja zadovoljena.
  - **Kvaliteta interpretacije u tekstu:** Dobra osnova, ali treba jasno objasniti da su „iskop” i „nasip” diskretne površine po jediničnoj širini, ne volumeni u \(\mathrm{m^3}\).
  - **Potrebna dorada:** Dodati stupce \(\max|D_1y|\), \(\max|D_2y|\), `exitflag`, te definirati širinu ceste ako se želi rabiti riječ „volumen”.

- **[Element: Slike 4.1 i 4.2 — profili A i B]**
  - **Opravdanost:** Opravdano, ali mogu biti jedna slika s dva podgrafa.
  - **Tehnička ispravnost:** Osi trebaju biti \(x\,[\mathrm{m}]\) i \(h(x),y(x)\,[\mathrm{m}]\). Zasjenjeni iskop/nasip treba imati legendu dostupnu i bez boje.
  - **Kvaliteta interpretacije u tekstu:** Tekst nakon slika bolje interpretira učinak \(b_2\) nego same slike.
  - **Potrebna dorada:** U tekstu izravno navesti položaje ili intervale na kojima je ograničenje drugog reda aktivno. Ukloniti tvrdnju da finija mreža sama po sebi „omogućuje vjernije praćenje” bez metrike pogreške; to je razumna interpretacija, ali nije dokazana ovim četirima rezultatima.

- **[Element: Slike 4.3 i 4.4 — provjera derivacija]**
  - **Opravdanost:** Opravdano; to su najvažnije validacijske slike zadatka 3.
  - **Tehnička ispravnost:** Slika 4.3 mora pokazati obje granice \(+b_1\) i \(-b_1\), a slika 4.4 sve četiri granice \(\pm0.5\), \(\pm0.2\). Trenutačni opis govori o „granicama \(b_2\)”, no bez negativnih granica provjera nije potpuna.
  - **Kvaliteta interpretacije u tekstu:** Rečenica o dosezanju \(0.2\,\mathrm{m^{-1}}\) je korisna, ali treba navesti apsolutnu vrijednost i diskretni operator.
  - **Potrebna dorada:** Pisati \(\max_i |(D_2y)_i|=0.2\,\mathrm{m^{-1}}\), a ne neformalno „zakrivljenost doseže”. Prikazati i rezultate za \(N=20\), ili navesti da su grafovi namjerno ograničeni na \(N=100\), dok tablica pokriva sva četiri slučaja.

### Zadatak 4

- **[Element: Slika 5.1 — otvoreni krug]**
  - **Opravdanost:** Opravdano i zahtijevano zadatkom.
  - **Tehnička ispravnost:** Vremenski graf mora imati \(t\,[\mathrm{s}]\), \(x_1,x_2\) i označene trenutke prespajanja; fazni portret mora imati osi \(x_1\), \(x_2\). Budući da je pogreška u (5.10)–(5.11) kritična, ovu sliku treba generirati ponovno iz ispravljenog koda.
  - **Kvaliteta interpretacije u tekstu:** „Promjena smjera vektorskog polja ubacuje energiju” je intuitivna, ali nije dokaz u radu.
  - **Potrebna dorada:** Zamijeniti tom formulacijom: „Nestabilnost periodičkog prespajanja slijedi iz \(\rho(\Phi_{\mathrm{cycle}})>1\); simulacija je numerička ilustracija tog zaključka.”

- **[Element: Slika 5.2 — zatvoreni krug i elipse Ljapunova]**
  - **Opravdanost:** Opravdano.
  - **Tehnička ispravnost:** Potrebno je navesti konkretne \(P\) i \(K\) korištene u slici. Ako su elipse stvarno iz \(x^TPx=c\), njihova razina \(c\) mora biti navedena u legendi ili opisu.
  - **Kvaliteta interpretacije u tekstu:** Izraz „bez ikakvih oscilacija” nije potkrijepljen i lako može biti pogrešan za kompleksne polove.
  - **Potrebna dorada:** Zamijeniti s: „Trajektorija konvergira prema ishodištu; zbog kompleksnih svojstvenih vrijednosti moguća je rotacija u faznoj ravnini.”

- **[Element: Slika 5.3 — Ljapunovljeva energija]**
  - **Opravdanost:** Opravdano samo ako je kod za izračun dostupan.
  - **Tehnička ispravnost:** Na logaritamskoj osi nije dopuštena nula. Eksponencijalna ovojnica mora imati naveden oblik \(V(0)e^{-\alpha t}\) i porijeklo \(\alpha\). Diskontinuitet u \(A(t)\) ne uzrokuje skok stanja ni \(V\), ali derivacija \(\dot V\) može promijeniti vrijednost.
  - **Kvaliteta interpretacije u tekstu:** „Dokazuje” je prejako ako se oslanja na graf. Dokaz daje LMI nejednakost, graf je provjera simulacijom.
  - **Potrebna dorada:** Napisati: „LMI nejednakosti dokazuju eksponencijalnu stabilnost; slika numerički potvrđuje monotoni pad \(V\) za odabrani početni uvjet.”

---

## 4. JEZIČNE, STILSKE I „HUMAN-WRITTEN” KOREKCIJE

Glavni problem stila nije pojedinačna pravopisna pogreška nego stalno nadopisivanje očitog: mnoge rečenice najavljuju „rigoroznost”, „snagu” ili „važnost”, umjesto da daju rezultat. U tehničkom radu neka tvrdnja stoji samo ako uvodi definiciju, izvod, brojčanu provjeru ili ograničenje valjanosti.

| Lokacija / Izvorni tekst | Vrsta problema | Predloženi ispravak (autentični tehnički hrvatski) |
|---|---|---|
| Uvod: „Matematičko optimiranje i teorija sustava čine temelj suvremenog inženjerskog projektiranja...” | Generički, preširok uvod | „U radu se analiziraju četiri optimizacijska zadatka iz kvadratnog, robusnog i linearnog programiranja te stabilizacije sklopnog sustava.” |
| Uvod: „S povijesnog i teorijskog stajališta, razvoj optimizacijskih metoda doživio je ključnu promjenu paradigme.” | AI-floskula; nije relevantno za zadatke | Ukloniti cijelu rečenicu. |
| Uvod: „iznimno efikasnih, polinomijalno složenih algoritama unutarnje točke” | Preširoka, djelomično neprecizna tvrdnja | „Za konveksne probleme dostupni su numerički postupci s pouzdanim kriterijima optimalnosti.” |
| 1.2: „četiri samostalne, matematički i numerički rigorozno obrađene inženjerske cjeline” | Samohvala/metakomentar | „Rad je podijeljen na četiri zadatka.” |
| 2.1.2: „što jamči postojanje jedinstvenog globalnog minimuma” | Matematička nepreciznost | „Budući da je \(f\) koercivna, a \(F\) neprazan i zatvoren, minimum postoji; stroga konveksnost daje jedinstvenost.” |
| 2.4: „Uočava se savršena kolinearnost suprotnog smjera” | Suvišni pridjev | „Vrijedi \(\nabla f(x^*)=-\mu_1\nabla g_1(x^*)\).” |
| 2.4: „Fizika interpretacija ... ravnotei sila” | Metafora bez potrebe | „KKT uvjet stacionarnosti pokazuje da je negativni gradijent funkcije cilja u konusnoj ljusci gradijenata aktivnih ograničenja.” |
| 2.7.1: „teorem osjetljivosti u potpunosti verificiran” | Prejaka tvrdnja | „Jednostrana numerička derivacija slaže se s \(-\mu_1^*\) unutar navedenog odstupanja.” |
| 3.1: „rijetko su egzaktno poznati” i sljedeći opći odlomak | Preopširna motivacija | Skratiti na dvije rečenice koje uvode interval \(\pm15\%\). |
| 3.5: „neumitno povlači određenu konzervativnost” | Napuhana formulacija | „Robusni uvjet sužava dopustivi skup i ovdje povećava optimalnu vrijednost.” |
| 3.5: „inženjersku premiju osiguranja koja jamči apsolutnu operativnu sigurnost” | Marketinški/AI stil; tehnički neodrživo | „Povećanje vrijednosti funkcije cilja iznosi \(24.017901\), odnosno \(39.63\%\), zbog zahtjeva dopustivosti u cijelom zadanom intervalnom skupu.” |
| 4.1: „temeljni optimizacijski zadatak” | Suvišni pridjev | „Projektiranje uzdužnog profila može se formulirati kao optimizacijski problem.” |
| 4.1: „maksimalne zakrivljenosti trase (udobnost vožnje i ograničenje vertikalnih akceleracija)” | Terminološka prečica | „maksimalne druge derivacije nivelete, koja u pojednostavnjenom modelu ograničava promjenu nagiba.” |
| 4.3: „slack variables” za \(z_i\) | Krivi/zbunjujući termin | „epigrafske pomoćne varijable” |
| 4.4: „algoritma dupleksnog simpleksa linprog s opcijom dual-simplex i highs” | Nejasno i miješa implementacije | „MATLAB funkcijom `linprog` uz algoritam `dual-simplex`.” Ako je korišten SciPy/HiGHS, to navesti odvojeno. |
| 4.5: „otkrivaju ključne fizikalne i numeričke zakonitosti” | AI-floskula | „Usporedba pokazuje sljedeće razlike.” |
| 4.5: „Fina mreža omogućuje vjernije praćenje lokalnih promjena bez numeričkog peglanja” | Kolokvijalno, nedokazano | „Razlike između \(N=20\) i \(N=100\) pokazuju osjetljivost diskretne aproksimacije na gustoću mreže.” |
| 5.2: „Jedan od najintrigantnijih fenomena...” | Uvodna floskula | „Stabilnost pojedinačnih modova ne implicira stabilnost periodički prespajanog sustava.” |
| 5.2: „Slika 5.1 zorno prikazuje...” | Prejak vizualni komentar | „Slika 5.1 numerički ilustrira rast stanja, u skladu s \(\rho(\Phi_{\mathrm{cycle}})>1\).” |
| 5.4: „globalnom konvergencijom” | Preširoka tvrdnja | „Dobiveni problem je SDP s konveksnim skupom dopustivih varijabli \(Q,Y\).” |
| 5.6: „brzo i glatko konvergiraju ... bez ikakvih oscilacija” | Neutemeljeno; kontradiktorno kompleksnim polovima | „Konvergiraju prema ishodištu u prikazanom intervalu simulacije.” |
| 5.6: „dokazuje uniformnu eksponencijalnu stabilnost” (za sliku) | Graf nije dokaz | „Numerički je u skladu s dokazom koji slijedi iz strogo negativnih LMI nejednakosti.” |
| 6.2: „Rad demonstrira snagu i fleksibilnost...” | Generički zaključak | „Primijenjeni modeli pokazuju kako se QP, robusni QP, LP i LMI mogu koristiti za zadane klase problema.” |
| 6.2: „numerički pouzdanih rješavača koji jamče globalnu konvergenciju u polinomijalnom vremenu” | Neopravdano općenito | „Konveksna formulacija omogućuje primjenu standardnih QP, LP i SDP rješavača.” |
| Cijeli rad: „engl.” uz gotovo svaki pojam | Vizualni šum | Engleski naziv navesti samo pri prvom pojavljivanju ako je stvarno potreban: „zajednička kvadratna funkcija Ljapunova (CQLF)”. Ostatak rada koristiti hrvatski naziv ili kraticu. |
| Cijeli rad: „Kao što je vidljivo na slici...” | Slaba referenca na dokaz | Zamijeniti konkretnom tvrdnjom s brojkom, npr. „Na slici 4.4 vrijedi \(\max_i |(D_2y)_i|=0.2\,\mathrm{m^{-1}}\) za slučaj B.” |

**Preporučena redukcija opsega:** Uvod skratiti na približno pola stranice. Svaki zadatak započeti samo s formulacijom i potrebnom teorijom. Ukloniti opću motivaciju iz poglavlja 3–5 ako ne vodi izravno do sljedeće jednadžbe. Zaključak ograničiti na jedan rezultat po zadatku i jedno ograničenje modela; izbaciti spekulativne smjernice poput Tube MPC-a, adaptivnih LMI regulatora i vremenskih kašnjenja, jer nisu razvijene u radu.

---

## 5. KORAK-PO-KORAK AKCIJSKI PLAN ZA POPRAVAK

1. **Prioritet 1 — popraviti zadatak 4 prije bilo kakve lekture.** Ponovno izračunati \(e^{A_{\mathrm{parno}}}\), \(e^{A_{\mathrm{neparno}}}\), \(\Phi_{\mathrm{cycle}}\) i sve iz njih izvedene rezultate. Uskladiti (5.10)–(5.13), kôd, sliku 5.1 i tekst. Ne ostavljati sadašnje kontradiktorne vrijednosti.
2. **Prioritet 2 — učiniti rad reproducibilnim.** Priložiti kompletan MATLAB i Python kôd ili ukloniti neprovjerljive tvrdnje. Dodati `config_plot.m`, implementirati stvarne simulacije i izvoz svih prikazanih slika, provjeravati `exitflag`, te u dodatku ili repozitoriju dati jednu točnu naredbu za reprodukciju rezultata.
3. **Prioritet 3 — popraviti formulaciju zadatka 3.** U (4.13) i (4.17) dosljedno uključiti \(\Delta x\); definirati jedinice kao površinu po jediničnoj širini; naziv „zakrivljenost” zamijeniti s „drugom derivacijom nivelete” ili jasno navesti aproksimaciju.
4. **Prioritet 4 — zatvoriti logičke rupe.** U zadatku 2 dokazati izbor aktivnih vrhova bez prešutne pretpostavke o ortantu ili provjeriti svih osam robusnih ograničenja. Monte Carlo prikazati kao ilustraciju, a analitički robusni ekvivalent kao dokaz jamstva. U zadatku 1 dodati koercivnost/zatvorenost pri tvrdnji o egzistenciji optimuma.
5. **Prioritet 5 — revidirati tablice i slike.** Svaka slika mora imati čitljive osi, jedinice gdje postoje, minimalnu legendu i jednu konkretnu interpretacijsku rečenicu. Tablica 4.1 mora dokazati oba ograničenja. Slike 3.1 i 3.2 spojiti ili ukloniti redundanciju. Izvesti stvarnu sliku 3.2, ne ostaviti generički tekstualni artefakt.
6. **Prioritet 6 — skratiti tekst za 25–35 %.** Najprije izbrisati generičke uvode, samohvalu i „inženjerske” metafore. Zatim svaku preostalu tvrdnju vezati uz jednadžbu, tablicu, broj ili jasno ograničenje. Zadržati KKT i LMI izvode, ali izbjeći ponovno prepričavanje istog rezultata u opisu slike, zaključku i sljedećem poglavlju.
7. **Prioritet 7 — završna tehnička lektura.** Ujednačiti \(x^*\), \(x_{\mathrm{rob}}^*\), \(p^*\), \(J_{\mathrm{disc}}\), \(\Delta x\), \(\mu\), \(P\), \(Q\), \(K\) i indeksiranje. Potom provjeriti da se svaka brojka u tablicama, opisima slika i zaključku podudara s jednim reproducibilnim izlazom koda.

**Završna recenzentska presuda:** Nakon prioriteta 1–4 rad može postati tehnički čvrst seminarski rad. Nakon prioriteta 5–7 bit će kraći, uvjerljiviji i znatno prirodniji za čitanje. Trenutačno nije preporučljivo predati ga bez značajne revizije, prvenstveno zbog numeričke kontradikcije u zadatku 4 i neusklađenosti između navedenih rezultata i dostavljenog koda.
