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

def kjøpeNiBilletter(): #brukstilfelle 3
    #denne skal kjøpe 9 billetter på samme rad og gi pris

def forestillingerPåDato(): #brukstilfelle 4
    #denne skal ha input og gi alle forestillinger på dato

def skuespillereIStykker(): #brukstilfelle 5
    #usikker på funksjon her, skal i alle fall være query om alle skuespillere med navn, stykke og rolle
def forestillingerRangert(): #brukstilfelle 6
    #returnerer alle forestillinger med navn, dato og antall billetter solgt i synkende rekkefølge
def skuespillereISammeAkt(): #brukstilfelle 7
    #tar input på navn, returnerer alle skuespillere den har spilt i akt med, med begge navn og spillet
