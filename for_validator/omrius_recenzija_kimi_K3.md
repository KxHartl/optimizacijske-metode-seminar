# Recenzija i validacija seminarskog rada — OMRiUS

**Rad:** *Optimizacijske metode u razvoju i upravljanju sustava* — seminarski rad (38 str.)
**Autor:** Krešimir Hartl
**Recenzent:** Neovisni tehnički validator (uloga: strogi akademsko-tehnički recenzent)
**Datum recenzije:** 17. 8. 2026.
**Obuhvat provjere:** tekst rada (PDF), tekst zadatka (PDF), MATLAB kod (5 datoteka), Python kod (6 datoteka). Sve ključne brojke iz rada **neovisno su preračunate** (QP/KKT/dual/osjetljivost, robusni QP + Monte Carlo, LP nivelacija ceste, matrice prijelaza stanja i monodromijska matrica, dopustivost zajedničke funkcije Ljapunova).

---

## 1. SAŽETAK OCJENE (SCORECARD)

| Kategorija | Ocjena | Status |
|---|---|---|
| Usklađenost sa zadatkom | ~93% | Zadovoljava (uz manje dopune) |
| Matematička i inženjerska točnost | ~85% | Djelomično (jedna numerička greška u Zadatku 4) |
| Vizualizacije i podaci (grafovi/tablice) | ~85% | Zadovoljava (uz upute za doradu) |
| Jezik, pravopis i akademski stil | ~65% | Nezadovoljava — potrebna temeljita jezička redakcija |

**KONAČNI STATUS: POTREBNE MANJE KOREKCIJE** — uz jednu obaveznu ispravku blokirajuće prirode (jednadžbe (5.10)–(5.11)) i obaveznu jezičku redakciju. Zadaci su u biti točno riješeni; problem je u prezentaciji pojedinih međurezultata i u stilu.

### Opći dojam

Rad je sadržajno jači od prosječnog seminarskog: sva četiri zadatka su obrađena, proračuni su (uz jednu iznimku) točni i numerički potvrđeni u dva programska okruženja. Tri glavna problema koja ruše dojam:

1. **Jednadžbe (5.10) i (5.11) sadrže pogrešne numeričke vrijednosti** koje su u internoj kontradikciji s (5.12) — vidi Kritični nedostatak br. 1.
2. **Tekst na mjestima zvuči generički i "AI-ovski"**: samohvala ("rigorozno obrađene cjeline", "moćan matematički aparat", "najintrigantniji fenomen", "savršena kolinearnost"), generički uvodni odlomci na počecima poglavlja 3, 4 i 5, te pretjerano opširan Uvod koji ne odgovara na ništa iz zadatka.
3. **Terminološke i pravopisne greške** koje profesor odmah uočava: "dupleksni simpleks" (treba *dualni simpleks*), "stanjski regulator" (kalk), miješanje "prespajanje"/"sklopni sustav", numeracija jednadžbi koja preskače (2.48)–(2.50).

---

## 2. KRITIČNI NEDOSTACI I BLOKIRAJUĆE GREŠKE

### 2.1. [Poglavlje 5.2, jednadžbe (5.10)–(5.12)] — Pogrešne numeričke vrijednosti matrica prijelaza; interna kontradikcija

- **Uočeni problem:** U (5.10) stoji
  Φ_parno ≈ [[0, −0.2122], [1.9099, 0]], Φ_neparno ≈ [[0, −1.9099], [0.2122, 0]],
  a u (5.11) Φ_cycle ≈ diag(−3.6476, −0.0450). Zatim (5.12) tvrdi da su svojstvene vrijednosti te matrice −1.2180 i −0.0150.
