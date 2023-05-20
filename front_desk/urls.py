from django.urls import path
from . import views

urlpatterns = [
    # Guest URLs
    path('', views.guest_list, name='guest_list'),
    path('guest_detail/<int:pk>/', views.guest_detail, name='guest_detail'),
    path('guest_create/', views.guest_create, name='guest_create'),
    path('guest_update/<int:pk>/', views.guest_update, name='guest_update'),
    path('guest_delete/<int:pk>/', views.guest_delete, name='guest_delete'),

     # Room URLs
    path('room_list/', views.room_list, name='room_list'),
    path('room_detail/<int:pk>/', views.room_detail, name='room_detail'),
    path('room_create/', views.room_create, name='room_create'),
    path('room_update/<int:pk>/', views.room_update, name='room_update'),
    path('room_delete/<int:pk>/', views.room_delete, name='room_delete'),

    # Reservation URLs
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/create/', views.reservation_create, name='reservation_create'),
    path('reservations/<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('reservations/<int:pk>/update/', views.reservation_update, name='reservation_update'),
    path('reservations/<int:pk>/delete/', views.reservation_delete, name='reservation_delete'),


]

