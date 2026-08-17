# Recenzija — OMRiUS seminar (1. verzija)

**Predmet:** Optimizacijske metode u razvoju i upravljanju sustava  
**Autor:** Krešimir Hartl  
**Dokument:** `OMRiUS_seminar_Kresimir_Hartl-2.pdf` (38 str.)  
**Prilozi:** MATLAB + Python kodovi, originalni tekst zadatka  
**Recenzent:** strogi nezavisni akademsko-tehnički validator  
**Datum:** 17. kolovoza 2026.

---

## 1. SAŽETAK OCJENE (SCORECARD)

| Kriterij | Ocjena | Status |
|---|---|---|
| Usklađenost sa zadatkom | **88%** | Zadovoljava |
| Matematička i inženjerska točnost | **81%** | Djelomično |
| Vizualizacije i podaci | **82%** | Djelomično |
| Jezik, pravopis i akademski stil | **54%** | Djelomično |
| **KONAČNI STATUS** | — | **POTREBNA ZNAČAJNA REVIZIJA** |

**Jedna rečenica.** Tehnička jezgra zadataka 1–3 je točna i rješavanje je ispravno postavljeno; rad pada na napuhanom, strojnom jeziku, suvišnom uvodu/zaključku i na interno proturječnim matricama prijelaza u zadatku 4.

**Što je dobro.** Konveksnost, sva 4 KKT slučaja, dual, osjetljivost, vertex-robusni ekvivalent, LP formulacija ceste s 4 scenarija i LMI sinteza regulatora — to je napravljeno kako treba, a brojke u zadacima 1–3 se slažu s neovisnim proračunom.

**Što ruši dojam.** Rad zvuči kao generirani pregledni članak, ne kao seminar. Naslovnica, taksonomija, „cijena robusnosti“, „smjernice za praksu“ i reciklirani uvodi po poglavljima nisu traženi i štete vjerodostojnosti. Profesor će to prepoznati brže nego grešku u KKT-u.

---

## 2. KRITIČNI NEDOSTACI I BLOKIRAJUĆE GREŠKE

### [Lokacija: §5.2, jedn. (5.10)–(5.11)]

- **Uočeni problem.** Ispišane matrice prijelaza i monodromije **ne odgovaraju** njihovim svojstvenim vrijednostima niti `expm(A)`.
- **Zašto je pogrešno.** Neovisni račun daje

```
Φ_parno  = exp(A_parno)  ≈ [[ 0.0000, -0.1226], [ 1.1036,  0.0000]]
Φ_neparno = exp(A_neparno) ≈ [[ 0.0000, -1.1036], [ 0.1226,  0.0000]]
Φ_cycle   = Φ_neparno Φ_parno ≈ [[-1.2180, 0], [0, -0.0150]]
```

U radu stoji `[[0, -0.2122],[1.9099, 0]]`, `[[0, -1.9099],[0.2122, 0]]` i `[[-3.6476, 0],[0, -0.0450]]`.  
Svojstvene vrijednosti koje navodite, `λ ≈ -1.218` i `-0.015`, te `ρ = 1.218 > 1`, **jesu točne** — ali one pripadaju pravoj matrici, ne onoj koju ste ispisali. Matrica `diag(-3.6476, -0.0450)` imala bi spektralni radijus **3.65**, ne 1.218. To je interna kontradikcija: recenzent koji pomnoži dvije ispisane matrice odmah vidi da tekst nije usklađen.

- **Konkretan ispravak.** Zamijeniti (5.10)–(5.11) gornjim vrijednostima. U tekstu jednom rečenicom napisati: *svojstvene vrijednosti monodromije jednake su dijagonalnim elementima, pa je `ρ(Φ_cycle) = 1.218 > 1`*. Ne izmišljati „zaokružene“ unose koji se ne dobiju iz `expm`.

---

### [Lokacija: §5.5, (5.24) i sljedeći odlomak]

