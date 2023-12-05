# Асинхронное программирование

import asyncio

# async def say_hello(delay,name):
#     await asyncio.sleep(delay)
#     print(f'Hello {name}')

# # delay задержка 
# # name объект
# async def main():
#     task = [
#         say_hello(1,'Jhon'),
#         say_hello(2,'Wick'),
#         say_hello(3,'Bob')
#     ]
#     await asyncio.gather(*task)

# if __name__ == "__main__":
#     asyncio.run(main())


# async def data2(data):
#     await asyncio.sleep(1)
#     return f"процесс {data}"

# async def main():
#     data = [1,2,3,4,5]
#     results = await asyncio.gather(*(data2(item)for item in data))
#     for item , result in zip(data,results):
#         print(f'Data: {item}, result: {result}')

# if __name__ == "__main__":
#     asyncio.run(main())    

# В данном случае разъединяет
# data = {'key':'value',1:3}
# d = data.items()
# x,y = zip(*d)
# print(list(x))
# print(list(y))