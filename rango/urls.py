from django.urls import path
from rango import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),

]
