def filtering_category(database: dict,
                       category_key: [int, str],
                       ordering_key: [None, str] = None,
                       reverse: bool = False):
    if category_key is not None:
        data = list(DATABASE.values())
        result = [dict for dict in data if dict['category'] == category_key]
        # TODO При помощи фильтрации в list comprehension профильтруйте товары по категории.

    else:
        result = list(database) #  TODO Трансформируйте database в список словарей
    if ordering_key is not None:
        result = sorted(result, key=lambda x: x[ordering_key], reverse=reverse)
        #  TODO Проведите сортировку result по ordering_key и параметру reverse
    return result

if __name__ == "__main__":
    from store.models import DATABASE

    test = [
        {'name': 'Клубника', 'discount': None, 'price_before': 500.0,
         'price_after': 500.0,
         'description': 'Сладкая и ароматная клубника, полная витаминов, чтобы сделать ваш день ярче.',
         'rating': 5.0, 'review': 200, 'sold_value': 700,
         'weight_in_stock': 400,
         'category': 'Фрукты', 'id': 2, 'url': 'store/images/product-2.jpg',
         'html': 'strawberry'},

        {'name': 'Яблоки', 'discount': None, 'price_before': 130.0,
         'price_after': 130.0,
         'description': 'Сочные и сладкие яблоки - идеальная закуска для здорового перекуса.',
         'rating': 4.7, 'review': 30, 'sold_value': 70, 'weight_in_stock': 200,
         'category': 'Фрукты', 'id': 10, 'url': 'store/images/product-10.jpg',
         'html': 'apple'}
    ]

    print(filtering_category(DATABASE, 'Фрукты', 'price_after', True) == test)  # True