- **Uočeni problem.** Istovremeno se navode **dva** regulatora: Python/CVXPY `K = [-2.7120, 0.0926]` i „referentni YALMIP“ `K = [-3.7097, 0.0000]`. Zatvorene matrice (5.25)–(5.30) i slike 5.2–5.3 odgovaraju **samo prvom** `K`. MATLAB skripta pri padu YALMIP-a koristi drugi `K`, a u njoj stoji i programska greška `eig(Acl_even(1))` (skalar, ne matrica).
- **Zašto je pogrešno.** Čitatelj ne zna koji je regulator „službeni“. Dva različita `K` daju različite spektralne slike (kompleksni par naspram dva realna pola). To nije „referenca“, nego druga točka u skupu dopustivih LMI rješenja.
- **Konkretan ispravak.** Odabrati **jedan** `K` (preporuka: onaj iz slika, `[-2.7120, 0.0926]`). Drugi, ako uopće, u fusnotu: *LMI nije jednoznačan; YALMIP/SDPT3 daje npr. `K = [-3.7097, 0]`, koji također stabilizira.* Popraviti MATLAB: `eig(Acl_even)`, ne `eig(Acl_even(1))`. Uskladiti Python i MATLAB na isti `K` prije predaje.

---

### [Lokacija: §5.6 naslov; §6.1 točka 4]

- **Uočeni problem.** Simulacija se zove „dokazom“ eksponencijalne stabilnosti. Monte Carlo u §3.4 „dokazuje 100 % pouzdanost“.
- **Zašto je pogrešno.** Dokaz za zadatak 4 je LMI (5.23) + `P ≻ 0`. Jedna trajektorija iz `x(0) = [1, 0]ᵀ` je ilustracija. Monte Carlo sa 100 uzoraka **ne može** jamčiti 100 %; jamstvo daje vertex-ekvivalent (3.11)–(3.18).
- **Konkretan ispravak.**  
  - §5.6: *Simulacija zatvorenog kruga.*  
  - §3.4: *Nominalna točka krši ograničenje u 57 od 100 realizacija. Robusna točka nije prekršila nijednu; dopustivost za cijeli `U` slijedi iz ekvivalenta (3.19), ne iz uzorka.*

---

### [Lokacija: §3.3, tvrdnja da su oba najgora ograničenja aktivna]

- **Uočeni problem.** Sjecište (3.22) postulirano je bez KKT provjere. Brojke su slučajno točne, obrazloženje nije.
- **Zašto bi moglo biti krivo.** Kod nominalnog QP-a aktivno je samo `g₁`. Ista pretpostavka ovdje **ne vrijedi automatski**.
- **Što recenzent provjerava.** KKT samo s najgorim `g₁` (`x₁ + x₂ = 10/0.85`) daje `x ≈ (6.907, 4.857)`, ali tada `1.15x₁ − 0.85x₂ − 3 ≈ +0.815 > 0` — točka je nedopustiva. Zato oba najgora ograničenja **moraju** biti aktivna, i sjecište `(6.5, 179/34)` jest optimum. `f(x_rob*) = 978253/11560 ≈ 84.623962` je točno.
- **Konkretan ispravak.** Dodati 8–10 redaka: KKT samo s `g₁^{wc}` → nedopustivo za `g₂^{wc}` → oba aktivna → (3.22). Tek tada smijete reći da je to optimum, a ne samo sjecište pravaca.

---

### [Lokacija: zadatak 1d — tvrdnja o YALMIP-u]

- **Uočeni problem.** U §2.5 piše da je problem riješen u MATLAB-u (`quadprog`, **YALMIP**) i Pythonu. Priloženi `task1_qp_analysis.m` koristi samo `quadprog` i `fmincon`. YALMIP se pojavljuje tek u zadatku 4.
- **Zašto je pogrešno.** Zadatak 1d izričito traži MATLAB (`quadprog` i/ili YALMIP). `quadprog` je dovoljan. Tvrditi YALMIP tamo gdje ga nema je nepotrebna samohvala i lako se uhvati.
- **Konkretan ispravak.** Napisati točno što kod radi: primal `quadprog`, dual `fmincon` na `−g(μ)`, `μ ≥ 0`. Python ostaviti u jednoj rečenici kao dodatnu provjeru, ne kao ravnopravni „službeni“ solver predmeta.