- **Zašto je pogrešno:** Svojstvene vrijednosti dijagonalne matrice diag(−3.6476, −0.0450) jesu −3.6476 i −0.0450 — **a ne** −1.2180 i −0.0150. Dakle (5.12) ne slijedi iz (5.11). Nadalje, determinanta mora zadovoljavati det Φ_cycle = e^(tr(A_p)+tr(A_n)) = e^(−4) = 0.01832, a za ispisane matrice iznosi (−3.6476)(−0.0450) = 0.1641 — dodatna nekonzistentnost. Neovisnim proračunom (`scipy.linalg.expm`) dobivam točne vrijednosti:
  Φ_parno = e^(−1)·[[0, −1/3], [3, 0]] ≈ [[0, −0.1226], [1.1036, 0]],
  Φ_neparno = e^(−1)·[[0, −3], [1/3, 0]] ≈ [[0, −1.1036], [0.1226, 0]],
  Φ_cycle = e^(−2)·diag(−9, −1/9) ≈ diag(−1.2180, −0.0150).
  Dakle **(5.12) i (5.13) su točni** (ρ = 1.2180 > 1, zaključak o nestabilnosti valjan), ali (5.10) i (5.11) nisu — ispisan je umanjeni faktor e^(−1) po modu (ispisane vrijednosti 0.2122 = (2/π)·(1/3) i 1.9099 = (2/π)·3 odgovaraju rotacijskom dijelu bez prigušenja). MATLAB kod (`expm`) računa ispravno — greška je u prepisivanju/ručnom izvođenju za tekst.
- **Konkretan ispravak:** Zamijeniti brojke u (5.10) i (5.11) gornjim točnim vrijednostima (ili zatvorenim oblikom s faktorima e^(−1), e^(−2)). Provjeriti da det Φ_cycle = e^(−4) ≈ 0.01832. Poruka ρ = 1.2180 > 1 ostaje ista.

### 2.2. [Poglavlje 5.5 / kod task4] — Nedosljednost između prezentiranog LMI-ja i onoga što kod zapravo rješava

- **Uočeni problem:** Tekst (5.23) postavlja čisti problem dopustivosti (feasibility) po (Q, Y). Python kod (`task4_lmi_switched_stabilization-11.py`) rješava **drugačiji, regularizirani problem**: dodaje Q ⪰ I, rub decaja −αI s α = 0.1 i funkciju cilja min ‖Y‖_F, uz komentar da se time "podudara s YALMIP/SDPT3 rješenjem K ≈ [−3.7097, 0]". MATLAB kod pak, ako YALMIP ne uspije, koristi hardkodirano K = [−3.7097, 0].
- **Zašto je pogrešno:** Problem dopustivosti nema jedinstveno rješenje; tvrdnja da se dva različita solvera (jedan feasibility, drugi s min ‖Y‖) podudaraju na istom K je najmanje sumnjiva, a u tekstu se regularizacija nigdje ne spominje. Hardkodirani fallback potkopava tvrdnju o reproduktibilnoj sintezi.
- **Konkretan ispravak:** U 5.5 eksplicitno navesti: (a) točnu postavku koju solver rješava (ako je regularizirana, zapisati je jednadžbom i obrazložiti), (b) dobivene matrice **K i P eksplicitno s brojkama** i tolerancijama solvera, (c) verifikaciju: λ_max((A_i+BK)ᵀP + P(A_i+BK)) < 0 za oba moda. Neovisna provjera: za K = [−3.7097, 0] je **P = I dopustiva CQLF** — (A_i+BK)ᵀ + (A_i+BK) ima λ_max = −0.1144 < 0 za oba moda, pa sinteza valja; to samo treba transparentno pokazati. Ukloniti hardkodirani fallback iz MATLAB koda ili ga jasno označiti kao demonstracijski.

### 2.3. [Poglavlje 5.6 / Slika 5.3] — "Teorijska eksponencijalna ovojnica" nije izvedena iz dokaza

