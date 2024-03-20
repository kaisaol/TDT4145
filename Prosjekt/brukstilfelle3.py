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
    print(radNr, omrade, amountLedigeStoler, ledigeStoler)
    exit(1)

    # 3 & 4. Gruppere ledige stoler etter RadNr og finne en rad med minst 9 ledige stoler
    rad_med_ledige_stoler = {}
    for stol in ledige_stoler:
        rad_nr = stol[1]
        rad_med_ledige_stoler.setdefault(rad_nr, []).append(stol)

    rad_for_kjop = None
    for rad_nr, stoler in rad_med_ledige_stoler.items():
        if len(stoler) >= antall_billetter:
            rad_for_kjop = rad_nr
            break

    if not rad_for_kjop:
        print("Fant ikke en rad med nok ledige stoler.")
        return

    # 5. Kjøpe billetter for stolene på valgte rad
    valgte_stoler = rad_med_ledige_stoler[rad_for_kjop][:antall_billetter]
    for stol in valgte_stoler:
        referanse_nr = f"{forestilling_dato.replace('-', '')}{stykkeID}{stol[1]}{stol[0]}"
        c.execute('INSERT INTO BilettKjop (ReferanseNr, Tidspunkt, KundeNr) VALUES (:referanseNr, :tidspunkt, :kundeNr)',
                  {"referanseNr": referanse_nr, "tidspunkt": forestilling_dato, "kundeNr": 1})
        c.execute('INSERT INTO Billett (ReferanseNr, StolNr, RadNr, Omrade, SalID) VALUES (:referanseNr, :stolNr, :radNr, :omrade, :salID)',
                  {"referanseNr": referanse_nr, "stolNr": stol[0], "radNr": stol[1], "omrade": stol[2], "salID": stol[3]})

    # 6. Beregne totalprisen for billettene
    c.execute('SELECT Pris FROM TypeBillett WHERE KundegruppeID = :kundegruppeID AND StykkeID = :stykkeID', {"kundegruppeID": kundegruppeID, "stykkeID": stykkeID})
    pris_per_billett = c.fetchone()[0]
    totalpris = pris_per_billett * antall_billetter

    con.commit()
    print(f"Kjøpte {antall_billetter} billetter til 'Størst av alt er kjærligheten' den {forestilling_dato}. Totalpris: {totalpris} NOK.")

if __name__ == '__main__':
    kjopNiBilletter()