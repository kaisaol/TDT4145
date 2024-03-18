import sqlite3
import datetime
from queries import antallSolgteBilletterPaDato, skuespillereIStykker, forestillingerSortertEtterSolgteBilletter, skuespillereISammeAkt
con = sqlite3.connect("teater.db")
c = con.cursor()

startquery = True

def setteInnSolgteStoler(): #brukstilfelle 2
    #denne skal lese fil og skrive inn i db
     with open("gamle-scene.txt", 'r') as fil:
        omrade = None
        rad_nr = 0
        for linje in fil:
            linje = linje.strip()
            if linje.startswith("Dato"):
                continue  # Vi antar at forestilling_dato allerede er gitt som parameter
            elif linje.isalpha():
                omrade = linje  # Når linjen inneholder områdenavnet
                rad_nr = 0
            else:
                rad_nr += 1
                for stol_nr, status in enumerate(linje, start=1):
                    if status == '1':  # Sjekker om setet er solgt
                        # Genererer en ny ReferanseNr, dette bør unikt for hver billett
                        referanse_nr = f"{forestilling_dato.replace('-', '')}{sal_id}{rad_nr}{stol_nr}"
                        try:
                            # Sett inn en ny billettkjøp for hver solgte billett
                            c.execute('INSERT INTO BilettKjop (ReferanseNr, Tidspunkt, KundeNr) VALUES (?, ?, ?)',
                                           (referanse_nr, forestilling_dato, standard_kunde_id))
                            
                            # Sett inn den solgte billetten
                            c.execute('INSERT INTO Billett (ReferanseNr, StolNr, RadNr, Omrade, SalID) VALUES (?, ?, ?, ?, ?)',
                                           (referanse_nr, stol_nr, rad_nr, omrade, sal_id))
                        except sqlite3.IntegrityError:
                            print(f"Billett for stol {stol_nr}, rad {rad_nr}, i område {omrade} på dato {forestilling_dato} er allerede registrert.")


#BRUKSTILFELLE 3:
    #denne skal kjøpe 9 billetter på samme rad og gi pris
    #Utkast
def kjopNiBilletter(forestilling_dato="2024-02-03", stykkeID=2, kundegruppeID="O", antall_billetter=9):
    # 1 & 2. Identifiser ledige stoler ved å sjekke mot de som allerede er solgt
    c.execute("""
        SELECT s.StolNr, s.RadNr, s.Omrade, s.SalID
        FROM Stol s
        WHERE NOT EXISTS (
            SELECT 1 FROM Billett b
            JOIN BilettKjop bk ON b.ReferanseNr = bk.ReferanseNr
            JOIN Forestilling f ON f.SalID = b.SalID AND f.StykkeID = :stykkeID AND f.Tidspunkt LIKE :dato
            WHERE b.StolNr = s.StolNr AND b.RadNr = s.RadNr AND b.Omrade = s.Omrade AND b.SalID = s.SalID
        )
        AND s.SalID IN (
            SELECT SalID FROM Forestilling WHERE Tidspunkt LIKE :dato AND StykkeID = :stykkeID
        )
    """, {"dato": forestilling_dato + "%", "stykkeID": stykkeID})

    ledige_stoler = c.fetchall()

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

   

#######



def forestillingerPåDato(): #brukstilfelle 4
    #denne skal ha input og gi alle forestillinger på dato

def skuespillereIStykker(): #brukstilfelle 5
    #usikker på funksjon her, skal i alle fall være query om alle skuespillere med navn, stykke og rolle
def forestillingerRangert(): #brukstilfelle 6
    #returnerer alle forestillinger med navn, dato og antall billetter solgt i synkende rekkefølge
def skuespillereISammeAkt(): #brukstilfelle 7
    #tar input på navn, returnerer alle skuespillere den har spilt i akt med, med begge navn og spillet
