import sqlite3
from queries import skuespillereISammeAktQuery
con = sqlite3.connect("teater.db")
c = con.cursor()
def skuespillereISammeAkt(skuespillernavn):
    c.execute(skuespillereISammeAktQuery, (skuespillernavn,))
    results = c.fetchall()
    if results:
        for row in results:
            print(f"{row[0]} har spilt med {row[1]} i '{row[2]}'")
    else:
        print("Ingen resultater funnet.")
    con.close()
if __name__ == "__main__":
    skuespillernavn = input("Skriv inn navnet på skuespilleren: ")
    skuespillereISammeAkt(skuespillernavn)