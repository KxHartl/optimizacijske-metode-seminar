# OMRiUS seminar review — v1.2 audit and v1.6 closure

## 0. Final closure status for v1.6

Closure date: 8 September 2026. Final artifact:
`dist/v1.6/OMRiUS_seminar_Kresimir_Hartl.pdf`, 30 physical A4 pages,
SHA-256 `799383ADB736880AC3A63E5BD5060512CEA98D62EE0376B63F5148A3F5E2AFB6`.

All findings F01–F11 from the v1.2 audit are closed in v1.6. The table records
what changed, why the new statement is defensible, and the direct check.

| Finding | Status | v1.6 closure and verification |
|---|---|---|
| F01 | CLOSED | Minimizing $\lVert Y\rVert$ is described only as selecting one feasible normalized LMI solution. Since $K=Y\mathcal Q^{-1}$ and $\mathcal Q$ is also a variable, no minimum-gain claim remains. Checked in Task 4 text, MATLAB comments, and defense Q10. |
| F02 | CLOSED | The $N=20$ versus $N=100$ comparison is limited to the two observed discrete optima. No convergence order, systematic quadrature bias, or single unproved cause is claimed. Checked against the four reproduced values in `docs/code/task3_output.txt`. |
| F03 | CLOSED | The general coefficient interval is $[a^0-0.15|a^0|,\,a^0+0.15|a^0|]$, which has the correct ordering for negative nominal coefficients. Checked explicitly with $a^0=-1$. |
| F04 | CLOSED | The true off-diagonal product is reported as $-\pi^2/4$; the positive $+\pi^2/4$ term in the characteristic polynomial is explained by the subtraction in the determinant. Direct symbolic expansion confirms the displayed polynomial. |
| F05 | CLOSED | Geometric growth is stated for the assigned initial condition $x(0)=e_1$: $x(2k)=(-9e^{-2})^k e_1$. The text does not claim that every trajectory grows. The spectral-radius calculation still proves instability. |
| F06 | CLOSED | The value-function sensitivity statement is explicitly local and conditioned on an unchanged active set. The $10^{-4}$ finite-difference check agrees with $-\mu^*$ within the printed residuals. |
| F07 | CLOSED | The robust-QP figure shows 12 representative boundary pairs and one shaded robust feasible intersection, with the feasible side identified. All 100 sets are no longer individually shaded; `rng(42)` and the 54/100 and 0/100 counts are unchanged. |
| F08 | CLOSED | The report states that the electronic attachment contains MATLAB sources in `src/` and literal outputs in `docs/code/`; the synchronized verification package contains the same files. No nonexistent printed appendix is promised. |
| F09 | CLOSED | Version metadata, the 30-page PDF, `STATE.md`, and `for_validator/` are synchronized to v1.6. The validator PDF is byte-identical to the named final PDF. |
| F10 | CLOSED | The historical comparison is retained only as review evidence. Matija's actual PDF contains the correct Task 1 result; the incorrect Markdown transcription is explicitly non-authoritative. No colleague report is used as a content source. |
| F11 | CLOSED | The orphan before Figure 4.3 and the nearly empty conclusion page were removed. $J$ is consistently an area in m², $V=wJ$ a volume in m³, and the second divided difference carries m⁻¹. All 30 pages were rendered and visually checked. |

Additional source check: all four bibliography entries point to locally available
course PDFs in `data/sources/lectures/`; no inaccessible book citation remains.
The final Tectonic build completed successfully, and its log contains no
overfull/underfull box, undefined reference/citation, missing-character, or
undefined-control-sequence warning. The original assignment and the normalized
embedded scan render identically page by page at 72 dpi.

The remainder of this document preserves the original v1.2 audit as historical
evidence. Its open-status wording and page references describe v1.2, not v1.6.

---

## Historical v1.2 audit

Datum: 7. rujna 2026. Autor rada: Krešimir Hartl. Predmet: usporedba s izvornim zadatkom, Matijinim i Ivanovim seminarom, uz neovisnu provjeru točnosti, potpunosti i prikaza.

## 1. Recenzentski zaključak

**Glavna brojčana rješenja svih četiriju zadataka potvrđena su. Nije utvrđeno zajedničko pogrešno numeričko rješenje s kolegama. Ipak, prije predaje potrebna je ciljana revizija nekoliko tvrdnji, jednog grafičkog prikaza i dokumentacije izvora.**

Najvažniji nalazi:

1. **Zajednička terminološka pogreška s Ivanom:** pozitivan izraz π²/4 naziva se umnoškom izvandijagonalnih elemenata, iako je stvarni umnožak −π²/4. Karakteristični polinom i svojstvene vrijednosti u oba rada ostaju ispravni. To je konkretna podudarnost koju treba ispraviti, ali nije dokaz prepisivanja.
2. **Samostalna važna pogreška v1.2:** minimizacija norme Y ne daje nužno regulator najmanje norme K. Postojeći regulator stabilizira sustav; netočna je dodatna tvrdnja o njegovoj optimalnosti.
3. **Samostalno nepotkrijepljeno tumačenje v1.2:** porast diskretnog troška ceste nije dokazan kao posljedica isključivo pravokutne kvadrature, niti su dvije mreže dokaz reda konvergencije O(Δx).
4. **Graf robusnog problema djelomično pokriva zahtjev:** prikazuje granice realizacija i optimum, ali nedovoljno jasno njihove dopustive strane.
5. **Vrlo sitni reziduali jednaki Matijinima reproducirani su neovisnim pokretanjem MATLAB-a.** To su ponovljivi rezultati istog algoritma, ne zajedničke pogreške.
6. **Evidencija verzija i izvora zahtijeva ispravak:** aktualni PDF ima 31 stranicu, paket `for_validator` ima stariji raspored od 29 stranica; Matijin Markdown prijepis pogrešno prenosi njegov točan rezultat; tri citirane knjige nemaju lokalni PDF ni evidentiranu iznimku.

Procjena rizika podudarnosti pretežno je **niska**, a za konkretan izraz u zadatku 4 **srednja**. Pregledani materijal ne potkrepljuje visoku razinu rizika. Ova recenzija ne utvrđuje povijest nastanka rada i ne može certificirati potpuno originalno autorstvo niti isključiti podudarnost s nepregledanim izvorima.

## 2. Izvori, verzije i metoda provjere

### 2.1. Primarni dokumenti

Sve oznake **PDF str.** znače fizički redni broj stranice, počevši od naslovnice. Kod v1.2 vrijedi: tiskana stranica = PDF stranica − 4 za glavni tekst. Matijine rukom pisane stranice citiraju se fizičkim PDF brojem.

| Oznaka | Dokument u repozitoriju | Uloga |
|---|---|---|
| K | `dist/v1.2/OMRiUS_seminar_Kresimir_Hartl.pdf` | Jedini primarni predmet ove recenzije; 31 stranica |
| Z | `TASK/Zadatak_OMRiUS_Kresimir_Hartl.pdf` | Izvorni sken službenih zahtjeva, 2 stranice |
| M | `data/sources/matija/Matija_Pongracic_OMURIUS_seminar.pdf` | Matijin stvarni PDF, uključujući rukopis |
| I | `data/sources/ivan/OMRUS_ivan-norsic.pdf` | Ivanov seminar; ne kasnije dodana `skripta_ivan.pdf` |
| N | `data/sources/lectures/` | Nastavni materijali kao kontrola zajedničkih standardnih postupaka |

