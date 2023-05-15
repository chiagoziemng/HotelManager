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

      # Invoice URLs
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/create/', views.invoice_create, name='invoice_create'),
    path('invoices/<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('invoices/<int:pk>/update/', views.invoice_update, name='invoice_update'),
    path('invoices/<int:pk>/delete/', views.invoice_delete, name='invoice_delete'),

        # HousekeepingTask URLs
    path('task_list/', views.task_list, name='task_list'),
    path('task_detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('task_create/', views.task_create, name='task_create'),
    path('task_update/<int:pk>/', views.task_update, name='task_update'),
    path('task_delete/<int:pk>/', views.task_delete, name='task_delete'),

       # Maintenance Request URLs
    path('maintenance_request/', views.maintenance_request_list, name='maintenance_request_list'),
    path('maintenance_request/create/', views.maintenance_request_create, name='maintenance_request_create'),
    path('maintenance_request/<int:pk>/', views.maintenance_request_detail, name='maintenance_request_detail'),
    path('maintenance_request/<int:pk>/update/', views.maintenance_request_update, name='maintenance_request_update'),
    path('maintenance_request/<int:pk>/delete/', views.maintenance_request_delete, name='maintenance_request_delete'),



]

