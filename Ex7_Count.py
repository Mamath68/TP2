# Avec un dictionnaire
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

occurrences = {}

for element in L1:
    if element in occurrences:
        occurrences[element] += 1
    else:
        occurrences[element] = 1

element_le_plus_frequent = max(occurrences, key=occurrences.get)
frequence = occurrences[element_le_plus_frequent]

print(f"Le nombre le plus frequent dans la liste est le : {element_le_plus_frequent} ({frequence} x)")


# Avec Count
L1 = [2, 7, 6, 6, 5, 1, 6, 2, 1, 7]

element_le_plus_frequent = max(L1, key=L1.count)
frequence = L1.count(element_le_plus_frequent)

print(f"Le nombre le plus frequent dans la liste est le : {element_le_plus_frequent} ({frequence} x)")
