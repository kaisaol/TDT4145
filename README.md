# Teater-database
Prosjekt  i TDT4145 Databaser og datamodellering våren 2024.  
Studenter som har medvirket til leveransen: Kaisa Øyre Larsen, Emrik Sjølie Moe og Kristoffer Ryen Skullerud.

## **Generell informasjon**
I prosjektet foregår all kommunikasjon mellom bruker og programmet i terminalen.

### Steg for å teste prosjektet
1. Dersom [teater.db](./Prosjekt/teater.db)-filen ikke eksisterer; Kjør [init.py](./Prosjekt/init.py) for å opprette databasen og legge til all tilhørende data.
2. Kjør [teater.py](./Prosjekt/teater.py) for å teste brukstilfellene.
3. Dersom du ønsker å fjerne endringer du har gjort; Slett [teater.db](./Prosjekt/teater.db)-filen og gjenta steg 1.
-----
### **Brukstillfelle 1**
**Beskrivelse**  
Vi ønsker å sette inn de to salene nevnt over (Hovedscenen og Gamle Scene), sammen med stoler,
teaterstykker, forestillinger, akter, roller, skuespillere og andre medvirkende,
slik det er beskrevet i teksten over. Dette kan implementeres i SQL.

**Løsning**  
Vi har løst brukerhistorien i [init.py](./Prosjekt/init.py)-filen. Ved å kjøre denne filen opprettes databasen og det legges til inndata for Nordlandsbanen. 

### revidere

-----
### **Brukstilfelle 2**
**Beskrivelse**  
Med oppgaven er det lagt ut noen filer som beskriver hvilke stoler som
allerede er solgt til noen forestillinger. Her skal det lages Pythonprogram som
leser filene og setter inn hvilke stoler som er solgt. Det er OK å sette inn
stolene basert på disse filene også. Her er det ok at kjøper av de allerede
solgte stolene er en standardbruker. dvs. samme forhåndsinnsatte bruker 

**Løsning**  
Vi har løst brukerhistorien i [init.py](./Prosjekt/init.py)-filen. Ved å kjøre denne filen opprettes databasen og det legges inn data for de tre togrutene på Nordlandsbanen.  

-----
### **Brukstilfelle 3**
**Beskrivelse**  
Her skal du kjøpe 9 voksenbilletter til forestillingen for Størst av alt er
kjærligheten 3. februar, hvor det er 9 ledige billetter og hvor stolene er på
samme rad. Stolene trenger ikke være ved siden av hverandre. Vi ønsker å få
summert hva det koster å kjøpe disse billettene, men du trenger ikke ta
hensyn til selve betalingen, den antar vi skjer på et annet system som dere
ikke trenger å lage. Denne funksjonen skal implementeres i Python og SQL.

**Løsning**  
Vi har løst brukerhistorien i [teater.py](./Prosjekt/teater.py)-filen. Ved å kjøre filen og skrive inn 'S' for 'Vis stasjoner'. Etter vil man få skrevet ut alle togstasjoner. Man får så valget om å skrive inn en togstasjon og en dag. 

----
### **Brukstilfelle 4**
**Beskrivelse**  
Her skal du implementere et Pythonprogram (med bruk av SQL) som tar inn
en dato og skriver ut hvilke forestillinger som finnes på denne datoen og lister
opp hvor mange billetter (dvs. stoler) som er solgt. Ta også med forestillinger
hvor det ikke er solgt noen billetter.
**Løsning**  
Vi har løst brukerhistorien i [teater.py](./Prosjekt/teater.py)-filen. Ved å kjøre filen og skrive inn 'T' for 'Søk etter togruter'. Man skriver så inn en startstasjon og en sluttstasjon, ønsket data og klokkeslett. Det vil så bli skrevet ut informasjon om de togrutene som stemmer overens med input.

-----
### **Brukstilfelle 5**
**Beskrivelse**  
Vi ønsker å lage et query i SQL som finner hvilke (navn på) skuespillere som
opptrer i de forskjellige teaterstykkene. Skriv ut navn på teaterstykke, navn på skuespiller og rolle.

**Løsning**  
Vi har løst brukerhistorien i [teater.py](./tog.py)-filen. Kjør filen og skriv inn 'R' for 'Registerer deg i kunderegisteret'. Man skriver så inn fornavn, etternavn, epost og telefonnummer for å bli registert som en kunde.

-----
### **Brukstilfelle 6**
**Beskrivelse**  
Vi ønsker å lage et query i SQL som finner hvilke forestillinger som har solgt
best. Skriv ut navn på forestilling og dato og antall solgte plasser sortert på
antall plasser i synkende rekkefølge.

**Løsning**  
Vi har løst brukerhistorien i [init.py](./init.py)-filen. 

-----
### **Brukstilfelle 7**
**Beskrivelse**  
Du skal lage et Pythonprogram (og SQL) som tar et skuespillernavn og finner
hvilke skuespilllere de har spilt med i samme akt. Skriv ut navn på begge og
hvilket skuespill det skjedde.

**Løsning**  
Vi har løst brukerhistorien i [teater.py](./tog.py)-filen. Kjør filen og skriv inn 'F' for 'Finn informasjon om fremtidige reiser'. Man skriver så inn fornavn og etternavn. Man vil så få ut informasjon om fremtidige reiser.