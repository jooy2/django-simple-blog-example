from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('about', views.about, name='about'),
    path('post', views.post_list, name='post_list'),
    path('post/add', views.post_add, name='post_add'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('post/comment/like/', views.comment_like, name='comment_like'),
    path('post/comment/delete/', views.comment_delete, name='comment_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('summernote/', include('django_summernote.urls')),
]
