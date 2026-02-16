from datetime import datetime
import random

def if_conditions():
    a = 10
    b = 10
    c = "www"
    x = a == b

    print(type(x), x)

    # условные операторы
    x = input('введи число: ')

    x = int(x)
    if x < 10 and x > 0:
        print ("1")
    elif x > 9 and x < 100:
        print ("2")
    elif x >= 100 and x < 1000:
        print ("3")
    else:
        print ("хуйня брат")

def main():
    """
    list
    if elif else

    for range while + while True
    break continue
    """
    
    # if_conditions()

    # if not x.isnumeric():
    #     print("введи блин число!")

    # x = int(x)

    # x > 0 -> "{x} положительный"
    # x < 0 -> "{x} отрицательный"

    # if x > 0:
    #     print(f"{x} - положительный")
    # elif x < 0:
    #     print(f"{x} - отрицательный")
    # elif x == 0:
    #     print('x == 0')
    # else:
    #     print('вообще не знаю такое')

    # # циклы и листы
    # l = [66, 9, -3, 457, -346, 99, 22, -1235, 55, 54]

    # # print(l)

    # # print(l[0], l[1], l[2], l[3], l[4], l[5])
    # x = 0

    # for number in l:
    #     if number % 2 == 0:
    #         x = x + 1

    #     if x == 3:
    #         # print(number)
    #         break # тут произойдет выход из цикла

    # for n in range(5, 9):
    #     print(n)

    # цикл while

    # for num in l:
    #     print(num)

    # while True:
    #     now = datetime.now()
        
    #     if now.hour == 22 and now.minute == 25:
    #         print('hello')
    #         break
    
    """
    домашка:

    игра угадай число

    + под * если 10 попыток комп говрит ты проиграл и выдат ответ
    """

    random_number = random.randint(1, 10)
    # print(random_number)

    dz()

def dz():
    # тут пишем домашку
    spisok = [4, 33, -32, 435, 26, 40]
    print (spisok)
    for chicelka in spisok:
       if chicelka < 0:
        print (chicelka)

    index = 0
    while index < len(spisok):
        chicelka = spisok [index]
        index = index + 1     
        print (chicelka + 5)
    # while True:
    #     if index < len(spisok):
    #         chicelka = spisok [index]
    #         index = index + 1
    #         print (chicelka)

    #игра угадай число 
    # a = 3
    # # spisok = [1, 2, 3, 4, 5] 
    # c = input ("Введи число: ")
    # # for b in spisok:
    # if c > a:
    #     print (f"Число {c} больше загаданного")
    # if c < a:
    #     print (f"Число {c} меньше загаданного")
    # if c == a:
    #     print ("Ты выиграл")
    

main()
    
