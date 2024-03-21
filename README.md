# Teater-database

Prosjekt i TDT4145 Databaser og datamodellering våren 2024.  
Studenter som har medvirket til leveransen: Kaisa Øyre Larsen, Emrik Sjølie Moe og Kristoffer Ryen Skullerud.

## **Generell informasjon**

I prosjektet foregår all kommunikasjon mellom bruker og programmet i terminalen. Vi har brukt python versjon 3.9 og nyere, så dette er nødvendig for å at alt skal kjøres.

### Steg for å teste prosjektet

1. Sørg for at du er i riktig i riktig filsti. Fra start må du inn i TDT4145/Prosjekt. Vi anbefaler utvidelsen SQLite viewer for å kunne enkelt lese fra databasefilen.

```py
cd Prosjekt/
```

2. Kjør [init.py](./Prosjekt/init.py) for å opprette databasen og legge til all tilhørende data. Dersom [teater.db](./Prosjekt/teater.db)-filen ikke eksisterer vil denne opprettes, og dersom den eksisterer vil os.remove() funksjonen slette eksisterende, og opprette på nytt. Dette sikrer riktig oppsett ved start. 
```py
python3 init.py
```
3. Kjør deretter brukstilfeller 2-7 for å teste alle brukstilfellene brukshistoriene. Noen av brukstilfellene krever kjøring av [brukstilfelle2.py](./Prosjekt/brukstilfelle2.py) først, så denne bør kjøres først.
````
python3 brukstilfelle2.py
````
4. Dersom du ønsker å fjerne endringer du har gjort; Kjør [init.py](./Prosjekt/init.py)-filen på nytt for å opprette databasen på nytt.
```py
python3 init.py
```
---

### **Brukstillfelle 1**

**Beskrivelse**  
Vi ønsker å sette inn de to salene nevnt over (Hovedscenen og Gamle Scene), sammen med stoler,
teaterstykker, forestillinger, akter, roller, skuespillere og andre medvirkende,
slik det er beskrevet i teksten over. Dette kan implementeres i SQL.

**Løsning**  
Vi har løst brukerhistorien i [init.py](./Prosjekt/init.py)-filen. Ved å kjøre denne filen opprettes tabellene til databasen, teater.db, og det legges til inndata for:
-Selve teateret
-De to salene og sesongen teaterer er "i"
-Teatertykkene "Størst av alt er kjærligheten" og "Kongsemnene"
-De ansatte (begrenset til direktøren, skuespillerene i de to teaterstykkene og tilhørende "kunstnerisk lag" for hvert stykke)
-Hvilke roller som er i hvert skuespill, hvem disse spilles av, og i hvilke akter disse rollene er med i

-Stoler 

-De ulike kundegruppene og TypeBillett for begge teaterstykkene. Dette er for å løse senere brukshistorier

Merknad:
I oppgavefilen var "Guttorm Ingesson", oppført som en rolle. Da denne rollen ikke sto oppført på teaterets nettsider, er den heller ikke med i databasen. Dette fordi vi ikke kan koble roller til skuespillere, om det ikke er oppført.

```py
python3 init.py
```
---

### **Brukstilfelle 2**

**Beskrivelse**  
Med oppgaven er det lagt ut noen filer som beskriver hvilke stoler som
allerede er solgt til noen forestillinger. Her skal det lages Pythonprogram som
leser filene og setter inn hvilke stoler som er solgt. Det er OK å sette inn
stolene basert på disse filene også.

Her er det ok at kjøper av de allerede
solgte stolene er en standardbruker. dvs. samme forhåndsinnsatte bruker

**Løsning**  
Vi har løst brukerhistorien i [brukstilfelle2.py](./Prosjekt/brukstilfelle2.py)-filen. 
Programmet leser fra tekstfilene i txtFiles mappa, og legger inn billetkjøp i henhold til databasemodellen for hver "1" det kommer over.

For å kjøre programmet:
```py
python3 brukstilfelle2.py
```

---

