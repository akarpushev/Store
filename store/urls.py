from django.urls import path
from .views import products_view_json, shop_view, products_view, products_page_view
from .views import cart_view, cart_add_view, cart_del_view

urlpatterns = [
    path('products/', products_view_json),
    path('', shop_view),
    path('product/', products_view),
    path('product/<slug:page>.html', products_page_view),
    path('product/<int:page>', products_page_view),
    path('cart/', cart_view),
    path('cart/add/<str:id_product>', cart_add_view),
    path('cart/del/<str:id_product>', cart_del_view),
]