SHA-256 identifikatori provjerenih artefakata:

```text
K  53664F93E83216A573D3BD74860437F1CAD6665F5E6800871BEBB53F48D40F14
Z  2513B3662C9C816D3DCC8297BE7684CCD0483F0A3185B9E4D7279FED35AC3351
M  D24938E13104EE266B470A5DD95DF27C6213A7D54C7353A5FA38EE8EF74E0159
I  EF200CD69CA3D57268BCC42024BF68186254749F6FC53DBFCD31D2596804385B
```

Kopija u `for_validator/02_REPORT_PDF/` ima SHA-256 `59DE27FD7C26959F39C46EE63DC293E43DF5B862091D843EEB735ADF209D97BB` i 29 stranica. Usporedba izvora pokazala je jednaka poglavlja i MATLAB skripte za četiri zadatka; u `main.tex` razlikuju se duljina zaglavlja i prisilni početak poglavlja na novoj stranici. Razlika PDF-ova stoga nije sama po sebi dokaz različitih matematičkih rezultata, ali onemogućuje korištenje starih brojeva stranica za aktualni dokument.

### 2.2. Što je provjereno

- Zahtjevi su čitani iz skena Z. `TASK/zadatak_omrius.md` razrađuje dodatne korake te nije tretiran kao doslovan tekst svih profesorovih obveza.
- Tekst i jednadžbe uspoređeni su s LaTeX izvorima, objavljenim PDF-ovima i MATLAB ispisima. Rukopis i grafovi provjereni su vizualno, bez oslanjanja samo na OCR.
- Provedena je neovisna matematička i numerička provjera nominalnog i robusnog QP-a, četiriju LP slučajeva, Monte Carlo pokusa, LMI certifikata i dinamike. Posebno novo pokretanje MATLAB-a R2025b reproduciralo je oba podudarna reziduala.
- Renderirano je svih 31 stranica K; pregled rasporeda proveden je kroz kontaktne listove, a svi grafovi i sumnjiva mjesta dodatno u većoj rezoluciji. To nije provjera tiska na fizičkom papiru.
- RAG je korišten za lociranje i provjeru navoda; konačnu prednost imaju izvorni PDF i neposredna matematička provjera. Tehnički zapis RAG provjere nalazi se u §12.
- Nije provođena pretraga cjelokupne internetske literature ni komercijalni postupak detekcije plagijata. Ne izvodi se postotak originalnosti iz broja zajedničkih riječi ili formula.

### 2.3. Granice ranijih evidencija

**Matijin prijepis nije vjeran izvorniku.** Datoteka `data/sources/matija/Matija_Pongracic_OMURIUS_seminar.md:79` navodi x=(5.4762,4.5238), dok stvarni M, PDF str. 6, rukom daje ispravno x=(190/33,140/33); numerički ispis na str. 10 potvrđuje taj rezultat. Stara tvrdnja u `STATE.md` o Matijinu pogrešnom optimumu zato se ne smije koristiti kao dokaz različitosti radova. Bilješka `matija/notes.md` da je drugi zadatak pogrešan također nije zamjena za provjeru aktualnog PDF-a i zahtjeva.

`for_validator/README.md` izričito identificira šest ranijih recenzija kao recenzije **v1.0**. Nije pronađen jasno označen PDF v1.1 i sljediv zaseban popis njegovih komentara. Stoga §10 provjerava konkretne stare nalaze, ali ne tvrdi da su svi komentari v1.1 zatvoreni.

## 3. Registar zajedničkih pogrešaka i neuobičajenih podudarnosti

| ID | Nalaz i dokaz | V1.2 | Referentni rad | Ocjena, sigurnost i postupak |
|---|---|---|---|---|
| S01 | Pozitivan π²/4 nazvan je umnoškom izvandijagonalnih elemenata | PDF24 / tisk20, §5.2: „Za neparni mod umnožak izvandijagonalnih elemenata…” | I PDF19 / tisk12: „U oba moda umnožak izvandijagonalnih elemenata je jednak”, potom αβ=π²/4 | Potvrđena zajednička terminološka nepreciznost; visoka sigurnost. Ispraviti K. Srednji rizik specifične podudarnosti; nije zajednički pogrešan rezultat. |
| S02 | Dualni procjep 2.480e−10 | PDF11 / tisk7 | M PDF12 | Potvrđena podudarnost završnih znamenki; neovisno reproducirana u MATLAB-u. Nizak rizik nakon provjere, bez izmjene brojeva. |
| S03 | Maksimalni robusni rezidual −2.793e−11 | PDF15 / tisk11 | M PDF16 | Isto kao S02; isti deterministički algoritam i podaci. Ne prikazivati kao grešku. |
| S04 | Osam vršnih ograničenja, dva aktivna vrha i isti optimum | PDF13–15 | M PDF14–17; I PDF13–14 | Matematička posljedica istog intervalnog problema, ne proizvoljna podudarnost. |
| S05 | Segmentna simulacija i tolerancije 1e−9/1e−11 | PDF24–25; `src/task4_lmi_switched_stabilization.m` | I kod PDF34–35 | Tehnički smislen postupak zbog prespajanja svake sekunde. Uobičajene tolerancije; različiti horizonti i regulatori. Niska specifičnost. |

### 3.1. Razgraničenje nalaza S01

U matrici oblika A=[−1,−α;β,−1], za α,β>0, stvarni izvandijagonalni umnožak jest A12 A21=−αβ. Karakteristični polinom je (λ+1)²+αβ. Ivan pozitivne α i β prethodno definira, pa je njegov račun αβ=π²/4 ispravan. Pogrešno je imenovanje tog izraza kao umnoška stvarnih izvandijagonalnih elemenata. U K je prisutna ista nepreciznost.

**Preporučeni ispravak:** „U oba moda umnožak izvandijagonalnih elemenata jednak je −π²/4, pa karakteristični polinom iznosi (λ+1)²+π²/4.” Time se uklanja stvarna nepreciznost, a ne samo površinska sličnost.

### 3.2. Neovisna kontrola podudarnih reziduala

Novo pokretanje iz zadanih matrica i s algoritmom `interior-point-convex` dalo je:

```text
dualni procjep = 2.4801938280916147e-10
maximalni robusni rezidual = -2.7927882229050738e-11
exitflag = 1 za primarni, dualni i robusni QP
```

To reproducira ispis u `docs/code/task1_output.txt` i `task2_output.txt`. Matijin objavljeni kod također koristi `interior-point-convex`. Nema stručnog razloga mijenjati te vrijednosti radi različitosti. Reprodukcija dokazuje da ih vlastiti proračun daje, ali sama ne dokazuje povijest autorstva izvornog koda.

### 3.3. Pogreške kolega koje nisu prenesene

