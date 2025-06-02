def month_to_season(n):
    if n <= 2:
        print("Зима")
    elif n > 2 and n <= 5:
        print("Весна")
    elif n > 5 and n <= 8:
        print("Лето")
    elif n > 8 and n <= 11:
        print("Осень")
    else:
        print("Зима")


n = int(input("Введите номер месяца: "))

month_to_season(n)
