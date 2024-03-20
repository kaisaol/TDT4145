#prøver å gjøre oppgaven på egen måte siden ikke forsto gammel kode

import sqlite3
from brukstilfelle2 import kjopBillett, billettKjop

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
    print(radNr, omrade, amountLedigeStoler, ledigeStoler)