---

### Nisu blocker, ali se moraju popraviti

1. **§4.3, diskretni integral.** `J_disc = Δx ∑_{i=0}^{N} |yᵢ − hᵢ|` ima **N+1** članova na **N** intervala. To je pristrana kvadratura (prema gore za ~`Δx·(|y₀−h₀|+|y_N−h_N|)/2` u odnosu na trapez). Ili trapez, ili `Δx ∑_{i=1}^{N}` sredine intervala. Brojke u tablici 4.1 ostaju valjane samo uz jasno definiran diskretni kriterij; nemojte ih zvati „kontinuiranim integralom“ bez rezerve.
2. **§4.3.** `zᵢ` nisu slack varijable. Slack pretvara nejednakost u jednakost. Ovo su **epigrafske** (pomoćne) varijable. Engleski termin *slack* ovdje je kriv.
3. **§4.4.** „algoritam dupleksnog simpleksa“ → **dualni simpleks**. *Dupleks* ne postoji.
4. **Naslovnica.** Naslov predmeta ispisan je dvaput. Nema maticnog broja (u zadatku je prazan, ali na seminaru treba stajati).
5. **Zadatak ne traži** taksonomiju LP/QP/SDP, *Price of Robustness*, Tube-MPC, adaptivne LMI regulatore. To je volumen bez ocjene.

---

## 3. ANALIZA GRAFOVA, SLIKA I TABLICA

### Slika 2.1 — geometrija QP i KKT

- **Opravdanost:** Opravdano (zadatak 1c).
- **Tehnička ispravnost:** Osnovna geometrija je ispravna: `x*`, `x⁰`, nivo-krivulje, `∇f` i `∇g₁`. Osovnice su `x₁`, `x₂` bez jedinica (u redu, bezdimenzijski QP). U tekstu slike stoji **„kolineran“** — treba **kolinearan**. Vektori nisu u istom mjerilu (`0.25·∇f` naspram fiksnog `∇g₁`); napisati da je duljina shematska.
- **Interpretacija:** Dobra. Ravnoteža `∇f + μ₁* ∇g₁ = 0` je izračunata i slaže se s `μ₁* = 404/33`.
- **Dorada:** Ukloniti naslov unutar slike tipa „Zadatak 1: Geometrija…“. Potpis ispod slike je dovoljan. Osjenčati `F` tako da se vidi da je neomeđen.

### Slika 2.2 — dualna funkcija `g(μ)`

- **Opravdanost:** Opravdano (zadatak 1e).
- **Tehnička ispravnost:** Osovnice u izvatku nisu čitljivo imenovane s `μ₁`, `μ₂` i jedinicom (bezdim.). Optimum na osi `μ₂ = 0` mora biti očit.
- **Interpretacija:** Tanka. Jedna rečenica „slika prikazuje nivo-krivulje“ nije interpretacija.
- **Dorada:** Napisati da je `g` konkavna, da se maksimum postiže na granici `μ₂ = 0` i da to odgovara neaktivnom `g₂`.

### Slika 2.3 — osjetljivost `p*(b₁+Δb₁)`

- **Opravdanost:** Opravdano (zadatak 1f).
- **Tehnička ispravnost:** Nagib `−μ₁* = −12.2424` slaže se s (2.54). Osovnice trebaju `Δb₁` i `p*`.
- **Interpretacija:** Brojčano u redu; rečenica „u potpunosti verificiran“ je pretjerana.
- **Dorada:** Označiti interval u kojem je linearna aproksimacija dobra i gdje se lomi aktivni skup.

### Slika 3.1 — robusni skup i Monte Carlo

- **Opravdanost:** Opravdano (zadatak 2 izričito traži niz slučajnih granica + optimum).
- **Tehnička ispravnost:** Nominalne i najgore granice su ispravne. Sive realizacije imaju smisla. Legenda je gusta.
- **Interpretacija:** Dobra, uz pretjerivanje „100 % pouzdanost“.
- **Dorada:** Označiti robusni dopustivi skup kao presjek, ne samo ovojnicu linija. U legendi hrvatski, bez `wc` ako već imate „najgora granica“.

