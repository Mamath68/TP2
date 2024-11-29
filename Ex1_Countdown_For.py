from time import sleep

n = int(input("Entrez un nombre entier positif : "))

for i in range(n, -1, -1):
    print(i)
    sleep(0.5)
