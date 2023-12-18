cart = [3, 4, 12, 17, 19, 21, 23, 26, 30]
cashier = []  # новый список с помощью метода append
for item in cart:
    cashier.append(item) # это не comprehention
print(cashier)

cashier = [item for item in cart] # вот comprehention
print(cashier)

#Внутри list comprehension можно
#вызывать целые функции и
#помещать их результат в список.
import random
# если сама переменная цикла for не нужна, то можно использовать нижнее подчеркивание
random_list = [random.randint(1, 10) for _ in range(10)]
print(random_list)

# Сделать имена студентов с заглавной буквы.
students_list = ['cаша', 'кИРилл', 'пЕТЯ', 'оЛя']
students_list = [student.capitalize() for student in students_list]
print(students_list)

# Получить список цифр числа.
number = 12345
list_digits = [int(d) for d in str(number)]  # Получить список цифр числа N
print(list_digits)  # [1, 2, 3, 4, 5]

#Фильтрация элементов
cart = [5, 7, 9, 10, 12, 15, 19, 20, 22]
cashier_3 = []
for item in cart:
    if item % 2 == 0:  # только четные
        cashier_3.append(item) # это не comprehention
print(cashier_3)

cashier_3 = [item for item in cart if item % 2 == 0] # вот comprehention
print(cashier_3)

# Составить список учеников старше 18.
students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]
min_age = 18  # минимальный возраст
print([student for student in students_list if student["age"] > min_age])
