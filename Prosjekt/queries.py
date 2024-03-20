
# antallSolgteBilletterPaDato = """
# SELECT Forestilling.Tidspunkt, Teaterstykke.Navn, COUNT(Billett.BillettID) AS AntallSolgteBilletter
# FROM Forestilling
# JOIN Teaterstykke ON Forestilling.StykkeID = Teaterstykke.StykkeID
# LEFT JOIN Billett ON Forestilling.SalID = Billett.SalID AND Forestilling.Tidspunkt = Billett.Tidspunkt
# GROUP BY Forestilling.Tidspunkt, Teaterstykke.Navn
# HAVING Forestilling.Tidspunkt = '2024-02-03';
# """
skuespillereIStykkerQuery = """
SELECT DISTINCT
    Teaterstykke.Navn AS "Teaterstykke",
    Ansatt.Navn AS "Skuespiller",
    Rolle.Rollenavn AS "Rolle"
FROM Skuespillere
JOIN Ansatt ON Skuespillere.AnsattID = Ansatt.AnsattID
JOIN Rolle ON Skuespillere.RolleID = Rolle.RolleID
JOIN RolleIAkt ON Rolle.RolleID = RolleIAkt.RolleID
JOIN Teaterstykke ON RolleIAkt.StykkeID = Teaterstykke.StykkeID
ORDER BY Teaterstykke.Navn, Ansatt.Navn, Rolle.Rollenavn;
"""
forestillingerPaaDatoQuery = """
 SELECT 
        f.Tidspunkt, 
        ts.Navn AS StykkeNavn, 
        COUNT(b.BillettID) AS SoldTickets
    FROM 
        Forestilling AS f
    JOIN 
        Teaterstykke AS ts ON f.StykkeID = ts.StykkeID
    LEFT JOIN 
        Billett AS b ON f.SalID = b.SalID
    WHERE 
        DATE(f.Tidspunkt) = ?
    GROUP BY 
        f.Tidspunkt, ts.Navn;
    """
forestillingerRangertQuery = """
SELECT
        Teaterstykke.Navn AS "Forestilling",
        Forestilling.Tidspunkt AS "Dato",
        COUNT(Billett.BillettID) AS "Antall Solgte Plasser"
    FROM
        Forestilling
    JOIN Teaterstykke ON Forestilling.StykkeID = Teaterstykke.StykkeID
    LEFT JOIN BilettKjop ON Forestilling.Tidspunkt = BilettKjop.Tidspunkt
    LEFT JOIN Billett ON BilettKjop.ReferanseNr = Billett.ReferanseNr
    GROUP BY Forestilling.Tidspunkt, Teaterstykke.Navn
    ORDER BY COUNT(Billett.BillettID) DESC;
"""


skuespillereISammeAktQuery = """
  SELECT DISTINCT
        a1.Navn AS Skuespiller1,
        a2.Navn AS Skuespiller2,
        t.Navn AS Teaterstykke
    FROM
        Skuespillere s1
    JOIN Skuespillere s2 ON s1.StykkeID = s2.StykkeID AND s1.AktNr = s2.AktNr AND s1.AnsattID != s2.AnsattID
    JOIN Ansatt a1 ON s1.AnsattID = a1.AnsattID
    JOIN Ansatt a2 ON s2.AnsattID = a2.AnsattID
    JOIN RolleIAkt r ON s1.StykkeID = r.StykkeID AND s1.AktNr = r.AktNr
    JOIN Teaterstykke t ON r.StykkeID = t.StykkeID
    WHERE a1.Navn = ?
    ORDER BY Teaterstykke, Skuespiller1, Skuespiller2;
"""

