import math

def one(): #делает из введенных цифр макисмальное число (не учитывает, что может быть строка, работает наоборот)
    print('Введите число: ')
    a = list(input())
    a.sort(reverse=False)
    print(int(''.join(a)))

def two(): #приводит к виду сложения разрядов (если есть одинаковые цифры -- ломается)
    print('Введите число: ')
    a = list(input())
    res = ''
    for i in a:
        res = res + i + ' * 10**' + str(len(a) - a.index(i) - 1) + ' + '
    res = res[:-3]
    print(res)

def three(): #решает квадратные уравнения (если дискриминант меньше нуля, то ломается)
    print("Введите коэффициенты для уравнения")
    print("ax^2 + bx + c = 0:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    discr = b ** 2 - 4 * a * c
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(x1)
    print(x2)

def four(n): # функция проверки на простоту
    n = int(n)  # ERROR не должен принимать значения <=0

    i = 2
    while i <= n ** (0.5):
        if n % i == 0:
            return False
    i += 1
    if n > 1:
        return True


def main():
    print("0. Выход")
    print("1. Максимальное число")
    print("2. Число по разрядам")
    print("3. Решение квадратных уравнений")
    print("4. Проверка простоты")

    a = int(input("Введите номер функиции: "))

    match a:
        case 1:
            one()
        case 2:
            two()
        case 3:
            three()
        case 4:
            four()
        case _:
            exit()
    print('\n')
    main()

main()