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
    
    a = random.randint(1, 10)
    print (a)
    while True:
        c = input ("Введи число: ")
        c = int(c)
        if c > a:
            print (f"Число {c} больше загаданного")
        
        elif c < a:
             print (f"Число {c} меньше загаданного")
        else:
            print (f"Ты выиграл, ответ - {a}")
            break
        

main()    