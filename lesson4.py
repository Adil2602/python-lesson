# Операторы if,else (если, иначе)

# num = 20
# if num == 10: # == если условие соблюдается
#     print('Hello')
# else:
#     print('NeHello')

# if num != 20: # != если условие не соблюдается 
#     print('Hello')
# else:
#     print('hi')

# num = int(input('Введите число:')) # вводит пользователь 
# if num == 10:
#     print('да')
# else:
#     print('нет')

word = str(input('Введите слово:')) # вводит пользователь 
if word == 'приз':
    print('да')
else:
    print('нет')

# num = 30
# if num >= 30:
#     print('да')
# elif num == 30:
#     print('равно')
# else:
#     print('нет')

# num = 30
# if num == 30 and num < 20:
#     print('Da')
# else:
#     print('Net')

# num = 30
# if num == 30 or num < 20:
#     print('Da')
# else:
#     print('Net')

# num = 30
# num2 = -10
# if num > 0:
#     if num2 > 0:
#         print('num and num2 положительный')
#     else:
#         print('num положительный, но num2 отрицательный')
# else:
#     print('они оба отрицательные')

#1
# num = int(input('Введите возраст:'))
# if num < 16:
#     print('ребенок')
# if num < 18:
#         print('подросток')
# elif num < 65:
#         print('взрослый')
# else:
#     print('пожилой')

#2
# num2 = int(input('Введите число:'))
# if num2 % 2 == 0:
#     print('да')
# else:
#     print('нет')

#3

password = str(input('Введите пароль:'))
if password == 'solid':
    print('Доступ разрешен')
else:
     print('Доступ запрещен')