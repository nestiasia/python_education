


# def main(x:list[int], offset:int = 0) -> None:
#     for y in x:
#         y = y + offset
#         print (y)
# main(range(1,11))

# def nan(*args:int):
#     y = 0
#     for x in args:
#         y = x + y
#     return y
# z = nan(5,4,6,7,4441)
# print(z)

def main():
    def get_mean(*args:int) -> float:
        y=0
        a = len(args)
        if a == 0:
            return 0
        for x in args:
            y=y+x
        z = y/a
        return z
    get_mean()

    def print_data(**kwargs: int):
        for argum, value in kwargs.items():
            z = argum, value
        print(f"Аргумент {argum}, значение = {value}")
        return z

    print_data(one = 5, two = 6, three =7)


    # print (get_mean(1,2,6))
main()