from datetime import datetime
import random
def main():
    # v=4
    # a=3
    # p=a+v
    # print(p)
    # s="wewe"
    # print(type(s))
    # print (datetime.now())
    # t=datetime.now()
    # print (type(t))
    # age = input("скока лет тебе?: \n")
    # print (f"тем кому {age} вход запрещен")
    # игра угадай число 
    
    # a = random.randint(1, 10)
    # print (a)
    # x = 0
    # while x < 10:
    #     c = input ("Введи число: ")
    #     c = int(c)
    #     if c > a:
    #         x = x + 1
    #         print (f"Число {c} больше загаданного")
        
    #     elif c < a:
    #          x = x + 1
    #          print (f"Число {c} меньше загаданного")
    #     else:
    #         print (f"Ты выиграл, ответ - {a}")
    #         break
    # else:
    #     print (f"Ты проиграл, ответ - {a}")

    # for i in range(1, 6):
    #         for j in range(1, 6):
    #             for k in range (1, 6):
    #                 print(i, j, k)
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
    
    
    for index in range (0, len(matrix)):
        # print (index)
        a = matrix [index]
        # print (a)
        for dindex in range (0, len(a)):
            # print (dindex)
            b = a[dindex]
            print (b)
    # print (matrix [0])
    # while True:
    #     a = input ("Какая строка у загаданной позиции? - ")
    #     a = int(a)
    #     a = a-1
    #     b = matrix [a]
      
    #     c = input ("а столбец? - ")
    #     c = int(c)
    #     c = c - 1 
    #     d = b[c]
    #     print (f'Твое число {d}')
    #     break



   
main()    