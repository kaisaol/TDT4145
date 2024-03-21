import sqlite3
from queries import forestillingerRangertQuery
con = sqlite3.connect("teater.db")
c = con.cursor()
def forestillingerRangert():
        c.execute(forestillingerRangertQuery)
        resultater = c.fetchall()
        con.close()
    
        for row in resultater:
            print(f"Forestilling: {row[0]}, Dato: {row[1]}, Antall Solgte Plasser: {row[2]}")

if __name__ == "__main__":
    forestillingerRangert()
