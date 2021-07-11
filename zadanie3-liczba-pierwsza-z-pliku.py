def liczpierwsza(n):

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


listaliczb = open('zadanie3-liczby.txt', 'r')

for line in listaliczb.readlines():
    if liczpierwsza(int(line)):
        print("Liczba", int(line), "jest liczbą pierwszą.")
    else:
        print("Liczba", int(line), "nie jest liczbą pierwszą.")
