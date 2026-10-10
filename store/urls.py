from django.urls import path
from . import views as v
urlpatterns = [
    path("", v.product_list, name="home"), path("product/<int:pk>/", v.product_detail, name="detail"),
    path("cart/", v.cart_view, name="cart"), path("cart/add/<int:pk>/", v.cart_add, name="cart_add"),
    path("cart/dec/<int:pk>/", v.cart_dec, name="cart_dec"), path("cart/remove/<int:pk>/", v.cart_remove, name="cart_remove"),
    path("checkout/", v.checkout, name="checkout"), path("orders/", v.orders, name="orders")]
