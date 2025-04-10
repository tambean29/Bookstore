from django.urls import path
from . import views
urlpatterns = [
    path('',views.load_books,name='load_books'),
    path("add_book/",views.add_to_cart,name="add_to_cart"),
    path("your_cart/",views.view_cart,name="view_cart"),
    path("clear_cart/",views.clear_cart,name="clear_cart")
    ]