#forsøk op oppgave 3

import sqlite3
from queries import skuespillereIStykkerQuery, forestillingerRangertQuery, forestillingerPaaDatoQuery
con = sqlite3.connect("teater.db")
c = con.cursor()

def kjopNiBilletter(forestilling_dato="2024-02-03 18:30:00", stykkeID=2, kundegruppeID="O", antall_billetter=9):
    # 1 & 2. Identifiser ledige stoler ved å sjekke mot de som allerede er solgt
    c.execute("""
       SELECT s.RadNr, s.Omrade, COUNT(s.StolNr) AS ledigeStoler, GROUP_CONCAT(s.StolNr) FROM Stol s
    INNER JOIN Forestilling f ON f.SalID = s.SalID
    WHERE f.Tidspunkt = '2024-02-03 18:30:00' 
        AND NOT EXISTS (SELECT 1 FROM Billett b WHERE b.Tidspunkt = f.Tidspunkt AND b.StolNr = s.StolNr AND b.RadNr = s.RadNr AND b.Omrade = s.Omrade)
    GROUP BY s.RadNr, s.Omrade
	HAVING ledigeStoler >= 9
	LIMIT 1;
    """)

    result = c.fetchone()
    radNr, omrade, amountLedigeStoler, ledigeStoler = result
    ledigeStoler = ledigeStoler.split(",")

    c.execute("SELECT max(ReferanseNr) FROM BilettKjop")
    result1 = c.fetchone() #finner forrige ref nummer

    if result1 is not None:
        newRef = result1[0] + 1 #lager variabel så lenge ikke null

    c.execute("SELECT max(BillettID) FROM Billett")
    result2 = c.fetchone() #forrige billett nr

    if result2 is not None:
        newTick = result2[0] + 1 #så lenge ikke null
    #print(radNr, omrade, amountLedigeStoler, ledigeStoler)
    bought = 0
    billettKjopNine(1, newRef, forestilling_dato) #nytt kjøp for standarbruker som alle 9 biletter går på
    n = 1 #counter
    
    for i in ledigeStoler:
        if n >= 9:
            break
        kjopBillettNine(i, radNr, forestilling_dato, omrade, newTick, 2, newRef) #kjøper 9 biletter
        newTick += 1
        n += 1
    exit(1)

def billettKjopNine(kundeNr, referanseNr, dato):
    c.execute('INSERT INTO BilettKjop(ReferanseNr, Tidspunkt, KundeNr) VALUES(:ReferanseNr, :Tidspunkt, :KundeNr)', {"ReferanseNr":referanseNr, "Tidspunkt": dato, "KundeNr":kundeNr})
    referanseNr += 1 

def kjopBillettNine(stolNr, radNr, tidspunkt, omrade, billettId, salId, refNr):
    c.execute('INSERT INTO Billett(BillettID, ReferanseNr, Tidspunkt, StolNr, RadNr, Omrade, SalID) VALUES(:BillettID, :ReferanseNr, :Tidspunkt, :StolNr, :RadNr, :Omrade, :SalID)', {"BillettID":billettId, "ReferanseNr":refNr, "Tidspunkt": tidspunkt, "StolNr":stolNr, "RadNr":radNr, "Omrade":omrade, "SalID":salId})
    billettId += 1

if __name__ == '__main__':
    kjopNiBilletter()