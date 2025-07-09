import random
def este_par(numar):
    return numar % 2 == 0
random.randint(0 , 10)

print('Bun venit la jocul meu')

while True:

    alegere = input("Alegi 'par' sau 'impar'? ")
    while alegere not in ['par', 'impar']:
        alegere = input("Te rog să alegi 'par' sau 'impar': ")


    try:
        numar_utilizator = int(input("Alege un număr între 0 și 10: "))
        if not (0 <= numar_utilizator <= 10):
            raise ValueError
    except ValueError:
        print("Număr invalid. Trebuie să fie între 0 și 10.")
        continue



    numar_calculator = random.randint(0, 10)
    print(f"Calculatorul a ales: {numar_calculator}")

    suma = numar_utilizator + numar_calculator
    rezultat = "par" if este_par(suma) else "impar"
    print(f"Suma este {suma}, care este {rezultat}.")


    if alegere == rezultat:
        print("Ai câștigat această rundă!")
        numar_utilizator += 1
    else:
        print("Calculatorul a câștigat această rundă.")
        numar_calculator += 1
print(f"Suma este {suma}, care este {rezultat}.")


def joc_par_sau_impar():
    scor_utilizator = 0
    scor_calculator = 0

def este_par(numar):
    return numar % 2 == 0


