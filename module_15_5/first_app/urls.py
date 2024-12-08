from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_list, name='musician_list'),
    path('musician/add/', views.musician_create, name='musician_create'),
    path('musician/edit/<int:pk>/', views.musician_edit, name='musician_edit'),
    path('musician/delete/<int:pk>/', views.musician_delete, name='musician_delete'),
    path('album/add/', views.album_create, name='album_create'),
    path('album/edit/<int:pk>/', views.album_edit, name='album_edit'),
    path('album/delete/<int:pk>/', views.album_delete, name='album_delete'),
]
