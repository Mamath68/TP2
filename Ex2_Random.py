from random import randint

valeur_recherche = randint(0, 100)

nb_tentative = 0

while True:
    valeur_propose = int(input("Devinez la valeur (entre 0 et 100) : "))
    nb_tentative += 1
    if valeur_propose == valeur_recherche:
        print(f"Bravo ! Vous avez deviné la valeur en {nb_tentative} tentatives.")
        break
    elif valeur_propose < valeur_recherche:
        print("Le nombre recherché est plus grande.")
    else:
        print("Le nombre recherché est plus petite.")
