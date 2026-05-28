# Infinity Puzzles Wild — Neo4j & Hybrid App Context

> Denna fil är startkontext för att bygga den digitala hybrid-appen till det fysiska pusslet Wild.
> För bolagsöversikt, se `Company_Context/INFINITYPUZZLES_CONTEXT.md`.
> För webbapp-teknisk kontext, se `web/CLAUDE.md`.

---

## Vad vi bygger

En hybrid-upplevelse där det fysiska pusslet (19 träbitar) förlängs digitalt. Användaren loggar sin formation → appen känner igen den → karaktärerna lever, hemligheter låses upp, narrativ AI svarar i varje karaktärs röst.

**Kärnproblemet appen löser:** Folk lägger pusslet en gång och slutar. Appen ger dem en anledning att lägga tillbaka det i påsen och försöka igen.

---

## Tech Stack

- **Neo4j** — grafdatabas för bitarnas nätverkstopologi, discovery-tracking, secrets/conditions
- **Next.js 16** (App Router, TypeScript) — frontend
- **Claude API** — karaktärs-AI, narrativ röst per karaktär
- **ElevenLabs** — röstproduktion per karaktär
- **Repo:** `https://github.com/leovickman-eng/infinity-puzzles-neo4j`
- **Lokal sökväg:** `/Users/leovickman/Documents/InfinityPuzzles/neo4j/`

---

## Adjacency-nätverket (fysiska kontaktpunkter)

Varje nummer = karaktär. Nätverket är **toroidalt** — ingen kant, kan tile i oändlighet. Ingen bit kan roteras eller speglas.

```
1  Dolores       → 2, 6, 15, 19
2  Zuki          → 1, 3, 6, 7, 15, 16, 17
3  Mani          → 2, 4, 7, 17, 18
4  Ziggy-Lou     → 3, 5, 8, 9, 10, 18
5  Lana Manana   → 4, 6, 10, 18, 19
6  Tarah         → 1, 2, 5, 7, 10, 19
7  Mambo Viento  → 2, 3, 6, 8, 10, 11
8  Salvador      → 4, 7, 9, 11, 12
9  Pinto         → 4, 8, 10, 12, 13, 14, 15
10 Sixten        → 4, 5, 6, 7, 9, 11, 15, 16
11 Coco          → 7, 8, 10, 12, 16
12 Mona Moon     → 8, 9, 11, 13, 16, 17
13 Borro         → 9, 12, 14, 17, 18, 19
14 Pepe          → 9, 13, 15, 19
15 Ronda         → 1, 2, 9, 10, 14, 16, 19
16 Rumi          → 2, 10, 11, 12, 15, 17
17 Daffy Giraffy → 2, 3, 12, 13, 16, 18
18 Jerry         → 3, 4, 5, 13, 17, 19
19 Silvana       → 1, 5, 6, 13, 14, 15, 18
```

---

## Karaktärerna — Fullständig Profil

Varje karaktär har fem fält: **Djur · Grannar · Motsägelse · Talsätt · Vad de vill · Hemlighet**

---

### 1. DOLORES
**Djur:** Narval · **Grannar:** 2, 6, 15, 19
**Motsägelse:** Ser ut som någon från havet — bär kraften från landet
**Talsätt:** *"Vi rör oss nu. Inga frågor."*
**Vad hon vill:** Att unicorns ska vara trygga — utan att någon vet att det är hon som ser till det
**Hemlighet:** Narwhals är hemliga beskyddare av unicorn tribe sedan urminnes tider. Dolores är den sista i en lång rad. Ingen i tribe vet om det längre.

---

### 2. ZUKI
**Djur:** Rådjur (horn på väg) · **Grannar:** 1, 3, 6, 7, 15, 16, 17
**Motsägelse:** Känner sig för liten och barnslig för sällskapet hon befinner sig i — är precis den de alla väntar på
**Talsätt:** *"Men varför får jag vara med egentligen? Inte att jag klagar bara."*
**Vad hon vill:** Passa in — och slippa känna att hon inte gör det
**Hemlighet:** Zukis horn har inte kommit än. När det gör det förändras allt. Dolores vet. Mani vet. Daffy vet. De vaktar henne tills den dagen — utan att sätta press på henne. Hon är den de alla väntat på.

---

### 3. MANI
**Djur:** Tukan · **Grannar:** 2, 4, 7, 17, 18
**Motsägelse:** Alla ser skönheten — ingen ser kraften bakom den
**Talsätt:** *"Det här är rätt. Det vet jag."*
**Vad hon vill:** Ingenting utöver det rätta i varje ögonblick
**Hemlighet:** Mani vet att skatten är stulen från sin ursprungliga plats — tillbaka i Inka-tid. Hon vill inte äga den. Hon vill återföra den dit den hör hemma. Med Mambos förmåga att resa i tiden är det möjligt. Men hon har inte berättat det för honom än.