| Referenca | Pogreška ili nepreciznost kolege | Stanje u K |
|---|---|---|
| M PDF7 | Tekst granice x2≥x1+3, dok treba x2≥x1−3; crtež odgovara −3 | Ispravna granica, nije preneseno |
| M PDF13 | Pozitivan znak uz derivaciju osjetljivosti, bez jasne suprotne definicije perturbacije | Eksplicitno definirano Gx−h≤v i derivacija −μ; nije preneseno |
| M PDF34 | Uokvireni drugi član K je −1.1744, a ispis i kod koriste −1.7144 | Drugi regulator, konzistentan kroz tekst i ispis |
| I PDF8 / tisk1 | H12 nazvan polovicom koeficijenta mješovitog člana u konvenciji ½xᵀHx, iako je numerički H12=−0.3 točan | Nema te rečenice; matrica ispravna |
| I PDF14–15 / tisk7–8 | Uzorkovni presjek poistovjećen s egzaktnim robusnim skupom | K izričito odvaja Monte Carlo ilustraciju od certifikata preko svih vrhova |
| I PDF21 / tisk14 | U obrazloženju stope pada pozivanje na donju granicu za V ondje gdje je potrebna gornja | Nije ponovljen isti pogrešan međukorak; stopa K neovisno potvrđena |

Ovi nalazi ne dokazuju neovisno autorstvo, ali sprječavaju pogrešno proglašavanje svih zajedničkih metoda i rezultata zajedničkim pogreškama.

## 4. Usporedba po zadacima i podzadacima

### 4.1. Zadatak 1 — QP, KKT, dualnost i osjetljivost

Sva tri rada koriste isti zadani cilj i ograničenja. Zato isti Hessian, racionalni optimum i množitelji nisu proizvoljno preklapanje.

| Podzadatak | K: pristup i detaljnost | M | I | Značenje razlike / preporuka |
|---|---|---|---|---|
| (a), K PDF6 | Svojstvene vrijednosti, koercivnost, postojanje, jedinstvenost i konkretna Slaterova točka [7,6] | PDF4: parcijalni izvodi i Sylvesterovi minori 2 i 7.91 | PDF9: svojstvene vrijednosti i Sylvester | K ima sadržajan dodatak o postojanju i Slateru; zadržati |
| (b), K PDF7–8 | Četiri aktivna skupa, redoslijed 00,10,01,11; racionalni rezultati i blok-matrica | PDF5–7: rukopis, redoslijed 11,00,10,01 | PDF9–10: tablica svih skupova, blok-matrica, razrada aktivnog g1 | Enumeracija je zadana metodom; redoslijed nije jednak M; nije potrebno izmišljati alternativni algoritam |
| (c), K PDF9 | Dopustivi skup, konture, bezuvjetni minimum, optimum i tri gradijenta; navedeno skaliranje strelica | PDF7: ručna skica s tri gradijenta | PDF11: računalni graf, plavi skup, posebno označena optimalna kontura | Obvezne varijable iste, izgled i naglasci različiti; bezuvjetni minimum je opravdan dodatak |
| (d), K PDF10 | `quadprog`, sažeti kod, ispis i tablična usporedba | PDF8–10: opširniji kod i reziduali | PDF12: `quadprog` i YALMIP, detalji u prilogu | K sažetiji od M u kodu, eksplicitan u usporedbi rezultata; sačuvati vlastiti log |
| (e), K PDF10–11 | Ekspandirana dualna funkcija, konstantni član, zaseban QP u μ | PDF11–12: naglasak na kodu i rezidualima | PDF12: kompaktni zatvoreni oblik i rezultat | K detaljniji u algebri; isti gap objašnjen neovisnom reprodukcijom |
| (f), K PDF11–12 | Perturbirani problem, −μ, jednostrana razlika δ=1e−4 i rezerva 1.484848 | PDF13: kratki rukopis, sporan znak | PDF12: −μ, centralna razlika ε=1e−6 i rezerva | Stvarno različita numerička provjera; ne mijenjati ispravni predznak ili zadane brojke |

Nije potreban dodatni graf dualne površine ili osjetljivosti. Dovoljna je postojeća numerička provjera. Teorijsku rečenicu o diferencijabilnosti suziti na ovaj problem (§7, F06).

### 4.2. Zadatak 2 — robusni QP

Sva tri rada polaze od ±15% nesigurnosti istih koeficijenata. Za svaki redak postoje četiri vrha, odnosno osam linearnih nejednakosti ukupno.

| Aspekt | K | M | I | Procjena |
|---|---|---|---|---|
| Model i dokaz | PDF13–14: skupovi, supremum i dokaz konveksnom kombinacijom | PDF14: konkretni intervali i osam ručno zapisanih redaka | PDF13: vršni argument uz vezu s predavanjem | K daje detaljniji dokaz; početna opća formula intervala ima vlastitu notacijsku pogrešku |
| Optimum i međukoraci | PDF14–15: nedopustivi kandidat s jednim aktivnim ograničenjem, sjecište, KKT množitelji, tablica svih osam provjera | PDF15–17: numeričko rješenje, množitelji i ručna skica | PDF13–14: rezultat i kraći izvod sjecišta | Dodatni kandidat i provjera svih vrhova sadržajno razlikuju K |
| Uzorak | 100 realizacija, `rng(42)`; 54/100 i 0/100 | Nije pronađen niz slučajnih skupova; prikazane najgore granice | 300 realizacija, karta udjela dopustivosti i dodatne granice | Broj uzoraka nije zadan; očite su različite izvedbe |
| Graf | PDF16: sive granice, nominalne i najgore granice, oba optimuma | PDF17: rukom najgore granice i optimum | PDF14: sivinska karta i zelena kontura uzorkovnog presjeka | Nema potrebe za kozmetičkom promjenom; K treba jasnije označiti dopustive strane |
| Tumačenje | PDF16–17: uzorak nije dokaz; jamstvo daju vrhovi | Naglasak na rješenju najgoreg slučaja | Uzorkovni presjek opisan previše snažno | Važna Ivanova interpretacijska pogreška nije preuzeta |

Ne mijenjati `rng(42)` ili broj uzoraka radi prikrivanja podudarnosti. Zadržati ponovljivost. Ako se graf dorađuje, mijenjati ono što nedostaje njegovoj matematičkoj poruci: poluravnine i njihov presjek.

### 4.3. Zadatak 3 — nivelacija ceste

Jednaki su zadani L=10, polinom terena, krajnje visine, N=20/100 te b1=0.5 i b2=0.5/0.2. Jednaki profili i skalirane optimalne vrijednosti očekivani su za isti problem; eventualno različiti profili uz isti cilj mogu potjecati od nejedinstvenosti LP optimuma.