### Slika 3.2 — pomak optimuma / cijena robusnosti

- **Opravdanost:** Suvišno / spojiti sa 3.1. Zadatak ne traži „price of robustness“. Ista informacija već stoji na 3.1 (`x_nom*`, `x_rob*`, `f`).
- **Dorada:** Baciti sliku ili je pretvoriti u mali umetak na 3.1. Ako ostane, maknuti marketinški komentar o „premiji osiguranja“.

### Tablica 2.1

- **Opravdanost:** Opravdano.
- **Tehnička ispravnost:** Brojke točne (`190/33`, `140/33`, `404/33`, `2000/33`). Stupac „Egzaktno“ je loš: numerika nije egzaktna, ima apsolutnu pogrešku `< 10⁻⁸`.
- **Dorada:** Status: *slaže se do 1e-8*.

### Tablica 3.1

- **Opravdanost:** Opravdano kao empirijska potvrda.
- **Dorada:** Naslov ne smije tvrditi jamstvo. 57/100 vrijedi za `seed = 42`; napisati sjeme ili reći „u provedenom uzorku“.

### Slike 4.1 i 4.2 — profili ceste

- **Opravdanost:** Opravdano (4 slučaja; ovdje A i B, N = 20 i 100 preklopljeni — prihvatljivo).
- **Tehnička ispravnost:** Os `x [m]`, visina treba `[m]`. „Iskop (Cut) / Nasip (Fill)“ — maknuti engleski.
- **Interpretacija:** U §4.5 postoji, ali preopćenito („peglanje“, „udobnost pri višim brzinama“ — brzina nije u modelu).
- **Dorada:** Jednom rečenicom: u A trasa prati teren uz aktivno `|y''| = 0.5`; u B se odvaja jer je `|y''| ≤ 0.2` aktivno na dugim odsječcima.

### Slike 4.3 i 4.4 — `y'`, `y''`

- **Opravdanost:** Opravdano (provjera ograničenja).
- **Tehnička ispravnost:** 4.3 ima jedinice `x [m]`, `y' [m/m]`. 4.4 treba `y'' [m⁻¹]`. Granice `±b₁`, `±b₂` vidljive. Dobro.
- **Interpretacija:** 4.4 je bolja (zasićenje u B). 4.3 ostaje na „evo grafa“.
- **Dorada:** Reći je li `|y'| = 0.5` aktivno ili nije (iz koda slijedi da je aktivna zakrivljenost, ne nužno nagib). To je inženjerski sadržaj koji sada nedostaje.

### Tablica 4.1

- **Opravdanost:** Opravdano.
- **Tehnička ispravnost:** Četiri tražena slučaja tu su. Jedinica `m²` za `∫|y−h| dx` je u redu (površina uzdužnog presjeka, ne volumen). `max |y''|` točno na granici — očekivano.
- **Dorada:** Dodati `max |y'|`. Napisati da je `J*` diskretni kriterij, ne kontinuirani integral. Iskop+nasip treba biti jednak `J*` (kod A/N=20: 0.0877+1.8285=1.9162 — slaže se; provjeriti ostale retke na zaokruživanje).

### Slika 5.1 — otvoreni krug

- **Opravdanost:** Opravdano (zadatak 4b).
- **Tehnička ispravnost:** Traži se `x(t)` **i** fazni portret — kombinacija u jednoj slici je u redu ako su paneli označeni. Osovnice: `t [s]`, `x₁, x₂`, fazni `x₁`–`x₂`.
- **Interpretacija:** „ubacuje energiju“ je slikovito i netočno (nema energetskog skladišta u zadatku). Reći: *u trenutku prespajanja vektorsko polje se okreće tako da se amplituda poveća; monodromija ima `ρ > 1`*.
- **Dorada:** Ograničiti `T` (npr. 10–20 s) i označiti parne/neparne intervale.

### Slika 5.2 — zatvoreni krug

