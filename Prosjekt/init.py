import sqlite3
import os

os.remove("teater.db")

con = sqlite3.connect("teater.db") #kobler til database 
c = con.cursor()

#Oppretter tabeller

try: 
    # c.execute('''CREATE TABLE Kunde(
    #     KundeNr INTEGER NOT NULL,
    #     TelefonNr INTEGER NOT NULL,
    #     Navn TEXT NOT NULL,
    #     Adresse TEXT NOT NULL,
    #     PRIMARY KEY (KundeNr)
    # )''')

    # c.execute('''CREATE TABLE BilettKjop (
    #     ReferanseNr INTEGER NOT NULL UNIQUE,
    #     Tidspunkt DATETIME NOT NULL,
	#     KundeNr INTEGER NOT NULL,
    #     PRIMARY KEY (ReferanseNr),
    #     FOREIGN KEY (KundeNr) REFERENCES Kunde (KundeNr) ON DELETE CASCADE ON UPDATE NO ACTION
    # )''')

    # c.execute('''CREATE TABLE Billett (
    #     BillettID INTEGER NOT NULL UNIQUE,
    #     ReferanseNr INTEGER NOT NULL,
    #     StolNr INTEGER NOT NULL,
    #     RadNr INTEGER NOT NULL,
    #     Omrade TEXT NOT NULL,
    #     SalID INTEGER NOT NULL,
    #     PRIMARY KEY (BillettID),
    #     FOREIGN KEY (ReferanseNr) REFERENCES BilettKjop (ReferanseNr)ON DELETE CASCADE ON UPDATE NO ACTION,
    #     FOREIGN KEY (StolNr, RadNr, Omrade) REFERENCES Stol (StolNr, RadNr, Omrade) ON DELETE CASCADE ON UPDATE NO ACTION,
    #     FOREIGN KEY (SalID) REFERENCES Teatersal (SalID) ON DELETE CASCADE ON UPDATE NO ACTION
    # )''')

    # c.execute('''CREATE TABLE Kundegruppe(
    #     KundegruppeID TEXT NOT NULL UNIQUE,
    #     PRIMARY KEY (KundegruppeID)
    # )''')

    # c.execute('''CREATE TABLE Stol (
    #     StolNr INTEGER NOT NULL,
    #     RadNr INTEGER NOT NULL,
    #     Omrade TEXT NOT NULL,
    #     SalID INTEGER NOT NULL,
    #     PRIMARY KEY (StolNr, RadNr, Omrade, SalID),
    #     FOREIGN KEY (SalID) REFERENCES Teatersal (SalID) ON DELETE CASCADE ON UPDATE NO ACTION
    # )''')

    # c.execute('''CREATE TABLE Teatersal(
    #     SalID INTEGER NOT NULL UNIQUE,
    #     Navn TEXT NOT NULL,
    #     Kapasitet INTEGER NOT NULL,
    #     TeaterID INTEGER NOT NULL,
    #     PRIMARY KEY (SalID),
    #     FOREIGN KEY (TeaterID) REFERENCES Teater (TeaterID) ON DELETE CASCADE ON UPDATE NO ACTION
    # )''')

    # c.execute('''CREATE TABLE Teater(
    #     TeaterID INTEGER NOT NULL UNIQUE,
    #     Navn TEXT NOT NULL,
    #     AnsattID INTEGER NOT NULL,
    #     PRIMARY KEY (TeaterID),
    #     FOREIGN KEY (AnsattID) REFERENCES Ansatt (AnsattID) ON DELETE CASCADE
    #     ON UPDATE NO ACTION
    # )''')

    # c.execute('''
    # )''')

    # c.execute('''CREATE TABLE Ansatt(
    #     AnsattID INTEGER NOT NULL UNIQUE,
    #     Navn TEXT NOT NULL,
    #     TelefonNr INTEGER,
    #     Epost TEXT,
    #     Jobbstatus TEXT NOT NULL,
    #     Stillingstittel TEXT NOT NULL,
    #     PRIMARY KEY (AnsattID)
    # )''')

    # c.execute('''CREATE TABLE Forestilling(
    #     Tidspunkt DATETIME NOT NULL,
    #     SalID INTEGER NOT NULL,
    #     StykkeID INTEGER NOT NULL,
    #     PRIMARY KEY (Tidspunkt, SalID, StykkeID),
    #     FOREIGN KEY (SalID) REFERENCES Teatersal (SalID) ON DELETE CASCADE ON UPDATE NO ACTION,
    #     FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON DELETE CASCADE ON UPDATE NO ACTION
    # )''')

    # c.execute('''CREATE TABLE Teaterstykke(
    #     StykkeID INTEGER NOT NULL,
    #     Navn TEXT NOT NULL,
    #     StartDato DATE NOT NULL,
    #     PRIMARY KEY (StykkeID),
    #     FOREIGN KEY (StartDato) REFERENCES Sesong (StartDato) ON DELETE CASCADE ON UPDATE NO ACTION
    # )''')

    # c.execute('''CREATE TABLE Rolle(
    #     RolleID INTEGER NOT NULL,
    #     Rollenavn TEXT NOT NULL,
    #     PRIMARY KEY (RolleID)
    # )''')
    
    # c.execute('''CREATE TABLE Sesong(
    #     StartDato DATE NOT NULL,
    #     SluttDato DATE NOT NULL,
    #     TeaterID INTEGER NOT NULL,
    #     PRIMARY KEY (StartDato, TeaterID),
    #     FOREIGN KEY (TeaterID)  REFERENCES Teater (TeaterID) ON DELETE CASCADE ON UPDATE NO ACTION
    # )''')
    
    # c.execute('''CREATE TABLE Oppgave(
    #     OppgaveID INTEGER NOT NULL,
    #     Beskrivelse TEXT NOT NULL,
    #     PRIMARY KEY (OppgaveID)
    # )''')
    
    # c.execute('''CREATE TABLE TeaterOppgave(
    #     StykkeID INTEGER NOT NULL,
    #     OppgaveID INTEGER NOT NULL,
    #     PRIMARY KEY (StykkeID, OppgaveID),
    #     FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON DELETE CASCADE ON UPDATE NO ACTION,
    #     FOREIGN KEY (OppgaveID) REFERENCES Oppgave (OppgaveID) ON DELETE CASCADE ON UPDATE NO ACTION
    # )''')

    # c.execute('''CREATE TABLE DelegerteOppgaver(
    #    OppgaveID INTEGER NOT NULL,
    #     AnsattID INTEGER NOT NULL,
    #     PRIMARY KEY (OppgaveID, AnsattID),
    #     FOREIGN KEY (OppgaveID) REFERENCES Oppgave (OppgaveID) ON DELETE CASCADE ON UPDATE NO ACTION,
    #     FOREIGN KEY (AnsattID) REFERENCES Ansatt (AnsattID) ON DELETE CASCADE ON UPDATE NO ACTION
    # )''')

    # c.execute('''CREATE TABLE Skuespillere (
    #     AnsattID INTEGER NOT NULL,
    #     RolleID INTEGER NOT NULL,
    #     PRIMARY KEY (AnsattID, RolleID),
    #     FOREIGN KEY (AnsattID) REFERENCES Ansatt (AnsattID) ON DELETE CASCADE ON UPDATE NO ACTION,
    #     FOREIGN KEY (RolleID) REFERENCES Rolle (RolleID) ON DELETE CASCADE ON UPDATE NO ACTION
    #     )''')
        
        
    # c.execute('''CREATE TABLE RolleAkt(
    #     StykkeID INTEGER NOT NULL,
    #     AktNr INTEGER NOT NULL,
    #     RolleID INTEGER NOT NULL,
    #     PRIMARY KEY (StykkeID, AktNr, RolleID),
    #     FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON DELETE CASCADE ON UPDATE NO ACTION,
    #     FOREIGN KEY (AktNr) REFERENCES Akt (AktNr) ON DELETE CASCADE ON UPDATE NO ACTION,
    #     FOREIGN KEY (RolleID) REFERENCES Rolle (RolleID) ON DELETE CASCADE ON UPDATE NO ACTION
    #     )''')

    
    # c.execute('''CREATE TABLE TypeBillett(
    #     KundegruppeID TEXT NOT NULL,
    #     StykkeID INTEGER NOT NULL,
    #     Pris FLOAT NOT NULL,
    #     PRIMARY KEY (KundegruppeID, StykkeID),
    #     FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON DELETE CASCADE ON UPDATE NO ACTION,
    #     FOREIGN KEY (KundegruppeID) REFERENCES BillettType (KundegruppeID) ON DELETE CASCADE ON UPDATE NO ACTION
    #     )''')
    

    with open("teater.sql", "r") as fp:
        sql = fp.read()
    
    c.executescript(sql)











    #INNSETTING AV VERDIER

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










    #stoler (ingenting om de er solgt eller ikke)
    f = open("txtFiles/hovedscenen.txt","r")
    while True: 
        area = ""
        line = f.readline()
        next(f) #hopper over første linje som er en dato
        n = 524
        for i, line in enumerate(f):
            if i == 1: #linjen om galeri
                area = line
            if i > 1 and i < 6:
                c.execute('INSERT INTO Stol()')
                
                
            
        if not line:
            break 
    f.close()
    
    f = open("txtFiles/gamle-scene.txt","r")
    f.close()

    print("Databasen er opprettet")
except FileNotFoundError:
    print("Databasen eksisterer allerede")

con.close()