| Aspekt | K | M | I | Procjena |
|---|---|---|---|---|
| Model | PDF18: integral, jedinična širina, jednake težine iskopa/nasipa | PDF18–21: diskretna suma i pomoćne varijable | PDF15–17: integral, diskretizacija, apsolutne vrijednosti | Fizikalno obrazloženje K je detaljnije; jasno razlučiti površinu od volumena |
| Kriterij | Δx∑|y−h|; jedinica m² | Sirovi zbroj ∑|y−h| | Sirovi i naknadno skalirani kriterij | Pozitivni faktor ne mijenja minimizator; sirovi brojevi različitih mreža nisu izravno usporedivi |
| Ograničenja | D1, D2 i objedinjeni blok LP matrice | Ručno razvijeni blokovi i dimenzije, detaljnije jednakosti | Posebno rastavljeni parovi nejednakosti | Metoda i konačne razlike proizlaze iz zadatka; ne treba ih mijenjati |
| Rješavanje | PDF20–21: dualni simpleks, četiri slučaja i provjere | PDF22–27: dualni simpleks i opširan kod | PDF18: tablica i broj aktivnih ograničenja | I je detaljniji po broju aktivnih ograničenja; K po fizikalnom mjerilu |
| Grafovi | PDF21–23: dvije usporedbe N20/N100 po A/B te treći graf derivacija | PDF25–27: zasebni tamni grafovi | PDF18: raspored 2×2, teren crn, cesta crvena, rubne točke zelene | K već ima drukčiju i svrsishodnu organizaciju |
| Tumačenje | Konkretne međe y(9)≥3.5 i y(8)≥3; utjecaj b2 i mreže | Kratka napomena o odstupanjima čvorova | Dolina oko x≈8, aktivnost ograničenja i oko 2% promjene | Vlastite donje međe korisne; ukloniti nepotkrijepljeni uzrok/konvergencijski red |

M navodi sirove kriterije približno 3.832359, 19.659396, 4.907453 i 25.060469. Nakon množenja pripadajućim Δx=0.5/0.1 dobivaju se vrijednosti K. To je razlika mjerila, ne različito rješenje. I to izričito pokazuje tablicom oba kriterija.

### 4.4. Zadatak 4 — robusna stabilizacija

| Aspekt | K | M | I | Procjena |
|---|---|---|---|---|
| Hurwitz | PDF24: polinom prvog moda i zaključak za drugi | PDF28: oba determinantna izvoda | PDF19: opća matrica s α,β | Standardni postupak; specifična zajednička nepreciznost K/I je S01 |
| Simulacija bez upravljanja | PDF24–26: segmentni `ode45`, 20 s, vrijeme i fazna ravnina | PDF29–31: integracija s `floor(t)` kroz 40 s; dodatna norma | PDF20 i prilog: segmentno, 12 s | Različiti horizonti i organizacija. Segmentni pristup opravdan prekidima dinamike |
| Dokaz nestabilnosti | Egzaktne prijelazne matrice i ρ=9e−2 | Naglasak na numeričkoj simulaciji | Naglasak na numeričkoj simulaciji | Monodromijski dokaz K jest sadržajna razlika; zadržati |
| LMI transformacija | Q=P⁻¹, Y=KQ, kongruencija | Ista osnovna transformacija | Ista osnovna transformacija | Nastavni standard; sama sličnost nije sumnjiva |
| Numerički odabir | Q≥I, LMI≤−I, min ‖Y‖₂, SDPT3 | ε=1e−8, dopustivost, SDPT3 | ε=1e−4, dopustivost, SeDuMi | Formulacije i kriteriji nisu identični |
| K | [−3.424629,−0.104650] | Ispis/kod [−16.2912,−1.7144]; okvir ima tipfeler | [−6.800717,−0.532251] | Različita valjana pojačanja očekivana su u nejedinstvenom LMI problemu; različitost sama ne dokazuje autorstvo |
| Certifikat i grafovi | PDF27–28: P, obje maksimalne svojstvene vrijednosti, α, monodromija; nivoelipse | PDF32–36: izvod, kod, odzivi i norma | PDF20–22: certifikat i 12 s odziv | K pruža dodatni analitički dokaz i elipse; graf norme kao kod M nije potreban |

Ne preporučuje se mijenjanje valjanog regulatora radi originalnosti. Ispraviti tvrdnju o najmanjem pojačanju i precizirati uvjet pod kojim norma otvorenog sustava geometrijski raste.

## 5. Stilska i frazeološka usporedba

| Mjesto / obrazac | Usporedba | Specifičnost i preporuka |
|---|---|---|
| Uvodi: K PDF5, I PDF8 | Oba redom navode četiri problema, konveksnost, MATLAB i skripte | Niska. Zadatak sam određuje strukturu; K detaljnije navodi solvere i verziju. Nije izdvojen dugi doslovno zajednički pasus. |
| KKT, dualnost i LP | „Lagrangeova funkcija”, „KKT uvjeti”, „konveksna ljuska svojih vrhova” i standardni nazivi ograničenja | Stručni termini nemaju korisne zamjene radi originalnosti. Terminologiju zadržati, izvor nastavnog postupka precizno navesti. |
| LMI izvod | „zajednička kvadratna Ljapunovljeva funkcija”, „transformacija kongruencije” | Standardan sadržaj potvrđen nastavnim materijalom N7, PDF25 i 28–33. Niz supstitucija ne treba umjetno preuređivati. |
| Hurwitzovost: K PDF24, I PDF19 | Slična konstrukcija rečenice o „umnošku izvandijagonalnih elemenata” | Izdvojeni, konkretni zajednički propust S01. Zamijeniti matematički preciznom rečenicom iz §3.1. |
| Tumačenje ceste: K PDF22, I PDF19 | Dolina, aktivna ograničenja i približno 2% promjene | Opažanja prirodno slijede istom terenu. K daje dodatne numeričke međe; zadržati ih. Ukloniti vlastitu nedokazanu tvrdnju o kvadraturi. |
| Zaključci | Redom odgovaraju na ista četiri zadatka | Očekivano. K može biti sažetiji jer ponavlja mnoge tablične brojke i prelazi na dodatnu stranicu. |

Nije izdvojen dodatni pasus s dovoljno specifičnom kombinacijom formulacija i istih pogrešaka koji bi opravdao ocjenu visokog rizika. To je ograničeni nalaz ove usporedbe, a ne jamstvo da nema parafraziranja ili utjecaja među radovima. Matijin rukopis i OCR ograničavaju automatiziranu frazeološku usporedbu; zato se ne navodi pseudo-precizan postotak sličnosti.

**Sadržajne intervencije za autentičnost:** zadržati vlastitu Slaterovu provjeru, tablicu svih robusnih reziduala, konkretne međe nivelete i egzaktni monodromijski dokaz. To su provjerljivi dijelovi vlastitog objašnjenja. Ako su pojedini tuđi tekstovi ili kod stvarno korišteni kao polazište, navesti stvaran izvor i opseg korištenja; recenzija ne može rekonstruirati to iz PDF-a. Ne preporučuje se zamjena boja, oznaka, slučajnog sjemena ili numerike samo radi manje vizualne sličnosti.

## 6. Točnost i potpunost prema izvornom zadatku

### 6.1. Matrica zahtjeva

