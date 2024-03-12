CREATE TABLE IF NOT EXISTS Kunde (
    KundeNr INTEGER NOT NULL,
    TelefonNr INTEGER NOT NULL,
    Navn TEXT NOT NULL,
    Adresse TEXT NOT NULL,
    PRIMARY KEY (KundeNr)
);
CREATE TABLE IF NOT EXISTS BilettKjop (
    ReferanseNr INTEGER NOT NULL,
    Tidspunkt DATETIME NOT NULL,
	KundeNr INTEGER NOT NULL,
    PRIMARY KEY (ReferanseNr),
    FOREIGN KEY (KundeNr)
        REFERENCES Kunde (KundeNr)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Billett (
    BillettID INTEGER NOT NULL,
    ReferanseNr INTEGER NOT NULL,
    StolNr INTEGER NOT NULL,
    RadNr INTEGER NOT NULL,
    Omrade TEXT NOT NULL,
    SalID INTEGER NOT NULL,
    PRIMARY KEY (BillettID),
    FOREIGN KEY (ReferanseNr)
        REFERENCES BilettKjop (ReferanseNr)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (StolNr, RadNr, Omrade)
        REFERENCES Stol (StolNr, RadNr, Omrade)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (SalID)
        REFERENCES Teatersal (SalID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Kundegruppe (
    KundegruppeID TEXT NOT NULL,
    PRIMARY KEY (KundegruppeID)
);

CREATE TABLE IF NOT EXISTS Stol (
    StolNr INTEGER NOT NULL,
    RadNr INTEGER NOT NULL,
    Omrade TEXT NOT NULL,
    SalID INTEGER NOT NULL,
    PRIMARY KEY (StolNr, RadNr, Omrade, SalID),
    FOREIGN KEY (SalID)
        REFERENCES Teatersal (SalID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);


CREATE TABLE IF NOT EXISTS Teatersal (
    SalID INTEGER NOT NULL,
    Navn TEXT NOT NULL,
    Kapasitet INTEGER NOT NULL,
    TeaterID INTEGER NOT NULL,
    PRIMARY KEY (SalID),
    FOREIGN KEY (TeaterID)
        REFERENCES Teater (TeaterID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Teater (
    TeaterID INTEGER NOT NULL,
    Navn TEXT NOT NULL,
    AnsattID INTEGER NOT NULL,
    PRIMARY KEY (TeaterID),
    FOREIGN KEY (AnsattID)
        REFERENCES  Ansatt (AnsattID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);

"Endret TelefonNr og Epost til aa kunne ha NULL-verdier, da dette ikke var tilgjeng"
CREATE TABLE IF NOT EXISTS Ansatt (
    AnsattID INTEGER NOT NULL,
    Navn TEXT NOT NULL,
    TelefonNr INTEGER,
    Epost TEXT,
    Jobbstatus TEXT NOT NULL,
    Stillingstittel TEXT NOT NULL,
    PRIMARY KEY (AnsattID)
);

CREATE TABLE IF NOT EXISTS Forestilling (
    Tidspunkt DATETIME NOT NULL,
    SalID INTEGER NOT NULL,
    StykkeID INTEGER NOT NULL,
    PRIMARY KEY (Tidspunkt, SalID, StykkeID),
    FOREIGN KEY (SalID)
        REFERENCES Teatersal (SalID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (StykkeID) 
        REFERENCES Teaterstykke (StykkeID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Teaterstykke (
    StykkeID INTEGER NOT NULL,
    Navn TEXT NOT NULL,
    StartDato DATE NOT NULL,
    PRIMARY KEY (StykkeID),
    FOREIGN KEY (StartDato)
        REFERENCES Sesong (StartDato)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Akt (
    AktNr INTEGER NOT NULL,
    Navn TEXT NOT NULL,
    StykkeID INTEGER NOT NULL,
    PRIMARY KEY (AktNr, StykkeID),
    FOREIGN KEY (StykkeID)
        REFERENCES Teaterstykke (StykkeID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Rolle (
    RolleID INTEGER NOT NULL,
    Rollenavn TEXT NOT NULL,
    PRIMARY KEY (RolleID)
);

CREATE TABLE IF NOT EXISTS Sesong (
    StartDato DATE NOT NULL,
    SluttDato DATE NOT NULL,
    TeaterID INTEGER NOT NULL,
    PRIMARY KEY (StartDato, TeaterID),
    FOREIGN KEY (TeaterID)
        REFERENCES Teater (TeaterID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Oppgave (
    OppgaveID INTEGER NOT NULL,
    Beskrivelse TEXT NOT NULL,
    PRIMARY KEY (OppgaveID)
);



CREATE TABLE IF NOT EXISTS TeaterOppgaver (
    StykkeID INTEGER NOT NULL,
    OppgaveID INTEGER NOT NULL,
    PRIMARY KEY (StykkeID, OppgaveID),
    FOREIGN KEY (StykkeID)
        REFERENCES Teaterstykke (StykkeID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (OppgaveID)
        REFERENCES Oppgave (OppgaveID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS DelegerteOppgaver (
    OppgaveID INTEGER NOT NULL,
    AnsattID INTEGER NOT NULL,
    PRIMARY KEY (OppgaveID, AnsattID),
    FOREIGN KEY (OppgaveID)
        REFERENCES Oppgave (OppgaveID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (AnsattID)
        REFERENCES Ansatt (AnsattID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS Skuespillere (
    AnsattID INTEGER NOT NULL,
    RolleID INTEGER NOT NULL,
    PRIMARY KEY (AnsattID, RolleID),
    FOREIGN KEY (AnsattID)
        REFERENCES Ansatt (AnsattID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (RolleID)
        REFERENCES Rolle (RolleID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS RolleIAkt (
    StykkeID INTEGER NOT NULL,
    AktNr INTEGER NOT NULL,
    RolleID INTEGER NOT NULL,
    PRIMARY KEY (StykkeID, AktNr, RolleID),
    FOREIGN KEY (StykkeID)
        REFERENCES Teaterstykke (StykkeID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (AktNr)
        REFERENCES Akt (AktNr)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (RolleID)
        REFERENCES Rolle (RolleID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS TypeBillett (
    KundegruppeID TEXT NOT NULL,
    StykkeID INTEGER NOT NULL,
    Pris FLOAT NOT NULL,
    PRIMARY KEY (KundegruppeID, StykkeID),
    FOREIGN KEY (StykkeID)
        REFERENCES Teaterstykke (StykkeID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION,
    FOREIGN KEY (KundegruppeID)
        REFERENCES BillettType (KundegruppeID)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);