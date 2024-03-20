import sqlite3
from queries import skuespillereIStykkerQuery
con = sqlite3.connect("teater.db")
c = con.cursor()
#antar siden det ikke står i oppgavebeskrivelsen at funksjonen skal ta inn noe, så skal alle skuespillere med tilhørende stykker og roller skrives ut hver gang
def skuespillereIStykker(): #brukstilfelle 5
    c.execute(skuespillereIStykkerQuery)
    results = c.fetchall()
    for row in results:
        print(f"Teaterstykke: {row[0]}, Skuespiller: {row[1]}, Rolle: {row[2]}")
if __name__ == "__main__":
    skuespillereIStykker()