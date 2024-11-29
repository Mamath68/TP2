# Déclarer une variable nMax représentant la taille maximale des vecteurs
nMax = 10

# Déclarer deux listes vides v1 et v2
v1 = []
v2 = []

# Demander à l'utilisateur d'entrer n, la taille effective des vecteurs
while True:
    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
    if 1 <= n <= nMax:
        break
    else:
        print(f"Veuillez entrer une valeur entre 1 et {nMax}.")

# Demander à l'utilisateur les composantes des vecteurs v1 et v2
print("Saisie du premier vecteur :")
for i in range(n):
    composante = int(input(f"v1[{i}] = "))
    v1.append(composante)

print("Saisie du second vecteur :")
for i in range(n):
    composante = int(input(f"v2[{i}] = "))
    v2.append(composante)

# Calculer le produit scalaire de v1 et v2
produit_scalaire = sum(v1[i] * v2[i] for i in range(n))

# Afficher le résultat
print(f"Le produit scalaire de v1 par v2 vaut {produit_scalaire}.")
