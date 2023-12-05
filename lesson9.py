# Исключения

# try:
#     num = int(input('Введите число: '))
#     res = 10 / num
#     print(res)
# except (ValueError,ZeroDivisionError):
#     print('Ошибка')
# except ValueError:
#     print('Идиот')
# except ZeroDivisionError:
#     print('Дебил')



# try:
#     num = int(input('Введите число: '))
#     res = 10 / num
#     print(res)
# except ValueError as ve:
#     print('Ошибка1 {0}'.format(ve))
# except ZeroDivisionError:
#     print('Ошибка2')
# finally:
#     print('Finish')



# try:
#     num = int(input('Введите число: '))
#     res = 10 / num
#     print(res)
# except Exception as ex:
#     print('Error')

# print('ok')



# Задачи

#1
# num = int(input('Число: '))
# if num % 2 == 0:
#     print('Четное')
# else:
#     print('Нечётное')


#2 
while True:
    s = input("Выберите способ операции (+, -, *, /): ")
    if s == '0':
        print('Конец операции!')
        break
    if s in ('+', '-', '*', '/'):
        a = float(input("a = "))
        b = float(input("b = "))
        if s == '+':
            print(a + b)
        elif s == '-':
            print(a - b)
        elif s == '*':
            print(a * b)
        elif s == '/':
            if b != 0:
                print(a / b)
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
        



#3
# def cesar(text,shift):
#     result = ''
#     alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
#     # alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#     for i in text:
#         is_upper = str(i).upper()
#         if str(i).isalpha():
#             i_index = alphabet_lower.index(str(i).lower())
#             i_shift = alphabet_lower[(i_index + shift)] % 26
#             result += i_shift if not is_upper else i_shift.upper()
#         else:
#             result += i

# inp_text = 'abc xyz'
# shift_v = 3
# enc_text = cesar(inp_text,shift=shift_v)
# print(enc_text)


#4
# user = str(input('Запись: '))
# user2 = user.split()
# word = user2[::-1]
# print(word)



















