import sqlite3

con = sqlite3.connect("teater.db") #kobler til database 
c = con.cursor()

#Oppretter tabeller

try: 
    c.execute('''CREATE TABLE Kunde(
        KundeNr INTEGER PRIMARY KEY NOT NULL UNIQUE,
        TelefonNr INTEGER NOT NULL,
        Navn TEXT NOT NULL,
        Adresse TEXT NOT NULL,
        PRIMARY KEY (KundeNr)
    )''')

    c.execute('''CREATE TABLE BilettKjop (
        ReferanseNr INTEGER NOT NULL UNIQUE,
        Tidspunkt DATETIME NOT NULL,
	    KundeNr INTEGER NOT NULL,
        PRIMARY KEY (ReferanseNr),
        FOREIGN KEY (KundeNr) REFERENCES Kunde (KundeNr) ON DELETE CASCADE ON UPDATE NO ACTION
    )''')

    c.execute('''CREATE TABLE Billett (
        BillettID INTEGER NOT NULL UNIQUE,
        ReferanseNr INTEGER NOT NULL,
        StolNr INTEGER NOT NULL,
        RadNr INTEGER NOT NULL,
        Omrade TEXT NOT NULL,
        SalID INTEGER NOT NULL,
        PRIMARY KEY (BillettID),
        FOREIGN KEY (ReferanseNr) REFERENCES BilettKjop (ReferanseNr)ON DELETE CASCADE ON UPDATE NO ACTION,
        FOREIGN KEY (StolNr, RadNr, Omrade) REFERENCES Stol (StolNr, RadNr, Omrade) ON DELETE CASCADE ON UPDATE NO ACTION,
        FOREIGN KEY (SalID) REFERENCES Teatersal (SalID) ON DELETE CASCADE ON UPDATE NO ACTION
    )''')

    c.execute('''CREATE TABLE Kundegruppe(
        KundegruppeID TEXT NOT NUL UNIQUE,
        PRIMARY KEY (KundegruppeID)
    )''')

    c.execute('''CREATE TABLE Stol (
        StolNr INTEGER NOT NULL,
        RadNr INTEGER NOT NULL,
        Omrade TEXT NOT NULL,
        SalID INTEGER NOT NULL,
        PRIMARY KEY (StolNr, RadNr, Omrade, SalID),
        FOREIGN KEY (SalID) REFERENCES Teatersal (SalID) ON DELETE CASCADE ON UPDATE NO ACTION
    )''')

    c.execute('''CREATE TABLE Teatersal(
        SalID INTEGER NOT NULL UNIQUE,
        Navn TEXT NOT NULL,
        Kapasitet INTEGER NOT NULL,
        TeaterID INTEGER NOT NULL,
        PRIMARY KEY (SalID),
        FOREIGN KEY (TeaterID) REFERENCES Teater (TeaterID) ON DELETE CASCADE ON UPDATE NO ACTION
    )''')

    c.execute('''CREATE TABLE Teater(
        TeaterID INTEGER NOT NULL UNIQUE,
        Navn TEXT NOT NULL,
        AnsattID INTEGER NOT NULL,
        PRIMARY KEY (TeaterID),
        FOREIGN KEY (AnsattID) REFERENCES Ansatt (AnsattID) ON DELETE CASCADE
        ON UPDATE NO ACTION
    )''')

    c.execute('''CREATE TABLE Ansatt(
        AnsattID INTEGER NOT NULL UNIQUE,
        Navn TEXT NOT NULL,
        TelefonNr INTEGER,
        Epost TEXT,
        Jobbstatus TEXT NOT NULL,
        Stillingstittel TEXT NOT NULL,
        PRIMARY KEY (AnsattID)
    )''')

    c.execute('''CREATE TABLE Forestilling(
        Tidspunkt DATETIME NOT NULL,
        SalID INTEGER NOT NULL,
        StykkeID INTEGER NOT NULL,
        PRIMARY KEY (Tidspunkt, SalID, StykkeID),
        FOREIGN KEY (SalID) REFERENCES Teatersal (SalID) ON DELETE CASCADE ON UPDATE NO ACTION,
        FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON DELETE CASCADE ON UPDATE NO ACTION
    )''')

    c.execute('''CREATE TABLE Teaterstykke(
        StykkeID INTEGER NOT NULL,
        Navn TEXT NOT NULL,
        StartDato DATE NOT NULL,
        PRIMARY KEY (StykkeID),
        FOREIGN KEY (StartDato) REFERENCES Sesong (StartDato) ON DELETE CASCADE ON UPDATE NO ACTION
    )''')

    c.execute('''CREATE TABLE Rolle(
        RolleID INTEGER NOT NULL,
        Rollenavn TEXT NOT NULL,
        PRIMARY KEY (RolleID)
    )''')
    
    c.execute('''CREATE TABLE Sesong(
        StartDato DATE NOT NULL,
        SluttDato DATE NOT NULL,
        TeaterID INTEGER NOT NULL,
        PRIMARY KEY (StartDato, TeaterID),
        FOREIGN KEY (TeaterID)  REFERENCES Teater (TeaterID) ON DELETE CASCADE ON UPDATE NO ACTION
    )''')
    
    c.execute('''CREATE TABLE Oppgave(
        OppgaveID INTEGER NOT NULL,
        Beskrivelse TEXT NOT NULL,
        PRIMARY KEY (OppgaveID)
    )''')
    
    c.execute('''CREATE TABLE TeaterOppgave(
        tykkeID INTEGER NOT NULL,
        OppgaveID INTEGER NOT NULL,
        PRIMARY KEY (StykkeID, OppgaveID),
        FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON DELETE CASCADE ON UPDATE NO ACTION,
        FOREIGN KEY (OppgaveID) REFERENCES Oppgave (OppgaveID) ON DELETE CASCADE ON UPDATE NO ACTION
    )''')

    c.execute('''CREATE TABLE DelegerteOppgaver(
       OppgaveID INTEGER NOT NULL,
        AnsattID INTEGER NOT NULL,
        PRIMARY KEY (OppgaveID, AnsattID),
        FOREIGN KEY (OppgaveID) REFERENCES Oppgave (OppgaveID) ON DELETE CASCADE ON UPDATE NO ACTION,
        FOREIGN KEY (AnsattID) REFERENCES Ansatt (AnsattID) ON DELETE CASCADE ON UPDATE NO ACTION
    )''')

    c.execute('''CREATE TABLE Skuespillere (
        AnsattID INTEGER NOT NULL,
        RolleID INTEGER NOT NULL,
        PRIMARY KEY (AnsattID, RolleID),
        FOREIGN KEY (AnsattID) REFERENCES Ansatt (AnsattID) ON DELETE CASCADE ON UPDATE NO ACTION,
        FOREIGN KEY (RolleID) REFERENCES Rolle (RolleID) ON DELETE CASCADE ON UPDATE NO ACTION
        )''')
        
        
    c.execute('''CREATE TABLE RolleAkt(
        StykkeID INTEGER NOT NULL,
        AktNr INTEGER NOT NULL,
        RolleID INTEGER NOT NULL,
        PRIMARY KEY (StykkeID, AktNr, RolleID),
        FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON DELETE CASCADE ON UPDATE NO ACTION,
        FOREIGN KEY (AktNr) REFERENCES Akt (AktNr) ON DELETE CASCADE ON UPDATE NO ACTION,
        FOREIGN KEY (RolleID) REFERENCES Rolle (RolleID) ON DELETE CASCADE ON UPDATE NO ACTION
        )''')

    
    c.execute('''CREATE TABLE TypeBillett(
        KundegruppeID TEXT NOT NULL,
        StykkeID INTEGER NOT NULL,
        Pris FLOAT NOT NULL,
        PRIMARY KEY (KundegruppeID, StykkeID),
        FOREIGN KEY (StykkeID) REFERENCES Teaterstykke (StykkeID) ON DELETE CASCADE ON UPDATE NO ACTION,
        FOREIGN KEY (KundegruppeID) REFERENCES BillettType (KundegruppeID) ON DELETE CASCADE ON UPDATE NO ACTION
        )''')
    













    #Innsetting av verdier

    #Teater
    c.execute('INSERT INTO Teater(TeaterID, Navn, AnsattID) VALUES(1, "Troendelag teater", 28)')

    #Saler
    c.execute('INSERT INTO Teatersal(SalID,Navn,Kapasitet,TeaterID) VALUES(1, "Hovedscenen", 524, 1)')
    c.execute('INSERT INTO Teatersal VALUES(2, "Gamle Scene", 332, 1)')

    #Teaterstykker

    #ANSATTE
    #TelefonNr og Epost var ikke tilgjengelig for mange av de ansatte, saa SQL maa endres. Bruker NULL
    #Da jobbstatus ikke var tilgjengelig for alle, la vi til grunn at de er fast ansatte for enkeltshetens skyld. Dette er også trivielt for aa loese oppgaven, så vi vektla det ikke så mye.

    #Direktøren - for at opprettelsen at teater med fremmednøkkel AnsattID mot direktør skal bli mest riktig
    c.execute('Insert INOT Ansatt VALUES (28, "Elisabeth Hansen", NULL, NULL, "Fast", "Direktoer")')

    #Kunstnerisk lag - "Kongsemnene"
    c.execute('INSERT INTO Ansatt(AnsattID, Navn, TelefonNr, Epost, Jobbstatus, Stillingstittel) VALUES(1, "Yury Butusoc", NULL, NULL, "Fast", "Regissoer")')
    c.execute('INSERT INTO Ansatt VALUES (2,"Aleksandr Shishkin Hokusai", NULL, NULL, "Fast", "Scenograf")')
    c.execute('INSERT INTO Ansatt VALUES (3, "Eivind Myren, NULL, NULL, "Fast", "Lysdesigner")')
    c.execute('INSERT INTO Ansatt VALUES (4, "Mina Rype Stokke", NULL, NULL, "Fast","Dramaturg")')
    #Kunsterisk lag - "Stoerst av alt er kjaerligheten"
    c.execute('INSERT INTO Ansatt VALUES(5, "Jonas Corell Petersen", NULL, NULL, "Innleid", "Reggisoer")')
    c.execute('INSERT INTO Ansatt VALUES(6, "David Gehrt, NULL, NULL "Innleid, "Scenograf")')
    c.execute('INSERT INTO Ansatt VALUES(7, "Gaute Toender", NULL, NULL, "Fast", "Lyddesigner")')
    c.execute('INSERT INTO Ansatt VALUES(8, "Magnus Mikaelsen", NULL, NULL, "Fast", "Lysdesigner")')
    c.execute('INSERT INTO Ansatt VALUES(9, "Kristoffer Spender", NULL, NULL, "Innleid", "Dramaturg")')


    #"Stoerst av alt er kjaerligheten" - Disse spiller seg selv (til når fylle inn roller)
    c.execute('INSERT INTO Ansatt VALUES(10, "Sunniva Du Mond Nordal", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(11, "Jo Saberniak", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(12), "Marte M. Steinholt", NULL, NULL, "Fast", "Skuespiller"')
    c.execute('INSERT INTO Ansatt VALUES(13), "Tor Ivar Hagen", NULL, NULL, "Fast", "Skuespiller"')
    c.execute('INSERT INTO Ansatt VALUES(14), "Trond-Ove Skrødal, NULL, NULL, "Fast", "Skuespiller""')
    c.execute('INSERT INTO Ansatt VALUES(15), "Natalie Grøndahl Tangen", NULL, NULL, "Fast", "Skuespiller"')
    c.execute('INSERT INTO Ansatt VALUES(16), "Åsmund Flaten", NULL, NULL, "Fast", "Skuespiller"')

    #"Kongsemnene"
    c.execute('INSERT INTO Ansatt VALUES(17, "Arturo Scotti", NULL, NULL, "Fast", "Skuespiller")')
    c.execute('INSERT INTO Ansatt VALUES(18), "Ingunn Beate Strige Øyen", NULL, NULL, "Fast", "Skuespiller"')
    c.execute('INSERT INTO Ansatt VALUES(19), "Hans Petter Nilsen", NULL, NULL, "Fast", "Skuespiller"')
    c.execute('INSERT INTO Ansatt VALUES(20), "Madeleine Brandtzæg Nilsen", NULL, NULL, "Fast", "Skuespiller"')
    c.execute('INSERT INTO Ansatt VALUES(21), "Synnøve Fossum Eriksen", NULL, NULL, "Fast", "Skuespiller"')
    c.execute('INSERT INTO Ansatt VALUES(22), "Emma Caroline Deichmann", NULL, NULL, "Fast", "Skuespiller"')
    c.execute('INSERT INTO Ansatt VALUES(23), "Thomas Jensen Takyi",NULL, NULL, "Fast", "Skuespiller"')
    c.execute('INSERT INTO Ansatt VALUES(24), "Per Bogstad Gulliksen",NULL, NULL, "Fast", "Skuespiller"')
    c.execute('INSERT INTO Ansatt VALUES(25), "Isak Holmen Sørensen",NULL, NULL, "Fast", "Skuespiller"')
    c.execute('INSERT INTO Ansatt VALUES(26), "Fabian Heidelberg Lunde",NULL, NULL, "Fast", "Skuespiller"')
    c.execute('INSERT INTO Ansatt VALUES(27), "Emil Olafsson", NULL, NULL, "Fast", "Skuespiller"')
    c.execute('INSERT INTO Ansatt VALUES(27), "Snorre Ryen Tøndel", NULL, NULL, "Fast", "Skuespiller"')

    #Akter


    #Roller


    #Skuespillere - hvem som spiller hvilke roller







    #Roller

    #Ak

except:
    print("Databasen eksisterer allerede")

con.close()