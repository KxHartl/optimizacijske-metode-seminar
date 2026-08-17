# RECENZIJA I VALIDACIJA SEMINARSKOG RADA
**Rad:** Optimizacijske metode u razvoju i upravljanju sustava — Krešimir Hartl
**Mentor:** prof. dr. sc. Andrej Jokić
**Recenzent:** nezavisna AI validacija (protokol 5 faza)

---

## 1. SAŽETAK OCJENE (SCORECARD)

| Kriterij | Ocjena | Status |
|---|---|---|
| Usklađenost sa zadatkom | 92% | Zadovoljava |
| Matematička i inženjerska točnost | 75% | Djelomično |
| Vizualizacije i podaci | 85% | Zadovoljava (uvjetno — vidi napomenu) |
| Jezik, pravopis i akademski stil | 65% | Djelomično |
| **KONAČNI STATUS** | | **POTREBNE ZNAČAJNE KOREKCIJE PRIJE PREDAJE** |

Rad je matematički vrlo ambiciozan i strukturno solidan — svi zadaci su obrađeni, izvodi su uglavnom točni i dobro dokumentirani, a numerika je u tri od četiri zadatka provjerena i konzistentna. Međutim, u poglavlju 5 (Zadatak 4) pronađena je **konkretna, dokazana numerička pogreška** u prijelaznim matricama moda (jednadžba 5.10), koja mora biti ispravljena jer narušava vjerodostojnost cijelog dokaza destabilizacije. Jezik je tehnički korektan, ali mjestimično opterećen suvišnim superlativima i formulacijama karakterističnima za automatski generiran tekst, što treba ukloniti da bi rad zvučao autentično inženjerski.

---

## 2. KRITIČNI NEDOSTACI I BLOKIRAJUĆE GREŠKE

### 2.1. Blokirajuća greška — pogrešne prijelazne matrice moda (jedn. 5.10, str. 26)

**Lokacija:** Poglavlje 5.2, jednadžba (5.10)

**Uočeni problem:** U tekstu je navedeno:
$$\Phi_{\text{parno}} \approx \begin{bmatrix} 0.0000 & -0.2122 \\ 1.9099 & 0.0000 \end{bmatrix}, \quad \Phi_{\text{neparno}} \approx \begin{bmatrix} 0.0000 & -1.9099 \\ 0.2122 & 0.0000 \end{bmatrix}$$

Ove vrijednosti su numerički netočne.

**Zašto je pogrešno:** Izravnim proračunom $\Phi_{\text{parno}} = e^{A_{\text{parno}} \cdot 1}$ (verificirano i u `scipy.linalg.expm` i analitički preko Cayley–Hamiltonova teorema, budući da $A_{\text{parno}}$ ima trag $-2$ i svojstvene vrijednosti $-1 \pm j\pi/2$) dobiva se:
$$\Phi_{\text{parno}} = \begin{bmatrix} 0 & -0.12263 \\ 1.10364 & 0 \end{bmatrix}$$

Determinanta matrice u tekstu iznosi $0.2122 \times 1.9099 = 0.4053$, dok teorijski mora vrijediti $\det(\Phi_{\text{parno}}) = e^{\operatorname{tr}(A_{\text{parno}}) \cdot 1} = e^{-2} = 0.13534$. Vrijednosti iz jednadžbe (5.10) tu identičnost krše, što je matematički nemoguće za matricu prijelaza stanja LTI sustava. Dodatno, u jednadžbi (5.11) navedena je monodromijska matrica $\Phi_{\text{cycle}} \approx \operatorname{diag}(-3.6476, -0.0450)$ — ali budući da je ta matrica dijagonalna, njezine svojstvene vrijednosti su *upravo* njezini dijagonalni elementi, tj. $-3.6476$ i $-0.0450$. To je u **izravnoj kontradikciji** s jednadžbom (5.12) koja za isti $\Phi_{\text{cycle}}$ navodi svojstvene vrijednosti $-1.2180$ i $-0.0150$. Dva uzastopna izraza na istoj stranici međusobno se ne slažu.