- **Uočeni problem:** Slika 5.3 prikazuje ovojnicu V₀e^(−αt) s α = 0.85. U Python kodu je `alpha_decay = 0.85` ručno odabran.
- **Zašto je pogrešno:** Ovojnica se naziva "teorijskom", ali konstanta nije izvedena iz LMI-ja. Iz V̇ ≤ λ_max(P^(−1/2)M_iP^(−1/2))‖x‖² slijedi ocjena V(t) ≤ V(0)e^(−2αt) s α = −½ max_i λ_max(P^(−1/2)M_iP^(−1/2)) (odnosno, za P = I i K = [−3.7097, 0]: α = 0.0572, jer V̇ ≤ −0.1144·V). Pripremljena vrijednost 0.85 ne odgovara niti jednoj izvedenoj ocjeni.
- **Konkretan ispravak:** Izračunati α iz dobivenog (P, K) po gornjoj formuli i tu vrijednost koristiti na slici, ili sliku opisati kao "referentna eksponencijalna krivulja" bez pridjeva "teorijska". Uz to, u 5.5.1 paziti na konceptualnu razinu: **Hurwitzovost zatvorenih modova ne dokazuje stabilnost sklopnog sustava** (što je upravo poanta zadatka); dokaz je CQLF. Rečenicu o svojstvenim vrijednostima zatvorenog kruga eksplicitno uokviriti kao ilustraciju, ne kao verifikaciju.

### 2.4. [Zadatak 1c / Slika 2.1] — Nedostaje gradijent drugog ograničenja

- Zadatak (c) traži "gradijente ograničenja i funkcije cilja u točki KKT". Na slici i u tekstu su samo ∇f i ∇g₁. Dodati ∇g₂(x*) = [1, −1]ᵀ na sliku (i u tekstu napomenuti da je ograničenje neaktivno, μ₂* = 0, pa ne sudjeluje u ravnoteži). Manji, ali formalni nedostatak pokrivenosti zadatka.

### 2.5. [Poglavlje 3.3] — Analitički izvod robusnog optimuma bez KKT provjere

- Pretpostavlja se (i točno je) da su u robusnom optimumu aktivna oba najgora ograničenja, ali se to ne dokazuje. Uz pretpostavku x ≥ 0 (koju treba eksplicitno zapisati i naknadno potvrditi) izbor vrhova je točan; međutim optimalnost točke (6.5, 179/34) treba potvrditi KKT uvjetima za 8-ograničeni problem. Neovisni proračun: gradijent u toj točki je [13.4206, 16.1088]ᵀ, a množitelji uz aktivne vrhove (−0.85,−0.85) i (1.15,−0.85) su μ = (17.6074, 1.3441) > 0 — **KKT vrijedi**. Dovoljno je dodati te dvije-tri rečenice.

### 2.6. [Poglavlje 3.4, jednadžba (3.27)] — Pogrešan zapis uniformne distribucije za negativne nominalne vrijednosti

- Zapis a_ij^(k) ~ U(0.85·a_ij⁰, 1.15·a_ij⁰) za a_ij⁰ = −1 daje U(−0.85, −1.15), tj. donja granica veća od gornje. Ispravak: a_ij^(k) ~ U(min, max) odnosno eksplicitno U(−1.15, −0.85), ili zapis preko skalara s ~ U(0.85, 1.15) pa a_ij^(k) = s·a_ij⁰ (ovako je i implementirano u kodu).

---

## 3. ANALIZA GRAFOVA, SLIKA I TABLICA

