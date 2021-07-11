from datetime import date

rok = int(input("Podaj rok urodzenia: "))
datadzisiaj = date.today()
wiek = datadzisiaj.year - rok

if rok >= datadzisiaj.year:
    print("Nieprawidłowy rok urodzenia")
elif rok <= 1900:
    print("To niemożliwe, żebyś żył aż tak długo... Można jednak uznać, że jesteś pełnoletni.")
elif wiek < 18:
    print("W wieku", wiek, "lat nie jesteś jeszcze pełnoletni.")
else:
    print("W wieku", wiek, "lat jesteś już pełnoletni.")
