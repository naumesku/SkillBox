import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
nums_1= set (nums_1)
nums_2= set (nums_2)

print ('Минимальный элемент 1-го множества: ', min(nums_1))
print ('Минимальный элемент 2-го множества: ', min(nums_2))
num1 = random.randint(100,200)
print ('\nСлучайное число для 1-го множества: ', (num1))
nums_1.add(num1)
num2 = random.randint(100,200)
print ('Случайное число для 2-го множества: ', (num2))
nums_2.add(num2)
print ('\nОбъединение множеств: ', nums_1 | nums_2)
print ('Пересечение  множеств: ', nums_1 & nums_2)
print ('Элементы, входящие в nums_2, но не входящие в nums_1: ', nums_2 - nums_1)