| Zahtjev iz Z | Mjesto u K | Ocjena |
|---|---|---|
| 1(a): konveksnost s obrazloženjem | §2.2, PDF6 / tisk2 | Ispunjeno |
| 1(b): KKT, projektne varijable i množitelji | §2.3, PDF7–8 / tisk3–4 | Ispunjeno; četiri aktivna skupa |
| 1(c): dopustivi skup, nivo-krivulje, gradijenti svih ograničenja i cilja | §2.4, sl.2.1, PDF9 / tisk5 | Ispunjeno, uključujući neaktivni g2 |
| 1(d): numeričke primarne i dualne varijable te usporedba s (b) | §2.5, PDF10 / tisk6 | Ispunjeno |
| 1(e): postaviti i numerički riješiti dualni problem | §2.6, PDF10–11 / tisk6–7 | Ispunjeno; zaseban dualni QP |
| 1(f): osjetljivost na desne strane ograničenja | §2.7, PDF11–12 / tisk7–8 | Ispunjeno; ograničiti opću teorijsku formulaciju |
| 2: robusno rješenje za ±15% | §3.1–3.4, PDF13–15 / tisk9–11 | Ispunjeno; ispraviti početnu intervalnu notaciju |
| 2: dopustivi skupovi slučajnih realizacija i optimum na istoj slici | §3.5, sl.3.1, PDF16 / tisk12 | Djelomično vizualno ispunjeno: dopustive strane nedovoljno jasno označene |
| 3: formulirati i klasificirati problem | §4.1–4.3, PDF18–19 / tisk14–15 | Ispunjeno: LP |
| 3: riješiti A20, A100, B20, B100 | §4.4, PDF20–22 / tisk16–18 | Sva četiri slučaja ispravno riješena |
| 4(a): Hurwitzovost oba moda | §5.2, PDF24 / tisk20 | Ispunjeno; ispraviti naziv predznačnog umnoška |
| 4(b): simulacija otvorenog kruga, oba prikaza i ocjena stabilnosti | §5.3, PDF24–26 / tisk20–22 | Ispunjeno; početni uvjet točan |
| 4(c): stabilizirajući K, simulacija i oba prikaza | §5.4, PDF26–28 / tisk22–24 | Ispunjeno; stabilizacija potvrđena, minimalnost pojačanja nije |

**Nije opravdano zaključiti da nedostaje cijeli zadatak ili podzadatak.** Glavni nedostatci su u preciznosti pojedinih objašnjenja i potpunosti označavanja sl.3.1. Zadatak ne traži dokaz globalno najmanjeg pojačanja regulatora.

### 6.2. Provjerene glavne vrijednosti

| Veličina | Vrijednost / status |
|---|---|
| Hessian | Q=[2,−0.3;−0.3,4], det Q=7.91, svojstvene vrijednosti 1.955969 i 4.044031 |
| Nominalni optimum | x*=(190/33,140/33)=(5.757576,4.242424) |
| Nominalni cilj i množitelji | p*=2000/33=60.606061; μ*=(404/33,0) |
| Osjetljivost | Analitički (−12.242424,0); jednostrana razlika (−12.242364,0) |
| Robusni optimum | (13/2,179/34)=(6.5,5.264706) |
| Robusni cilj | 978253/11560=84.623962 |
| Aktivni robusni vrhovi | Redci 1 i 7 u K; množitelji 17.607439 i 1.344118 |
| Monte Carlo | `rng(42)`, 100 uzoraka: nominalni 54 kršenja, robusni 0 |
| LP A20 / A100 | 1.916180 / 1.965940 m²; oba `exitflag=1` |
| LP B20 / B100 | 2.453727 / 2.506047 m²; oba `exitflag=1` |
| Maksimalni diskretni nagib | 0.5 u sva četiri LP slučaja |
| Maksimalna druga podijeljena razlika | 0.5 za A i 0.2 za B |
| Otvoreni sustav | Φ=e⁻²diag(−9,−1/9), ρ=1.218018>1; nestabilan |
| Regulator | K=[−3.424629,−0.104650] |
| Matrica P | [0.800314,0.217413;0.217413,0.763286], pozitivno definitna |
| Ljapunovljev certifikat | λmax(AclᵀP+PAcl)=−0.910478 i −0.329090 |
| Zajamčena stopa | α=0.288374 s⁻¹; faktor ocjene norme 1.332031 |
| Zatvoreni ciklus | ρ=0.069720<1 |
| Simulirane norme | Otvoreno ‖x(20)‖≈7.1868; zatvoreno ‖x(5)‖≈1.5176e−3, ‖x(20)‖≈4.7232e−12 |

Posljednje znamenke mogu ovisiti o verziji rješavača i tolerancijama; strogo provjerljive racionalne vrijednosti i predznaci certifikata važniji su od slučajne potpune identičnosti decimalnog ispisa. Monte Carlo broj nije dokaz robusnosti; analitički vršni ekvivalent jest.

## 7. Tehnički nalazi i konkretni ispravci

### F01 — Važno: min ‖Y‖ nije minimum pojačanja K

**Lokacija:** K PDF27 / tisk23, §5.4; `docs/chapters/04-zadatak4-lmi-stabilizacija.tex:124`.

Tvrdnja „čime se dobiva regulator najmanjeg pojačanja” nije točna jer je K=YQ⁻¹, a Q je također optimizacijska varijabla. Postojeći K ima normu približno 3.426228. Sljedeći par zadovoljava iste normalizirane LMI uvjete:

```text
K_alt = [-3, 0]
Q_alt = [1.7, -0.7; -0.7, 1.9]
Y_alt = K_alt*Q_alt = [-5.1, 2.1]
eig(Q_alt-I) = [0.09289322, 1.50710678]
lambda_max(M_par+I) = -0.04368249
lambda_max(M_nep+I) = -0.04031423
```

Ovdje je Mi=AiQ+QAiᵀ+BY+YᵀBᵀ. Dakle Q≥I i Mi≤−I, uz ‖K_alt‖₂=3<3.426228. To je neposredan kontraprimjer tvrdnji, ne prijedlog zamjene postojećeg regulatora.

**Zamjena:** „Među dopustivim parovima minimizira se norma pomoćne varijable Y radi odabira jednog rješenja. Ovaj kriterij ne jamči najmanju normu pojačanja K.”

**Kriterij zatvaranja:** uklonjena tvrdnja minimalnosti K; postojeći P, K, LMI certifikat i grafovi ostaju međusobno konzistentni.

### F02 — Važno: nedokazano objašnjenje utjecaja mreže

**Lokacija:** K PDF22 / tisk18, §4.5; ponovljeno PDF29 / tisk25; `03-zadatak3-cesta-lp.tex:182`, `zakljucak.tex:28`.

Zbog rubnih uvjeta krajnji reziduali r0=|y0−h0| i rN=|yN−hN| jednaki su nuli. Zato vrijedi:

Δx∑(i=0…N) ri = Δx[r0/2 + ∑(i=1…N−1)ri + rN/2].

Upotrijebljena suma jednaka je trapeznom izrazu na čvornim rezidualima. Uz promjenu N mijenjaju se i diskretna ograničenja i optimizirani profil. To ne dokazuje neki drugi univerzalni red pogreške, ali pokazuje zašto iz dva optimuma nije moguće zaključiti ni sustavnu podcjenjenost kontinuiranog integrala ni navedeni uzrok i red O(Δx).

**Zamjena:** „Pri povećanju N s 20 na 100 diskretni optimum raste za 2.60% u slučaju A i 2.13% u slučaju B. Promjena uključuje učinak diskretizacije funkcije cilja i ograničenja; dvije mreže nisu dovoljne za utvrđivanje reda konvergencije ili predznaka pogreške prema kontinuiranom problemu.”