### **Brukstilfelle 3**

**Beskrivelse**  
Her skal du kjøpe 9 voksenbilletter til forestillingen for Størst av alt er
kjærligheten 3. februar, hvor det er 9 ledige billetter og hvor stolene er på
samme rad. Stolene trenger ikke være ved siden av hverandre. Vi ønsker å få
summert hva det koster å kjøpe disse billettene, men du trenger ikke ta
hensyn til selve betalingen, den antar vi skjer på et annet system som dere
ikke trenger å lage.

Denne funksjonen skal implementeres i Python og SQL.

**Løsning**  
Vi har løst brukerhistorien i [brukstilfelle3.py](./Prosjekt/brukstilfelle3.py)-filen. Programmet kjører først en spørring for å hente ut en rad med 9 eller flere ledige seter, første "ledige" rad blir valgt. Deretter registreres kjøp i henhold til databasestrukturen på 9 av disse billettene. Vi har registrert dette kjøpet på standardbrukeren, for enkelhetens skyld. 

For å kjøre programmet:
```py
python3 brukstilfelle3.py
```

---

### **Brukstilfelle 4**

**Beskrivelse**  
Her skal du implementere et Pythonprogram (med bruk av SQL) som tar inn
en dato og skriver ut hvilke forestillinger som finnes på denne datoen og lister
opp hvor mange billetter (dvs. stoler) som er solgt. Ta også med forestillinger
hvor det ikke er solgt noen billetter.
**Løsning**  
Vi har løst brukerhistorien i [brukstilfelle4.py](./Prosjekt/brukstilfelle4.py)-filen. Programmet tar inn en input på dato-format (YYYY-MM-DD) og lister opp alle registrerte forestillinger som er på denne datoen, uavhengig av tidpunkt, og med tilhørende antall solgte billetter som kan være null. 

For å kjøre programmet:
```py
python3 brukstilfelle4.py
```

---

### **Brukstilfelle 5**

**Beskrivelse**  
Vi ønsker å lage et query i SQL som finner hvilke (navn på) skuespillere som
opptrer i de forskjellige teaterstykkene. Skriv ut navn på teaterstykke, navn på skuespiller og rolle.

**Løsning**  
Vi har løst brukerhistorien i [brukstilfelle5.py](./Prosjekt/brukstilfelle5.py)-filen. Programmet tar utgangspunkt i query lagt inn i [queries.py](./Prosjekt/queries.py) og printer ut alle registrerte skuespillere med tilhørende roller og teaterstykker. 

For å kjøre programmet:
```py
python3 brukstilfelle5.py
```

---

### **Brukstilfelle 6**

**Beskrivelse**  
Vi ønsker å lage et query i SQL som finner hvilke forestillinger som har solgt
best. Skriv ut navn på forestilling og dato og antall solgte plasser sortert på
antall plasser i synkende rekkefølge.

**Løsning**  
Vi har løst brukerhistorien i [brukstilfelle6.py](./Prosjekt/brukstilfelle6.py)-filen. Programmet tar utgangspunkt i query lagt inn i [queries.py](./Prosjekt/queries.py) og printer ut alle forestillinger med tilhørende dato og solgte plassert, rangert etter antall stolgte plasser. 

For å kjøre programmet:
```py
python3 brukstilfelle6.py
```

---

### **Brukstilfelle 7**

**Beskrivelse**  
Du skal lage et Pythonprogram (og SQL) som tar et skuespillernavn og finner
hvilke skuespilllere de har spilt med i samme akt. Skriv ut navn på begge og
hvilket skuespill det skjedde.

**Løsning**  
Vi har løst brukerhistorien i [brukstilfelle7.py](./Prosjekt/brukstilfelle7.py)-filen. Programmet tar inn navnet på en skuespiller (eks Arturo Scotti, rett frem uten "fnutter") og printer ut alle skuespillere denne personen har spilt med, sammen med tilhørende stykker.

For å kjøre programmet:
```py
python3 brukstilfelle7.py
```