- **Opravdanost:** Opravdano (zadatak 4c).
- **Tehnička ispravnost:** Eliptične nivo-krivulje `xᵀ P x = c` imaju smisla samo uz **isti** `P` i `K` iz (5.24).
- **Interpretacija:** „bez ikakvih oscilacija“ je netočno — polovi su kompleksni, odziv je prigušeno oscilatoran.
- **Dorada:** Maknuti tu rečenicu.

### Slika 5.3 — `V(x(t))`

- **Opravdanost:** Korisna, nije izričito tražena. Može ostati ako se skrati tekst oko nje.
- **Tehnička ispravnost:** Log-skala, usporedba s `V₀ e^{-αt}`, `α = 0.85`. Taj `α` nije izveden iz `λ_max(Ṗ)` (imate ≈0.055–0.095 za kvadratnu formu, što za `V` nije isto što i 0.85). Ili izvesti `α` iz LMI, ili maknuti „teorijsku ovojnicu“ ako je samo vizualno pogođena.
- **Dorada:** Ako `α` nije računat, ne zvati krivulju teorijskom.

---

## 4. JEZIČNE, STILSKE I „HUMAN-WRITTEN“ KOREKCIJE

Ovo je glavni problem rada. Tehnički sadržaj je studentski; **proza je modelna**: apstraktni uvod, taksonomija, tri pridjeva po imenici, „dokazano / verificirano / jamči“, pa marketinški zaključak.

### Pravilo za drugi nacrt

- Svako poglavlje počinje zadatkom, ne filozofijom.
- Rečenica nosi jedan sadržaj. Ako se može izbrisati bez gubitka brojke ili koraka, briše se.
- Zabranjene riječi osim ako ih dokazujete teoremom: *sveobuhvatan, ključan, izniman, moćan, rigorozno, zorno, neumitno, savršen, premija osiguranja, paradigme*.
- Engleski samo pri prvoj pojavi termina, u zagradi, jednom.

### Tablica ispravaka (nije potpuna — ovo su tipični uzorci; isti postupak primijeniti na cijeli tekst)

