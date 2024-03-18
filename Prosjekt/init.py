import sqlite3
import os

try:
    os.remove("teater.db")
except FileNotFoundError:
    pass

con = sqlite3.connect("teater.db") #kobler til database 
c = con.cursor()

try:
    with open("teater.sql", "r") as fp:
        sql_commands = fp.read().split(';')
    for command in sql_commands:
        try:
            if command.strip(): 
                c.execute(command)
        except sqlite3.OperationalError as e:
            print(f"An error occurred with SQLite: {e}")
            print(f"Problematic SQL command: {command}")
            break 
except FileNotFoundError:
    print("Failed to open 'teater.sql'. Please check if the file exists and the path is correct.")
except sqlite3.Error as e:
    print("An error occurred with SQLite:", e)
else:
     #BRUKSHISTORIE 1 - INNSETTING AV VERDIER

    #Teater
    c.execute('INSERT INTO Teater(TeaterID, Navn, AnsattID) VALUES(1, "Troendelag teater", 29)')

    #Saler
    c.execute('INSERT INTO Teatersal(SalID,Navn,Kapasitet,TeaterID) VALUES(1, "Hovedscenen", 524, 1)')
    c.execute('INSERT INTO Teatersal VALUES(2, "Gamle Scene", 332, 1)')

    #Sesong - Siden vi ser paa forestillingene som gikk i februar 2024, bruker vi dette som sesong
    c.execute('INSERT INTO Sesong(StartDato, SluttDato, TeaterID) VALUES("2024-02-01", "2024-02-29", 1)')

    #Teaterstykker
    c.execute('INSERT INTO Teaterstykke(StykkeID, Navn, StartDato) VALUES(1, "Kongsemnene", "2024-02-01")')
    c.execute('INSERT INTO Teaterstykke VALUES(2, "Stoerst av alt er kjaerligheten", "2024-02-01")')

    #ANSATTE
    #TelefonNr og Epost var ikke tilgjengelig for mange av de ansatte, saa SQL maa endres. Bruker NULL
    #Da jobbstatus ikke var tilgjengelig for alle, la vi til grunn at de er fast ansatte for enkeltshetens skyld. Dette er ogsaa trivielt for aa loese oppgaven, saa vi vektla det ikke mye tid.

    #Direktoeren - for at opprettelsen at teater med fremmednoekkel AnsattID mot direktoer skal bli mest riktig
    c.execute('Insert INTO Ansatt VALUES (29, "Elisabeth Hansen", NULL, NULL, "Fast", "Direktoer")')

    #Kunstnerisk lag - "Kongsemnene"
    c.execute('INSERT INTO Ansatt(AnsattID, Navn, TelefonNr, Epost, Jobbstatus, Stillingstittel) VALUES(1, "Yury Butusoc", NULL, NULL, "Fast", "Regissoer")')
    c.execute('INSERT INTO Ansatt VALUES (2,"Aleksandr Shishkin Hokusai", NULL, NULL, "Fast", "Scenograf")')
    c.execute('INSERT INTO Ansatt VALUES (3, "Eivind Myren", NULL, NULL, "Fast", "Lysdesigner")')
    c.execute('INSERT INTO Ansatt VALUES (4, "Mina Rype Stokke", NULL, NULL, "Fast","Dramaturg")')
    #Kunsterisk lag - "Stoerst av alt er kjaerligheten"
    c.execute('INSERT INTO Ansatt VALUES(5, "Jonas Corell Petersen", NULL, NULL, "Innleid", "Reggisoer")')
    c.execute('INSERT INTO Ansatt VALUES(6, "David Gehrt", NULL, NULL, "Innleid", "Scenograf")')
    c.execute('INSERT INTO Ansatt VALUES(7, "Gaute Toender", NULL, NULL, "Fast", "Lyddesigner")')
    c.execute('INSERT INTO Ansatt VALUES(8, "Magnus Mikaelsen", NULL, NULL, "Fast", "Lysdesigner")')
    c.execute('INSERT INTO Ansatt VALUES(9, "Kristoffer Spender", NULL, NULL, "Innleid", "Dramaturg")')


    #"Stoerst av alt er kjaerligheten" - Disse spiller seg selv (til naar fylle inn roller)
    c.execute('INSERT INTO Ansatt VALUES(10, "Sunniva Du Mond Nordal", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(11, "Jo Saberniak", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(12, "Marte M. Steinholt", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(13, "Tor Ivar Hagen", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(14, "Trond-Ove Skroedal", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(15, "Natalie Groendahl Tangen", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(16, "Aasmund Flaten", NULL, NULL, "Fast", "Skuespiller")')

    #"Kongsemnene"
    c.execute('INSERT INTO Ansatt VALUES(17, "Arturo Scotti", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(18, "Ingunn Beate Strige Oeyen", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(19, "Hans Petter Nilsen", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(20, "Madeleine Brandtzaeg Nilsen", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(21, "Synnoeve Fossum Eriksen", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(22, "Emma Caroline Deichmann", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(23, "Thomas Jensen Takyi",NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(24, "Per Bogstad Gulliksen",NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(25, "Isak Holmen Soerensen",NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(26, "Fabian Heidelberg Lunde",NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(27, "Emil Olafsson", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(28, "Snorre Ryen Toendel", NULL, NULL, "Fast", "Skuespiller")')

    #Roller - Kongsemne
    c.execute('INSERT INTO Rolle(RolleID, Rollenavn) VALUES(1,"Haakon Haakonsen")')
    c.execute('INSERT INTO Rolle VALUES(2,"Dagfinn Bonde")')
    c.execute('INSERT INTO Rolle VALUES(3,"Jatgeir Skald")')
    c.execute('INSERT INTO Rolle VALUES(4,"Sigrid")')
    c.execute('INSERT INTO Rolle VALUES(5,"Ingebjoerg")')
    c.execute('INSERT INTO Rolle VALUES(6,"Skule Jarl")')
    c.execute('INSERT INTO Rolle VALUES(7,"Inga fraa Vartejg")')
    c.execute('INSERT INTO Rolle VALUES(8,"Paal Flida")')
    c.execute('INSERT INTO Rolle VALUES(9,"Ragnhild")')
    c.execute('INSERT INTO Rolle VALUES(10,"Gregorius Jonsson")')
    c.execute('INSERT INTO Rolle VALUES(11,"Margrete")')
    c.execute('INSERT INTO Rolle VALUES(12, "Biskop Nikolas")')
    c.execute('INSERT INTO Rolle VALUES(13, "Peter")')
    c.execute('INSERT INTO Rolle VALUES(14, "Baard Bratte")')
    c.execute('INSERT INTO Rolle VALUES(15, "Troender")')

 
    #Roller - Stoest av alt er kjaerligheten - (rollene er de samme som skuespillerne)
    c.execute('INSERT INTO Rolle VALUES(16, "Sunniva Du Mond Nordal")')
    c.execute('INSERT INTO Rolle VALUES(17, "Jo Saberniak")')
    c.execute('INSERT INTO Rolle VALUES(18, "Marte M. Steinholt")')
    c.execute('INSERT INTO Rolle VALUES(19, "Tor Ivar Hagen")')
    c.execute('INSERT INTO Rolle VALUES(20, "Trond-Ove Skroedal")')
    c.execute('INSERT INTO Rolle VALUES(21, "Natalie Groendahl Tangen")')
    c.execute('INSERT INTO Rolle VALUES(22, "Aasmund Flaten")')

    #Skuespillere - hvem som spiller hvilke roller
    c.execute('INSERT INTO Skuespillere(AnsattID, RolleID) VALUES(17,1)')
    c.execute('INSERT INTO Skuespillere VALUES(27,2)')
    c.execute('INSERT INTO Skuespillere VALUES(27,3)')
    c.execute('INSERT INTO Skuespillere VALUES(22,4)')
    c.execute('INSERT INTO Skuespillere VALUES(22,5)')
    c.execute('INSERT INTO Skuespillere VALUES(19,6)')
    c.execute('INSERT INTO Skuespillere VALUES(18,7)')
    c.execute('INSERT INTO Skuespillere VALUES(25,8)')
    c.execute('INSERT INTO Skuespillere VALUES(20,9)')
    c.execute('INSERT INTO Skuespillere VALUES(24,10)')
    c.execute('INSERT INTO Skuespillere VALUES(21,11)')
    c.execute('INSERT INTO Skuespillere VALUES(23,12)')
    c.execute('INSERT INTO Skuespillere VALUES(28,13)')
    c.execute('INSERT INTO Skuespillere VALUES(26,14)')
    c.execute('INSERT INTO Skuespillere VALUES(25,15)')
    c.execute('INSERT INTO Skuespillere VALUES(26,15)')

    c.execute('INSERT INTO Skuespillere VALUES(10,16)')
    c.execute('INSERT INTO Skuespillere VALUES(11,17)')
    c.execute('INSERT INTO Skuespillere VALUES(12,18)')
    c.execute('INSERT INTO Skuespillere VALUES(13,19)')
    c.execute('INSERT INTO Skuespillere VALUES(14,20)')
    c.execute('INSERT INTO Skuespillere VALUES(15,21)')
    c.execute('INSERT INTO Skuespillere VALUES(16,22)')

    #Akter - I SQL er har Akt tabellen at Navn er TEXT NOT NULL, men Akter KAN ha et navn (valg), saa dette maa endres
    c.execute('INSERT INTO Akt(AktNr, Navn, StykkeID) VALUES(1, NULL, 1)')
    c.execute('INSERT INTO Akt(AktNr, Navn, StykkeID) VALUES(2, NULL, 1)')
    c.execute('INSERT INTO Akt(AktNr, Navn, StykkeID) VALUES(3, NULL, 1)')
    c.execute('INSERT INTO Akt(AktNr, Navn, StykkeID) VALUES(4, NULL, 1)')
    c.execute('INSERT INTO Akt(AktNr, Navn, StykkeID) VALUES(5, NULL, 1)')

    c.execute('INSERT INTO Akt(AktNr, Navn, StykkeID) VALUES(1, NULL, 2)')
    
    
    #RolleIAkt
    # c.execute('INSERT INTO RolleIAkt(StykkeID, AktNr, RolleID) VALUES(1,1)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,1,1)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,1,2)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,1,4)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,1,6)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,1,7)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,1,8)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,1,9)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,1,10)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,1,11)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,1,12)')

    c.execute('INSERT INTO RolleIAkt VALUES(1,2,1)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,2,2)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,2,4)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,2,6)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,2,8)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,2,10)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,2,11)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,2,12)')

    c.execute('INSERT INTO RolleIAkt VALUES(1,3,1)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,3,2)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,3,6)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,3,7)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,3,8)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,3,10)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,3,11)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,3,12)')

    c.execute('INSERT INTO RolleIAkt VALUES(1,4,1)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,4,2)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,4,3)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,4,5)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,4,6)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,4,8)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,4,10)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,4,11)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,4,13)')

    c.execute('INSERT INTO RolleIAkt VALUES(1,5,1)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,5,2)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,5,4)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,5,6)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,5,8)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,5,11)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,5,10)')
    # c.execute('INSERT INTO RolleIAkt VALUES(1,5,11)')
    c.execute('INSERT INTO RolleIAkt VALUES(1,5,13)')

    c.execute('INSERT INTO RolleIAkt VALUES(2,1,16)')
    c.execute('INSERT INTO RolleIAkt VALUES(2,1,17)')
    c.execute('INSERT INTO RolleIAkt VALUES(2,1,18)')
    c.execute('INSERT INTO RolleIAkt VALUES(2,1,19)')
    c.execute('INSERT INTO RolleIAkt VALUES(2,1,20)')
    c.execute('INSERT INTO RolleIAkt VALUES(2,1,21)')
    c.execute('INSERT INTO RolleIAkt VALUES(2,1,22)')




    #Kundegruppe
    c.execute('INSERT INTO Kundegruppe(KundegruppeID) VALUES("O")')
    c.execute('INSERT INTO Kundegruppe(KundegruppeID) VALUES("H")')
    c.execute('INSERT INTO Kundegruppe(KundegruppeID) VALUES("S")')
    c.execute('INSERT INTO Kundegruppe(KundegruppeID) VALUES("G")')
    c.execute('INSERT INTO Kundegruppe(KundegruppeID) VALUES("GH")')

    #TypeBillett - Stoerst av alt er kjaerligheten 
    c.execute('INSERT INTO TypeBillett(KundegruppeID, StykkeID, Pris) VALUES("O",2, 350)')
    c.execute('INSERT INTO TypeBillett VALUES("H",2, 300)')
    c.execute('INSERT INTO TypeBillett VALUES("S",2, 220)')
    c.execute('INSERT INTO TypeBillett VALUES("G",2, 320)')
    c.execute('INSERT INTO TypeBillett VALUES("GH",2, 270)')

    #TypeBillett - Kongsemnene
    c.execute('INSERT INTO TypeBillett VALUES("O", 1, 450)')
    c.execute('INSERT INTO TypeBillett VALUES("H", 1, 380)')
    c.execute('INSERT INTO TypeBillett VALUES("S", 1, 280)')
    c.execute('INSERT INTO TypeBillett VALUES("G", 1, 420)')
    c.execute('INSERT INTO TypeBillett VALUES("GH", 1, 360)')

    #Standardkunden til brukerhistorie 2 og 3, Billettkjøp, Billett, Kundegruppe, Typebillett - Må vel ha
    c.execute('INSERT INTO Kunde(KundeNr, TelefonNr, Navn, Adresse) VALUES(1, 94978082, "Stian Standard","Standarsvingen 13") ')

    #Stoler (ingenting om de er solgt eller ikke)

    def getAreaWithRow(file): #generell hent info fra txt funksjon
        f = open(file,"r")
        data = f.read()
        result = {}
        area = None

        for line in data.splitlines():

            if line.startswith("Dato"): #Finner ut om det er dato linje
                continue

            if not (line.startswith("0") or line.startswith("1")): #Finner ut om det er en stol eller ikke
                area = line
                result[area] = []
                continue

            result[area].insert(0, line)


        f.close()
        return result

     


#Henter fra hovedscene
    resultH = getAreaWithRow("txtFiles/hovedscenen.txt")
    mainStageArea = ["Parkett", "Galleri"]
    countH = 1
    for area in mainStageArea:
        lines = resultH[area]
        for rowN, line in enumerate(lines, 1):
            for seat in line:
                if seat != "x":
                    c.execute('INSERT INTO Stol(StolNr, RadNr, Omrade, SalID) VALUES(:StolNr, :RadNr, :Omrade, 1)', {"StolNr": countH, "RadNr": rowN, "Omrade": area})
                countH += 1

    
    #Henter fra gamle-scenen
    resultG = getAreaWithRow("txtFiles/gamle-scene.txt")
    for area, lines in resultG.items():
        for rowN, line in enumerate(lines, 1):
            count = 1
            for seat in line:
                if seat != "x":
                    c.execute('INSERT INTO Stol(StolNr, RadNr, Omrade, SalID) VALUES(:StolNr, :RadNr, :Omrade, 2)', {"StolNr": count, "RadNr": rowN, "Omrade": area})
                count += 1

    con.commit()
    print("Database setup completed successfully.")

finally:
    con.close()
    print("Closed connection successfully")
   
    

