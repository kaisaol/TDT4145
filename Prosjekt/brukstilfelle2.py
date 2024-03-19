import sqlite3
from init import getAreaWithRow
con = sqlite3.connect("teater.db")
c = con.cursor()

number_iter = iter(range(1,9999999))


def getData(file):
    with open(file,"r") as f:
        text = f.read()

    for line in text.splitlines():
        if line.startswith("Dato"):
            return line.split(' ')[1]
            

def aleredeKjopt(): 
    fileOne = "txtFiles/hovedscenen.txt"
    fileTwo = "txtFiles/gamle-scene.txt"

    resultH = getAreaWithRow(fileOne)
    dateOne = getData(fileOne)
    mainStageArea = ["Parkett", "Galleri"]
    countH = 1
    refNum = next(number_iter)

    billettKjop(dateOne, 1, refNum)

    for area in mainStageArea:
        lines = resultH[area]
        for rowN, line in enumerate(lines, 1):
            for seat in line:
                if seat == "1":
                    billettId = next(number_iter)
                    refNum = next(number_iter)
                    kjopBillett(countH, rowN, area, billettId, 1, refNum)
                countH += 1
    
    resultG = getAreaWithRow(fileTwo)
    dateTwo = getData(fileTwo)
    refNum = next(number_iter)
    billettKjop(dateTwo, 1, refNum)

    for area, lines in resultG.items():
        for rowN, line in enumerate(lines, 1):
            count = 1
            for seat in line:
                if seat == "1":
                    billettId = next(number_iter)
                    refNum = next(number_iter)
                    kjopBillett(count, rowN, area, billettId, 2, refNum)
                count += 1
    con.commit()


def billettKjop(dato, kundeNr, referanseNr):
    c.execute('INSERT INTO BilettKjop(ReferanseNr, Tidspunkt, KundeNr) VALUES(:ReferanseNr, :Tidspunkt, :KundeNr)', {"ReferanseNr":referanseNr, "Tidspunkt":dato, "KundeNr":kundeNr})
    referanseNr += 1 

def kjopBillett(stolNr, radNr, omrade, billettId, salId, refNr):
    c.execute('INSERT INTO Billett(BillettID, ReferanseNr, StolNr, RadNr, Omrade, SalID) VALUES(:BillettID, :ReferanseNr, :StolNr, :RadNr, :Omrade, :SalID)', {"BillettID":billettId, "ReferanseNr":refNr, "StolNr":stolNr, "RadNr":radNr, "Omrade":omrade, "SalID":salId})
    billettId += 1

aleredeKjopt()
