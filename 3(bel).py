def functions():
    """
    - функция и функция как объект первого порядка
    - ретурн и без него
    - анонимные функции (пока без них)
    """

    def func(x: int, s: str, f) -> int:
        a = x + 10
        f_result = f(s)
        print(f_result)
        return a

    def sdfsgs(r: float) -> None:
        print(r)
        # return None # это по дефолту будет, если никакой return не указан

    result = func(209876, "ddd", sdfsgs)
    print(result)


def args_kwargs():
    """
    - арги и кварги, таплы и дикты
    - обязательные и необязательные параметры
    """

    # параметр a не имеет значения по умолчанию, значит он обязательный
    # параметр x имеет значение по умолчанию = 90 - значит параметр необязательный
    def func(a: str, x: int = 90) -> None:
        print(a, x)

    # func('sdfgg')

    # args kwargs

    # args - позиционные аргументы. это кортеж - что-то типа неизменяемого листа
    def f(*args: int):
        print(args)

    # f(2, 87, 3490, 98, 214, 234)

    # kwargs - именованные аргументы. это словарь
    def f1(x: int, b: int):
        print(x, b)

    # f1(b=23, x=50)

    # kwargs - keyword arguments - именованные аргументы
    def f_with_kwargs(**kwargs: int):
        for k, v in kwargs.items():
            print(k, v)

    f_with_kwargs(x=20, y=-30, t=6)

    # резиновая сигнатура функции - аргсы кваргсы вместе
    def func_with_args_and_kwargs(*args, **kwargs):
        print(args, kwargs)

    func_with_args_and_kwargs(20, 50, arg=9, arg2=-2)



def scopes():
    """области видимости"""


def main():
    # functions()
    args_kwargs()


main()
