from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('about', views.about, name='about'),
    path('post', views.post_list, name='post_list'),
    path('post/add', views.post_add, name='post_add'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/modify/<int:pk>/', views.post_modify, name='post_modify'),
    path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),
]