---

### 4. ZIGGY-LOU
**Djur:** Räv · **Grannar:** 3, 5, 8, 9, 10, 18
**Motsägelse:** Alla tror de förstår henne — ingen gör det
**Talsätt:** *"Nej nej, berätta mer. Det här är verkligen intressant."* *(Det är det inte alltid.)*
**Vad hon vill:** Att ingen ska komma för nära Lana
**Hemlighet:** Ziggy-Lou och Lana Manana är systrar — de vet allt om varandra. Tillsammans bär de en hemlighet ingen annan känner till: de vet var en uråldrig Inka-skatt är gömd. Ziggy-Lou bär den kunskapen lätt utåt. Inåt är det det tyngsta hon har.

---

### 5. LANA MANANA
**Djur:** Lama · **Grannar:** 4, 6, 10, 18, 19
**Motsägelse:** Talar som brittisk overclass — bär Inka-världens tyngsta hemlighet
**Talsätt:** *"How fascinating. Truly."* *(Det är inte alltid en komplimang.)*
**Vad hon vill:** Att skatten förblir där den är tills världen är redo
**Hemlighet:** Lana har genom en spirituell resa sett var en uråldrig Inka-skatt är gömd. Hon är dess väktare — inte dess ägare. Hon och Ziggy-Lou är de enda som vet. Vad Lana inte vet är att Tarah och Mambo redan är på väg.

---

### 6. TARAH
**Djur:** Mörkblå tiger med ljusblå streck · **Grannar:** 1, 2, 5, 7, 10, 19
**Motsägelse:** Lugn och integritet utanpå — en plan som ingen anar innanpå
**Talsätt:** *"Jag vet vart jag ska."* *(Och det är allt hon säger.)*
**Vad hon vill:** Skatten. Punkt.
**Hemlighet:** Tarah vet var Lana Mananas skatt är gömd och tänker ta den. Hon har planerat länge. Mambo Viento har sett det hända — i en annan tid. Han har inte sagt något. Tarah tror hon jobbar ensam. Det gör hon inte.

---

### 7. MAMBO VIENTO
**Djur:** Drake (två små horn — unicorn tribe) · **Grannar:** 2, 3, 6, 8, 10, 11
**Motsägelse:** Uråldig och allvetande — kan knappt hålla sig i luften i den här världen
**Talsätt:** *"Det har redan hänt. Du vet bara inte om det än."*
**Vad han vill:** Komma åt skatten — men kan inte göra det själv
**Hemlighet:** Mambo har byggt en osynlig kedja — Coco, Sixten, Lana — utan att någon vet att de är länkade. Han har sett slutet. Han vet vad som krävs. Frågan är om Tarah hinner först. Och om Mani låter något av det ske.

---

### 8. SALVADOR
**Djur:** Okänt — färgglad, psykadelisk · **Grannar:** 4, 7, 9, 11, 12
**Motsägelse:** Verkar galen — är den enda som ser klart
**Talsätt:** *"Titta inte på tavlan. Titta på vad tavlan tittar på."*
**Vad han vill:** Att någon ska följa honom hela vägen in — ingen har vågat än
**Hemlighet:** Salvador och Pinto har tillsammans tappat in på världens energiflöde — en outömlig källa av idéer och möjligheter. Salvador törstar dessutom efter Sixtens sociala genialitet och har skickat Coco för att kartlägga den. Han förstår inte att det är omöjligt att stjäla något man inte vet att man har.

---

### 9. PINTO
**Djur:** Leopard · **Grannar:** 4, 8, 10, 12, 13, 14, 15
**Motsägelse:** Lugn och kontrollerad utanpå — kanaliserar oändlig kosmisk kreativitet innanpå
**Talsätt:** *"Sätt dig. Vi har tid."*
**Vad han vill:** Skapa — det är allt. Det räcker.
**Hemlighet:** Pinto och Salvador delar en hemlighet — de har tappat in på världens energiflöde tillsammans. En outömlig källa. Mona Moon anar det. Det är en av anledningarna hon inte kan välja mellan dem — de är samma källa i två olika former.

---

### 10. SIXTEN
**Djur:** Katt · **Grannar:** 4, 5, 6, 7, 9, 11, 15, 16
**Motsägelse:** Känner alla — känner inte sig själv
**Talsätt:** *"Vet du vem du borde träffa? Vänta, jag har någon perfekt—"*
**Vad han vill:** Fler kopplingar, fler samtal, fler världar — utan att förstå att han flyr
**Hemlighet:** Sixten har aldrig stannat tillräckligt länge för att upptäcka vem han är. Svaret finns utspritt i fragment hos de 8 som står honom närmast. Ingen av dem har hela bilden. Tillsammans har de den.

