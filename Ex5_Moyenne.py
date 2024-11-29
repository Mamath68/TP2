nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []

for i in range(nombreEtudiants):
    while True:
        note = float(input(f"Entrez la note de l'étudiant {i + 1} (entre 0 et 20) : "))
        if 0 <= note <= 20:
            notes.append(note)
            break
        else:
            print("La note doit être comprise entre 0 et 20. Veuillez réessayer.")

moyenne = sum(notes) / nombreEtudiants

print("Les notes des étudiants sont : ", notes)
print(f"La moyenne des notes est : {moyenne:.2f}")

print("Numéro de l’Étudiant | Note | Écart à la Moyenne")
for i, note in enumerate(notes, start=1):
    ecart = note - moyenne
    print(f"{i} | {note} | {ecart:.2f}")
