from datetime import datetime
import time

# f(x,y,z) = x + y * z + 675

def main():
    # переменные и их типы

    # тип "целое число"
    v = 9
    # print(type(v))

    # тип "строка"
    s = "987trfghjkllkjh"
    # print(type(s))
    
    # вещественные числа (с плавающей запятой)
    d = 9.23435
    # print(type(d))
    
    # тип дата-время
    t = datetime.now()
    # print(v, s, d, t, type(t))
    
    # логический тип
    b = False
    # print(b, type(b))

    # операции над типами
    q = 10
    w = -5
    e = q / w

    # // это целочисленное деление с отбрасыванием остатка
    # e = q // w

    # print("до", type(e), e)
    
    # # приведение типа float к int
    # e = int(e)
    # print("после", type(e), e)

    # сложение/умножение строк
    a = "ляля"
    b = "пупу"
    m = a + b
    print(m)

    print("qwe " * 3)

    # ввод-вывод (и шаблонные строки)
    name = input("введи имя пж:\n")
    print(f"привет, {name}!")

main()
