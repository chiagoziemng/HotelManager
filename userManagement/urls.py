from django.urls import path
from . import views

handler404 = 'userManagement.views.error_404_view'


urlpatterns = [
      # Other URL patterns
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),

      # CRUD URL patterns
    # path('create_user/', views.create_user, name='create_user'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_detail/<int:user_id>/', views.user_detail, name='user_detail'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

    path('manage_roles/', views.manage_roles, name='manage_roles'),
    path('update_role/<int:user_id>/', views.update_role, name='update_role'),


    

] 