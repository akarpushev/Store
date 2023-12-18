from django.urls import path
from .views import products_view_json, shop_view, products_view, products_page_view


urlpatterns = [
    path('products/', products_view_json),
    path('', shop_view),
    path('product/', products_view),
    path('product/<slug:page>.html', products_page_view),
    path('product/<int:page>', products_page_view),
]