Zanimljivo je da je vrijednost spektralnog radijusa $\rho(\Phi_{\text{cycle}}) = 1.218$ **ispravna** (potvrđeno numeričkom provjerom te se poklapa s izlazom priloženog Python/MATLAB koda), što upućuje na to da je sam zaključak izveden iz koda ispravno, ali su međukoraci (5.10)–(5.11) pri prepisivanju u tekst dobili krive brojeve.

**Konkretan ispravak:** Zamijeniti jednadžbe (5.10) i (5.11) s ispravnim vrijednostima:
$$\Phi_{\text{parno}} \approx \begin{bmatrix} 0.0000 & -0.1226 \\ 1.1036 & 0.0000 \end{bmatrix}, \quad \Phi_{\text{neparno}} \approx \begin{bmatrix} 0.0000 & -1.1036 \\ 0.1226 & 0.0000 \end{bmatrix}$$
$$\Phi_{\text{cycle}} = \Phi_{\text{neparno}}\Phi_{\text{parno}} \approx \begin{bmatrix} -1.2180 & 0.0000 \\ 0.0000 & -0.0150 \end{bmatrix}$$
Nakon ispravka, dijagonalni elementi $\Phi_{\text{cycle}}$ se poklapaju sa svojstvenim vrijednostima navedenim u (5.12), čime se uklanja unutarnja kontradikcija.

### 2.2. Neobjašnjena dvostrukost rezultata regulatora K (str. 28, jedn. 5.24)

**Lokacija:** Poglavlje 5.5, jednadžba (5.24) i tekst koji slijedi

**Uočeni problem:** Tekst navodi izračunati $K = [-2.7120,\ 0.0926]$ na temelju vlastite matrice $P$, a zatim u sljedećoj rečenici bez ikakvog objašnjenja dodaje: *"Referentno YALMIP pojačanje iznosi $K = [-3.7097, 0.0000]$, koje također u potpunosti zadovoljava LMI sustav."*

**Zašto je pogrešno:** Numerička provjera potvrđuje da oba pojačanja zaista stabiliziraju sustav (zatvoreni krug je Hurwitzov u oba slučaja), pa to nije matematička greška — ali je **metodološki nedostatak izlaganja**. LMI problem sinteze regulatora nema jedinstveno rješenje (feasibility problem), pa se dva različita rješenja mogu dobiti iz dva različita rješavača/kriterija (uvidom u priloženi Python kod, `K` se dobiva minimizacijom $\|Y\|_F$, dok MATLAB kod koristi hardkodiranu "benchmark" vrijednost $K=[-3.7097,0]$ kao *fallback* kad YALMIP nije dostupan). Ovo nigdje nije objašnjeno čitatelju, koji ostaje zbunjen zašto postoje dva "točna" rješenja.

**Konkretan ispravak:** Dodati jednu rečenicu koja objašnjava da LMI sustav (5.23) nema jedinstveno rješenje te da se prikazana dva pojačanja razlikuju jer dolaze iz različitih optimizacijskih kriterija (npr. minimalna norma $Y$ nasuprot direktnom SDPT3 rješenju), uz jasnu naznaku koje je pojačanje korišteno u simulacijama sa slika 5.2–5.3.

### 2.3. Nedostatak eksplicitne provjere svih 8 vrhova robusnog poliedra (str. 14, Zadatak 2)

**Lokacija:** Poglavlje 3.3

**Uočeni problem:** Autor bira "najgore" vrhove skupa nesigurnosti heurističkim zaključivanjem o predznaku ("budući da su koeficijenti negativni...") umjesto da eksplicitno provjeri i odbaci preostalih 6 od 8 vrhova.

**Zašto je (potencijalno) nedovoljno rigorozno:** Zaključak je matematički točan (numerički verificirano u ovoj recenziji da su izabrani vrhovi zaista aktivni u optimumu), ali s formalnog gledišta rigoroznog dokaza trebalo bi eksplicitno navesti da se ostalih 6 nejednakosti provjeravaju kao slack (neaktivne) u dobivenom optimumu, ne samo pretpostaviti.

**Konkretan ispravak:** Dodati kratku tablicu ili rečenicu koja prikazuje vrijednosti svih 8 nejednakosti (3.11)–(3.18) u točki $x^*_{\text{rob}} = (6.5, 5.265)$, s naznakom koje su aktivne (=) a koje strogo zadovoljene (<).

---

