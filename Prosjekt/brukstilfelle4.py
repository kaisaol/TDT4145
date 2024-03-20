import sqlite3
from datetime import datetime
from queries import forestillingerPaaDatoQuery
con = sqlite3.connect("teater.db")
c = con.cursor()
def forestillingerPaaDato(dato): #brukstilfelle 4

    c.execute(forestillingerPaaDatoQuery, (dato,))
    performances = c.fetchall()
    con.close()
    return performances

if __name__ == "__main__":
    date_input = input("Skriv inn dato på formatet YYYY-MM-DD: ")
    try:
        _ = datetime.strptime(date_input, "%Y-%m-%d")
        print(f"Søker på dato: {date_input}")  # Debugging output
        performances = forestillingerPaaDato(date_input)
        if performances:
            for performance in performances:
                print(f"Tidspunkt: {performance[0]}, Stykke: {performance[1]}, Solgte billetter: {performance[2]}")
        else:
            print("Ingen forestillinger funnet for denne datoen.")
    except ValueError:
        print("Ugyldig dato-format. Vennligst bruk formatet YYYY-MM-DD.")

##MÅ FIKSES: den antar nå at alle forestillingene av samme stykke har solgt samme antall billetter, så må fikse logikken for dette