**Kriterij zatvaranja:** ista dorada u poglavlju i zaključku. Dodatna studija više mreža nije potrebna za zadani seminar ako se ukloni nepotkrijepljena tvrdnja.

### F03 — Manje, ali obvezno: obrnute granice intervala

**Lokacija:** K PDF13 / tisk9, (3.1); `02-zadatak2-rob-qp.tex:7`.

Za a0=−1 zapis [0.85a0,1.15a0] daje [−0.85,−1.15]. Sljedeći eksplicitni intervali i račun su ispravni. Zadatak verbalno koristi „od…do…”, što može objasniti nastanak nepreciznosti, ali ne opravdava formalno obrnut interval.

**Zamjena:** aij∈[aij⁰−0.15|aij⁰|, aij⁰+0.15|aij⁰|], ili aij=sij aij⁰, sij∈[0.85,1.15].

**Kriterij zatvaranja:** opći i eksplicitni zapisi su suglasni; numeriku ne treba mijenjati.

### F04 — Manje: zajednička nepreciznost umnoška

**Lokacija:** K PDF24 / tisk20; `04-zadatak4-lmi-stabilizacija.tex:41`.

Ispravak prema S01 i §3.1. **Nije potrebno ponovno izvoditi svojstvene vrijednosti**, jer su polinom i konačne vrijednosti ispravni. U registru rizika ovaj se propust odvojeno prati zbog podudarnosti s Ivanom.

### F05 — Manje: geometrijski rast ovisi o početnom smjeru

**Lokacija:** K PDF26 / tisk22, iza (5.10); `04-zadatak4-lmi-stabilizacija.tex:91`, te sažeta formulacija u zaključku.

ρ>1 dokazuje nestabilnost, ali ne rast svake trajektorije. Za x(0)=[0,1] uzorkovana norma opada faktorom e⁻²/9. Za zadano x(0)=[1,0] zaključak o geometrijskom rastu jest točan.

**Zamjena:** „Za zadani x(0)=[1,0]ᵀ vrijedi ‖x(2k)‖=(9e⁻²)^k, pa norma u trenucima 2k raste geometrijski i ravnoteža sklopnog sustava nije stabilna.”

### F06 — Manje: Slaterov uvjet sam ne jamči diferencijabilnost

**Lokacija:** K §2.7, PDF11 / tisk7; `01-zadatak1-qp.tex:247`.

Generička formulacija da za konveksan problem sa Slaterovim uvjetom vrijedi obična derivacija −μ preširoka je bez dodatne regularnosti. Za ovaj QP lokalni aktivni skup daje navedenu ispravnu osjetljivost.

**Zamjena početka:** „Za ovaj problem, lokalno oko neperturbirane desne strane i bez promjene aktivnog skupa, vrijedi…” Ne širiti seminar općom teorijom nediferencijabilnih vrijednosnih funkcija.

### F07 — Dopuna potpunosti: dopustiva strana na robusnom grafu

**Lokacija:** K sl.3.1, PDF16 / tisk12; `02-zadatak2-rob-qp.tex:161` i pripadajuća MATLAB rutina crtanja.

Dodati strelice dopustivosti ili prozirno sjenčanje nekoliko reprezentativnih skupova. Za zadane predznake koeficijenata svaka realizacija zadovoljava x2≥max(l1k(x1),l2k(x1)), gdje su l1k i l2k prikazani granični pravci. Jasno označiti i robusni presjek, uz postojeća oba optimuma.

**Kriterij zatvaranja:** čitatelj iz samoga prikaza može odrediti dopuštenu stranu i položaj robusnog optimuma. Sjenčanje svih 100 skupova nije preporučljivo jer može zakloniti bitne elemente.

### F08 — Sljedivost literature prema pravilima projekta

**Lokacija:** K PDF31 / tisk27; `docs/references.bib` i `data/SOURCES_LOG.md`.

Citirani `boyd2004convex`, `bental2009robust` i `boyd1994lmi` nemaju odgovarajuće lokalne PDF-ove u `data/sources/` ni evidentiranu paywall iznimku. Nastavni PDF-ovi postoje. Ovo je nedostatak sljedivosti prema AGENTS pravilima, **ne tvrdnja da su knjige ili citati izmišljeni**.

**Postupak:** pribaviti odgovarajući dostupni izvor i provjeriti stvarnu tvrdnju/stranicu kroz RAG ili zamijeniti citat odgovarajućim stvarno provjerenim nastavnim izvorom. Zadržati samo literaturu koja je stvarno korištena. Ako se koristi propisana iznimka za nedostupni PDF, transparentno je evidentirati. U ovoj recenziji literatura nije preuzimana niti je bibliografija mijenjana.

### F09 — Prilog i reproducibilnost predaje

**Lokacija:** K uvod, PDF5 / tisk1, tvrdnja „Skripte se nalaze u prilogu”.

PDF završava literaturom, bez punog zasebnog priloga sa skriptama. U tekstu postoje odabrani isječci, a potpuni izvori su u repozitoriju/paketu. Nije jasno znači li „prilog” elektronički prilog uz predaju.

**Postupak:** ako se predaje paket, napisati „Potpune MATLAB skripte priložene su u elektroničkom prilogu…” s točnom lokacijom. Ako se predaje samo PDF, ispraviti tvrdnju ili osigurati dostupnost punog koda. Ne treba automatski dodavati mnogo stranica koda u glavni tekst.

### F10 — Evidencija verzija i nepouzdan prijepis

Aktualni K ima **31**, a ne 29 stranica. `max_pages: 30` je projektno konfigurirano ograničenje; nije u ovom pregledu potvrđeno kao zasebno profesorovo pravilo iz skena. Aktualni raspored prelazi projektni prag za jednu stranicu. `for_validator` nije ista publikacijska verzija.

Matijin netočan Markdown prijepis ne smije ostati izvor netočnih tvrdnji o izvorniku. **Postupak:** pri sljedećem uređivanju evidencije jasno označiti prijepis kao neprovjeren ili ga ispraviti prema PDF-u; nakon završne dorade sinkronizirati predajni paket i navod broja stranica. Izvorne PDF-ove sačuvati.

### F11 — Manje vizualne i dimenzijske dorade

- PDF23 / tisk19 počinje izoliranom riječi „radova.” iz prethodnog odlomka. Prelomiti odlomak/sliku tako da riječ ne ostane sama.
- PDF30 / tisk26 sadrži kratak nastavak zaključka i mnogo praznine. Sažeti ponovljene brojke ili urediti prijelom; to može pomoći i projektnom ograničenju opsega.
- U tablici 4.1 dodati jedinicu m⁻¹ uz drugu podijeljenu razliku. Tablica je inače čitljiva i bez sudara stupaca.
- Precizno razlikovati J u m² i V=wJ u m³. Za w=1 m brojne vrijednosti jednake su u tim jedinicama, ali površina nije volumen. Sadašnja rečenica nije jednoznačna dimenzijska greška jer se „izraženoj u m²” gramatički odnosi na površinu; preporuka služi jasnoći.
- Sl.5.2 prikazuje početni vremenski prozor do približno 8 s, a tekst daje i x(20). U potpisu navesti da je prikazan početni dio simulacije; sama razlika prozora nije pogreška simulacije.