| Lokacija / izvorni tekst | Vrsta problema | Predloženi ispravak |
|---|---|---|
| §1: „Matematičko optimiranje i teorija sustava čine temelj suvremenog inženjerskog projektiranja…“ | AI uvod, prazna fraza | **Obrisati cijeli prvi odlomak.** Početi: *Seminar rješava četiri zadana problema: QP s KKT i dualom, robusni QP, nivelaciju ceste i stabilizaciju sklopnog sustava.* |
| §1: „ključnu promjenu paradigme“, „iznimno efikasnih, polinomijalno složenih algoritama“ | suvišni pridjevi, udžbenik | Obrisati. Konveksnost se dokazuje u §2.1, ne u uvodu. |
| §1.1 cijela taksonomija LP/QP/robusno/SDP | nije traženo; generički pregled | **Obrisati poglavlje 1.1.** Klasa se kaže na mjestu zadatka: „problem (2.1)–(2.3) je strogo konveksan QP“. |
| §1.2: „matematički i numerički rigorozno obrađene inženjerske cjeline“ | samohvala | *Rad ima četiri poglavlja, po jedan zadatak, i kratak zaključak.* |
| §2.1: „Zadan je optimizacijski problem kvadratnog programiranja (engl. *Quadratic Programming* – QP)“ | nepotreban anglicizam | *Zadan je QP* — i krenuti na (2.1). |
| §2.4: „Uočava se savršena kolinearnost“ / „kolineran“ | pretjerivanje + pravopis | *∇f(x*) i ∇g₁(x*) su kolinearni i suprotnog smjera.* |
| §2.4: „Fizička interpretacija … ravnoteži sila … graničnu silu“ | metafora bez modela sila | *Stacionarnost KKT: ∇f(x*) = −μ₁* ∇g₁(x*).* |
| §2.5 / tablica: „Egzaktno“ | krivi termin | *Pogreška < 10⁻⁸.* |
| §2.6.1 / §2.7: „u potpunosti verificiran“, „jamči“ | AI superlativ | *Slaterov uvjet vrijedi za x_int = [7, 6]ᵀ, pa je p* = d*. Numerički kvocijent odstupa od −μ₁* za 6.7·10⁻⁵.* |
| §3.1 cijeli prvi odlomak („U stvarnim inženjerskim primjenama… otpori…“) | generički uvod | Obrisati. Početi: *Koeficijenti aᵢⱼ nesigurni su na ±15 % oko nominalnih vrijednosti iz zadatka 1.* |
| §3.5: „neumitno povlači“, „Price of Robustness“, „inženjersku premiju osiguranja koja jamči apsolutnu operativnu sigurnost“ | marketing + engleski | *Robusni optimum poskupljuje kriterij za 24.018 (39.63 %). To je cijena za dopustivost na cijelom U.* Ili cijeli §3.5 izbaciti. |
| §4.1: „U građevinarstvu i prometnom inženjerstvu… temeljni optimizacijski zadatak“ | AI uvod | Obrisati. *Traži se y(x) koja minimizira ∫\|y−h\| dx uz \|y′\|≤b₁, \|y″\|≤b₂ i rubne uvjete.* |
| §4.3: „epigrafskih pomoćnih varijabli (engl. slack variables)“ | krivi termin | *epigrafske varijable zᵢ ≥ \|yᵢ − hᵢ\|* |
| §4.4: „dupleksnog simpleksa“ | nepostojeća riječ | *dualnim simpleksom (`linprog`)* |
| §4.5: „numeričkog peglanja“, „udobnost vožnje pri višim brzinama“ | žargon / tvrdnja izvan modela | *Grublja mreža daje manji diskretni J* jer ne vidi lokalne pregibe. Manji b₂ prisiljava glađu niveletu i veći J*.* |
| §5.1: „važnu klasu sustava“, udžbenički uvod o hybrid/switched | generički uvod | Obrisati. Krenuti od (5.1)–(5.3). |
| §5.2: „Jedan od najintrigantnijih fenomena“ | AI floskula | *Prespajanje dvaju Hurwitzovih modova ovdje daje nestabilan sustav.* |
| §5.2: „zorno prikazuje“, „ubacuje energiju“ | prilog + kriva fizika | *Slika 5.1 pokazuje rast amplitude; to je u skladu s ρ(Φ_cycle)>1.* |
| §5.6: „dokaz eksponencijalne stabilnosti“ | krivi termin | *Simulacija zatvorenog kruga* |
| §5.6: „brzo i glatko“, „bez ikakvih oscilacija“ | netočno + floskula | *Stanja padaju ispod 10⁻² unutar približno 3 s. Polovi su kompleksni, odziv je prigušeno oscilatoran.* |
| §6: „sveobuhvatna matematička, teorijska i numerička analiza četiri fundamentalna problema suvremene teorije“ | čisti AI zaključak | *Riješena su četiri zadatka. Donose se samo brojke i jedna rečenica po zadatku.* |
| §6.2 cijeli | nije traženo; Tube MPC, adaptivni LMI | **Obrisati 6.2.** |
| kroz tekst: „Kao što je vidljivo“, „Kao što vidimo“ | meta-komentar | *Na slici 4.4 zakrivljenost u slučaju B leži na ±0.2 m⁻¹.* |
| kroz tekst: *switched linear systems, worst-case approach, Price of Robustness, interior-point, CQLF, Tube MPC* | engleski tamo gdje postoji hrvatski | sklopni linearni sustav; najgori slučaj; cijena robusnosti; metode unutarnje točke; zajednička kvadratna funkcija Ljapunova |
| „Slučaje A i B“ (sadržaj slika, §4) | gramatika | *Slučajeve A i B* / *slučaje A i B* |
| „funkcja Vx“ (§5.5.1) | tipfeler | *funkcija* |
| naslov slike 5.2 u sadržaju: `x TP x` | slomljen LaTeX | `x^{\mathrm{T}} P x = c` |

### Što izrezati po opsegu (cilj: ~20–22 stranice, ne 38)

