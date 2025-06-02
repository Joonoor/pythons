def is_year_leap(n):
    if n % 4 == 0:
        print(True)
    else:
        print(False)


n = int(input("Номер года "))
is_year_leap(2024)