- **Slika 2.1 (geometrija QP + gradijenti):** Opravdano. Osi imenovane (x₁, x₂; bezdimenzionalno — prihvatljivo), legenda postoji. Nedostatak: nema ∇g₂ (vidi 2.4). Dorada: dodati ∇g₂(x*) i tekstualno označiti aktivno/neaktivno ograničenje.
- **Slika 2.2 (dualna funkcija):** Opravdano, uredno; osi μ₁, μ₂ označene. OK.
- **Slika 2.3 (osjetljivost p*(b₁+Δb₁) + tangenta):** Opravdano i korisno; dobro veže teorem osjetljivosti na numeriku. OK.
- **Tablica 2.1:** Točna; neovisnom provjerom sve brojke potvrđene (x* = (5.757576, 4.242424), μ* = (12.242424, 0), p* = d* = 60.606061, gap ~ 10⁻¹⁴). Napomena: tekst tvrdi verifikaciju "MATLAB (quadprog, YALMIP) i Python (scipy.optimize, cvxpy)", ali isporučeni kod za Zadatak 1 koristi samo quadprog/scipy — uskladiti tvrdnju ili isporučiti YALMIP/cvxpy varijantu.
- **Slika 3.1 (robusni skup + Monte Carlo ovojnica):** Opravdano i dobro koncipirano. Nedostaci: (a) u legendi je MC prikazano samo za g₁ — nesigurnost pogađa i g₂, treba crtati realizacije obaju ili obrazložiti zašto samo g₁; (b) naslov i legenda uredni. Dorada obavezna samo za (a).
- **Tablica 3.1 (MC dopustivost):** Sadržajno točno (nominalni optimum krši ograničenje u ~50% realizacija jer leži na granici; moja MC provjera s 10⁵ uzoraka daje 49.9%). Napomene: (a) broj 57/100 ovisi o sjemenu generatora — navesti seed (`rng(42)`) u tekstu ili povećati N i navesti ocjenu ~50%; (b) oznaka "(N = 100)" u naslovu tablice u koliziji je s N iz Zadatka 3 — u 3.4 koristite N_MC, uskladiti; (c) stupac "100% Dopustivo (Zajamčeno)" — riječ "pouzdanost"/"%" implicira vjerojatnosni jamac, a ovdje je jamstvo determinističko (vršna analiza); preformulirati u "dopustivo za sve realizacije iz U (vršno zajamčeno)".
- **Slika 3.2 (cijena robusnosti):** Djelomice redundantna prema Slici 3.1 (ista geometrija, iste točke). Preporuka: spojiti u jednu sliku s anotacijom Δf*, ili na 3.2 jasno dodati nivo-krivulje f s vrijednostima 60.61 i 84.62 koje 3.1 nema — tada svaka slika ima zasebnu svrhu.
- **Slike 4.1 i 4.2 (profili ceste):** Opravdano, s jedinicama [m], s iskopom/nasipom. Brojke u legendama (J* = 1.92/1.97/2.45/2.51) podudaraju se s Tablicom 4.1. OK. Manja napomena: J* ima dimenziju površine (m²), a u tekstu se naziva "volumen" — dodati "po jediničnoj širini trase".
- **Tablica 4.1:** Sve brojke neovisno reproducirane točno na 6 decimala (J* = 1.916180 / 1.965940 / 2.453727 / 2.506047; iskop/nasip; max|y″| = 0.5/0.2). Dimenzije LP-a (42 varijable/120 nejednakosti; 202/600) točne. OK.
- **Slike 4.3 i 4.4 (provjera nagiba i zakrivljenosti):** Opravdano; osi s jedinicama; granice b₁, b₂ ucrtane. Komentar u tekstu uz Sliku 4.4 postoji i korektan je (aktivnost ograničenja u Slučaju B). Preporuka: uz Sliku 4.3 dodati jednu rečenicu — nagib u oba slučaja dotiče ±b₁ samo na kratkim segmentima, dok je u Slučaju B dominantno aktivno ograničenje zakrivljenosti.
- **Slika 5.1 (otvoreni krug):** Opravdano; dobro ilustrira eskalirajuću spiralu. Provjeriti da raspon osi u faznom portretu pokazuje dovoljno ciklusa (t ∈ [0, 20] s divergencijom — čitljivost).
- **Slika 5.2 (zatvoreni krug + nivo-elipse):** Opravdano; elipse V(x) = xᵀPx = c moraju odgovarati **stvarno dobivenom P** iz SDP-a (u kodu je tako) — u tekstu navesti P.
- **Slika 5.3 (disipacija V):** Vidi kritični nedostatak 2.3 (α = 0.85 nije izveden). Prije uključivanja u rad obavezno popraviti.
- **Opća primjedba o izvoru figura:** U tekstu negdje piše da su figure iz MATLAB-a, a kod ih generira iz oba okruženja s istim imenima; navesti u uvodu poglavlja rezultata ili u proširenom podnaslovu da su svi numerički rezultati neovisno reproducirani u MATLAB-u i Pythonu (to je jaka strana rada — istaknuti je činjenično, jednom).

