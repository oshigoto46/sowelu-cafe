from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_home, name='inventory_home'),
    path('<int:item_id>/', views.inventory_detail, name='inventory_detail'),
    path('list/', views.inventory_list, name='inventory_list'),  # inventory_listビューのURLパターン
    path('add/', views.inventory_add, name='inventory_add'),
    path('<int:item_id>/', views.inventory_detail, name='inventory_detail'),
]