| Blok | Akcija | Razlog |
|---|---|---|
| §1.1 Taksonomija | brisati | nije u zadatku |
| §1 uvodna dva odlomka | brisati | floskule |
| §3.1 prvi odlomak | brisati | generički |
| §3.5 cijeli | skratiti na 4 retka ili brisati | nije traženo |
| §4.1 prvi odlomak | brisati | generički |
| §5.1 prvi odlomak | brisati | generički |
| §6.2 | brisati | nije traženo |
| Slika 3.2 | spojiti s 3.1 | duplikat |
| Ponavljanje rezultata u §6.1 | ostaviti tablicu od 4 retka, ne mini-eseje | §6 sada prepisuje §§2–5 |

---

## 5. KORAK-PO-KORAK AKCIJSKI PLAN

### Prioritet 1 — ispraviti činjenice (pola dana)

1. Zamijeniti (5.10)–(5.11) točnim `expm` matricama. Provjeriti da se svojstvene vrijednosti i `ρ` slažu s ispisom.
2. Jedan `K` svuda. MATLAB: `eig(Acl_even)`, isti `K` kao u Pythonu i na slikama 5.2–5.3.
3. U §3.3 dodati KKT obrazloženje zašto su oba najgora ograničenja aktivna.
4. Maknuti riječ „dokaz“ s simulacije i s Monte Carla.
5. U §2.5 maknuti YALMIP ako nije u kodu zadatka 1.

### Prioritet 2 — smršaviti tekst (glavni posao)

6. Obrisati §1.1, §6.2, generičke prve odlomke §§1, 3, 4, 5 i (po želji) §3.5 / sliku 3.2.
7. Svako poglavlje: zadatak → formulacija → račun → brojka → jedna interpretacija slike. Ništa prije formule.
8. Proći tekst i izbaciti pridjeve i „jamči/verificirano/sveobuhvatno“. Cilj: rečenice koje bi student napisao na predavanju, ne u preglednom članku.
9. Hrvatski termini, engleski samo jednom u zagradi.
10. Naslovnica: jedan naslov, profesor, student, **matični broj**, Zagreb, 2026.

### Prioritet 3 — slike, kod, lektura

11. Jedinice na svim osima; hrvatska legenda; bez naslova *unutar* slike koji ponavlja potpis.
12. Tablica 4.1: `max |y′|`, jasno da je `J*` diskretan. Tablica 2.1: ne pisati „Egzaktno“.
13. Uskladiti imena skripti (`task1_qp_analysis.m` vs `run_all` pozivi). Python import `common.config_plot` mora odgovarati stvarnom rasporedu mapa.
14. Lektura: č/ć, *kolinearan*, *funkcija*, *slučajeve*, *dualni simpleks*.
15. Tek nakon toga: zaključak od **najviše** 3/4 stranice, samo brojke iz zadataka.

### Kontrolni popis usklađenosti sa zadatkom (nakon revizije)

**Zadatak 1** — sve stavke pokrivene i brojčano točne:

- [x] (a) konveksnost: `Q ≻ 0`, `λ ≈ 1.956, 4.044`, afin skup
- [x] (b) KKT, 4 slučaja, optimum `x* = (190/33, 140/33)`, `μ* = (404/33, 0)`, `p* = 2000/33`
- [x] (c) skup, nivo-krivulje, gradijenti
- [x] (d) `quadprog` + usporedba množitelja *(YALMIP maknuti ako ga nema)*
- [x] (e) dual `g(μ) = −½(c+Aᵀμ)ᵀQ⁻¹(c+Aᵀμ) − bᵀμ`, `d* = p*`
- [x] (f) `∂p*/∂b₁ = −μ₁*`, `∂p*/∂b₂ = 0`, numerička provjera

**Zadatak 2** — točno, treba samo KKT rečenica + manje patetike.

**Zadatak 3** — formulacija LP, 4 slučaja, slike; popraviti kvadraturu/terminologiju.

**Zadatak 4**

- [x] (a) oba moda Hurwitz, `−1 ± jπ/2`
- [x] (b) simulacija + fazni portret; nestabilan zbog `ρ>1` — **matrice prijelaza popraviti**
- [x] (c) `u = Kx`, LMI, simulacija zatvorenog kruga — **jedan K**

---

## DODATAK A — neovisna provjera brojki

Račun recenzenta (NumPy / SciPy), 17. 8. 2026.