---

## 4. JEZIČNE, STILSKE I "HUMAN-WRITTEN" KOREKCIJE

| Lokacija / Izvorni tekst | Vrsta problema | Predloženi ispravak |
|---|---|---|
| §4.4: "algoritma **dupleksnog simpleksa**" | Pogrešan termin (tipfeler) | "algoritma **dualnog simpleksa**" |
| §1.2: "četiri samostalne, **matematički i numerički rigorozno obrađene** inženjerske cjeline" | Samohvala / AI stil | "četiri cjeline koje odgovaraju zadacima 1–4" |
| Uvod: "iznimno efikasnih, polinomijalno složenih algoritama unutrašnje točke" | Suvišni pridjev + gramatika (padež) | "algoritama **unutarnjih točaka polinomijalne složenosti**" |
| Uvod: "doživio je **ključnu** promjenu paradigme" | Suvišni pridjev | "promjenu paradigme" |
| §1.1 (cijeli podnaslov "Taksonomija…") | Opširnost bez veze sa zadatkom; zvuči kao predložak | Skratiti na 3–4 rečenice koje samo najavljuju metode koje se koriste (LP, QP, robusni QP, LMI) |
| §5.2: "**Jedan od najintrigantnijih fenomena** u teoriji hibridnih sustava jest…" | AI floskula | "Poznato je da preklapanje između dva stabilna LTI podsustava može dati nestabilan sustav [6]." |
| §1.1: "LMI **pruža moćan matematički aparat**" | Samohvala / floskula | "LMI formalizam omogućuje sintezu regulatora i dokaz stabilnosti…" |
| §2.4: "Uočava se **savršena** kolinearnost" | Suvišni pridjev | "Gradijenti su kolinearni i suprotnog smjera:" |
| §3.4: "krši ograničenja u **čak** 57%" | Suvišna partikula | "…u 57% realizacija (uzorak od 100; teorijski ~50%)" |
| §3.4: "posjeduje **100% pouzdanost**" | Pogrešan registar (vjerojatnosni) | "dopustivo je za sve realizacije iz skupa nesigurnosti (vršno zajamčeno)" |
| §3.5: "**inženjersku premiju osiguranja koja jamči apsolutnu operativnu sigurnost**" | Marketinški ton / floskula | "povećanje funkcije cilja koje se plaća za zajamčenu dopustivost pod svim realizacijama nesigurnosti" |
| §3.5: "**neumitno** povlači" | Stil | "neminovno povlači" ili samo "povlači" |
| §5.2 (naslov poglavlja u sadržaju) i svugdje: "**prespajanje**" | Terminološka nedosljednost (u tekstu i "sklopni sustav") | Ujednačiti: "sklopni sustav" + "**preklapanje**" (ili "sklapanje") — jedan termin kroz cijeli rad |
| §1.2: "sinteze robusnog **stanjskog regulatora**" | Kalk (engl. state feedback) | "regulatora po varijablama stanja" (kao u §5.3, gdje je ispravno) |
| §1.2: "**Dokazuje se otvoreni** mehanizam destabilizacije" | Pogrešan izbor riječi | "Prikazuje se mehanizam destabilizacije preko monodromijske matrice" |
| §2.7 → jednadžbe (2.51)–(2.54) nakon (2.47) | Rupa u numeraciji (2.48–2.50 ne postoje) | Renumerirati |
| §2.2/§2.3/§5.x: miješanje "definiramo / provodimo / računamo / imamo" s bezličnim stilom | Nedosljedan akademski stil | Ujednačiti u bezlični: "definirana je", "rješava se", "za dva ograničenja postoje 4 kombinacije" |
| §3.1, §4.1, §5.1: uvodni odlomci općenite motivacije (2–3 odlomka prije konkretnog problema) | Generički "AI" uvodnik; zadatak to ne traži | Skratiti na jednu rečenicu koja veže metodu na zadatak; ostatak izbaciti |
| §3.2 (naslov): "Egzaktna **derivacija** determinističkog robusnog ekvivalenta" | Kalk (engl. derivation) | "Egzaktni **izvod** determinističkog robusnog ekvivalenta" |
| §5.2: "Slika 5.1 **zorno** prikazuje" | Stil | "Slika 5.1 prikazuje" |
| §4.5: "numeričkog '**peglanja**' na gruboj skali" | Kolokvijalno i netočno obrazloženje | Vidi napomenu 5.2 dolje — objasniti da pravokutna integracija na rijetkoj mreži podcjenjuje integral |
| Naslovna stranica | Nedostaje matični broj (u zadatku je predviđen) | Dodati JMBAG |

