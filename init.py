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
        SalID INTEGER NOT NULL,
        Navn TEXT NOT NULL,
        Kapasitet INTEGER NOT NULL,
        TeaterID INTEGER NOT NULL,
        PRIMARY KEY (SalID),
        FOREIGN KEY (TeaterID) REFERENCES Teater (TeaterID) ON DELETE CASCADE ON UPDATE NO ACTION
    )''')

    c.execute('''CREATE TABLE Teater(
        TeaterID INTEGER NOT NULL,
        Navn TEXT NOT NULL,
        AnsattID INTEGER NOT NULL,
        PRIMARY KEY (TeaterID),
        FOREIGN KEY (AnsattID) REFERENCES Ansatt (AnsattID) ON DELETE CASCADE ON UPDATE NO ACTION
    )''')

    c.execute('''CREATE TABLE (

    )''')

    c.execute('''CREATE TABLE (

    )''')

    c.execute('''CREATE TABLE (

    )''')













#Innsetting av verdier

#Ansatte 
#TelefonNr og Epost var ikke tilgjengelig for mange av de ansatte, saa SQL maa endres. Bruker NULL
#Da jobbstatus ikke var tilgjengelig for alle, la vi til grunn at de er fast ansatte for enkeltshetens skyld. Dette er også trivielt for aa loese oppgaven, så vi vektla det ikke så mye.

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

#Skuespillere - "Stoerst av alt er kjaerligheten"
c.execute('INSERT INTO Ansatt VALUES(10, "Sunniva Du Mond Nordal", NULL, NULL, "Fast", "Skuespiller")')
c.execute('INSERT INTO Ansatt VALUES(11)')
c.execute('INSERT INTO Ansatt VALUES(12)')
c.execute('INSERT INTO Ansatt VALUES(13)')
c.execute('INSERT INTO Ansatt VALUES(14)')
c.execute('INSERT INTO Ansatt VALUES(15)')
c.execute('INSERT INTO Ansatt VALUES(16)')




#Skuespillere - "Kongsemnene"






#Roller

#Akt