---

### 11. COCO
**Djur:** Okänt · **Grannar:** 7, 8, 10, 12, 16
**Motsägelse:** Verkar lojal mot Salvador — tjänar någon från en helt annan tid
**Talsätt:** *"Ingenting att rapportera. Allt är som vanligt."* *(Det är det aldrig.)*
**Vad han vill:** Slutföra Mambos plan — vad den än är
**Hemlighet:** Coco är dubbelagent. Salvador tror han jobbar för honom. Men Coco rapporterar till Mambo Viento. Uppdraget mot Sixten är en rökridå. Coco har omedvetet absorberat något från Rumi och Mona Moon. Rumi ser det. Säger ingenting.

---

### 12. MONA MOON
**Djur:** Ko · **Grannar:** 8, 9, 11, 13, 16, 17
**Motsägelse:** Ser ut som den mest jordnära — är den mest kosmiskt uppkopplade
**Talsätt:** *"Mmm."* *(En lång paus.)* *"Ja."* *(Tre dagar senare förstår du vad hon menade.)*
**Vad hon vill:** Ingenting. Hon väntar bara. Allt kommer till henne till slut.
**Hemlighet:** Mona Moon kanaliserar information från månen — uråldig feminin kunskap som passerat genom kor sedan världens begynnelse. Salvador och Pinto anar det. De kallar det inspiration. De vet inte att de dricker från samma källa.

---

### 13. BORRO
**Djur:** Noshörning · **Grannar:** 9, 12, 14, 17, 18, 19
**Motsägelse:** Sprider mörker och lögner — bär ett horn han inte förstår innebörden av
**Talsätt:** *"Jag ljuger aldrig. Det vet du ju."* *(Han ljuger alltid.)*
**Vad han vill:** Andras kunskap och kraft — helst utan att de märker det
**Hemlighet:** Borro stjäl fragment av månkanalisationen från Mona utan hennes vetskap. Han förstår inte vad han tar men det växer inom honom och förändrar honom långsamt. Dolores vet. Hon vaktar honom på avstånd — för hans horn gör honom till något han ännu inte förstår.

---

### 14. PEPE
**Djur:** Pingvin · **Grannar:** 9, 13, 15, 19
**Motsägelse:** Ser ut som den som blir trampad på — är den som sätter igång alltihop
**Talsätt:** *"Nej men jag undrar bara... har du pratat med Borro om det där? Inte för att det spelar någon roll."* *(Det gör det alltid.)*
**Vad han vill:** Se vad som händer när han drar i rätt tråd
**Hemlighet:** Pepe kan se igenom andra karaktärers skal och plantera idéer direkt i deras undermedvetna. De tror tankarna är sina egna. Han ser på medan de utvecklas. Ingen har kopplat ett kaos till den lille pingvinen i hörnet. Än.

---

### 15. RONDA
**Djur:** Alligator/Krokodil · **Grannar:** 1, 2, 9, 10, 14, 16, 19
**Motsägelse:** Dominerar varje rum hon går in i — är egentligen det mest sårbara barnet av alla
**Talsätt:** *"Det där är fel. Och det ska jag berätta varför."*
**Vad hon vill:** Att någon ska se igenom henne — utan att hon behöver be om det
**Hemlighet:** Under allt det tuffa finns ett litet barn som bara vill ha en kram. Rumi är den enda som vet. Han har aldrig sagt det högt. Han behöver inte — hon känner att han vet, och det räcker för att hon ska hålla ihop.

---

### 16. RUMI
**Djur:** Papegoja · **Grannar:** 2, 10, 11, 12, 15, 17
**Motsägelse:** Vet allt — säger nästan ingenting
**Talsätt:** *"Det är en bra fråga."* *(Lång paus.)* *"Ställ den igen om tre år."*
**Vad han vill:** Att någon ska ställa rätt fråga
**Hemlighet:** Rumi vet att alla 19 är ett — inte som metafor, utan bokstavligen. Nätverket är en levande organism och han är den enda som känner hela dess puls. När någon lägger alla 19 bitar tillsammans händer något. Rumi väntar på den dagen.

---

### 17. DAFFY GIRAFFY
**Djur:** Giraff · **Grannar:** 2, 3, 12, 13, 16, 18
**Motsägelse:** Den mest avslappnade av alla — bär på universumets längsta perspektiv
**Talsätt:** *"Mmm. Ja. Det löser sig."* *(Det gör det alltid, för honom.)*
**Vad han vill:** Ingenting just nu. Han väntar.
**Hemlighet:** Daffy Giraffy är den enda i Wild som passar in i nästa pussel. Han vet om det. Han har alltid vetat att han hör hemma i två världar samtidigt. Han väntar på att den andra ska dyka upp.

---

