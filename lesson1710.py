# n = input("Enter the version of the project ")

# def ask_digits():
#         while True:
#                 try:
#                         digit = int(input("Enter the digit: "))
#                 except:
#                         print("Please enter digit")
#                         continue
#                 else:
#                         print("kjhsdf")
#                         break
# ask_digits()

# var1 = "50456"

# var2 = var1.isdigit()
# print(var2)


# nspisok1 = [[i for i in range(1,11)] for _ in range(1, 11)]
# print(nspisok1)

# for num in nspisok1:
#         print(num)

# list1 = [
#         {"key1": "value4"},
#         {"key1": "value2"},
#         {"key1": "value1"},
# ]
# list1.sort(key = lambda key: key['key1'])
# print(list1)

# list11 = list1[::-1]
# print(list11)

# import requests

# from threading import *
# from time import time, sleep 

# start = time()

# def one(threadname):
#         url = "https://via.placeholder.com/150/92c952"

#         for i in range(10):
#                 data = requests.get(url)
#                 with open(f"images/{i}-{threadname}.png", "wb") as f:
#                         f.write(data.content)

# finish = time()
# print(f'Finished in {finish-start}seconds')


# x1 = Thread(target=one, args=(1,))
# x1.start()
# one(2)
# x1.join()


# class Auto:
#     def ride1(self):
#         print("Riding 23")

# class Boat:
#     def swim(self):
#         print("Sailing in the ocean")

#     def ride(self):
#         print("Something another")

# class Amphibian(Auto, Boat):
#         pass
 
# a = Amphibian()
# a.ride1()
# a.swim()
