## 8. Inventar grafova i akademska prezentacija

| Slika / lokacija | Svrha | Nužnost | Nalaz i konkretna odluka |
|---|---|---|---|
| 2.1, PDF9 / tisk5 | Dopustivi skup, konture, optimum i svi gradijenti | Izričito traženo 1(c) | Zadržati. Oznake gradijenata bliske su, ali čitljive; skaliranje strelica je objašnjeno. |
| 3.1, PDF16 / tisk12 | Slučajne realizacije i robusni/nominalni optimum | Izričito traženo zadatkom 2 | Zadržati i dopuniti dopustive strane, F07. |
| 4.1, PDF21 / tisk17 | Teren i cesta A, N20/N100 | Koristan prikaz dvaju zadanih rješenja | Zadržati; neposredna usporedba mreža smislenija je od četiri razdvojena prikaza. |
| 4.2, PDF22 / tisk18 | Teren i cesta B, N20/N100 | Koristan prikaz preostalih rješenja | Zadržati. |
| 4.3, PDF23 / tisk19 | Nagib i druga podijeljena razlika A/B za N100 | Dodatni dijagnostički prikaz, opravdan raspravom | Zadržati zbog provjere aktivnih ograničenja. Nije nužno dodavati iste panele za N20 jer tablica daje provjeru sva četiri slučaja. |
| 5.1, PDF25 / tisk21 | Otvoreni vremenski odziv i fazna trajektorija | Izričito traženo 4(b) | Zadržati; analitička monodromija daje dokaz izvan samoga grafa. |
| 5.2, PDF28 / tisk24 | Zatvoreni vremenski odziv i fazna trajektorija s nivoelipsama | Izričito traženo 4(c); elipse koristan dodatak | Zadržati, precizirati vremenski prozor u potpisu. |

**Odgovor na pitanje o „svim i isključivo potrebnim grafovima”:** sva izričito tražena vrsta prikaza prisutna je, uz navedenu djelomičnu manjkavost robusnog skupa. Nema očito besvrhovitog cijelog grafa. Sl.4.3 nije doslovno dodatno zahtijevana u skenu, ali opravdano pokazuje proces/provjeru rješavanja. Ako bi se tražio apsolutni minimum, ona je prvi kandidat za dodatak; za akademski potpun prikaz preporučuje se zadržati je.

Nisu potrebni novi grafovi dualne površine, upravljačkog signala u(t), Ljapunovljeve funkcije V(t), konvergencije solvera ili norme stanja. Ne treba uvoditi vizualizacije samo zato što ih ima kolega. Postojeći grafovi imaju oznake osi, legende i potpise te su čitljivi; pri pregledu nije uočeno očito rezanje ili preklapanje. Tamni Matijini prikazi i Ivanov raspored ceste 2×2 vizualno se razlikuju od K.

Konzolni ispis uz tablicu 4.1 velikim dijelom ponavlja iste brojeve. To nije tehnička pogreška; za skraćivanje rada može se zadržati tablica u tijelu, a puni ispis u elektroničkom prilogu.

## 9. Matrica rizika

Rizik podudarnosti nije isto što i ozbiljnost matematičke pogreške. Razine se odnose na pregledane dokumente i ne predstavljaju vjerojatnost plagijata.

| Poglavlje | Rizik specifične podudarnosti | Točnost / potpunost | Obrazloženje i prioritet |
|---|---|---|---|
| Uvod | Niska | Manja dokumentacijska dorada | Sličan tok očekivan; pojasniti elektronički prilog |
| Zadatak 1 | Niska | Rješenje točno; manja teorijska ograda | Aktivni skupovi zadani metodom; jednak rezidual neovisno reproduciran |
| Zadatak 2 | Niska | Rješenje točno; dopuniti graf i interval | Različiti uzorci i grafovi; jednak rezidual reproduciran; MC nije proglašen dokazom |
| Zadatak 3 | Niska | LP rezultati točni; važna dorada tumačenja | Isto mjerilo nakon skaliranja; različiti prikazi; vlastita pogreška o kvadraturi |
| Zadatak 4 | Srednja, lokalizirana na S01 | Stabilizacija točna; važna netočna tvrdnja o minimumu K | Zajednički terminološki propust s I; različiti K, kriteriji i dodatni dokaz |
| Zaključak | Niska | Prenosi F02 i skraćenu generalizaciju F05 | Uskladiti nakon ispravka poglavlja; sažeti ponavljanje |
| Literatura i paket | Nema osnove za ocjenu autorstva | Važan nedostatak sljedivosti | Nedostaju PDF-ovi triju citiranih knjiga; neusklađene publikacijske kopije |

**Visoka razina rizika nije dodijeljena** jer nije potkrijepljena pronađenim dokazima. Srednja ocjena zadatka 4 ne odnosi se na cijeli izvod, nego na konkretan zajednički naziv pogrešnog predznaka.

## 10. Status ranijih primjedbi

Ovo je provjera konkretnih primjedbi iz dostupnih recenzija v1.0, ne formalno zatvaranje neidentificiranog paketa v1.1.

| Raniji problem | Status u K | Dokaz / preostali posao |
|---|---|---|
| Pogrešne matrice prijelaza stanja | Zatvoreno | PDF25–26: e⁻¹ matrice i e⁻²diag(−9,−1/9) konzistentni |
| Više različitih K i hardkodirani fallback | Zatvoreno u aktualnom seminaru i kodu | Jedan K i stvarna YALMIP/SDPT3 sinteza; F01 se odnosi na dodatno tumačenje kriterija |
| Heuristički vrhovi bez potpune provjere | Zatvoreno | Svih osam nejednakosti i KKT provjera na PDF15 |
| Monte Carlo kao dokaz robusnosti | Zatvoreno | PDF16–17 izričito razlikuju ilustraciju i egzaktno jamstvo |
| 57/100 iz ranije Python implementacije | Zatvoreno | Aktualno 54/100 u MATLAB-u, neovisno potvrđeno |
| Nedostajući gradijent g2 | Zatvoreno | Sl.2.1 sadrži sva tri gradijenta |
| Nepotkrijepljena stopa α=0.85 | Zatvoreno za aktualnu brojku | α=0.288374 odgovara stvarnom certifikatu |
| Nedosljedna skala cilja ceste | Poboljšano | Δx i m² eksplicitni; preostaje F02 o tumačenju mreže |
| Podjela iskopa/nasipa kao jedinstvena | Uklonjeni sporni stupci | Tablica prikazuje ukupan cilj; nejedinstvenost ne ruši LP rezultat |
| Opširnost i suvišni prikazi | Znatno smanjeno | Sedam opravdanih slika; još postoji ponavljanje i nepovoljan prijelom zaključka |
| Opći zapis intervala negativnih koeficijenata | Nije potpuno zatvoreno | Početna (3.1) i dalje obrnuta; F03 |

## 11. Konkretan akcijski plan