## 3. ANALIZA GRAFOVA, SLIKA I TABLICA

| Element | Opravdanost | Tehnička ispravnost | Kvaliteta interpretacije | Potrebna dorada |
|---|---|---|---|---|
| Slika 2.1 (geometrija QP, gradijenti) | Opravdano — nužna za KKT interpretaciju | Nema uvida u stvarni render; opisane osi/oznake su primjerene | Detaljno objašnjena (ravnoteža gradijenata, jedn. 2.42–2.43) | Provjeriti da su brojčane oznake gradijenata na slici ($12.24$) čitljive i da se strelice ne preklapaju s nivo-krivuljama |
| Slika 2.2 (nivo-krivulje dualne funkcije) | Opravdano | Treba potvrditi da su osi $\mu_1,\mu_2$ imenovane s jedinicama (bezdimenzijske u ovom slučaju, ali to navesti) | Kratko, ali dovoljno | Dodati naznaku smjera rasta $g(\mu)$ (gradijent prema optimalnoj točki) |
| Slika 2.3 (osjetljivost $p^*(b_1+\Delta b_1)$) | Opravdano, direktno verificira teorem | U redu prema opisu | Dobro — numerička provjera $10^{-4}$ koraka je kvantificirana | Nema — ovo je najbolje interpretiran element rada |
| Tablica 2.1 | Opravdano, sažima 6 veličina | U redu | Jasno predstavlja slaganje analitike i numerike | Nema |
| Slika 3.1 (Monte Carlo ovojnica) | Opravdano | Legenda opisana u tekstu detaljno | Vrlo dobro objašnjena, uz tablicu 3.1 koja je kvantitativno potkrepljuje | Nema |
| Slika 3.2 (cijena robusnosti) | Djelomično suvišna — velik dio informacije (pomak optimuma, $\Delta f^*$) već je dan brojčano u (3.28)–(3.29) | Ne mogu se ocijeniti osi jer je opis u izvornom PDF-u sažet na jednu rečenicu ("[Graph: Contour plot...]"), što upućuje da slika možda nije potpuno integrirana u LaTeX izvor | Interpretacija je kratka (dvije rečenice) u odnosu na ostale slike | Proširiti komentar slike ili je spojiti sa Slikom 3.1 ako prikazuje bitno preklapajuće informacije |
| Slike 4.1–4.2 (profil ceste) | Opravdano | Osi opisane (potrebno potvrditi mjerne jedinice $[m]$ na obje osi) | Dobra kvantitativna rasprava u 4.5 | Nema |
| Slike 4.3–4.4 (nagib, zakrivljenost) | Opravdano — direktna provjera ograničenja | Dobro, granice $\pm b_1, \pm b_2$ su prikazane | Dobro — zasićenje ograničenja je fizikalno protumačeno | Nema |
| Slika 5.1 (otvoreni krug, divergencija) | Opravdano | U redu | Dobra fizikalna interpretacija ("ubacuje energiju u sustav") | Nema |
| Slika 5.2 (zatvoreni krug, elipse Ljapunova) | Opravdano | U redu | Dobra | Naznačiti koje $K$ (vidi §2.2) je korišteno za ovu simulaciju |
| Slika 5.3 (disipacija energije, log-mjerilo) | Opravdano, direktan dokaz eksponencijalne stabilnosti | U redu, uspoređuje s teorijskom ovojnicom | Vrlo dobra — jedna od najjačih slika u radu | Nema |

**Opća napomena o Fazi 3:** Recenzija je provedena nad ekstrahiranim tekstom PDF-a; sami rasterizirani grafovi nisu bili dostupni za izravnu vizualnu inspekciju (npr. da se doslovno provjeri debljina linija ili preklapanje oznaka). Preporuka je da autor **sam** još jednom vizualno prođe kroz sve slike i provjeri: (a) da je font oznaka osi čitljiv u printanoj veličini, (b) da su brojevi u legendama identični onima u tekstu (što je verbalno provjereno i **jest** slučaj), (c) da slika 3.2 ima potpun opis u samom poglavlju, a ne samo naslov.

---

## 4. JEZIČNE, STILSKE I "HUMAN-WRITTEN" KOREKCIJE

