def factorielle_for(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
        print(f"i = {i}, factorielle = {resultat}")
    return resultat


def factorielle_while(n):
    resultat = 1
    i = 1
    while i <= n:
        resultat *= i
        print(f"i = {i}, factorielle = {resultat}")
        i += 1
    return resultat


choix = input("Choisissez le type de boucle (for/while) : ").strip().lower()

n = int(input("Entrez un nombre entier positif : "))

if choix == "for":
    factorielle = factorielle_for(n)
elif choix == "while":
    factorielle = factorielle_while(n)
else:
    print("Choix invalide. Veuillez choisir 'for' ou 'while'.")

print(f"La factorielle de {n} est {factorielle}.")
