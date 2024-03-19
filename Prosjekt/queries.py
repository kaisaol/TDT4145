
antallSolgteBilletterPaDato = """
SELECT Forestilling.Tidspunkt, Teaterstykke.Navn, COUNT(Billett.BillettID) AS AntallSolgteBilletter
FROM Forestilling
JOIN Teaterstykke ON Forestilling.StykkeID = Teaterstykke.StykkeID
LEFT JOIN Billett ON Forestilling.SalID = Billett.SalID AND Forestilling.Tidspunkt = Billett.Tidspunkt
GROUP BY Forestilling.Tidspunkt, Teaterstykke.Navn
HAVING Forestilling.Tidspunkt = '2024-02-03';
"""
skuespillereIStykker = """
SELECT Teaterstykke.Navn AS StykkeNavn, Ansatt.Navn AS SkuespillerNavn, Rolle.Rollenavn
FROM Skuespillere
JOIN Ansatt ON Skuespillere.AnsattID = Ansatt.AnsattID
JOIN Rolle ON Skuespillere.RolleID = Rolle.RolleID
JOIN Teaterstykke ON RolleIAkt.StykkeID = Teaterstykke.StykkeID
JOIN RolleIAkt ON Rolle.RolleID = RolleIAkt.RolleID;
"""
forestillingerPaaDatoQuery = """
    SELECT Forestilling.Tidspunkt, Teaterstykke.Navn, COUNT(Billett.BillettID) as SoldTickets
    FROM Forestilling
    JOIN Teaterstykke ON Forestilling.StykkeID = Teaterstykke.StykkeID
    LEFT JOIN BilettKjop ON BilettKjop.Tidspunkt = Forestilling.Tidspunkt
    LEFT JOIN Billett ON Billett.ReferanseNr = BilettKjop.ReferanseNr
    WHERE DATE(Forestilling.Tidspunkt) = ?
    GROUP BY Forestilling.Tidspunkt, Teaterstykke.Navn
    """
forestillingerSortertEtterSolgteBilletter = """
SELECT Forestilling.Tidspunkt, Teaterstykke.Navn, COUNT(Billett.BillettID) AS AntallSolgteBilletter
FROM Forestilling
JOIN Teaterstykke ON Forestilling.StykkeID = Teaterstykke.StykkeID
JOIN Billett ON Forestilling.SalID = Billett.SalID AND Forestilling.Tidspunkt = Billett.Tidspunkt
GROUP BY Forestilling.Tidspunkt, Teaterstykke.Navn
ORDER BY AntallSolgteBilletter DESC;
"""

skuespillereISammeAkt = """
SELECT DISTINCT a.Navn AS AktNavn, s.Navn AS SkuespillerNavn, t.Navn AS StykkeNavn
FROM Skuespillere AS sk
JOIN Ansatt AS a1 ON sk.AnsattID = a1.AnsattID
JOIN RolleIAkt ON sk.RolleID = RolleIAkt.RolleID
JOIN Akt AS a ON RolleIAkt.AktNr = a.AktNr AND RolleIAkt.StykkeID = a.StykkeID
JOIN Teaterstykke AS t ON a.StykkeID = t.StykkeID
JOIN Skuespillere AS sk2 ON a.AktNr = sk2.AnsattID AND a.StykkeID = sk2.RolleID
JOIN Ansatt AS s ON sk2.AnsattID = s.AnsattID
WHERE a1.Navn = '<Skuespillernavn>'
AND s.Navn != '<Skuespillernavn>';
"""

