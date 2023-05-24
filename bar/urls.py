from django.urls import path
from . import views

urlpatterns = [
    # Drink URLs
    path('', views.drink_list, name='drink_list'),
    path('detail/<int:pk>/', views.drink_detail, name='drink_detail'),
    path('create/', views.drink_create, name='drink_create'),
    path('update/<int:pk>/', views.drink_update, name='drink_update'),
    path('delete/<int:pk>/', views.drink_delete, name='drink_delete'),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('reduce_stock/', views.reduce_stock, name='reduce_stock'),


     # # Sale URLs
    path('sale_list/', views.sale_list, name='sale_list'),
    path('sale_create/', views.sale_create, name='sale_create'),
    path('<int:pk>/update/', views.sale_update, name='sale_update'),
    path('<int:pk>/delete/', views.sale_delete, name='sale_delete'),
    # # Sale Report URL
    path('sale_report/', views.sale_report, name='sale_report'),
    # debt URLs
    path('debt_list', views.debt_list, name='debt_list'),
    path('debts/<str:status>/', views.debt_list, name='debt_list'),
    path('clear-debt/<int:pk>/', views.clear_debt, name='clear_debt'),
    path('<int:pk>/debt_delete/', views.debt_delete, name='debt_delete'),
 
]

