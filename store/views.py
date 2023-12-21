from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from store.models import DATABASE
from logic.services import filtering_category
from logic.services import view_in_cart, add_to_cart, remove_from_cart

def products_view_json(request):
    if request.method == "GET":
        return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False, 'indent': 4})

def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ

def products_view(request):
    if request.method == "GET":
        if id_product := request.GET.get("id"):
            if data := DATABASE.get(id_product):
                return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
            return HttpResponseNotFound("Данного продукта нет в базе данных")
        # else:
        #     data = DATABASE
        #     return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
        # return HttpResponseNotFound("Данного продукта нет в базе данных")
        # Обработка фильтрации из параметров запроса
        category_key = request.GET.get("category")  # Считали 'category'
        if ordering_key := request.GET.get("ordering"):  # Если в параметрах есть 'ordering'
            if request.GET.get("reverse") in ('true', 'True'):  # Если в параметрах есть 'ordering' и 'reverse'=True
                data = filtering_category(DATABASE, category_key, ordering_key, reverse=True)
            else:
                data = filtering_category(DATABASE, category_key, ordering_key, reverse=False)
        else:
            data = filtering_category(DATABASE, category_key)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})

# def products_page_view(request, page):
#      if request.method == "GET":
#          for data in DATABASE.values():
#              if data['html'] == page:  # Если значение переданного параметра совпадает именем html файла
#                  with open(f'store/products/{page}.html', encoding="utf-8") as f:
#                      data = f.read()
#                  return HttpResponse(data)

def products_page_view(request, page):
    if request.method == "GET":
        if isinstance(page, str): # если page - это строка
            # То, что было ранее для обработки типа slug
            for data in DATABASE.values():
                if data['html'] == page:  # Если значение переданного параметра совпадает именем html файла
                    with open(f'store/products/{page}.html', encoding="utf-8") as f:
                        data = f.read()
                    return HttpResponse(data)
        elif isinstance(page, int): # если page - это число
            data = DATABASE.get(str(page))  # Получаем какой странице соответствует данный id
            if data:  # Если по данному page было найдено значение
                with open(f'store/products/{data["html"]}.html', encoding="utf-8") as f:
                    data = f.read()
                return HttpResponse(data)
        return HttpResponse(status=404)

def cart_view(request):
    if request.method == "GET":
        data = view_in_cart()
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})

def cart_add_view(request, id_product):
    if request.method == "GET":
        result = add_to_cart(id_product)
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в корзину"},
                                json_dumps_params={'ensure_ascii': False})
        return JsonResponse({"answer": "Неудачное добавление в корзину"},
                            status=404, json_dumps_params={'ensure_ascii': False})

def cart_del_view(request, id_product):
    if request.method == "GET":
        result = remove_from_cart(id_product)
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из корзины"},
                                json_dumps_params={'ensure_ascii': False})
        return JsonResponse({"answer": "Неудачное удаление из корзины"},
                             status=404, json_dumps_params={'ensure_ascii': False})