| Redoslijed | Mjesto / nalaz | Akcija | Kriterij prihvaćanja |
|---|---|---|---|
| 1 | §5.4, F01 | Ukloniti tvrdnju najmanjeg pojačanja K; pravilno opisati odabir min ‖Y‖ | Nema tvrdnje koju pobija navedeni kontraprimjer; regulator i certifikat ostaju isti |
| 2 | §4.5 i zaključak, F02 | Zamijeniti tvrdnju o kvadraturi opisom opažene promjene bez nedokazanog reda | Poglavlje i zaključak dosljedni; zadržane točne brojke |
| 3 | §5.2, S01/F04 | Ispraviti predznak/naziv umnoška | Iz teksta i polinoma jasno razlikovati −αβ i +αβ |
| 4 | (3.1), F03 | Uvesti interval s apsolutnom vrijednošću ili skalirajućim faktorom | Opća formula daje točne granice i za −1 |
| 5 | §2.7 i §5.3, F05–F06 | Ograničiti osjetljivost na lokalni režim i rast norme na zadani početni uvjet | Nema preširokih općih tvrdnji |
| 6 | Sl.3.1, F07 | Označiti dopustive strane i robusni presjek | Skupovi razumljivi bez pogađanja strane granice |
| 7 | Literatura, F08 | Osigurati provjerene lokalne izvore ili stvarno odgovarajuće citate na nastavu | Svaki citat sljediv; bez izmišljenih RAG ključeva |
| 8 | Uvod/paket, F09–F10 | Pojasniti elektronički prilog, sinkronizirati finalni PDF i metapodatke | Jedna nedvosmislena predajna verzija s točnim brojem stranica |
| 9 | Prijelom, F11 | Ukloniti izdvojenu riječ i kratki nastavak zaključka; po potrebi sažeti duplicirani ispis | Pregledan novi PDF; provjeren projektni prag 30 stranica |
| 10 | Završna provjera | Provjeriti da izmjene teksta nisu promijenile rezultate i reference slika/tablica | Rješenja i brojke iste; svi zahtjevi iz §6 pokriveni |

**Gdje dodati vlastiti izvod?** Rad već ima dovoljne distinktivne izvode: Slaterova točka, dodatni kandidat robusnog QP-a, donje međe nivelete i monodromija. Njih treba zadržati i moći objasniti. Ako se želi dodatno učvrstiti jedan korak, najkorisniji je kratak lokalni izvod osjetljivosti iz aktivnog ograničenja ili eksplicitan izraz za stopu α iz P i Ljapunovljevih matrica. To je neobvezno; nema potrebe uvoditi novu metodu ili novi regulator radi umjetne različitosti.

**Status predaje:** preporučuje se ciljana revizija prije predaje. Ne treba ponovno rješavati cijeli seminar. Treba ispraviti identificirane tvrdnje, dovršiti označavanje robusnog skupa i urediti sljedivost izvora/paketa.

## 12. RAG i tehnički trag provjere

Izvorna RAG konfiguracija nije odmah radila: zadani Python nije imao `dotenv`, postojeća baza nije prihvatila polje `domain`, a zadani backend/model vraćao je nepovezane rezultate ili dimenzijski nesklad. Izvornici i postojeća baza nisu destruktivno popravljani. Provjera je dovršena u izoliranoj privremenoj bazi s odgovarajućim runtimeom i eksplicitnim modelom.

Baza: **293 odsječka iz šest PDF-ova** — Matija 30, Ivan 95, Vježbe 3 43, Vježbe 4 41, predavanje 7 63, predavanje 8 21. Vlastiti seminar i službeni zadatak nisu u toj bazi; njihove provjere temelje se na izravnim PDF-ovima i računu.

Ponovljiva naredba u ovoj lokalnoj okolini:

```powershell
$env:RAG_DB_DIR='C:/Users/KHartl/AppData/Local/Temp/omrius_review_rag'
$env:OLLAMA_EMBED_MODEL='qwen3-embedding:8b'
& C:/Users/KHartl/.agentbrain/.venv/Scripts/python.exe C:/Users/KHartl/.agentbrain/scripts/rag/query.py '2.480 dualni jaz 2.793 robusno' --scope local --backend lancedb -k 4
```

Privremena baza je regenerabilan radni artefakt, nije trajni dio predaje. Naziv PDF-a, stranica i gore navedeni hash služe kao trajniji identifikator izvora.

| Upit | Provjeren oslonac | Granica zaključka |
|---|---|---|
| `2.480 dualni jaz 2.793 robusno` | M PDF12 i PDF16: dualni i robusni ispis | Potvrđuje lokaciju podudarnih brojeva; autorstvo se iz toga ne izvodi |
| `umnožak izvandijagonalnih elemenata pi stabilnost` | I PDF19 i PDF33 | Potvrđuje pozitivan izraz i sporno nazivlje; kontekst provjeren u PDF-u |
| `Vježbe Karush Kuhn Tucker provjeriti kombinacije aktivna ograničenja` | Vježbe 3, PDF24–26 | Nastava eksplicitno enumerira aktivne skupove; isti obrazac u seminarima nije neobičan |
| `l1 aproksimacija apsolutna vrijednost linearno programiranje` | Vježbe 4, PDF5 | Nastavni LP postupak s apsolutnim rezidualima |
| `Ljapunov kvadratna stabilnost Q P inverz Y KP` | Predavanje 7, PDF25 | Zajednička kvadratna Ljapunovljeva funkcija za skup matrica |
| `stabilizacija povratnom vezom Y Q matricne nejednakosti` | Predavanje 7, PDF28–33 | Kongruencija, Q/Y formulacija, P=Q⁻¹ i K=YP |
| `robusno optimiranje poliedarski skup vrhovi nejednakosti` | Predavanje 8, PDF2–3 | Robusna ograničenja nad poliedrom i dualna LP formulacija; ti odsječci sami ne pokazuju eksplicitnu tablicu svih vrhova |

RAG izlaz ne daje `\cite` ključeve za ove dokumente zbog nedostajućih mapiranja datoteka u bibliografiji. Zato ova recenzija koristi oznake dokumenata i stvarne stranice; nije izmišljen nijedan novi bibliografski ključ. Potvrda standardne nastavne metode nije tvrdnja da je baš ta stranica dokaz svih pojedinačnih izvoda u seminaru.

### Kontrolni MATLAB izraz za F01

Ovo je neovisna provjera kontraprimjera, bez mijenjanja regulatora u seminaru:

```matlab
A1 = [-1, -pi/6; 3*pi/2, -1];
A2 = [-1, -3*pi/2; pi/6, -1];
B = [1; 0];
Qa = [1.7, -0.7; -0.7, 1.9];
Ka = [-3, 0];
Ya = Ka*Qa;
M1 = A1*Qa + Qa*A1' + B*Ya + Ya'*B';
M2 = A2*Qa + Qa*A2' + B*Ya + Ya'*B';
[min(eig(Qa-eye(2))), max(eig(M1+eye(2))), max(eig(M2+eye(2)))]
[norm(Ka,2), norm([-3.424629,-0.104650],2)]
```

Recenzija mijenja samo recenzentski dokument i evidenciju provjere. LaTeX sadržaj seminara, MATLAB izvori, izvorni PDF-ovi i grafovi nisu uređivani u okviru ove analize.
