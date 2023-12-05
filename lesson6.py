# Цикл while 

# while условие :
#     блок кода будет работать до тех пор пака условие == True

# num = 0
# while True:
#     num +=1
#     print(num)  # бесконечный цикл

# n = int(input('Число:')) # цикл пока не будет False
# num = 1
# while num <= n:
#     print(num)
#     num +=1

# password = str(input('Придумайте пароль: '))

# input_pass = input('Введите пароль: ')
# count = 3
# while input_pass != password:
#     input_pass = input('Введите ещё раз: ')
#     count -=1
#     print(f'Осталось {count} попытки')
#     if count == 0:
#         print('Вы истратили все попытки')
#         print('Доступ запрещён!')
#         break
# else:
#     print('Доступ разрешён!') 

# while True:
#     answer = input('Хотите выйти из цикла?(да/нет) ')
#     if answer == 'да':
#         break
# print('Вы вышли')

# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# flag = True
# while flag:
#     answer = input('Хотите выйти из цикла?(да/нет) ')
#     if answer == 'да':
#         flag = False
# print('Вы вышли')

# Задачи
#1
# n = int(input('Введите число: ')) 
# f = 1
# while n > 1:
#     f *= n
#     n -= 1
# print(f)

# n = int(input('Введите число: ')) 
# f = 1
# i = 1
# while i <= n:
#     f *= i
#     i += 1
# print(f)

#2
# password = str(input('Придумайте пароль: '))

# input_pass = input('Введите пароль: ')
# while input_pass != password:
#     input_pass = input('Введите ещё раз: ')
# print('Доступ разрешён!') 

#3
# num = 10
# input_num = int(input('Число: '))
# while input_num != num:
#     input_num = int(input('Повторите попытку: '))
#     if input_num < num:
#         print('Подсказка-больше')
#     elif input_num > num:
#         print('Подсказка-меньше')
# else:
#     print('Правильно!')