| Lokacija / Izvorni tekst | Vrsta problema | Predloženi ispravak |
|---|---|---|
| *"Matematičko optimiranje i teorija sustava čine temelj suvremenog inženjerskog projektiranja..."* (Uvod) | Generički, "AI" uvodni obrazac — širok, apstraktan uvod bez konkretnog vezivanja na zadatak | *"Ovaj rad rješava četiri zadatka iz kolegija OMRiUS: kvadratno programiranje s KKT analizom, robusnu inačicu istog problema, LP formulaciju nivelacije ceste i LMI stabilizaciju sklopnog sustava."* — krenuti direktno na sadržaj, uvod skratiti na 2–3 rečenice |
| *"razvoj optimizacijskih metoda doživio je ključnu promjenu paradigme"* | Fraza-floskula, prazna generalizacija | *"Podjela optimizacijskih problema na konveksne i nekonveksne danas je važnija od klasične podjele na linearne i nelinearne."* |
| *"iznimno efikasnih, polinomijalno složenih algoritama"* | Suvišan pridjev "iznimno" bez mjerljive potpore | *"algoritama polinomijalne složenosti"* |
| *"Jedan od najintrigantnijih fenomena u teoriji hibridnih sustava jest da prespajanje..."* | Subjektivna ocjena ("najintrigantnijih") — nije inženjerski iskaz | *"Poznato je da prespajanje između dva stabilna LTI podsustava može generirati nestabilan sustav [6]."* |
| *"Slika 5.1 zorno prikazuje nestabilnost..."* | Riječ "zorno" — tipičan popunjivač, subjektivna kvalifikacija | *"Slika 5.1 prikazuje nestabilnost otvorenog kruga za $x(0)=[1,0]^T$: ..."* (izbrisati "zorno") |
| *"Uočava se savršena kolinearnost suprotnog smjera"* | "savršena" je suvišan i nepotreban superlativ — kolinearnost je matematička činjenica, ne stupnjuje se | *"Vektori $\nabla f(x^*)$ i $\nabla g_1(x^*)$ kolinearni su i suprotnog smjera, u skladu s uvjetom stacionarnosti."* |
| *"LMI pruža moćan matematički aparat za sintezu robusnih regulatora"* | "moćan" — prazan pridjev | *"LMI formulacija omogućuje sintezu robusnih regulatora i dokazivanje stabilnosti korištenjem konveksnih rješavača."* |
| *"Povećanje troška od 39.63% predstavlja inženjersku premiju osiguranja koja jamči apsolutnu operativnu sigurnost..."* | "apsolutnu" je preuveličavanje — robusnost je zajamčena samo unutar definiranog $\pm15\%$ intervala, ne apsolutno | *"Povećanje troška od 39.63% predstavlja cijenu osiguranja dopustivosti rješenja za sve realizacije parametara unutar definiranog $\pm15\%$ intervala nesigurnosti."* |
| *"U ovom seminarskom radu provedena je sveobuhvatna matematička, teorijska i numerička analiza..."* (Zaključak) | Klasična AI-floskula za otvaranje zaključka — "sveobuhvatna" bez sadržaja | *"Rad obrađuje četiri zadatka iz konveksne optimizacije i teorije upravljanja: kvadratno programiranje, robusnu optimizaciju, linearno programiranje i LMI stabilizaciju."* |
| *"Rad demonstrira snagu i fleksibilnost konveksne optimizacije u inženjerskom modeliranju..."* (Zaključak, 6.2) | Samohvala rada u trećem licu — čest AI obrazac | *"Prikazani primjeri pokazuju da se fizikalni i geometrijski zahtjevi mogu egzaktno prevesti u standardne oblike LP, QP i SDP te riješiti numerički pouzdanim rješavačima."* |
| *"Rad je strukturiran kroz četiri samostalne, matematički i numerički rigorozno obrađene inženjerske cjeline"* | Samohvala vlastite rigoroznosti prije nego je dokazana | *"Rad je podijeljen u četiri poglavlja, svako vezano na jedan zadatak."* |
| *"Slika 5.3 prikazuje vremenski tijek energije Ljapunova... Strogo monoton pad krivulje... dokazuje uniformnu eksponencijalnu stabilnost"* | Terminološki: "dokazuje" je jako — grafička provjera *ilustrira/potvrđuje*, formalni dokaz je već dan LMI-jem u 5.4 | *"...potvrđuje (ali ne zamjenjuje) analitički dokaz eksponencijalne stabilnosti dan kongruentnom transformacijom u §5.4."* |
| Opći obrazac kroz rad: *"Kao što je vidljivo..."*, *"Uočava se da..."* (ponavlja se >10 puta) | Nije greška, ali prekomjerno ponavljanje iste konstrukcije djeluje mehanički | Variranje: *"Podaci u tablici 3.1 pokazuju..."*, *"Rezultat u (3.26) potvrđuje..."*, *"Slijedi da..."* |
| *"nesputani optimum narušava primarno ograničenje"* / *"nesputanom minimumu"* | Terminološki — standardni hrvatski izraz je *"nekonstrainirani"* ili bolje *"bez ograničenja"*; "nesputan" je razumljivo ali rjeđe u tehničkoj literaturi | Prihvatljivo, ali preporučen dosljedan izraz *"minimum bez ograničenja"* kroz cijeli rad radi konzistentnosti s uvriježenom terminologijom |

