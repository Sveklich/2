import math

def plus():
    result = num1 + num2
    return result
def minus():
    result = num1 - num2
    return result
def umn():
    result = num1 * num2
    return result
def step():
    result = num1 ** num2
    return result
def delen():
    if num2 == 0:
        print("Ошибка: деление на ноль!")
        exit()
    else:
        result = num1 / num2
        return result
def koren():
    if num1 < 0:
        print("Ошибка: Квадратного корня из отрицательного числа быть не может!")
        exit()
    else:
        result = math.sqrt(num1)
        return result
def fact():
    if num1 < 0:
        print("Ошибка: Факториал отрицательного числа быть не может!")
    else:
        result = math.factorial(num1)
        return result
def sin():
    result = math.sin(math.radians(num1))
    return result
def cos():
    result = math.cos(math.radians(num1))
    return result
def tg():
    result = math.tan(math.radians(num1))
    return result
result = 0
operator = input("Введите оператор (+, -, *, /, **, sqrt, !, sin, cos, tg): ")
if operator == "sqrt" or operator == "!" or operator == "sin" or operator == "cos" or operator == "tg":
    try:
        num1 = float(input("Введите число: "))
    except:
        print("Ошибка: Введённое значение не является числом!")
        exit()
else:
    try:
        num1 = float(input("Введите первое число: "))
    except:
        print("Ошибка: Введённое значение не является числом!")
        exit()
    try:
        num2 = float(input("Введите второе число: "))
    except:
        print("Ошибка: Введённое значение не является числом!")
        exit()

if operator == "+":
    x = plus()
elif operator == "-":
    x = minus()
elif operator == "*":
    x = umn()
elif operator == "**":
    x = step()
elif operator == "/":
    x = delen()
elif operator == "sqrt":
    x = koren()
elif operator == "!":
    x = fact()
elif operator == "sin":
    x = sin()
elif operator == "cos":
    x = cos()
elif operator == "tg":
    x = tg()
else:
    print("Ошибка: неверный оператор!")
    exit()

print("Результат:", x)