---

## 5. DODATNE TEHNIČKE NAPOMENE (ne blokiraju, ali dižu kvalitetu)

**5.1. Zadatak 1 — potpuna potvrda.** Sve brojke su neovisno reproducirane i točne: svojstvene vrijednosti Q (1.955969, 4.044031), nesputani minimum (−0.897598, 0.682680) s g₁ = 10.214918 > 0, optimum x* = (190/33, 140/33), μ* = (404/33, 0), p* = 2000/33 = 60.606061; Slučajevi 3 i 4 ispravno odbačeni (μ₂ = −6.7093 odnosno μ₂ = −2.45); dualna funkcija i d* = p*; Slaterova točka [7, 6]ᵀ valjana; numerička derivacija ∂p*/∂b₁ = −12.24236 uz analitičku −12.24242 (odstupanje 6.7·10⁻⁵, kako je i navedeno). Jednadžba (2.52) i konvencija predznaka (Ax ≤ b + u ⟹ ∂p*/∂bᵢ = −μᵢ*) konzistentni su kroz cijeli tekst. Interpretacija relaksacije b₁ je ispravna.

**5.2. Zadatak 3 — objašnjenje ponašanja J*(N) nije točno.** Tvrdnja da J_disc "asimptotski konvergira prema točnom integralu" i da fina mreža "uklanja peglanje" ne objašnjava zašto J* **raste** s N (1.9162 → 1.9659). Razlog: kriterij je pravokutna (rectangle-rule) aproksimacija integrala po čvorovima; na rijetkoj mreži su funkcije |yᵢ − hᵢ| uzorkovane rijetko i dio površine "promiče" između čvorova, pa je J_disc podcijenjen. Preformulirati odlomak u tom smjeru i (po želji) dodati jednu rečenicu o redu konvergencije O(Δx).

**5.3. Zadatak 4 — redoslijed modova u simulaciji.** Kod pretpostavlja parni mod na [0,1), neprani na [1,2) itd., što odgovara pravilu ⌊t⌋ — konzistentno s (5.2). Monodromija Φ_cycle = Φ_nep·Φ_parn odgovara tom redoslijedu. OK. (Vrijedi napomenuti da za periodičku analizu redoslijed unutar perioda ne mijenja svojstvene vrijednosti produkta do na konjugaciju, ali to nije nužno za rad.)

**5.4. Ponovljivost.** `run_all` skripte postoje za oba jezika — dobro. Preporuka: u rad dodati kratku "Napomenu o reproduktibilnosti" (verzije paketa, seedevi, datoteke), ili barem seed uz svaku Monte Carlo brojku.

