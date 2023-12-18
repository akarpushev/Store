data = [[5, 'Алексей', 'синий'],
        [3, 'Виктор', 'красный'],
        [7, 'Алексей', 'желтый']]
from operator import itemgetter

sorted_data = sorted(data, key=itemgetter(1))


list_dicts = [{'имя': 'Анна', 'возраст': 25}, {'имя': 'Маша', 'возраст': 18}, {'имя': 'Вася', 'возраст': 30}]
sorted_list = sorted(list_dicts, key=lambda x: x['имя'], reverse=True)
print(sorted_list)
