# def memory(func):
#     res = {}
#     def wrapper(*args):
#         if args in res:
#             return res[args]
#         else:
#             n = func(*args)
#             res[args] = n
#         return n
#     return wrapper

# @memory
# def func(a,b) -> int:
#     return a * b


# print(func(2,5))



def deco(func):
    def wrapper(*args):
        n = 0
        try:
            n = func(*args)
        except ZeroDivisionError as ex:
            print("don't do this")
            return n
    return wrapper


@deco
def dev(a,b) -> float:
    return a / b


print(dev(10,0))