### 18. JERRY
**Djur:** Hund · **Grannar:** 3, 4, 5, 13, 17, 19
**Motsägelse:** Ser lite dum ut — är den bästa på att hitta det ingen annan hittar
**Talsätt:** *"Hittade nåt här borta. Vet inte vad det är. Men det luktar viktigt."*
**Vad han vill:** Hitta nästa sak. Det är allt han behöver.
**Hemlighet:** Jerry har redan hittat saker i det här universumet som ingen annan vet om. Han förstår inte alltid vad han hittat — men han minns allt. Han är ett levande arkiv av lösa trådar som ännu inte knutits ihop.

---

### 19. SILVANA
**Djur:** Kamel · **Grannar:** 1, 5, 6, 13, 14, 15, 18
**Motsägelse:** Kommer från den hårdaste platsen — bär på den mjukaste visheten
**Talsätt:** *"Jag har sett öknen blomma. Du har ingen aning om vad som är möjligt."*
**Vad hon vill:** Ingenting mer än det hon redan har — hon är hel
**Hemlighet:** Öknen lärde Silvana något ingen annan vet — att liv blommar starkast där ingen tror det är möjligt. Hon bär på en karta över dolda oaser. Platser där det omöjliga händer. Hon delar den bara med de som förtjänar att veta.

---

## Spänningslinjer i universumet

**Skatten** — Lana väktaren (vet inte att den är stulen), Ziggy-Lou systern/skyddet, Tarah tjuven, Mambo spelaren, Mani den rättfärdiga (vill återlämna till Inka), Jerry som kanske redan hittat den

**Unicorn Club** — Dolores (narval/beskyddare), Zuki (rådjur, horn på väg — den väntade), Mambo (drake, två horn), Borro (noshörning, vet inte vad hans horn betyder)

**Mona Moons källa** — Salvador och Pinto kanaliserar hennes månkunskap utan att veta det, Borro stjäl fragment, ingen vet att det är samma källa

**Sixtens fragment** — hans identitet utspridd hos 8 grannar, Coco kartlägger honom för Mambo, ingen kan ta det som inte vet att det finns

**Rumi väntar** — på att någon lägger alla 19 och ställer rätt fråga. Triggar hemlig animation.

**Daffy Giraffy** — enda biten som passar i nästa pussel-set

---

## Formation Logger (MVP)

Användaren klickar i bitar i den ordning de lagts. Två lägen:

**Formations-läge:** Varje ny bit måste vara granne med någon redan lagd bit.

**Kedje-läge:** Varje ny bit måste vara granne med den *senast* lagda biten.

| Antal bitar | Poäng/bit |
|-------------|-----------|
| 2–4         | 10 pts    |
| 5–8         | 25 pts    |
| 9–12        | 50 pts    |
| 13–16       | 100 pts   |
| 17–19       | 250 pts   |

Systemet genererar en unik formation-kod (t.ex. `WLD-A3F9K2`) och svarar om formationen är unik eller hur många som lagt samma förut.

---

## Secrets-systemet

- **Fasta secrets** — planterade av Leo, låsta, sanna för alla spelare
- **Conditions** — specifika formations-kombinationer (vilka bitar som ligger intill varandra) låser upp secrets
- **Artefakter** — röst, bild, text — något som känns verkligt och unikt
- **Discovery-tracking i Neo4j** — vad är hittat av vem, vad är fortfarande mörkt

---

## Berättelse-systemet — Tre lager

**Canon** — fast, ägt av Leo, oföränderligt. Karaktärernas hemligheter och spänningslinjer.

**Formation** — spelarens egna berättelser kopplade till specifika layouts de lagt.

**Collective Influence** — karaktärer reagerar på events i andra spelares formationer. Nätverket lever.

---

## Narrativ AI (Claude API)

Karaktärsröster genereras via Claude API baserat på varje karaktärs fem fält. Konversationer följer adjacency-edges som ledtrådar. Varje karaktär svarar i sin unika röst:

- Borro ljuger om allt
- Mona svarar med långa pauser
- Rumi väntar på rätt fråga
- Pepe planterar idéer utan att det märks
- Mambo vet alltid mer än han säger

---

## Nästa steg

1. **Neo4j schema** — noder (Character, Formation, Secret, Player), edges (ADJACENT_TO, CONTAINS, UNLOCKS, DISCOVERED_BY)
2. **Karaktärs-API** kopplat till Claude med adjacency-kontext per karaktär
3. **Secrets och conditions design** — vilka formations-kombinationer låser vad
4. **Formation Logger** kopplat till Neo4j backend

---

*Se även: `infinity_puzzles_wild_characters.md` (karaktärsbibeln, version 1.0)*
*Se även: `Company_Context/INFINITYPUZZLES_CONTEXT.md` (projektöversikt)*
