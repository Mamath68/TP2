from time import sleep

n = int(input("Entrez un nombre entier positif : "))

while n >= 0:
    print(n)
    sleep(0.5)
    n -= 1
