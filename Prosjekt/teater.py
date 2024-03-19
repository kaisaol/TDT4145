import sqlite3
import datetime
from queries import antallSolgteBilletterPaDato, skuespillereIStykker, forestillingerSortertEtterSolgteBilletter, skuespillereISammeAkt
con = sqlite3.connect("teater.db")
c = con.cursor()

billettId = 1
referanseNr = 1

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


def getData(file):
    f = open(file,"r")
    line = f.readline()
    date = None

    while True:
        if line.startswith("Dato"):
            return date
            
        if not line: 
            break

def aleredeKjopt(): #Finner allerede kjøpte seter
    # setter opp gamle scene 
    fileOne = "txtFiles/hovedscene.txt"
    fileTwo = "txtFiles/gamle-scene.txt"

    resultH = getAreaWithRow(fileOne)
    dateOne = getData(fileOne)
    mainStageArea = ["Parkett", "Galleri"]
    countH = 1


    oldRefNum = referanseNr
    billettKjop(dateOne, 1, referanseNr)

    for area in mainStageArea:
        lines = resultH[area]
        for rowN, line in enumerate(lines, 1):
            for seat in line:
                if seat == "1":
                    kjopBillett(countH, rowN, area, billettId, 1, oldRefNum)
                countH += 1
    
    resultG = getAreaWithRow(fileTwo)
    dateTwo = getData(fileTwo)
    oldRefNum = referanseNr
    billettKjop(dateTwo, 1, referanseNr)

    for area, lines in resultG.items():
        for rowN, line in enumerate(lines, 1):
            count = 1
            for seat in line:
                if seat == "1":
                    kjopBillett(count, rowN, area, billettId, 2, oldRefNum)
                count += 1



def billettKjop(dato, kundeNr, referanseNr):
    c.execute('INSERT INTO BilettKjop(ReferanseNr, Tidspunkt, KundeNr) VALUES(:ReferanseNr, :Tidspunkt, :KundeNr)', {"ReferanseNr":referanseNr, "Tidspunkt":dato, "KundeNr":kundeNr})
    referanseNr += 1 

def kjopBillett(stolNr, radNr, omrade, billettId, salId, refNr):
    c.execute('INSERT INTO Billett(BillettID, ReferanseNr, StolNr, RadNr, Omrade, SalID) VALUES(:BillettID, :ReferanseNr, :StolNr, :RadNr, :Område, :SalID)', {"BillettID":billettId, "ReferanseNr":refNr, "StolNr":stolNr, "RadNr":radNr, "Omrade":omrade, "SalID":salId})
    billettId += 1


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



def forestillingerPaaDato(dato): #brukstilfelle 4
    c.execute(forestillingerPaaDatoQuery, (dato,))
    performances = c.fetchall()
    
    return performances

# Example usage
if __name__ == "__main__":
    date_input = input("Sett inn dato på formatet (YYYY-MM-DD): ")
    try:
        datetime.strptime(date_input, "%Y-%m-%d")
        performances = forestillingerPaaDato(date_input)
        for performance in performances:
            print(f"Tid: {performance[0]}, Stykke: {performance[1]}, Solgte billetter: {performance[2]}")
    except ValueError:
        print("Ugyldig dato-format. Vennligst bruk YYYY-MM-DD.")

# def skuespillereIStykker(): #brukstilfelle 5
#     #usikker på funksjon her, skal i alle fall være query om alle skuespillere med navn, stykke og rolle
# def forestillingerRangert(): #brukstilfelle 6
#     #returnerer alle forestillinger med navn, dato og antall billetter solgt i synkende rekkefølge
# def skuespillereISammeAkt(): #brukstilfelle 7
#     #tar input på navn, returnerer alle skuespillere den har spilt i akt med, med begge navn og spillet
