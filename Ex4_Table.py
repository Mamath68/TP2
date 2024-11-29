def table_multiplication(nombre):
    table = []
    for i in range(0, 11):
        resultat = round(nombre * i, 1)
        table.append(resultat)
    return table


def afficher_table(table, nombre):
    for i, resultat in enumerate(table):
        print(f"{nombre} x {i} = {resultat}")


nombre = float(input("Entrez un nombre (entier ou reel) : "))

table = table_multiplication(nombre)
afficher_table(table, nombre)