**5.5. Zaključak (pogl. 6) i Popis literature.** U ekstrakciji teksta te stranice nisu bile čitljive do kraja; prije predaje provjeriti da: (a) zaključak odgovara točno na pitanja a)–f) iz Zadatka 1, na zahtjev Zadatka 2 (robusno rješenje + slika), na formulaciju i 4 slučaja Zadatka 3, te na a)–c) iz Zadatka 4; (b) reference [1]–[7] stvarno postoje i citirane su na mjestima gdje se koriste (npr. [7] uz teorem osjetljivosti); (c) da se u zaključku ne pojavljuju nove floskule ("ovaj rad je pokazao snažan okvir…").

**5.6. Cjelokupni luk rada.** Luk zadatak→metoda→rješenje→verifikacija je prisutan i logičan u sva četiri poglavlja; jedino mjesto gdje naraтив "curi" je 5.5–5.6 (vidi 2.2 i 2.3) jer se rezultat sinteze ne prezentira s istom eksplicitnošću (brojke za K, P, λ_max) kao u poglavljima 2–4.

---

## 6. KORAK-PO-KORAK AKCIJSKI PLAN ZA POPRAVAK

1. **[Prioritet 1 — matematika]** Ispraviti brojke u (5.10) i (5.11) prema točnim vrijednostima iz `expm` (Φ_parno ≈ [[0, −0.1226], [1.1036, 0]], Φ_neparno ≈ [[0, −1.1036], [0.1226, 0]], Φ_cycle ≈ diag(−1.2180, −0.0150)); provjeriti det = e^(−4). Time (5.12)–(5.13) postaju konzistentni.
2. **[Prioritet 1 — sinteza]** U 5.5 eksplicitno ispisati dobivene K i P, postavku koju solver rješava (uključujući eventualnu regularizaciju), te verifikaciju λ_max((A_i+BK)ᵀP + P(A_i+BK)) < 0 za oba moda; izračunati α za Sliku 5.3 iz (P, K) i zamijeniti ručno odabrano 0.85; ukloniti hardkodirani K iz MATLAB koda.
3. **[Prioritet 2 — pokrivenost zadatka]** Dodati ∇g₂ na Sliku 2.1 (uz napomenu o neaktivnosti); u 3.3 dodati KKT provjeru robusnog optimuma (μ = (17.61, 1.34) > 0) i eksplicitnu pretpostavku x ≥ 0; ispraviti zapis distribucije u (3.27).
4. **[Prioritet 2 — jezik]** Provesti redakciju prema tablici u točki 4: prije svega "dupleksni simpleks" → "dualni simpleks", "stanjski regulator", ujednačiti "preklapanje/sklopni", skratiti generičke uvode u poglavljima 3–5 i podnaslov 1.1, ukloniti samohvalne pridjeve, renumerirati jednadžbe (2.48–2.50), ujednačiti bezlični stil.
5. **[Prioritet 3 — dorada figura i podataka]** Slika 3.1: dodati MC realizacije i za g₂; razmotriti spajanje Slika 3.1/3.2; Tablica 3.1: navesti seed i zamijeniti "pouzdanost" determinističkom formulacijom; uz J* svugdje naznačiti m² (po jediničnoj širini); popraviti objašnjenje rasta J*(N) u 4.5; dodati matični broj na naslovnicu.
6. **[Prioritet 3 — završna provjera]** Provjeriti poglavlje 6 i Literaturu prema točki 5.5; proći cijeli PDF još jednom uz pravilo "svaka rečenica mora nositi informaciju koja postoji u zadatku ili u rezultatu — ako ne nosi, briše se".

---

*Kraj recenzije. Sve numeričke tvrdnje navedene kao "neovisno preračunato" reproducirane su u Pythonu (numpy/scipy) izravno iz podataka zadatka, ne iz autorovih kodova.*
