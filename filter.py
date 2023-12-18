#Вызов функции filter() без функции
# Список значений, которые могут быть True или False
bools = ['bool', 0, None, True, False, 1, 1-1, 2%2]
# Передали None вместо функции в filter()
out = filter(None, bools)
# Вывод результата
for iter in out:
    print(iter)

# функция filter
numbers = [1, 2, 4, 5, 7, 8, 10, 11]
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False
out_filter = filter(filter_odd_num, numbers)
print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))