### Zadatak 1 — slaže se

| Veličina | Rad | Provjera |
|---|---|---|
| `eig(Q)` | 1.955969, 4.044031 | 1.955969, 4.044031 |
| `x⁰` | (−0.897598, 0.682680) | isto |
| `x*` | 190/33, 140/33 | isto |
| `μ₁*` | 404/33 ≈ 12.242424 | isto |
| `p* = d*` | 2000/33 ≈ 60.606061 | isto |
| slučaj 3 | 121/54, −41/54, −3623/540 | isto |
| slučaj 4 | μ = (11.50, −2.45) | isto |

Postupak (4 aktivna skupa, dual, Slater, osjetljivost) je ispravan.

### Zadatak 2 — rezultat točan, obrazloženje dopuniti

| Veličina | Rad | Provjera |
|---|---|---|
| `x_rob*` | (6.5, 179/34) | isto; 8 vertex-nejednakosti zadovoljeno (dvije aktivne) |
| `f(x_rob*)` | 978253/11560 ≈ 84.623962 | isto |
| samo `g₁^{wc}` aktivno | nije razmatrano | nedopustivo za `g₂^{wc}` (+0.815) → oba aktivna nužno |

### Zadatak 3 — formulacija ispravna

- `h(0)=1`, `h(10)=4` vrijedi.
- `D₁`, `D₂`, epigraf, rubni uvjeti — usklađeno sa zadatkom (`∇yᵢ`, `∇²yᵢ`).
- Klasa: nakon diskretizacije **LP** (kontinuirano: konveksan varijacijski problem s `L¹` kriterijem). To je rečeno, može kraće.
- Vrijednosti `J*` nisu ovdje preslagane solverom; kod (`linprog` / `highs`) odgovara formulaciji. Prihvatiti tablicu 4.1 uz napomenu o diskretnom zbroju.

### Zadatak 4 — zaključak točan, ispis matrica nije

| Veličina | Rad | Provjera |
|---|---|---|
| `λ(A_parno)`, `λ(A_neparno)` | `−1 ± jπ/2` | točno |
| `Φ_parno`, `Φ_neparno`, `Φ_cycle` (ispis) | ≈ 0.2122 / 1.9099 / −3.6476 | **krivo** (vidi §2) |
| `λ(Φ_cycle)`, `ρ` | −1.218, −0.015; ρ=1.218 | **točno** (prava matrica) |
| `K` (Python) | [−2.7120, 0.0926] | zatvorene matrice i polovi u radu se slažu s ovim `K` |
| `λ(A_cl)` | −2.356 ± 0.4387j / ±0.7617j | točno za taj `K` |
| `λ_max(A_clᵀP+PA_cl)` | −9.50·10⁻², −5.49·10⁻² | ≈ −9.48·10⁻², −5.50·10⁻² |
| `ρ(Φ_cl)` | 0.1320 | 0.1320 |

---

## DODATAK B — kako da drugi nacrt zvuči kao čovjek

Uzeti odlomak iz sadašnjeg §3.1 i zamijeniti ga ovime, pa isti rez primijeniti svugdje:

**Sada (strojno):**  
*U stvarnim inženjerskim primjenama parametri optimizacijskog modela … rijetko su egzaktno poznati. Oni podliježu mjernim pogreškama… Robusna optimizacija pristupa ovom problemu formuliranjem zahtjeva da optimalno rješenje mora zadovoljiti sva ograničenja za sve moguće realizacije… (koncept najgoreg slučaja – engl. worst-case approach).*

**Treba (studentski, tehnički):**  
*U zadatku 2 koeficijenti `aᵢⱼ` nisu poznati točno, nego leže u intervalu `[0.85 aᵢⱼ, 1.15 aᵢⱼ]`. Traži se `x` koje minimizira istu `f` i zadovoljava oba ograničenja za svaki takav `A`. To je konačan QP s 8 linearnih nejednakosti, po jednom za svaki vrh pravokutnika nesigurnosti.*

Ako rečenica ne sadrži simbol, broj ili korak rješenja — vjerojatno ne treba biti u seminaru.

---

*Kraj recenzije.*
