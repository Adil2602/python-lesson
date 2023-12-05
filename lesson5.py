# Цикл for 
# итерация - одно и тоже действие несколько раз 
# for элемент (куда мы хотим итерировать),последовательность (то что мы хотим итерировать)

# name = 'adil'
# for n in name:
#     print(n)

# fruits = ['яблоко','апельсин','виноград','банан','мандарин']
# for x in fruits:
#     print(x)

# numbers = [30, 50, 70, 90, 100]
# sums = 0
# for num in numbers:
#     sums += num # sums = sums + num
#     print(sums)
# print(sums)

# for i in range(1,6): # range - генератор чисел (начало, конец, шаг)
#     print(i)

# fruits = ['яблоко','апельсин','виноград','банан','мандарин']
# for index in range(len(fruits)):
#     print(index+1,'',fruits[index]) 

# vegetables = {'картошка':23,'помидор':50,'перец':40,'лук':36,'капуста':60}
# for vegetable , price in vegetables.items():
#     print(vegetable,':',price)

# fruits = ['яблоко','апельсин','виноград','банан','мандарин']
# for fruit in fruits:
#     if fruit == 'апельсин':
#         break # принудительно заканчивает цикл 
#     print(fruit)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# for num in numbers:
#     if num % 2 == 0:
#         continue
#     print(num)


#1
num = int(input('Введите число:'))
for x in range(num):
    print(x+1)

#2
num2 = int(input('Введите число:'))
for i in range(num2):
    print((i+1)*2)

#3
num3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sums = 0
for s in num3:
    sums += s
print(sums)

#4
# dict = str(input('Введите предложение:'))
# print(len(dict))

user = str(input('Введите предложение:'))
words = 'аеиоуэюя'
count = 0
for char in user:
    if char.lower() in words:
        count +=1
print('вывод', count)