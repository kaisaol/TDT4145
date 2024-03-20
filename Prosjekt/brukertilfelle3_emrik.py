#forsøk op oppgave 3

import sqlite3
from queries import skuespillereIStykkerQuery, forestillingerRangertQuery, forestillingerPaaDatoQuery
from brukstilfelle2 import kjopBillett, billettKjop, refNum
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
    billettKjop(1, newRef) #nytt kjøp for standarbruker
    n = 1 #counter
    
    for i in ledigeStoler:
        if n >= 9:
            break
        kjopBillett(i, radNr, forestilling_dato, omrade, newTick, 2, newRef)
        newTick += 1
        n += 1
    exit(1)

if __name__ == '__main__':
    kjopNiBilletter()