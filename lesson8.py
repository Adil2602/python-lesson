# Файлы чтение и запись



# file = open('text.txt','r',encoding='utf-8') # encoding для кириллицы

# content = file.read()
# print(content)

# file.close()



# with open('text.txt','r',encoding='utf-8') as file:
#     content = file.read()
#     print(content) Это чтение файла 



# with open('text.txt','w',encoding='utf-8') as file:
#     content = file.write('Hello')
#     print(content) # Это очистка файла и новая запись



# with open('text.txt','a',encoding='utf-8') as file:
#     content = file.read('hello')
#     print(content) # это запись файла без его очистки внутри



# with open('text.txt','a',encoding='utf-8') as file:
#     line = ['Строка 1',' ','Строка 2']
#     content = file.writelines(line)
#     print(content)



# with open('text.txt','w',encoding='utf-8') as file:
#     l = 5*5
#     content = file.write(str(l))
#     print(content)



# with open('text.txt','w',encoding='utf-8') as file:
#     user = str(input())
#     content = file.write(user)
#     print(content)



# with open('text.txt','r',encoding='utf-8') as file:

#     for l in file:
#         print(l)



# with open('text.txt','r',encoding='utf-8') as file:
#     with open('copy.txt','w',encoding='utf-8') as copy_file:
#         copy_file.write(file.read())



# with open('text.txt','r',encoding='utf-8') as file:
    
#     for l in file:
#         if 'света' in l:
#             print('yes')



# Задания
# 1
# with open('text.txt','r',encoding='utf-8') as file:
#     with open('copy.txt','w',encoding='utf-8') as copy_file:
#         copy_file.write(file.read())


#2
# with open('text.txt','r',encoding='utf-8') as file:
#     user = str(input('Поиск: '))
#     for l in file:
#         if user in l:
#             print(l)


#3
# with open('text.txt','r',encoding='utf-8') as file:
#     content = file.read()
#     word = content.split()
#     words = len(word)
#     print(words)


#4
# with open('text.txt','r',encoding='utf-8') as file:  # для замены слова, нужно сначала прочитать текст, а после замена
#     content = file.read() 

# user = str(input('Запись: '))
# user2 = str(input('Замена: '))
# new_content = content.replace(user, user2)

# with open('text.txt','w',encoding='utf-8') as new_file:
#     new_file.write(new_content)


#5
# with open('kg.txt','a',encoding='utf-8') as file:
#     content = file.read(str(input('Запись: ')))
#     print(content)
#     with open('kz.txt','a',encoding='utf-8') as file:
#         content = file.read(str(input('Запись: ')))
#         print(content)
#         with open('uz.txt','a',encoding='utf-8') as file:
#             content = file.read(str(input('Запись: ')))
#             print(content)

while True:
    s = input('Выберите страну (kg, kz, uz): ')
    if s == 0:
        print('Конец!')
        break
    if s in ('kg', 'kz', 'uz'):
        if s == 'kg':
            with open('kg.txt','a',encoding='utf-8') as file:
                content = file.read(str(input('Запись: ')))
                print(content)
        elif s == 'kz':
            with open('kz.txt','a',encoding='utf-8') as file:
                content = file.read(str(input('Запись: ')))
                print(content)
        if s == 'uz':
            with open('uz.txt','a',encoding='utf-8') as file:
                content = file.read(str(input('Запись: ')))
                print(content)
    else:
        print('Неправильно!')
    