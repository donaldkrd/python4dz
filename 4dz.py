# Вычислить число c заданной точностью d

# from math import pi
# d = int(input('Введите нужное число знаков после запятой: '))
# print(round(pi, d))


# Задайте натуральное число N. Напишите
# программу, которая составит список
# простых множителей числа N.

# n = int(input('Задайте натуральное число: '))
# i = 2
# list1 = []
# old = n
# while i <= n:
#     if n % i == 0:
#         list1.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(list1)


# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся
# элементов исходной последовательности.

# import random
# list1 = [random.randint(1, 9) for _ in range(10)]
# print(list1)
# list2 = []
# for i in range(len(list1)):
#     flag = 1
#     for j in range(len(list1)):
#         if list1[i] == list1[j] and i != j:
#             flag = 0
#             break
#     if flag:
#         print(list1[i])
