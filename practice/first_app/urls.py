from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    MusicianListView, MusicianCreateView, MusicianUpdateView, MusicianDeleteView,
    AlbumCreateView, AlbumUpdateView, AlbumDeleteView
)
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
urlpatterns = [
    path('', MusicianListView.as_view(), name='musician_list'),
    path('musician/add/', MusicianCreateView.as_view(), name='musician_add'),
    path('musician/<int:pk>/edit/', MusicianUpdateView.as_view(), name='musician_edit'),
    path('musician/<int:pk>/delete/', MusicianDeleteView.as_view(), name='musician_delete'),
    path('album/add/', AlbumCreateView.as_view(), name='album_add'),
    path('album/<int:pk>/edit/', AlbumUpdateView.as_view(), name='album_edit'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.user_logout, name='user_logout'),
    path('accounts/login/', LoginView.as_view(template_name='login.html',next_page='musician_list'), name='login'),
]
