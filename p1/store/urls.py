from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
]