**Opća zapažanja o stilu:**
- Rad koristi bezličan/pasivni akademski stil ispravno kroz većinu teksta ("Definira se...", "Provodi se...") — ovo je dobro i treba zadržati.
- Glavni problem nije gramatika (pravopis je vrlo čist, č/ć i ije/je su ispravno korišteni), nego **evaluativni pridjevi i fraze koje ne nose matematički sadržaj** ("savršena", "moćan", "zorno", "sveobuhvatna", "najintrigantnijih", "iznimno", "apsolutnu"). Ovo je najkarakterističniji trag automatski generiranog akademskog teksta i treba ih sustavno ukloniti kroz cijeli dokument, ne samo u navedenim primjerima.
- Uvod (poglavlje 1) i zaključak (poglavlje 6.2) su najopterećeniji ovim obrascem jer su generički "omotni" dijelovi — preporuka je da se oba skrate za približno 30-40% uz fokus na konkretne brojeve i rezultate, a ne opće tvrdnje o važnosti optimizacije.

---

## 5. KORAK-PO-KORAK AKCIJSKI PLAN ZA POPRAVAK

1. **Prioritet 1 (blokirajuće):** Ispraviti jednadžbe (5.10) i (5.11) u poglavlju 5.2 s točnim vrijednostima $\Phi_{\text{parno}}, \Phi_{\text{neparno}}, \Phi_{\text{cycle}}$ (vidi §2.1 ove recenzije) te provjeriti da se dijagonalni elementi $\Phi_{\text{cycle}}$ slažu sa svojstvenim vrijednostima u (5.12). Preporuka: prepisati brojeve izravno iz ispisa priloženog Python/MATLAB koda umjesto ručnog prijepisa, kako se pogreška ne bi ponovila.

2. **Prioritet 2:** Dodati jednu-dvije rečenice u §5.5 koje objašnjavaju razliku između izračunatog $K=[-2.712, 0.0926]$ i "referentnog YALMIP" $K=[-3.7097,0]$, uz jasnu naznaku koje se pojačanje koristi u simulacijama na slikama 5.2–5.3. Po mogućnosti, u §3.3 eksplicitno navesti/tablično prikazati provjeru svih 8 vrhova robusnog poliedra kako bi dokaz optimalnosti bio potpuno formalan, ne samo heuristički.

3. **Prioritet 3 (jezično poliranje):** Sustavno pretražiti cijeli dokument za riječi *"savršen(a)"*, *"moćan"*, *"zorno"*, *"sveobuhvatan"*, *"iznimno"*, *"apsolutn(a/o)"*, *"najintrigantnij(i)"* i ukloniti ih ili zamijeniti mjerljivim tvrdnjama (vidi tablicu u §4). Skratiti uvod i zaključak uklanjanjem generičkih rečenica o "važnosti optimizacije" i zamijeniti ih konkretnim sažetkom vlastitih brojčanih rezultata. Na kraju, proći Fazu 3 ove recenzije i vizualno potvrditi da svaka slika u finalnom PDF-u ima čitljive oznake osi s jedinicama i da je slika 3.2 popraćena dužim komentarom u tekstu.
