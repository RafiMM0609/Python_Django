from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='index'),
    path('login', views.login, name='login'),
    path('', views.simpan_pengguna, name='simpan_pengguna'),
    path('history', views.user_list, name='user_list'),
    path('<int:user_id>/update/', views.update_user, name='update_user'),
    path('<int:user_id>/delete/', views.delete_user, name='delete_user'),
]