from django.urls import path
from rango import views

app_name = "rango"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('set_preference/', views.set_user_preference, name='set_preference'),
    path('get_preference/', views.get_user_preference, name='get_preference'),
]
