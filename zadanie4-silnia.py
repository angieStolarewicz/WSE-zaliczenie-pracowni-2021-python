def silnia(n):

    if n == 0:
        return 1
    elif n >= 1:
        return n*silnia(n-1)
    else:
        return False


liczba = int(input("Podaj liczbę do wyliczenia z niej silni: "))
print("Silnia liczby", liczba, "wynosi", silnia(liczba))
