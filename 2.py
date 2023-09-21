def rectangle_area(width, height):
    ploshad = width * height
    return ploshad


def is_even(number):
    ost = number % 2
    if ost == 0:
        return True
    else:
        return False
def sum_digits(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_digits(number // 10)
print("Выберите фунцию: \n1)Площадь\n2)Чётность\n3)Сумма цифр")
v = input()
if v == "1":
    x = int(input("Введите ширину: "))
    y = int(input("Введите высоту: "))
    print(rectangle_area(x,y))
elif v == "2":
    x = int(input("Введите число: "))
    print(is_even(x))
else:
    x = int(input("Введите число: "))
    print(sum_digits(x))