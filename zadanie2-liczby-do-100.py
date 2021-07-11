for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "= BEST")
    elif i % 3 == 0:
        print(i, "= GOOD")
    elif i % 5 == 0:
        print(i, "= BETTER")
    else:
        print(i)
