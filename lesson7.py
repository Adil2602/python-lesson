# Функции в python

# def name_function():
#     тело функции 
#     действие функции

# def say_hello():  # Локальная часть кода, не зависит от глобальной 
#     print('hello world')
# say_hello()  

# name = 'Jhon'
# print(name)  # часть глобальной части кода

# hello = adil
# def say_hello(name):
#     print('hello', name)
# say_hello('Jhon')
# say_hello(name=hello) # можно приравнять переменные

# def sqad(number):
#     return number * number # возвращает значение 
# result = sqad(5)
# print(result)

# def sqad(number):
#     a = number * number
#     b = a * 3
#     n = b + 5
#     return print(b,n)
# sqad(int(input()))

# def sqad(num,m):
#     a = num * num
#     b = a * 3
#     s = b + 5
#     return print(b,s)
# n = int(input())
# m = int(input())
# sqad(num=n,m=m)

# def hi(name='незнакомец'):
#     return print(f'Привет, {name}')
# name = str(input(''))
# hi()
# hi('Анна')
# hi(name=name)

# Рекурсия-вызывает функцию саму себя бесконечно 

# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))

# lambda аргументы : выражение # анонимная функция 

# num = lambda x,y : x + y
# result = num(5,4)
# print(result)

# word = ["яюлоко","груша","апельсин"]
# word.sort(key=lambda word: len(word))
# print(word)


# def name(*args,**kwargs):  # *args - это позиционные аргумент, **kwargs - именной аргумент
#     print(args,kwargs)
# name()

