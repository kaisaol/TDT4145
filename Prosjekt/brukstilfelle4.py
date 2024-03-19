# def forestillingerPaaDato(dato): #brukstilfelle 4
#     c.execute(forestillingerPaaDatoQuery, (dato,))
#     performances = c.fetchall()
    
#     return performances

# if __name__ == "__main__":
#     date_input = input("Sett inn dato på formatet (YYYY-MM-DD): ")
#     try:
#         datetime.strptime(date_input, "%Y-%m-%d")
#         performances = forestillingerPaaDato(date_input)
#         for performance in performances:
#             print(f"Tid: {performance[0]}, Stykke: {performance[1]}, Solgte billetter: {performance[2]}")
#     except ValueError:
#         print("Ugyldig dato-format. Vennligst bruk YYYY-MM-DD.")
#     #her må jeg legge inn del to med antall solgte billetter!!!
