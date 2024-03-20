
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
            Forestilling f
        JOIN 
            Teaterstykke ts ON f.StykkeID = ts.StykkeID
        LEFT JOIN 
            Billett b ON f.SalID = b.SalID AND DATE(f.Tidspunkt) = DATE(b.Tidspunkt)
        WHERE 
            DATE(f.Tidspunkt) = ?
        GROUP BY 
            f.Tidspunkt, ts.Navn
        ORDER BY 
            SoldTickets DESC
    """
forestillingerRangertQuery = """
 SELECT
            ts.Navn AS "Forestilling",
            f.Tidspunkt AS "Dato",
            COUNT(DISTINCT b.BillettID) AS "Antall Solgte Plasser"
        FROM
            Forestilling f
        JOIN 
            Teaterstykke ts ON f.StykkeID = ts.StykkeID
        LEFT JOIN 
            Billett b ON f.SalID = b.SalID AND DATE(f.Tidspunkt) = DATE(b.Tidspunkt)
        GROUP BY 
            f.Tidspunkt, ts.Navn
        ORDER BY 
            COUNT(DISTINCT b.BillettID) DESC
"""


skuespillereISammeAktQuery = """
 SELECT DISTINCT
    a1.Navn AS Skuespiller1,
    a2.Navn AS Skuespiller2,
    ts.Navn AS Teaterstykke
FROM Skuespillere s1
INNER JOIN Ansatt a1 ON s1.AnsattID = a1.AnsattID
INNER JOIN RolleIAkt ria1 ON s1.RolleID = ria1.RolleID
INNER JOIN Akt a ON ria1.AktNr = a.AktNr AND ria1.StykkeID = a.StykkeID
INNER JOIN Teaterstykke ts ON a.StykkeID = ts.StykkeID
INNER JOIN RolleIAkt ria2 ON a.AktNr = ria2.AktNr AND ts.StykkeID = ria2.StykkeID
INNER JOIN Skuespillere s2 ON ria2.RolleID = s2.RolleID AND s1.AnsattID != s2.AnsattID
INNER JOIN Ansatt a2 ON s2.AnsattID = a2.AnsattID
WHERE a1.Navn = ?
ORDER BY ts.Navn, a1.Navn, a2.Navn;

"""